A jargon lorem ipsum generator.

This started as a translation into Python of James Weber's original Mennonite ipsum generator.
Then I swapped out the vocabulary and started using NLTK to generate grammatical productions.

Installation:

1. Get virtualenv::

    $ curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py

2. Create a virtualenv in this directory (this isolates our Python environment)::

    $ python virtualenv.py --no-site-packages .

3. Install the dependencies::

    $ bin/pip install PasteScript webob

4. Serve the app::

    $ bin/python generator.py

Then visit http://localhost:8080/ in your browser.
