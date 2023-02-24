import os
import argparse


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def main():
    assert os.path.exists(inputdir), 'Input dir not found'
    assert os.path.exists(targetdir), 'target dir not found'
    mkdir(outputdir)
    imgs = sorted(os.listdir(inputdir))
    for idx,img in enumerate(imgs):
        groups = ''

        groups += os.path.join(inputdir, img) + '|'
        groups += os.path.join(args.mask, img) + '|'
        groups += os.path.join(targetdir,img.replace('tif','jpg'))

        # if idx >= 800:
        #     break

        with open(os.path.join(outputdir, 'groups_test.txt'), 'a') as f:
            f.write(groups + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='/data1/cxh/Kligler/test/test_A', metavar='PATH', help='root dir to save low resolution images')
    parser.add_argument('--mask', type=str, default='/data1/cxh/Kligler/test/test_B', metavar='PATH', help='root dir to save high resolution images')
    parser.add_argument('--target', type=str, default='/data1/cxh/Kligler/test/test_C', metavar='PATH', help='root dir to save high resolution images')
    parser.add_argument('--output', type=str, default='/data/cxh/BMNet/MainNet/data/', metavar='PATH', help='output dir to save group txt files')
    parser.add_argument('--ext', type=str, default='.jpg', help='Extension of files')
    args = parser.parse_args()

    inputdir = args.input
    targetdir = args.target
    outputdir = args.output
    ext = args.ext

    main()
