import argparse

BATCH_SIZE = 1
ITER_SIZE = 1
NUM_WORKERS = 0
INPUT_SIZE = '600, 600'
TGT_SIZE = '500,500'
LEARNING_RATE = 1e-4
MOMENTUM = 0.9
NUM_CLASSES = 3
NUM_STEPS = 250000
NUM_STEPS_STOP = 200000  # early stopping
POWER = 0.9
RESTORE_FROM = ''
SAVE_NUM_IMAGES = 2
SAVE_PRED_EVERY = 1000
SNAPSHOT_DIR = '/home/charlietran/CADA_Tutorial/Model_Weights/Trial1/'
TENSORBOARD_DIR = '/home/charlietran/CADA_Tutorial/tensorboard_directory/Trial1/'
WEIGHT_DECAY = 0.0005
TEACHER_ALPHA = 0.99

LEARNING_RATE_D = 2.5e-5

class_weights=[0.4,0.4,0.2]


def get_arguments():
    """Parse all the arguments provided from the CLI.
    Returns:
      A list of parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Domain Adaptation ")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE,
                        help="Number of images sent to the network in one step.")
    parser.add_argument("--iter-size", type=int, default=ITER_SIZE,
                        help="Accumulate gradients for ITER_SIZE iterations.")
    parser.add_argument("--num-workers", type=int, default=NUM_WORKERS,
                        help="number of workers for multithread dataloading.")
    parser.add_argument("--input-size", type=str, default=INPUT_SIZE,
                        help="Comma-separated string with height and width of source images.")
    parser.add_argument("--tgt-size", type=str, default=TGT_SIZE,
                        help="Comma-separ   ated string with height and width of target images.")
    parser.add_argument("--is-training", action="store_true",
                        help="Whether to updates the running means and variances during the training.")
    parser.add_argument("--learning-rate", type=float, default=LEARNING_RATE,
                        help="Base learning rate for training with polynomial decay.")
    parser.add_argument("--learning-rate-D", type=float, default=LEARNING_RATE_D,
                        help="Base learning rate for discriminator.")
    parser.add_argument("--momentum", type=float, default=MOMENTUM,
                        help="Momentum component of the optimiser.")
    parser.add_argument("--num-classes", type=int, default=NUM_CLASSES,
                        help="Number of classes to predict (including background).")
    parser.add_argument("--num-steps", type=int, default=NUM_STEPS,
                        help="Number of training steps.")
    parser.add_argument("--num-steps-stop", type=int, default=NUM_STEPS_STOP,
                        help="Number of training steps for early stopping.")
    parser.add_argument("--power", type=float, default=POWER,
                        help="Decay parameter to compute the learning rate.")
    parser.add_argument("--random-mirror", action="store_true",
                        help="Whether to randomly mirror the inputs during the training.")
    parser.add_argument("--random-scale", action="store_true",
                        help="Whether to randomly scale the inputs during the training.")
    parser.add_argument("--restore-from", type=str, default=RESTORE_FROM,
                        help="Where restore model parameters from.")
    parser.add_argument("--save-num-images", type=int, default=SAVE_NUM_IMAGES,
                        help="How many images to save.")
    parser.add_argument("--save-pred-every", type=int, default=SAVE_PRED_EVERY,
                        help="Save summaries and checkpoint every often.")
    parser.add_argument("--snapshot-dir", type=str, default=SNAPSHOT_DIR,
                        help="Where to save snapshots of the model.")
    parser.add_argument("--tensorboard-dir", type =str, default= TENSORBOARD_DIR, help="WHERE TO TENSORBOARD")
    parser.add_argument("--weight-decay", type=float, default=WEIGHT_DECAY,
                        help="Regularisation parameter for L2-loss.")
    parser.add_argument("--gpu", type=int, default=0,
                        help="choose gpu device.")
    parser.add_argument("--teacher_alpha", type=float, default=TEACHER_ALPHA,
                        help="Teacher EMA alpha (decay)")
    parser.add_argument('--unsup_weight6', type=float, default= 1,
        help='unsupervised loss weight')
    parser.add_argument('--unsup_weight7', type=float, default= 1,
        help='unsupervised loss weight')
    parser.add_argument('--unsup_weight8', type=float, default= 1,
        help='unsupervised loss weight')
    parser.add_argument('--unsup_weight9', type=float, default= 1,
        help='unsupervised loss weight')
    parser.add_argument('--unsup_weight10', type=float, default=1,
                        help='unsupervised loss weight')
    parser.add_argument("--lambda-adv-tgt6", type=float, default= 1,
                        help="lambda_adv for adversarial training.")
    parser.add_argument("--lambda-adv-tgt7", type=float, default= 1,
                        help="lambda_adv for adversarial training.")
    parser.add_argument("--lambda-adv-tgt8", type=float, default= 1,
                        help="lambda_adv for adversarial training.")
    parser.add_argument("--lambda-adv-tgt9", type=float, default= 1,
                        help="lambda_adv for adversarial training.")
    parser.add_argument("--lambda-adv-tgt10", type=float, default= 1,
                        help="lambda_adv for adversarial training.")
    parser.add_argument('--mse-weight6', type=float, default=1,
                        help='mse weight for discriminative training')
    parser.add_argument('--mse-weight7', type=float, default=1,
                        help='mse weight for discriminative training')
    parser.add_argument('--mse-weight8', type=float, default=1,
                        help='mse weight for discriminative training')
    parser.add_argument('--mse-weight9', type=float, default=1,
                        help='mse weight for discriminative training')
    parser.add_argument('--mse-weight10', type=float, default=1,
                        help='mse weight for discriminative training')



    parser.add_argument("--class_weights", type=float, default=[0.4, 0.4, 0.2],
                        help="segmentation pixel-wise class weights.")

    parser.add_argument('--t', type=int, default=3, help='t for Recurrent step of R2U_Net or R2AttU_Net')

    return parser.parse_args()