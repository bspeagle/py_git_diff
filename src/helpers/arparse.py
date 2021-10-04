'''
CLI argument parsing
'''

import argparse

the_parser = argparse.ArgumentParser(prog='github_git_diff',
                                     description='git diff with github'
                                     )

the_parser.add_argument('-t',
                        metavar='token',
                        type=str,
                        help='github personal access token',
                        required=True
                        )

the_parser.add_argument('-o',
                        metavar='organization',
                        type=str,
                        help='github organization',
                        required=False
                        )

the_parser.add_argument('-r',
                        metavar='repo',
                        type=str,
                        help='repository name',
                        required=True
                        )

the_parser.add_argument('-hc',
                        metavar='head-commit',
                        type=str,
                        help='head commit',
                        required=True
                        )

the_parser.add_argument('-bc',
                        metavar='base-commit',
                        type=str,
                        help='base commit',
                        required=True
                        )

args = the_parser.parse_args()
