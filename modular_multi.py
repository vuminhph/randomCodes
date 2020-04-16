import png
from sys import argv
import imageio

SIZE = argv[1]

def modular_multi(size):
    img = []

    for i in range(size, 0, -1):
        row = ()
        for j in range(size, 0, -1):
            value = int ((i * j) % size / size * 255)
            row += (value, )
        img.append(row)
    # print(img)
    with open(f'{size}.png', 'wb') as fout:
        w = png.Writer(size, size, greyscale=True)
        w.write(fout,img)
        fout.close()

for i in range(SIZE):
    modular_multi(i)

def gif_maker():
    images = []
    for i in range(size):
        images.append(imageio.imread(f'{size}.png'))
    imageio.mimsave(f'{size}.gif',images)
