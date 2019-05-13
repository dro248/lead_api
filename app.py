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


@app.route('/leads', methods=['GET', 'POST'])
def receive_leads():
	""" Question: What do leads look like?"""
	print(request.data)
	with open('./leads.txt', 'a') as file:
		file.write(f"""
Request Method: {request.method}
Received: {datetime.datetime.utcnow()}
{'-' * 30}
{request.data}
{'=' * 50}
""")
	return f"Successfully received LEADS: {request.method}"


@app.route('/interesting_moments', methods=['GET', 'POST'])
def receive_ims():
	""" Question: What do `Interesting Moments` look like?"""
	print(request.data)
	with open('./interesting_moments.txt', 'a') as file:
		file.write(f"""
Request Method: {request.method}
Received: {datetime.datetime.utcnow()}
{'-' * 30}
{request.data}
{'=' * 50}
""")
	return f"Successfully received INTERESTING_MOMENTS: {request.method}"
