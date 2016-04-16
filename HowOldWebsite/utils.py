# -*- coding: UTF-8 -*-

import json

import cv2
import skimage
import skimage.color
import skimage.io

__author__ = 'Hao Yu'


def do_rgb2gray(image):
    if 3 == image.ndim:
        return skimage.img_as_ubyte(skimage.color.rgb2gray(rgb=image))
    else:
        return skimage.img_as_ubyte(image)


def do_rgb2gray_cv(cv_image):
    if 3 == cv_image.ndim:
        return cv2.cvtColor(src=cv_image, code=cv2.COLOR_BGR2GRAY)
    else:
        return cv_image


def do_imread(path):
    return skimage.img_as_ubyte(skimage.io.imread(fname=path))


def do_imread_cv(path):
    return cv2.imread(fname=path)


def do_message_maker(success=True, message=None, tip=None):
    return json.dumps({'success': success,
                       'message': message,
                       'tip': tip
                       })


def do_collect_feature(feature_jar, feature_single):
    for key in feature_single.keys():
        if key not in feature_jar.keys():
            feature_jar[key] = []

        feature_jar[key].append(feature_single[key][0])

    return feature_jar
