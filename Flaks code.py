from flask import Flask, redirect, request
from mangum import Mangum
import os
import requests

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
GUILD_ID = os.getenv("GUILD_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route("/api/verify")
def verify():
    url = (
        "https://discord.com/api/oauth2/authorize"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&response_type=code"
        "&scope=identify%20guilds.join"
    )
    return redirect(url)

@app.route("/api/callback")
def callback():
    code = request.args.get("code")
    # OAuth Token holen & User auf Server einladen
    # (wie in deinem vorherigen Flask-Code)
    return "Verification successful"

handler = Mangum(app)
