#!/usr/bin/env python3

import argparse
from config.config import file_signatures

parser = argparse.ArgumentParser(prog='headerhound', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('type', choices=['add', 'show', 'match', 'list'],
help='''
Required action type \n
  list: List all file signatures (use | grep to help you)
  show: Show exact match file signature from input file
      Ex: 
        show -f input_file
  add: Add file signature
      Ex:
        add -f input_file -o output_file -s pdf
        add -f input_file -o output_file -sn 34
''')
parser.add_argument('-f', '--file',  help='Input file', type=argparse.FileType('rb'))
parser.add_argument('-o', '--output', help='Output file', type=argparse.FileType('wb'))
parser.add_argument('-s', '--signature', 
                    help='Signature - header signature type ex: -s pdf (in case of multiple signatures, the first one will be used. See -sn option)', type=str)
parser.add_argument('-sn', '--signature-number',  dest='signature_number', help='Sign number', type=int)
parser.add_argument('--all', help='List with description', nargs='?', type=bool, default=False)
# parser.add_argument('-l', '--list', help='list signatures', type=bool, default=False)
# parser.add_argument('-', '--output', help='output file', type=bool)

args = parser.parse_args()

print('type => ' + str(args.type))
print('file => ' + str(args.file))
print('output => ' + str(args.output))
print('signature => ' + str(args.signature))
print('signature number => ' + str(args.signature_number))
print('all => ' + str(args.all))

# print(str(file_signatures))

def list_signatures():
  count = 0
  for obj in file_signatures:
    # if count > 10:
    #   break
    exts = ''
    if obj['extension']:
      exts = ', '.join(obj['extension'])
    description = ''
    if args.all != False:
      description = '- ' + obj['description']
    print('{0} - [{1}] - ({2}) {3}'.format(count, obj['signature'], exts, description))
    count += 1

def add_signature():
  fpRead = args.file
  fpOut = args.output
  sign = None
  if args.signature_number != None:
    if args.signature_number < len(file_signatures) and file_signatures[args.signature_number]:
      sign = file_signatures[args.signature_number]['signature']
    else:
      print('Signature number not found')
      return
    print('Will add signature :: ' + sign)


def main():
  if args.type == 'list':
    print('Will print all the list')
    list_signatures()
    return 0
  if args.type == 'add':
    if args.file is None or args.output is None or (args.signature is None and args.signature_number is None):
      parser.print_help()
      return 1
    add_signature()
    
  elif args.type == 'show':
    if args.file is None:
      parser.print_help()
      return 1
    else:
      print('Show file signature')
  elif args.type == 'match':
    if args.file is None:
      parser.print_help()
      return 1
    else:
      print('show best match')

  

if __name__ == '__main__':
  main()