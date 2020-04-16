import png
from sys import argv
from PIL import Image
from glob import glob

num_frames = int(argv[1])
frame_dimensions = [2 ** i for i in range(num_frames)]
frame_size = frame_dimensions[-1]

def modular_multi(size):
    img = []

    for i in range(size, 0, -1):
        row = ()
        for j in range(size, 0, -1):
            value = int ((i * j) % size / size * 255)
            row += (value, )
        img.append(row)
    # print(img)
    pixel_ratio = int(SIZE / size)
    with open(f'{size}.png', 'wb') as fout:
        # w = png.Writer(size, size, greyscale=True, x_pixels_per_unit=pixel_ratio, y_pixels_per_unit=pixel_ratio)
        w = png.Writer(size, size, greyscale=True)
        w.write(fout,img)
        fout.close()

for i in range(1, SIZE + 1):
    modular_multi(i)

def gif_maker(size):
    frames = []
    imgs = glob('*.png')
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
    frames[0].save(f'{size}_loop.gif', format='GIF',
                    append_images=frames[1:],
                    save_all=True,
                    duration=300, loop=0)

gif_maker(SIZE)