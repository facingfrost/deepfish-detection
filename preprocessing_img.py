from roboflow import Roboflow
from PIL import ImageEnhance, Image
import os


def enhance_img(api_key, workspace, input_path, output_path):
    # enhances the img from the input folder
    # and saves it in an output folder
    rf = Roboflow(api_key=api_key)
    project = rf.workspace(workspace).project(workspace)
    model = project.version(1).model
    image = Image.open(input_path)
    enhancer = ImageEnhance.Contrast(image) #method to use
    image_with_contrast = enhancer.enhance(1.5) #hyperparameter
    image_with_contrast.save(output_path)


def main():
    api_key =  ''
    input_path = './datasets/images/train/'
    output_path = './datasets/images_preprocessed/'
    workspace = 'dc3'
    for image in os.listdir(input_path):
        output = output_path + image[:-4] + '_contrast.jpg'
        enhance_img(api_key, workspace, input_path+image, output)

if __name__ == "__main__":
    main()