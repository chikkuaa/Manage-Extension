'''
Author: Sanjeev Jha
Email-id: sanjeev0390jha@gmail.com
Version: 1.2
'''

import re

extensions_set=set()
pattern='\.\w*$'
f=open("dirlist.txt","r") # File containing directory listing
f2=open("Other.txt","a")

print "[+] Bucketing extensions in File.........\n"

for var in f.readlines():
    match=re.search(pattern,var.strip())

    if match:
        extensions=match.group(0) # Returns matched character from the Regex used
        
        if extensions.lower() in ['.jpg','.jpeg','.ico','.ttf','.woff','.svg','.png','.gif','.eot','.htc','.flv','.mp3','.mp4','.3gp']:
            media_files=open("Media-files.txt","a")
            media_files.writelines(var)
        elif extensions.lower()in ['.doc','.txt','.docx','.pdf','.xls']:
            doc_files=open("documents.txt","a")
            doc_files.writelines(var)
            
        else:
            file_pointer=extensions[1:]
            file_pointer=open(extensions[1:]+".txt","a")
            file_pointer.writelines(var)
	            
    else:
        f2.writelines(var)

f2.close()
