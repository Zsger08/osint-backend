from flask import Flask, request, jsonify
import asyncio
from holehe import check_email

app = Flask(__name__)

@app.route("/check")
def check():
    email = request.args.get("email")

    results = asyncio.run(check_email(email, None))

    data = []

    for r in results:
        data.append({
            "name": r.name,
            "exists": r.exists
        })

    return jsonify(data)

if __name__ == "__main__":
    app.run()
