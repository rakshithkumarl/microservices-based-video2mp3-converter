import os, requests

def token(request):
    if not "Authorization" in request.headers:
        return None, ("Missing credentials", 401)
    
    token = request.headers["Authorization"]
    print("Token received at validate.token(request) method: ", token)
    if not token:
        return None, ("Missing credentials", 401)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}:5000/validate",
        headers={"Authorization": token},
    )
    print(response)
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
