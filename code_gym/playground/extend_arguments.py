#! /usr/bin/env python

import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="extend arguments")
    parser.add_argument(
        '-v', '--verbose', action='store_true', default=False, dest='verbose',
        help='verbose output')
    return parser


def extend_args(args: argparse.Namespace, extra_args: dict) -> argparse.Namespace:
    new_args = argparse.Namespace(**vars(args), **extra_args)
    return new_args


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    if args.verbose:
        print(args)
    args = extend_args(args, {'foo': 9})
    if args.verbose:
        print(args)
