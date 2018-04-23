# -*- coding: utf-8 -*-
"""
@author: Yan Shao, yan.shao@lingfil.uu.se
"""
import argparse

parser = argparse.ArgumentParser(description='A rule-based sentence segmenter for Chinese. Written by Y. Shao, Uppsala '
                                             'University')

parser.add_argument('-i', '--input', default=None, help='Path of the input file.')
parser.add_argument('-o', '--output', default='output.txt', help='Path of the output file.')

parser.add_argument('-e', '--encoding', default='utf-8', help='Encoding of the input file.')

args = parser.parse_args()

if args.input is None:
    parser.print_help()

else:

    wt = open(args.output, 'w', encoding=args.encoding)

    terminates = {'。', '！', '”', '…', '?', '!', '"', '？'}

    for line in open(args.input, 'r', encoding='utf-8'):
        line = line.strip()
        if len(line) > 0:
            p_line = ''
            for i in range(len(line)):
                p_line += line[i]
                if line[i] in terminates:
                    if i == len(line) - 1:
                        wt.write(p_line + '\n')
                        p_line = ''
                    elif line[i + 1] not in terminates and not terminates.issuperset(set(p_line)):
                        if line[i] == '”' or line[i] == '"':
                            if i > 0 and line[i - 1] in terminates:
                                wt.write(p_line + '\n')
                                p_line = ''
                        else:
                            wt.write(p_line + '\n')
                            p_line = ''

            if len(p_line) > 0:
                wt.write(p_line + '\n')

    wt.close()

