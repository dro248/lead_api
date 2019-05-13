export FLASK_APP=app.py
export FLASK_DEBUG=1

# Create a log files (if they don't exist)
touch -a received.log
touch -a leads.log
touch -a interesting_moments.log

# Run server on port 4000
python -m flask run --host=0.0.0.0 --port=4000
