.. raw:: html

   <h2 align="center">

spinners

.. raw:: html

   </h2>

    More than 60 spinners for terminal, python port of amazing node
    library cli-spinners

|Build Status| |Build status| |PyPI| |awesome|

.. figure:: https://github.com/ManrajGrover/py-spinners/blob/master/assets/spinners.gif
   :alt: spinners

   spinners

The list of spinners is just a `JSON
file <https://github.com/sindresorhus/cli-spinners/blob/dac4fc6571059bb9e9bc204711e9dfe8f72e5c6f/spinners.json>`__.

If you're looking to use them, consider using
`halo <https://github.com/ManrajGrover/halo>`__ module for Python, or
`ora <https://github.com/sindresorhus/ora>`__ for node.

Install
-------

.. code:: shell

    $ pip install spinners

Usage
-----

.. code:: py

    from spinners import Spinners #Enum

    print Spinner.line.value
    # {u'frames': [u'-', u'\\', u'|', u'/'], u'interval': 130}

Like it?
--------

:star2: this repo to show support. Let me know you liked it on
`Twitter <https://twitter.com/manrajsgrover>`__. Also, share the
`project <https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2FManrajGrover%2Fpy-spinners&via=manrajsgrover&text=Checkout%20%23spinners%20-%20%23python%20wrapper%20for%20amazing%20node%20library%20%23cli-spinners%20&hashtags=github%2C%20pypi>`__.

Related
-------

-  `halo <https://github.com/ManrajGrover/halo>`__
-  `cli-spinners <https://github.com/sindresorhus/cli-spinners>`__

License
-------

`MIT <https://github.com/ManrajGrover/py-spinners/blob/master/LICENSE>`__
© Manraj Singh

.. |Build Status| image:: https://travis-ci.org/ManrajGrover/py-spinners.svg?branch=master
   :target: https://travis-ci.org/ManrajGrover/py-spinners
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/8g2ar5pg5810t831?svg=true
   :target: https://ci.appveyor.com/project/ManrajGrover/py-spinners
.. |PyPI| image:: https://img.shields.io/pypi/v/spinners.svg
   :target: https://github.com/ManrajGrover/py-spinners
.. |awesome| image:: https://img.shields.io/badge/awesome-yes-green.svg

