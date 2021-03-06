import yaml
import numpy as np
from easydict import EasyDict as edict

config = edict()

config.boxsize = 256

config.TEST = edict()

config.TEST.scale_search = [0.5, 1, 1.5, 2, 2.3]

config.TEST.imgIds_num = -1

config.TEST.model_path = 'testConfigModel'

config.TEST.model_path = '../realtimePose'

config.TEST.epoch = 0

config.TEST.imgIds_num = 5

config.TRAIN = edict()

config.TRAIN.num_epoch = 1

#config.TRAIN.initial_model = '/data/guest_users/liangdong/liangdong/practice_demo/realtimePose'
config.TRAIN.output_model = 'testConfigModel'

#config.TRAIN.crop_size = 368
config.TRAIN.crop_size = 384
config.TRAIN.label_size = 48

config.TRAIN.crop_size_x = config.TRAIN.crop_size

config.TRAIN.crop_size_y = config.TRAIN.crop_size


config.TRAIN.center_perterb_max = 0

config.TRAIN.scale_prob = 1

config.TRAIN.scale_min = 0.75

config.TRAIN.scale_max = 1.25

config.TRAIN.flip = True

config.TRAIN.target_dist = 0.6

config.TRAIN.max_rotate_degree = 30

config.TRAIN.scale_set = True

# config.TRAIN.head = 'vgg'

config.TRAIN.head = 'RES'

# config.TRAIN.head = 'DPN'
# config.TRAIN.head = 'IRV2'

'''
config.TRAIN.vggparams = ['conv1_1_weight',
                          'conv1_1_bias',
                          'conv1_2_weight',
                          'conv1_2_bias',
                          'conv2_1_weight',
                          'conv2_1_bias',
                          'conv2_2_weight',
                          'conv2_2_bias',
                          'conv3_1_weight',
                          'conv3_1_bias',
                          'conv3_2_weight',
                          'conv3_2_bias',
                          'conv3_3_weight',
                          'conv3_3_bias',
                          'conv3_4_weight',
                          'conv3_4_bias',
                          'conv4_1_weight',
                          'conv4_1_bias',
                          'conv4_2_weight',
                          'conv4_2_bias']
'''
