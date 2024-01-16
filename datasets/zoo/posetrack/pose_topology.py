#!/usr/bin/python
# -*- coding:utf8 -*-
"""
    Author: Haoming Chen
    E-mail: chenhaomingbob@163.com
    Time: 2020/09/26
    Description:
"""
__all__ = ["POSETRACK_joint", "POSETRACK_joint_pairs", "COLOR_DICT", "POSETRACK_joint_name_color"]

# Not modify
POSETRACK_joint = [
    'right_ankle',
    'right_knee',
    'right_hip',  # = right pelvis
    'left_hip',  # = left pelvis
    'left_knee',
    'left_ankle',
    'right_wrist',
    'right_elbow',
    'right_shoulder',
    'left_shoulder',
    'left_elbow',
    'left_wrist',
    'head_bottom',  # = upper neck/head_bottom
    'nose',
    'head_top',  # = head /head_top
]
# len(POSETRACK_joint)=15
# Endpoint1 , Endpoint2 , line_color
POSETRACK_joint_pairs = [
    ['head_top', 'head_bottom', 'rosy'],
    ['head_bottom', 'right_shoulder', 'yellow'],
    ['head_bottom', 'left_shoulder', 'yellow'],
    ['right_shoulder', 'right_elbow', 'blue'],
    ['right_elbow', 'right_wrist', 'blue'],
    ['left_shoulder', 'left_elbow', 'green'],
    ['left_elbow', 'left_wrist', 'green'],
    ['right_shoulder', 'right_hip', 'purple'],
    ['left_shoulder', 'left_hip', 'skyblue'],
    ['right_hip', 'right_knee', 'purple'],
    ['right_knee', 'right_ankle', 'purple'],
    ['left_hip', 'left_knee', 'skyblue'],
    ['left_knee', 'left_ankle', 'skyblue'],
]

POSETRACK_joint_name_color = [['right_ankle', 'Gold'],
                              ['right_knee', 'Orange'],
                              ['right_hip', 'DarkOrange'],
                              ['left_hip', 'Peru'],
                              ['left_knee', 'LightSalmon'],
                              ['left_ankle', 'OrangeRed'],
                              ['right_wrist', 'LightGreen'],
                              ['right_elbow', 'LimeGreen'],
                              ['right_shoulder', 'ForestGreen'],
                              ['left_shoulder', 'DarkTurquoise'],
                              ['left_elbow', 'Cyan'],
                              ['left_wrist', 'PaleTurquoise'],
                              ['head_bottom', 'DoderBlue'],
                              ['nose', 'HotPink'],
                              ['head_top', 'SlateBlue']]



COLOR_DICT = {
    'rosy': (255, 47, 130),
    'purple': (252, 176, 243),
    'yellow': (255, 156, 49),
    'blue': (107, 183, 190),
    'green': (76, 255, 160),
    'skyblue': (76, 288, 255),
    'HotPink': (255, 105, 180),
    'SlateBlue': (106, 90, 205),
    'DoderBlue': (30, 144, 255),
    'PaleTurquoise': (175, 238, 238),
    'Cyan': (0, 255, 255),
    'DarkTurquoise': (0, 206, 209),
    'ForestGreen': (34, 139, 34),
    'LimeGreen': (50, 205, 50),
    'LightGreen': (144, 238, 144),
    'OrangeRed': (255, 69, 0),
    'Orange': (255, 165, 0),
    'LightSalmon': (255, 160, 122),
    'Peru': (205, 133, 63),
    'DarkOrange': (255, 140, 0),
    'Gold': (255, 215, 0),
}
