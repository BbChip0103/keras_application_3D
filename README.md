# keras-applications-3D

## keras-applications-3D is implementations of popular 2D-image deep learning models for 3D domain. (Based on the Keras)  

---
## Install
```
pip install Keras-Applications-3D
```
---
## Usage
``` python
import sklearn

# ...
### Prepare your 3D data [Ex. (64,64,64,1) shape]
X = np.zeros((128, 64, 64, 64, 1))
y = np.zeros((128, 10))
y[:,0] = 1
# ...

### Oriinal channel of model is '64->128->256->...'
### But it takes a lot of memory, So we reduce first channel 64 to 16
model = vgg19.VGG19(
  input_shape=(64,64,64,1), classes=10,
  base_channel=16
)
# model.summary()

### Training
model.compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(learning_rate=1e-4),
    metrics=['acc']
)

history = model.fit(
    x=X, y=y, 
)

### Inference
pred = model.predict(X_test).squeeze()
real = y_test

pred = pred.argmax(axis=1)
real = real.argmax(axis=1)

accr = (pred == real).sum() / len(real)
print('Accuracy: {:04f}'.format(accr))

```

---

## This repository provide below things 
- Major 2D CNN architecture for 3D (O: Complete, X: In progress)
  - [O] VGG (16, 19)
  - [O] ResNet (50, 101, 152)
  - [O] ResNetV2 (50, 101, 152)
  - [O] DenseNet (121, 169, 201)
  - [X] ResNext 
  - [X] InceptionV3
  - [X] Inception_Resnet_V2
  - [X] Xception
  - [X] EfficientNet (B0, B1, ..., B7)
  - [X] Mobilenet (V1, V2)
  - [X] SE-ResNet
  - [X] NFNet
- Convolution function for 3D (keras_applications_3d/custom_layers.py)
  - [O] DepthwiseConv3D
  - [O] SeparableConv3D
- Documentation
  - [X] Documentation
- Exmaple
  - [O] Classification
  - [X] Regression
  - [X] Visualize trained model
- Visualization
  - [X] Saliency map (Simple gradient)
  - [X] Class Activation Map (GradCAM)
  - [X] Activation Maximization
- Pretrained weight
  - [X] ModelNet10
  - [X] ModelNet40
  - (Please recommand any 3D dataset)
  
---

## Model benchmark (Test accuracy)
|Model|ModelNet10 accuracy|Number of parameters|
|:---:|:---:|:---:|
|VGG16 (16)|0.9001|23,780,058|
|VGG19 (16)|0.9075|24,775,706|
|ResNet50 (16)|0.8062|2,923,818|
|ResNet101 (16)|0.7467|5,393,578|
|ResNet152 (16)|0.7588|7,429,418|
|ResNet50V2 (16)|0.8194|2,918,090|
|ResNet101V2 (16)|0.8128|5,385,674|
|ResNet152V2 (16)|0.8007|7,419,594|
|DenseNet121 (16)|0.9042|2,884,010|
|DenseNet169 (16)|0.8855|4,768,298|
|DenseNet201 (16)|0.8998|6,519,594|

---

## If you want to use 3D CNN, you'd better reduce number of parameter because of curse of dimension.
- So We prepare some custom model to handle this.  
- Please check **base_channel** or **growth_rate** option.  
  
## When you use 3D CNN, BatchNormalization may not work well in the scarce data.
- So We also prepare some option to exclude batch-norm.  
---
## NOTICE
We are migrating for TF (>= 2.5)  
If you interested in this project, feel free and suggest anything.  
