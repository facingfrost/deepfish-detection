# Environment
```
conda create -n data_challenge python=3.10
conda activate data_challenge
pip install requirements.txt
```
# Dataset
The dataset I uploaded is already resized and can be upload to github for immediate training.
For the original data for better training, you can download it here:

[Deepfish.](https://alzayats.github.io/DeepFish/)

[Bounding box in json format.](https://drive.google.com/drive/folders/16SDv_V7RDjTKDk8uodL2ubyubYTMdd5q) FISH.tar.gz is deepfish.

[Bouding box in COCO format.](https://www.kaggle.com/datasets/vencerlanz09/deep-fish-object-detection)

[The source of this github data.](https://universe.roboflow.com/brrrrrrr/deepfish-fmyzf) Select yolo8 format to download.


Note that if you want to download the images from source link, you'll need to re-organize the folders following [ultralytics documentation](https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format). If the images doesn't match the required format, yolo model may not be able to recognize train and test images.

# Model training and testing
See `scripts.ipynb`.