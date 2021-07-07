import argparse

import numpy as np

from packaging import version

import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="2,3"
from PIL import Image
import matplotlib.pyplot as plt
import cv2
from skimage.transform import rotate
import torch
from torch.autograd import Variable

import torch.nn as nn
from torch.utils import data

from models.unet import UNet
from dataset.refuge import REFUGE

NUM_CLASSES = 3
NUM_STEPS = 512 # Number of images in the validation set.
RESTORE_FROM = '/home/charlietran/CADA_Tutorial/Model_Weights/Trial1/UNet1000_v18_weightedclass.pth'
SAVE_PATH = '/home/charlietran/CADA_Tutorial/result/Trial1/'
MODEL = 'Unet'
BATCH_SIZE = 1
is_polar = False  #If need to transfer the image and labels to polar coordinates: MICCAI version is False
ROI_size = 700  #ROI size
from evaluation.evaluation_segmentation import *


print(RESTORE_FROM)

palette=[
    255, 255, 255, # black background
    128, 128, 128, # index 1 is red
    0, 0, 0, # index 2 is yellow
    0, 0 , 0 # index 3 is orange
]

zero_pad = 256 * 3 - len(palette)
for i in range(zero_pad):
    palette.append(0)


def colorize_mask(mask):
    # mask: numpy array of the mask
    new_mask = Image.fromarray(mask.astype(np.uint8)).convert('P')
    new_mask.putpalette(palette)

    return new_mask

def get_arguments():
    """Parse all the arguments provided from the CLI.
    Returns:
      A list of parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Unet Network")
    parser.add_argument("--model", type=str, default=MODEL,
                        help="Model Choice Unet.")
    parser.add_argument("--num-classes", type=int, default=NUM_CLASSES,
                        help="Number of classes to predict (including background).")
    parser.add_argument("--restore-from", type=str, default=RESTORE_FROM,
                        help="Where restore model parameters from.")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE,
                        help="Number of images sent to the network in one step.")
    parser.add_argument("--gpu", type=int, default=0,
                        help="choose gpu device.")
    parser.add_argument("--save", type=str, default=SAVE_PATH,
                        help="Path to save result.")
    parser.add_argument("--is_polar", type=bool, default=False,
                        help="If proceed images in polar coordinate. MICCAI version is false")
    parser.add_argument("--ROI_size", type=int, default=460,
                        help="Size of ROI.")

    parser.add_argument('--t', type=int, default=3, help='t for Recurrent step of R2U_Net or R2AttU_Net')

    return parser.parse_args()


def main():
    """Create the model and start the evaluation process."""

    args = get_arguments()

    gpu0 = args.gpu

    if not os.path.exists(args.save):
        os.makedirs(args.save)

    model = UNet(3, n_classes=args.num_classes)

    saved_state_dict = torch.load(args.restore_from)
    model.load_state_dict(saved_state_dict)

    model.cuda(gpu0)
    model.train()

    testloader = data.DataLoader(REFUGE(False, domain='REFUGE_TEST', is_transform=True),
                                    batch_size=args.batch_size, shuffle=False, pin_memory=True)


    if version.parse(torch.__version__) >= version.parse('0.4.0'):
        interp = nn.Upsample(size=(ROI_size, ROI_size), mode='bilinear', align_corners=True)
    else:
        interp = nn.Upsample(size=(ROI_size, ROI_size), mode='bilinear')

    for index, batch in enumerate(testloader):
        if index % 100 == 0:
            print('%d processd' % index)
        image, label, _, _, name = batch
        if args.model == 'Unet':
            _,_,_,_, output2  = model(Variable(image, volatile=True).cuda(gpu0))

            output = interp(output2).cpu().data.numpy()


        for idx, one_name in enumerate(name):
            pred = output[idx]
            pred = pred.transpose(1,2,0)
            pred = np.asarray(np.argmax(pred, axis=2), dtype=np.uint8)
            output_col = colorize_mask(pred)

            print(output_col.size)
            one_name = one_name.split('/')[-1]
            output_col = output_col.convert('L')
            output_col.save('%s/%s.bmp' % (args.save, one_name))


if __name__ == '__main__':
    main()
    results_folder = SAVE_PATH
    gt_folder = '/DATA/charlie/AWC/CADA_Tutorial_Image/Target_Test/mask/'
    output_path = results_folder
    export_table = True
    evaluate_segmentation_results(results_folder, gt_folder, output_path, export_table)

