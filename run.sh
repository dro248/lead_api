export FLASK_APP=app.py
export FLASK_DEBUG=1

# Create a requirements.txt file if it doesn't exist
touch -a received.txt
touch -a leads.txt
touch -a interesting_moments.txt

# Run server on port 4000
python -m flask run --host=0.0.0.0 --port=4000
