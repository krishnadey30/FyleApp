import jwt
import datetime
import os
def genearte(username):
    data = {'name':username,'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)}
    secret = os.environ['SECRET']
    encoded = jwt.encode(data, secret,algorithm='HS256')
    return encoded.decode("utf-8")
