#!/usr/bin/env python
"""A simple asynchronous generator to count the
  number of public github gists given a username

  Instead of a callback as in async_fetch.py, this example
  uses yield to return control of the program to Tornado.
  This allows the app to do other tasks while the request is in progress.
  Once finished, tornado's RequestHandler resumes where it left off

  Run this program and go to http://localhost:3000/?user=alyssaq
  Change the user query parameter to see how others compare!
"""

import sys
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.escape

class IndexHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  @tornado.gen.engine
  def get(self):
    user = self.get_argument('user')
    client = tornado.httpclient.AsyncHTTPClient()
    response = yield tornado.gen.Task(client.fetch,
                                     'https://api.github.com/users/{0}/gists'.format(user),
                                     headers={'User-Agent': '{0}/tornado-demo'.format(user)}),
    print(response)
    data = tornado.escape.json_decode(response.body)
    user = data[0]['owner']['login']
    self.write("""
    <div style="text-align: center">
    <div style="font-size: 72px">
      <a href='https://github.com/%s'> %s </a>
    </div>
    <div style="font-size: 24px">has</div>
    <div style="font-size: 144px">%d</div>
    <div style="font-size: 24px">public gists</div>
    </div>""" % (user, user, len(data)))
    self.finish()

if __name__ == '__main__':
  app_port = app_port = sys.argv[1] if len(sys.argv) > 1 else 3000
  app = tornado.web.Application(handlers=[
    (r'/', IndexHandler)
  ], debug=True)
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(app_port)
  print('Listening on http://localhost:{0}'.format(app_port))
  tornado.ioloop.IOLoop.instance().start()
