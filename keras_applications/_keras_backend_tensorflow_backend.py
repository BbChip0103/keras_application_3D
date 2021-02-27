from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import functools
import threading

import numpy as np
from distutils.version import StrictVersion

import tensorflow as tf

def _preprocess_padding(padding):
    """Convert keras' padding to tensorflow's padding.
    # Arguments
        padding: string, `"same"` or `"valid"`.
    # Returns
        a string, `"SAME"` or `"VALID"`.
    # Raises
        ValueError: if `padding` is invalid.
    """
    if padding == 'same':
        padding = 'SAME'
    elif padding == 'valid':
        padding = 'VALID'
    else:
        raise ValueError('Invalid padding: ' + str(padding))
    return padding

# CONVOLUTIONS


def _preprocess_conv1d_input(x, data_format):
    """Transpose and cast the input before the conv1d.
    # Arguments
        x: input tensor.
        data_format: string, `"channels_last"` or `"channels_first"`.
    # Returns
        A tensor.
    """
    # tensorflow doesn't support float64 for conv layer before 1.8.0
    if (dtype(x) == 'float64' and
            StrictVersion(tf.__version__.split('-')[0]) < StrictVersion('1.8.0')):
        x = tf.cast(x, 'float32')
    tf_data_format = 'NWC'  # to pass TF Conv2dNative operations
    if data_format == 'channels_first':
        if not _has_nchw_support():
            x = tf.transpose(x, (0, 2, 1))  # NCW -> NWC
        else:
            tf_data_format = 'NCW'
    return x, tf_data_format


def _preprocess_conv2d_input(x, data_format, force_transpose=False):
    """Transpose and cast the input before the conv2d.
    # Arguments
        x: input tensor.
        data_format: string, `"channels_last"` or `"channels_first"`.
        force_transpose: boolean, whether force to transpose input from NCHW to NHWC
                        if the `data_format` is `"channels_first"`.
    # Returns
        A tensor.
    """
    # tensorflow doesn't support float64 for conv layer before 1.8.0
    if (dtype(x) == 'float64' and
            StrictVersion(tf.__version__.split('-')[0]) < StrictVersion('1.8.0')):
        x = tf.cast(x, 'float32')
    tf_data_format = 'NHWC'
    if data_format == 'channels_first':
        if not _has_nchw_support() or force_transpose:
            x = tf.transpose(x, (0, 2, 3, 1))  # NCHW -> NHWC
        else:
            tf_data_format = 'NCHW'
    return x, tf_data_format


def _preprocess_conv3d_input(x, data_format):
    """Transpose and cast the input before the conv3d.
    # Arguments
        x: input tensor.
        data_format: string, `"channels_last"` or `"channels_first"`.
    # Returns
        A tensor.
    """
    # tensorflow doesn't support float64 for conv layer before 1.8.0
    # if (dtype(x) == 'float64' and
    #         StrictVersion(tf.__version__.split('-')[0]) < StrictVersion('1.8.0')):
    #     x = tf.cast(x, 'float32')
    tf_data_format = 'NDHWC'
    if data_format == 'channels_first':
        if not _has_nchw_support():
            x = tf.transpose(x, (0, 2, 3, 4, 1))
        else:
            tf_data_format = 'NCDHW'
    return x, tf_data_format

