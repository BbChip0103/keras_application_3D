# keras-applications-3D

keras-applications-3D is implementations of popular deep learning models for 3D domain. (Based on the Keras)  

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

### Model benchmark (Test accuracy)
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

### If you want to use 3D CNN, you'd better reduce number of parameter because of curse of dimension.
- So We prepare some custom model to handle this.  
- Please check **base_channel** or **growth_rate** option.  
  
### When you use 3D CNN, BatchNormalization may not work well in the scarce data.
- So We also prepare some option to exclude batch-norm.  

## NOTICE
We are migrating for TF (>= 2.5)  
If you interested in this project, feel free and suggest anything.  
