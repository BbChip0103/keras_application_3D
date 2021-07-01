# keras-applications-3D

keras-applications-3D is implementations of popular deep learning models for 3D domain. (Based on the Keras)

## NOTICE
We are migrating for TF (>= 2.5)
If you interested in this project, feel free and suggest anything.

### This repository provide below things 
- Major CNN architecture for 3D
  - [x] VGG (16, 19)
  - [x] ResNet (50, 101, 152)
  - [x] ResNetV2 (50, 101, 152)
  - [x] DenseNet (121, 169, 201)
  - [ ] ResNext 
  - [ ] InceptionV3
  - [ ] Inception_Resnet_V2
  - [ ] Xception
  - [ ] EfficientNet (B0, B1, ..., B7)
  - [ ] Mobilenet (V1, V2)
  - [ ] SE-ResNet
  - [ ] NFNet
- Convolution function for 3D (keras_applications_3d/custom_layers.py)
  - [x] DepthwiseConv3D
  - [x] SeparableConv3D
- Documentation
  - [ ] Documentation
- Exmaple
  - [ ] Classification
  - [ ] Regression
  - [ ] Visualize trained model
- Visualization
  - [ ] Saliency map (Simple gradient)
  - [ ] Class Activation Map (GradCAM)
  - [ ] Activation Maximization
- Pretrained weight
  - [ ] ??? (Please recommand 3D dataset)


### If you want to use 3D CNN, you may have to reduce number of parameter.
- So I prepare some custom model to handle this.  
  
### When you use 3D CNN, BatchNormalization may not work well because of scarce data.
- So I also prepare some option to exclude batch-norm.
