# keras-applications-3D

### Hello, This repository provide below things 
- Major CNN architecture for 3D
  - [x] ResNetV1
  - [x] ResNetV2
  - [x] ResNext
  - [x] DenseNet
  - [x] InceptionV3
  - [x] Inception_Resnet_V2
  - [x] Xception
  - [ ] VGG
  - [ ] EfficientNet
  - [ ] Mobilenet V1, V2, V3
  - [ ] Nasnet
- Convolution function for 3D (Please see keras_applications/custom_layers.py)
  - [x] DepthwiseConv3D
  - [x] SeparableConv3D

### If you want to use 3D CNN, you may have to reduce number of parameter.
- So I prepare some custom model to handle this.  
  
### When you use 3D CNN, BatchNormalization may not work well because of scarce data.
- So I also prepare some option to exclude batch-norm.