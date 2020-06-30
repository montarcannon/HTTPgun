#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 2020

@author: TheM0ntarCann0n
"""
import sys
import urllib.request



print ('If you dont know how to use this script.');
print ('Check GitHub readme https://github.com/montarcannon/mcrepo branch httpgun');
print ('');
try:
    args = sys.argv;
    shooted1 = str(args[1]);
    shooted2 = str(args[2]);
    wordaddr = str(args[3]);
    outfile = str(args[4]);
    printout = int(args[5]);
    saveout = int(args[6]);
    endurl = int(args[7]);
except:
    print('something missing for example parameter');
    exit();
outfileread = open(outfile, 'w');
try:
    wordlist = open (wordaddr, 'r');
except:
    print('specifid wordlist does not exsist or python cant read it');
    exit();
words = wordlist.readlines();

#print(words);
#response = open('tmp.txt','w');
#response.write('only errors');

words[:] = [words.rstrip('\n') for words in words]
counter = 0;

if saveout > 0:
    out = open(outfile, 'w');
    out.close();
    out = open(outfile, 'a');
    print ('beeteven multiple responses are printed newlines');
print ('[*]using wordlist:',wordaddr);
wordscount =  len(words);
#print(shooted1,'',shooted2);
while wordscount > counter :
    fullurl = (shooted1 + words[counter] + shooted2);
    if endurl > 0:
        fullurl = (shooted1 + words[counter]);
    
        
    print('[*]full reqest:',fullurl);    
    
    counter += 1;
    #words[counter].split('\n');
    req = urllib.request.Request(fullurl);
    #print(req,fullurl);
    try :
        response = urllib.request.urlopen(req)
        print('[+]OK');
        print('');
        html = response.read();
    except:
        print('[-]ERROR!');
        html = ('ERROR!');
        print('');
    
    
    if printout > 0 :
        print('response:');
        print(html);
    if saveout > 0 :
        #out.write('\n\n\n resp number'counter'of'wordcount'\n\n\n\n');
        out.write(str(html));
        out.write('\n \n \n \n \n \n');
        
        
        
