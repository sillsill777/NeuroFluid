from tmp import get_cfg_defaults
import argparse
cfg=get_cfg_defaults()
cfg.merge_from_file('./tmp.yaml')
print(cfg)
opts = ["SYSTEM.NUM_GPUS", 8, "TRAIN.SCALES", "(1, 2, 3, 4)"]
cfg.merge_from_list(opts)
cfg.update([['adsasdsada',10]])
print(cfg)
parser=argparse.ArgumentParser()
parser.add_argument('--a',type=int,default=11)
parser.add_argument('--c',type=str,default='c')

args=parser.parse_args()
print(vars(args))
import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print('====')
print(cfg.TRAIN)
print(cfg['TRAIN'])