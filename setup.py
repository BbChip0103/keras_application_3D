from setuptools import setup
from setuptools import find_packages

long_description = '''
Keras Applications 3D is the `applications` module of
the Keras deep learning library for 3D domain.
It provides model definitions and pre-trained weights(for the future) for a number
of popular archictures, such as VGG16, ResNet50, Xception, MobileNet, and more.
Keras Applications is compatible with Python 3.x
and is distributed under the MIT license.
'''

setup(
    name='Keras_Applications_3D',
    version='0.1.1',
    description='Reference implementations of popular deep learning models for 3D domain',
    long_description=long_description,
    author='BbChip0103',
    author_email='bbchip13@gmail.com',
    url='https://github.com/BbChip0103/keras_application_3D',
    download_url='https://github.com/BbChip0103/keras_application_3D.git',
    license='Apache 2.0',
    install_requires=[
        'numpy>=1.9.1',
        'h5py',
        'tensorflow>=2.0.0',
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-pep8',
            'pytest-xdist',
            'pytest-cov'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages()
)
