from dataclasses import dataclass, field
from typing import List


@dataclass
class Config:
    # dataset
    dataset_dir: str = "./datasets"
    dataset_name: str = "cifar10"
    num_workers: int = 4

    # model
    nz: int = 100
    ngf: int = 64
    ndf: int = 64
    loss_type: str = "gan"  # "hinge", "ns", "gan", "wasserstein"
    vq_type: str = "Normal"  # "Normal"
    dict_size: int = 10
    quant_layers: List = field(default_factory=lambda: [3])

    # optimizer
    lrD: float = 2e-4
    lrG: float = 2e-4
    beta1: float = 0.0
    beta2: float = 0.9

    # training
    batch_size: int = 64
    n_dis: int = 4
    num_steps: int = 100000
    is_amp: bool = True
    opt_level: str = "O1"

    # evaluation
    metric: str = 'fid'
    num_real_samples: int = 10000
    num_fake_samples: int = 10000
    evaluate_step: int = 100000

    # logging
    log_dir: str = "./logs/fqgan_32_64d_64d"

    @property
    def betas(self):
        return (self.beta1, self.beta2)
