from flask import Flask, render_template, request

app = Flask(__name__)

import datetime

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	print(request.data)
	with open('./received.txt', 'a') as file:
		file.write(f"""
Request Method: {request.method}
Received: {datetime.datetime.utcnow()}
{'-' * 30}
{request.data}
{'=' * 50}
""")
	return f"Success. Hello World: {request.method}"

