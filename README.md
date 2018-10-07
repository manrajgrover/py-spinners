<h2 align="center">
  spinners
</h2>

> 🔄 More than 60 spinners for terminal, python wrapper for amazing node library [cli-spinners](https://github.com/sindresorhus/cli-spinners)

[![Build Status](https://travis-ci.org/manrajgrover/py-spinners.svg?branch=master)](https://travis-ci.org/manrajgrover/py-spinners) [![Build status](https://ci.appveyor.com/api/projects/status/8g2ar5pg5810t831?svg=true)](https://ci.appveyor.com/project/manrajgrover/py-spinners) [![PyPI](https://img.shields.io/pypi/v/spinners.svg)](https://github.com/manrajgrover/py-spinners) ![awesome](https://img.shields.io/badge/awesome-yes-green.svg)

![spinners](https://github.com/manrajgrover/py-spinners/blob/master/assets/spinners.gif)

The list of spinners is just a [JSON file](https://github.com/sindresorhus/cli-spinners/blob/dac4fc6571059bb9e9bc204711e9dfe8f72e5c6f/spinners.json).

If you're looking to use them, consider using [halo](https://github.com/manrajgrover/halo) module for Python, or [ora](https://github.com/sindresorhus/ora) for node.

## Install

```shell
$ pip install spinners
```

## Usage

```py
from spinners import Spinners #Enum

print Spinners.line.value
# {u'frames': [u'-', u'\\', u'|', u'/'], u'interval': 130}
```

## Like it?

:star2: this repo to show support. Let me know you liked it on [Twitter](https://twitter.com/manrajsgrover).
Also, share the [project](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fmanrajgrover%2Fpy-spinners&via=manrajsgrover&text=Checkout%20%23spinners%20-%20%23python%20wrapper%20for%20amazing%20node%20library%20%23cli-spinners%20&hashtags=github%2C%20pypi).

## Related

* [halo](https://github.com/manrajgrover/halo)
* [cli-spinners](https://github.com/sindresorhus/cli-spinners)

## License
[MIT](https://github.com/manrajgrover/py-spinners/blob/master/LICENSE) © Manraj Singh
