import os
import sys

def setting():
    print("setting")

    crnn_root_dir = "./opensource/CRNN/"
    dbnet_root_dir = "./opensource/DBNet.pytorch/"

    sys.path.append(os.path.abspath(crnn_root_dir))
    sys.path.append(os.path.abspath(dbnet_root_dir))

    from src.train import train as crnn_train
    from tools.train import train as db_train

    crnn_train()
    db_train()