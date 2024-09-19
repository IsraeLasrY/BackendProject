from flask_jwt_extended import create_access_token,decode_token,get_jwt_identity
from datetime import timedelta
import os

def generate_jwt(user_id):
    expirs = timedelta(days=1) #token expires after 1 day
    access_token = create_access_token(identity=user_id,expires_delta=expirs)
    return access_token

def decode_jwt(token):
    
    decode_token = decode_token(token)
    return decode_token['sub'] #sub contains the user_id in JWT

def get_currect_user():
    #    This utility function is used to retrieve the current user's identity (user_id).
    return get_jwt_identity()