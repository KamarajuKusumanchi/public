#! /usr/bin/env python3

import paramiko
import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser(description='Use scp to copy a file by specifying a password on the command line.')
    parser.add_argument('username', action='store', help='username')
    parser.add_argument('hostname', action='store', help='hostname')
    parser.add_argument('src_file', action='store', help='file to copy')
    parser.add_argument('dest_dir', action='store', help='destination directory')
    parser.add_argument('password', action='store', help='password')
    return parser

def copy_file(args):
    username = args.username
    hostname = args.hostname
    src_file = '\\C\\Users\\kusuman\\x\\junk3.csv'
    # src_file = os.path.expanduser(args.src_file)
    dest_dir = args.dest_dir
    password = args.password

    # using sample code from https://stackoverflow.com/a/53618099
    ssh_client = paramiko.SSHClient()
    ssh_client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    # To avoid an "unknown hosts" error.
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=password)
    command = "scp " + src_file + ' '  + username + '@' + hostname + ":"+ dest_dir
    # command = 'ls'
    print(command)
    # channel = ssh_client.get_transport().open_session()
    # channel.exec_command(command)
    # exit_status = channel.recv_exit_status()
    # if exit_status != 0:
    #     stderr = channel.recv_stderr(5000)
    #     print(stderr)
    #     print('Something went wrong!')
    # else:
    #     print('Successful')

    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read()
    print(output)
    error = stderr.read()
    print(error)
    ssh_client.close()


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    copy_file(args)