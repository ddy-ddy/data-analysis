# -*- coding: utf-8 -*-
# @Time    : 2023/9/1 16:25
# @Author  : ddy
# @FileName: utility.py
# @github  : https://github.com/ddy-ddy


import pickle
import pandas as pd

seed = 0

def load_model(path: str) -> pickle:
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def save_model(model: pickle, path: str):
    with open(path, "wb") as f:
        pickle.dump(model, f)


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def save_data(path: str, data: pd.DataFrame):
    data.to_csv(path, index=False)
