import imp, sys, os
sys.path.insert(0, os.path.dirname(__file__))
wsgi = imp.load_source('wsgi', 'main.py')
application = wsgi.application
