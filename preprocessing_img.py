from PIL import ImageEnhance, Image, ImageOps
import os
import re


def img_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    img_with_contrast = enhancer.enhance(1.5)
    return img_with_contrast


def img_histogram(image):
    return ImageOps.equalize(image)


def img_adapt(input_path):
    '''missing Adapative Equalization'''
    pass


def enhance_img(input_path, output_path, method='all'):
    '''
    enhances the img from the input folder
    and saves it in an output folder
    method:
        - contrast
        - histogram
        - adaptative
        - all (runs the 3 methods, one by one)
    '''
    image = Image.open(input_path)
    regex = re.search(r'(?<!\/)\/(?!.*\/)', input_path)
    file_name = regex.start()
    output = output_path + input_path[file_name:][:-4]

    if method == 'contrast':
        img_with_contrast = img_contrast(image)
        img_with_contrast.save(output + '_contrast.jpg')
    elif method == 'histogram':
        img_equalized = img_histogram(image)
        img_equalized.save(output + '_histogram.jpg')
    elif method == 'adaptative':
        pass
    elif method == 'all':
        enhance_img(input_path, output_path, method='contrast')
        enhance_img(input_path, output_path, method='histogram')
        enhance_img(input_path, output_path, method='adaptative')


def main():
    input_path = './datasets/images/train/'
    output_path = './datasets/images_preprocessed/'
    os.mkdir(output_path)
    for image in os.listdir(input_path):
        enhance_img(input_path+image, output_path, method='all')


if __name__ == "__main__":
    main()
