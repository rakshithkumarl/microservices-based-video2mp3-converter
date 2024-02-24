import os, requests


def login(request):
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)

    basicAuth = (auth.username, auth.password)
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}:5000/login", auth=basicAuth
    )
    # response = requests.post(
    #     "http://10.155.113.225:5000/login", auth=basicAuth
    # )
    if response.status_code == 200:
        print("JWT Token: ", response.text)
        return response.text, None
    else:
        return None, (response.text, response.status_code)