#!/usr/bin/env python
"""A simple asynchronous call to count the
  number of public github gists given a username

  Run this program and go to http://localhost:3000/?user=alyssaq
  Change the user query parameter to see how others compare!
"""

import sys
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.escape

class IndexHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  def get(self):
    user = self.get_argument('user')
    client = tornado.httpclient.AsyncHTTPClient()
    client.fetch('https://api.github.com/users/{0}/gists'.format(user),
                 headers={'User-Agent': '{0}/tornado-demo'.format(user)},
                 callback=self.on_response)

  def on_response(self, response):
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
