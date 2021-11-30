from flask import Flask, request, jsonify
from random import choice
from slack_sdk import WebClient
import config


app = Flask(__name__)
slack_client = WebClient(token=config.SLACK_TOKEN)

@app.route('/slash', methods=['POST'])
def slash():
    if request.form['token'] == config.VERIFICATION_TOKEN:
        res = slack_client.api_call(
            api_method='emoji.list'
        )
        emoji = choice(list(res['emoji'].keys()))

        payload = {
            'response_type': 'in_channel',
            'text': f':{emoji}:'
        }
        return jsonify(payload)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True)
