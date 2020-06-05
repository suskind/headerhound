# headerhound
Add, find and reverse file's headers

```
$> headerhound -h
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

Example: 

```
$ xxd file.php 
00000000: 3c3f 7068 700a 7068 7069 6e66 6f28 293b  <?php.phpinfo();
00000010: 0a3f 3e0a                                .?>.


$ ./headerhound.py add -f file.php -o file.pdf.php -s pdf 
Adding signature [25 50 44 46 2d] has been done.


$ xxd file.pdf.php 
00000000: 2550 4446 2d3c 3f70 6870 0a70 6870 696e  %PDF-<?php.phpin
00000010: 666f 2829 3b0a 3f3e 0a                   fo();.?>.


$ file file.pdf.php 
file.pdf.php: PDF document, version <.p


$ php -f file.pdf.php | head -3
%PDF-phpinfo()
PHP Version => 7.1.23


```


