"""
warmup renderer
"""

import torch

from trainer.trainer_renderer import Trainer
from configs import dataset_config, warmup_training_config

if __name__ == '__main__':
    torch.set_default_tensor_type('torch.cuda.FloatTensor')
    cfg_datasets = dataset_config()
    cfg_warmup = warmup_training_config()
    cfg_dataset = cfg_datasets[cfg_warmup.dataset]
    cfg_warmup.update(cfg_dataset)
    print(cfg_warmup.dump())
    trainer = Trainer(cfg_warmup)
    exit()
    trainer.train()
