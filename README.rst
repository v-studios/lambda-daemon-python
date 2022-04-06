=============================
 Lamdbda with Daemon: Python
=============================

We occassionally have need to run a Daemon in Lambda that our event
handler talks to.

* My Diazo in Lambda does this: a docker-packaged lambda gets a URL
  on the event, and sends it to an Nginx daemon running Diazo.
* I want to run GitHub prerender/prerender, but have to run the
  rendering service on localhost:3000, and have our event handler grab
  the desired URL and send it to the service like
  http://localhost:3000/render?url=https://example.com

But I'm finding the Prerender service case difficult; maybe it's my
lack of NodeJS-fu: I get connection refused:

* is the service really starting? There's no ``ps`` on Lambda.
* Is it listening on localhost, and what's that addr?
* Is the event GET happening before the service is starting?

Test a simple case with Python Lambda: a service listening on localhost:3000,
queried by a event handler.

Deploy and invoke it with the Serverless Framework::

  sls deploy
  sls invoke --function app

CloudWatch logs will be in ``/aws/lambda/lambda-with-daemon-dev-app/``.
