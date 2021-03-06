# Tornado Examples

Examples using Python [Tornado](http://tornado.readthedocs.org/en/latest/index.html) web server.
Runs on `Python 3.2+`

Each `.py` file is a standalone tornado web server example

Examples include:
 * Asynchronous, non-blocking call to a URL to retrive JSON data
 * Yield and co-routine
 * Non overlapping periodic calls every N seconds to a URL. Stop after X retries.
 * Overlapping periodic calls every N seconds to a URL. Stop after X retries.

## Running
```sh
$ python <file>.py 8888 # Specify a port
$ python <file>.py      # Use default 3000 port
```

## Developing
Clone the repo
```sh
$ git clone git@github.com:alyssaq/tornado-examples.git
```

Install requirements or check that you have them installed with `pip freeze`:
```sh
$ pip install -r requirements.txt
```

You may install requirements into a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
I recommend using virtualenvwrapper:
```sh
$ mkvirtualenv tornadoenv
$ workon tornadoenv
$ pip install -r requirements.txt
$ deactivate # Stop virtualenv when you are done
```

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
MIT