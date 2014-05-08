#!/usr/bin/env python
"""Make regular overlapping calls to itself
  every N seconds (configurable in self.seconds, default 3)
  Stops after X calls (configurable in self.max_count, default 10)

  If the function takes more than N seconds, the periodic timer will
  continue to call the function.

  See the non-overlapping version if the function needs to complete
  before starting the next function call after N seconds.

  To Run this program:
   $ python <file>.py
  Open another command prompt and do a request:
    $ curl 'http://localhost:3000'
"""

import sys
import random
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.escape

class IndexHandler(tornado.web.RequestHandler):
  def initialize(self):
    self.ioloop = tornado.ioloop.IOLoop.current()
    self.seconds = 3
    self.max_count = 10
    self.count = 0
    self.periodic_timer = None

  @tornado.gen.coroutine
  def periodic_func(self):
    self.count += 1
    response = yield tornado.httpclient.AsyncHTTPClient().fetch(
      'http://echo.jsontest.com/num/{0}'.format(random.randint(1, 100)))
    data = tornado.escape.json_decode(response.body)
    print('[{0}]. We got number {1}'.format(self.count, data['num']))

    if self.count == self.max_count:
      self.periodic_timer.stop()

  def get(self):
    self.periodic_timer = tornado.ioloop.PeriodicCallback(
      self.periodic_func,
      self.seconds * 1000,
      io_loop=self.ioloop)
    self.periodic_timer.start()
    self.write('Hallo! Periodic calls in progress...')

if __name__ == '__main__':
  app_port = app_port = sys.argv[1] if len(sys.argv) > 1 else 3000
  app = tornado.web.Application(handlers=[
    (r'/', IndexHandler)
  ], debug=True)
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(app_port)
  print('Listening on http://localhost:{0}'.format(app_port))
  tornado.ioloop.IOLoop.instance().start()
