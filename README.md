# pkm2png - Convert PKM files to PNG images

## Installation

pkm2png requires the [Python Imaging Library][0] ([documentation][1]), which
can be a very finicky installation. I suggest using [pip][2] to install it,
since solutions to most installation errors can be found through a quick
Google search.

[0]: http://www.pythonware.com/products/pil/
[1]: http://www.pythonware.com/library/pil/handbook/index.htm
[2]: http://pypi.python.org/pypi/pip

## Usage

Start by importing the module:

    import pkm2png

From here, you can convert a PKM file:

    my_pkm = open('/path/to/pokemonfile.pkm', 'r').read()
    my_pkm_img = pkm2png.pkm2png(gen=5, data=my_pkm)
    with open('/path/to/image.png', 'w') as f:
        f.write(my_pkm_img)

Or you can convert a PNG image:

    my_pkm_img = open('/path/to/image.png', 'r').read()
    my_pkm = pkm2png.png2pkm(my_pkm_img)
    with open('/path/to/pokemonfile.pkm', 'w') as f:
        f.write(my_pkm)