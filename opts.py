""" Define and parse commandline arguments """
import argparse
import os


def parse():
    print('parsing arguments')
    parser = argparse.ArgumentParser(description='PyTorch Charades-Ego Training')
    parser.add_argument('--data', metavar='DIR', default='/scratch/gsigurds/Charades_v1_rgb/', help='path to dataset')
    parser.add_argument('--dataset', default='fake', help='name of dataset under datasets/')
    parser.add_argument('--egocentric-test-data', default='./datasets/labels/CharadesEgo_v0_egocentric_test.csv', help='path to labels for egocentric classification')
    parser.add_argument('--original-charades-train', default='./Charades_v1_train.csv', help='Original Charades Train')
    parser.add_argument('--original-charades-test', default='./Charades_v1_test.csv', help='Original Charades Test')
    parser.add_argument('--train-file', default='./CharadesEgo_v1_train.csv', type=str)
    parser.add_argument('--val-file', default='./CharadesEgo_v1_test.csv', type=str)
    parser.add_argument('--arch', '-a', metavar='ARCH', default='alexnet', help='model architecture: ')
    parser.add_argument('--subarch', default='alexnet')
    parser.add_argument('--subloss', default='MarginRank')
    parser.add_argument('--loss', default='CrossEntropyLoss')
    parser.add_argument('--workers', default=4, type=int, metavar='N', help='# data loading workers (default: 4)')
    parser.add_argument('--epochs', default=20, type=int, metavar='N', help='number of total epochs to run')
    parser.add_argument('--start-epoch', default=0, type=int, metavar='N', help='manual epoch number')
    parser.add_argument('--batch-size', default=256, type=int, metavar='N', help='mini-batch size (default: 256)')
    parser.add_argument('--lr', '--learning-rate', default=1e-3, type=float, metavar='LR', help='initial learning rate')
    parser.add_argument('--lr-decay-rate', default=6, type=int)
    parser.add_argument('--momentum', default=0.9, type=float, metavar='M', help='momentum')
    parser.add_argument('--decay', default=0.9, type=float)
    parser.add_argument('--finaldecay', default=0.9, type=float)
    parser.add_argument('--margin', default=0.0, type=float)
    parser.add_argument('--clsweight', default=1.0, type=float)
    parser.add_argument('--metric', default='wtop1val', help='metric to find best model')
    parser.add_argument('--weight-decay', '--wd', default=1e-4, type=float, metavar='W', help='weight decay (1e-4)')
    parser.add_argument('--print-freq', '-p', default=10, type=int, metavar='N', help='print frequency (10)')
    parser.add_argument('--resume', default='', type=str, metavar='PATH', help='path to latest checkpoint (none)')
    parser.add_argument('--evaluate', dest='evaluate', action='store_true', help='evaluate on val sets')
    parser.add_argument('--pretrained', dest='pretrained', action='store_true', help='use pre-trained model')
    parser.add_argument('--no-logger', dest='no_logger', action='store_true')
    parser.add_argument('--cache-buster', dest='cache_buster', action='store_true')
    parser.add_argument('--valvideo', dest='valvideo', action='store_true')
    parser.add_argument('--valvideoego', dest='valvideoego', action='store_true')
    parser.add_argument('--alignment', dest='alignment', action='store_true')
    parser.add_argument('--usersalignment', dest='usersalignment', action='store_true')
    parser.add_argument('--nopdb', dest='nopdb', action='store_true')
    parser.add_argument('--pretrained-weights', default='', type=str)
    parser.add_argument('--pretrained-subweights', default='', type=str)
    parser.add_argument('--inputsize', default=224, type=int)
    parser.add_argument('--world-size', default=1, type=int, help='number of distributed processes')
    parser.add_argument('--manual-seed', default=0, type=int)
    parser.add_argument('--dist-url', default='tcp://224.66.41.62:23456', type=str, help='url for distributed training')
    parser.add_argument('--dist-backend', default='gloo', type=str, help='distributed backend')
    parser.add_argument('--train-size', default=1.0, type=float)
    parser.add_argument('--val-size', default=1.0, type=float)
    parser.add_argument('--cache-dir', default='./cache/', type=str)
    parser.add_argument('--name', default='test', type=str)
    parser.add_argument('--nclass', default=157, type=int)
    parser.add_argument('--accum-grad', default=4, type=int)
    args = parser.parse_args()
    args.distributed = args.world_size > 1
    args.cache = args.cache_dir + args.name + '/'
    if not os.path.exists(args.cache):
        os.makedirs(args.cache)

    return args
