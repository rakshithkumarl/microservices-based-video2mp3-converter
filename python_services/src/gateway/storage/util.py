import pika, json

def upload(f, fs, channel, access):
    try:
        fid =  fs.put(f)
    except Exception as err:
        return "Internal Server Error", 500
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"], 
    }

    try:  #Try to put the message on the queue
        channel.basic_publish(
            exchange = "",
            routing_key = "video",       # Name of the queue within the broker 
            body = json.dumps(message),
            properties = pika.BasicProperties(
                delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE  # To make the queue and its messages durable in the event of the failure of the pod
            ),
        )
    except:  # If that doesn't work, we have to delete the file from mongodb because if there is no message on the queue for the file and the file does exist on mongodb then the file will never get processed because down stream service does not know that the file exists if it never receive receives a message telling it to process. We will end up having stale files in mongodb if we don't delete them in the event if we can't put the message onto the queue.
        fs.delete(fid)
        return "Internal Server Error", 500