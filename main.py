import os

from app.index import app


if os.environ.get('SERVER_SOFTWARE', None):
    from bae.core.wsgi import WSGIApplication

    application = WSGIApplication(app)
else:
    app.run(host='0.0.0.0', debug=True)
