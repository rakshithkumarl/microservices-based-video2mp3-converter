import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

# config 
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

# Routes
# Login route
@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "Missing login credentials", 401
        
    # Check db for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username,)
    )
    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.username != email or auth.password != password:
            return "Invalid login credentials", 401
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return "Invalid login credentials", 401
    
# Validate JWT
@server.route('/validate', methods=["POST"])
def validate():
    print("Inside validate of auth service")
    encoded_jwt = request.headers["Authorization"]
    print(encoded_jwt)
    if not encoded_jwt:
        return "Missing credentials", 401
    
    # auth_type, encoded_jwt = encoded_jwt.split(" ") # "Bearer" or "Basic" and "token"
    try:
        decoded_jwt = jwt.decode(
            encoded_jwt, os.environ.get("JWT_SECRET"), algorithm=["HS256"]
        )
    except:
        return "Not Authorized", 403
    
    return decoded_jwt, 200


# Create JWT
def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days = 2),
            "iat": datetime.datetime.utcnow(),
            "admin":authz
        },
        secret,
        algorithm = "HS256"
    )

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000) 