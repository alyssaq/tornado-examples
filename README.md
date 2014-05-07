# Tornado Examples

Examples using Python [Tornado](http://tornado.readthedocs.org/en/latest/index.html) web server

Examples include:
 * Asynchronous calls to a URL to retrivee JSON data and return to user
 * Periodic calls every N seconds to a URL. Stop after X retries.

## Develop locally
Install requirements or check that you have them installed with `pip freeze`:
```sh
$ pip install -r requirements.txt
```

You may install requirements into a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
I recommend installing virtualenvwrapper:
```sh
$ mkvirtualenv tornadoenv
$ workon tornadoenv
$ pip install -r requirements.txt
$ deactivate # Stop virtualenv when you are done
```

## Running locally
```sh
$ python <file>.py 8888 # Specify a port
$ python <file>.py      # Use default 3000 port
```

## Contribute to the library
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
MIT