# keras-applications-3D

### Hello, This repository provide blow things 
* Convolution function for 3D (Please see keras_applications/custom_layers.py)
  * DepthwiseConv3D
  * SeparableConv3D
* Major CNN architecture for 3D
  * ResNetV1
  * ResNetV2
  * ResNext
  * DenseNet
  * InceptionV3
  * Inception_Resnet_V2
  * Xception
* In Progress
  * VGG
  * EfficientNet
  * Mobilenet V1, V2, V3
  * Nasnet

### If you want to use 3D CNN, you may have to reduce number of parameter.
- So I prepare some custom model to handle this.
### When you use 3D CNN, BatchNormalization may not work well because of scarce data.
- So I also prepare some option to handle this.
