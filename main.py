from flask import Flask
app = Flask(__name__)
application = app # required for passenger_wsgi

@app.route('/fuck')
def test():
    return 'asdf'

# for testing
if __name__ == '__main__': app.run()