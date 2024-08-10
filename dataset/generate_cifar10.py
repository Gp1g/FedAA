import numpy as np
import os
import sys
import random
import torch
import torchvision
import torchvision.transforms as transforms
from dataset_utils import check, separate_data, split_data, save_file

random.seed(1)
np.random.seed(1)
num_clients = 100
num_classes = 10
dir_path = "./Cifar10/"


# Allocate data to users
def generate_cifar10(dir_path, num_clients, num_classes, niid, balance, partition):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Setup directory for train/test data
    config_path = dir_path + "config.json"
    train_path = dir_path + "train/"
    test_path = dir_path + "test/"

    if check(config_path, train_path, test_path, num_clients, num_classes, niid, balance, partition):
        return

    # Get Cifar10 data
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    trainset = torchvision.datasets.CIFAR10(
        root=dir_path + "rawdata", train=True, download=True, transform=transform)
    testset = torchvision.datasets.CIFAR10(
        root=dir_path + "rawdata", train=False, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=len(trainset.data), shuffle=False)
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=len(testset.data), shuffle=False)

    for _, train_data in enumerate(trainloader, 0):
        trainset.data, trainset.targets = train_data
    for _, test_data in enumerate(testloader, 0):
        testset.data, testset.targets = test_data

    dataset_image = []
    dataset_label = []

    dataset_image.extend(trainset.data.cpu().detach().numpy())
    dataset_image.extend(testset.data.cpu().detach().numpy())
    dataset_label.extend(trainset.targets.cpu().detach().numpy())
    dataset_label.extend(testset.targets.cpu().detach().numpy())
    dataset_image = np.array(dataset_image)
    dataset_label = np.array(dataset_label)

    x_server, y_server, dataset_image, dataset_label = generate_server_test(dataset_image, dataset_label, num_classes)
    X, y, statistic = separate_data((dataset_image, dataset_label), num_clients, num_classes,
                                    niid, balance, partition)
    train_data, test_data = split_data(X, y)
    save_file(config_path, train_path, test_path, train_data, test_data, x_server, y_server, num_clients, num_classes,
              statistic, niid, balance, partition)

def generate_server_test(dataset_image, dataset_label, num_classes):
    x = []
    y = []
    for i in range(num_classes):
        idx = [dataset_label == i][0]
        idx = [index for index, value in enumerate(idx) if value][:100]
        x.extend(dataset_image[idx])
        y.extend(np.repeat(i, 100))
        dataset_image = np.delete(dataset_image, idx, axis=0)
        dataset_label = np.delete(dataset_label, idx, axis=0)
    x = np.vstack([inner_data for inner_data in x]).reshape(1000, 3, 32, 32)
    y = np.vstack([inner_data for inner_data in y]).reshape(-1)

    return x, y, dataset_image, dataset_label

if __name__ == "__main__":

    niid = True
    balance = False
    partition = 'dir'
    generate_cifar10(dir_path, num_clients, num_classes, niid, balance, partition)
