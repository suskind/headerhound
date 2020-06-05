# headerhound
Add, find and reverse file's headers

```
$ ./headerhound.py show -h
usage: headerhound [-h] [-f FILE] [-o OUTPUT] [-s SIGNATURE] [-sn SIGNATURE_NUMBER] [--all [ALL]] {list,add,show,match}

positional arguments:
  {list,add,show,match}
                        
                        Required action type
                          list: List all file signatures (use "| grep" and "--all" to help you)
                              Ex: 
                                $> headerhound list | grep -i pdf
                                71 - [25 50 44 46 2d] - (pdf) 
                        
                                $> headerhound list --all | grep -i pdf
                                71 - [25 50 44 46 2d] - (pdf) - PDF document
                          add: Add file signature
                              Ex:
                                $> headerhound add -f input_file -o output_file -s pdf
                                Adding signature [25 50 44 46 2d] has been done.
                        
                                $> headerhound add -f input_file -o output_file -sn 71
                                Adding signature [25 50 44 46 2d] has been done.
                          show: (TODO) Show exact match file signature from the input file
                              Ex: 
                                $> headerhound show -f input_file
                          match: (TODO) Try to find the best signature match for the input file
                              Ex:
                                $> headerhound match -f input_file
                        

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file
  -o OUTPUT, --output OUTPUT
                        Output file
  -s SIGNATURE, --signature SIGNATURE
                        Signature - header signature type ex: -s pdf (in case of multiple signatures, the first one will be used. See -sn option)
  -sn SIGNATURE_NUMBER, --signature-number SIGNATURE_NUMBER
                        Signature number
  --all [ALL]           List with description
  ```