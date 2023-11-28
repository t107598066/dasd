import os

import sys

import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)

import cv2
import torch
from torch.utils.data import DataLoader
import torch.optim as optim
from torch.nn import CTCLoss

from dataset import Synth90kDataset, synth90k_collate_fn
from model import CRNN
from evaluate import evaluate
from config import train_config as config

def train():
    print("crnn_train")


if __name__ == "__main__":
    train()