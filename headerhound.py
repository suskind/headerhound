#!/usr/bin/env python3

import argparse
from config.config import file_signatures

parser = argparse.ArgumentParser(prog='headerhound', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('type', choices=['list', 'add', 'show', 'match'],
help='''
Required action type
  list: List all file signatures (use "| grep" and "--all" to help you)
      Ex: 
        $> {0} list | grep -i pdf
        71 - [25 50 44 46 2d] - (pdf) 

        $> {0} list --all | grep -i pdf
        71 - [25 50 44 46 2d] - (pdf) - PDF document
  add: Add file signature
      Ex:
        $> {0} add -f input_file -o output_file -s pdf
        Adding signature [25 50 44 46 2d] has been done.

        $> {0} add -f input_file -o output_file -sn 71
        Adding signature [25 50 44 46 2d] has been done.
  show: (TODO) Show exact match file signature from the input file
      Ex: 
        $> {0} show -f input_file
  match: (TODO) Try to find the best signature match for the input file. Useful to find reversing obfuscation.
      Ex:
        $> {0} match -f input_file

'''.format(parser.prog))
parser.add_argument('-f', '--file',  help='Input file', type=argparse.FileType('r+b'))
parser.add_argument('-o', '--output', help='Output file', type=argparse.FileType('w+b'))
parser.add_argument('-s', '--signature', 
                    help='Signature - header signature type ex: -s pdf (in case of multiple signatures, the first one will be used. See -sn option)', type=str)
parser.add_argument('-sn', '--signature-number',  dest='signature_number', help='Signature number', type=int)
parser.add_argument('--all', help='List with description', nargs='?', type=bool, default=False)

args = parser.parse_args()

# print(parser.prog)
# print('type => ' + str(args.type))
# print('file => ' + str(args.file))
# print('output => ' + str(args.output))
# print('signature => ' + str(args.signature))
# print('signature number => ' + str(args.signature_number))
# print('all => ' + str(args.all))
# print(str(file_signatures))

def list_signatures():
  count = 0
  for obj in file_signatures:
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
      obj = file_signatures[args.signature_number]
    else:
      print('Signature number not found')
      return
  elif args.signature != None:
    obj = None
    for item in file_signatures:
      if item['extension'] and args.signature.upper() in (x.upper() for x in item['extension']):
        obj = item
        break
    if obj == None:
      print('No signature has been found for term "{0}". Try with "list --all | grep -i {0}"'.format(args.signature))
      return

  sign = obj['signature']
  offset = obj['offset']
  if obj['variable']:
    print('This signature [{0}] is variable, can\'t be added. Use (TODO feature)'.format(sign))
    return
  a_sign = sign.split(' ')
  fr_content = args.file.read()
  sign_as_bytes = bytes.fromhex(''.join(a_sign))
  args.output.seek(offset)
  args.output.write(sign_as_bytes)
  args.output.write(fr_content)
  print('Adding signature [{0}] has been done.'.format(sign))


def main():
  if args.type == 'list':
    list_signatures()
    return 0
  if args.type == 'add':
    if args.file is None or args.output is None or (args.signature is None and args.signature_number is None):
      parser.print_help()
      return 1
    add_signature()
    return 0
  elif args.type == 'show':
    if args.file is None:
      parser.print_help()
      return 1
    else:
      print('TODO - Show exact signature match')
  elif args.type == 'match':
    if args.file is None:
      parser.print_help()
      return 1
    else:
      print('TODO - Show best match')

if __name__ == '__main__':
  main()
