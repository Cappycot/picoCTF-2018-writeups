Warmup 1
========
0x41 in hex is 16 * 4 + 1 = 65 in dec, which is 'A' in ASCII.

picoCTF{A}

Warmup 2
========
27 in base 10...

27 % 2 = 1
13 % 2 = 1
6 % 2 = 0
3 % 2 = 1
1 % 2 = 1
Stop and go from top down.

picoCTF{11011}

Warmup 3
========
0x3D in hex is 16 * 3 + 13 = 61 in dec.

picoCTF{61}

Resources
=========
They just give you this one at their provided link.
"谢谢你来这里！" Pretty much translates to: "Thanks for visiting!"

picoCTF{xiexie_ni_lai_zheli}

Note
====
The given flags in this writeup may not work since they might have different sets of trailing hexadecimal characters for different users.

grep 1
======
Download the given file. It is plaintext.

This is not a flag that deviates from the ``picoCTF{some_l33tsp34k_phrase}`` format.
```
# grep picoCTF file
picoCTF{grep_and_you_will_find_cdf2e7c2}
```
You heard the man.

picoCTF{grep_and_you_will_find_cdf2e7c2}

Net Cat
=======
From the ``-h`` argument for netcat: ``connect to somewhere: nc [-options] hostname port[s] [ports] ...``
```
# nc 2018shell3.picoctf.com 49387
That wasn't so hard was it?
picoCTF{NEtcat_iS_a_NEcESSiTy_8b6a1fbc}
```
They literally give you the full hostname and port in later problems. You just need to type ``nc`` before it all.

picoCTF{NEtcat_iS_a_NEcESSiTy_8b6a1fbc}

strings
=======
Computers do a good job separating slightly worse junk from slightly better junk. Download the plaintext file.
```
# strings strings
*LOTS OF OUTPUT*
```
Whoops. But remembered what we learned from a previous task?
```
# strings strings | grep picoCTF
picoCTF{sTrIngS_sAVeS_Time_d7c8de6c}
```

picoCTF{sTrIngS_sAVeS_Time_d7c8de6c}

Pipe
====
Either funnel the netcat results into a new file, or pipe it into a grep. Your choice.
```
# nc 2018shell3.picoctf.com 37542 | grep picoCTF
picoCTF{almost_like_mario_a6975cdb}
```

picoCTF{almost_like_mario_a6975cdb}

grep 2
======
Honestly, grep is pretty OP since you can tell it to work like a find command.

Working in their given shell:
```
$ cd /problems/grep-2_0_783d3e2c8ea2ebd37
99ca6a5d28fc742/files
$ ls
files0  files1  files2  files3  files4  files5  files6  files7  files8  files9
```
From the grep ``-h`` argument: ``-r, --recursive like --directories=recurse``
```
$ grep -r picoCTF
files2/file2:picoCTF{grep_r_and_you_will_find_24c911ab}
```

picoCTF{grep_r_and_you_will_find_24c911ab}

Aca-Shell-A
===========
Time for a Linux shellventure!
```
# nc 2018shell3.picoctf.com 27833
```
Navigation through the simulated shell is a bit wonky since you have to backtrack with ``cd`` before moving into a different folder, so ``$ cd ../passwords`` has to be run as ``$ cd ..`` followed by ``$ cd passwords``.

First navigate to the secret folder and delete all their intel.
```
$ cd secret
$ ls
$ rm i*
```
The agent asks for you to echo "Drop it in!" and run the provided script:
```
$ echo "Drop it in!"
$ cd ..
$ cd executables
$ ./dontLookHere
```
The agent asks you to print the username of the current account:
```
$ whoami
```
Finally, copy a file from the /tmp directory and read it.
```
$ cp /tmp/TopSecret ../passwords
$ cd ..
$ cd passwords
$ cat TopSecret
```

picoCTF{CrUsHeD_It_17ab99f5}

Environ
=======
So they say that this flag is hidden in an environment variable.

I'm a lazy man. I look through everything at once.
```
$ export | grep pico
declare -x SECRET_FLAG="picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}"
```

picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}

ssh-keyz
========
Tutorial: https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html

And copy your .pub key into your ``~/.ssh/authorized_keys`` file.

Well, technically you can just ssh and get the flag anyway from the login banner since it displays regardless.

```
# ssh 2018shell3.picoctf.com
picoCTF{who_n33ds_p4ssw0rds_38dj21}
password:
```

picoCTF{who_n33ds_p4ssw0rds_38dj21}

What Base is This?
==================
So for the longest time I thought "word" meant hexadecimals grouped by 32-byte segments rather than the plain English thing.
```
# nc 2018shell3.picoctf.com 1225
```
Example sites to use for conversions:
https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html for binary and hex.
http://www.unit-conversion.info/texttools/octal for octal.

The binary answer is provided for some reason, but you'll have to decode the hexadecimal one and then the octal one.

Example:
```
We are going to start at the very beginning and make sure you understand how data is stored.
stitch
Please give me the 01110011 01110100 01101001 01110100 01100011 01101000 as a word.
To make things interesting, you have 30 seconds.
Input:
stitch
Please give me the 77696368697461 as a word.
Input:
wichita
Please give me the  163 164 151 164 143 150 as a word.
Input:
stitch
You got it! You're super quick!
```

picoCTF{delusions_about_finding_values_451a9a74}

You Can't See Me
================
*It's the franchise baby I'm shining now!*

```
$ cd /problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69
$ ls -l
total 0
```
Hmm... nothing. Well we know something's here.
```
$ ls -la
total 60
drwxr-xr-x   2 root       root        4096 Sep 28 08:35 .
-rw-rw-r--   1 hacksports hacksports    57 Sep 28 08:35 .  
drwxr-x--x 571 root       root       53248 Sep 30 03:52 ..
```
The damn file name is literally a dot followed by some spaces. There are several ways you can get this file to cat, but you'll still need to explicitly specify the current directory because of how the Unix filesystem works.
```
$ cat /problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69/.\ \  
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}
$ cat ./.\ \  
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}
$ cat .*
cat: .: Is a directory
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}
cat: ..: Permission denied
```
The first one uses the absolute path, the second one uses the relative path, and the last one uses the Kleene Star to brute force the thing lol.

picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}

Absolutely Relative
===================
So first we navigate to the directory and see what's there.
```
$ cd /problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6
$ ls -l
total 20
-rwxr-sr-x 1 hacksports absolutely-relative_0 8984 Sep 28 07:43 absolutely-relative
-rw-rw-r-- 1 hacksports hacksports             796 Sep 28 07:43 absolutely-relative.c
-r--r----- 1 hacksports absolutely-relative_0   37 Sep 28 07:43 flag.txt
```
While it's not visible here, the absolutely-relative program has the set GID bit set (description may be inaccurate), meaning it is able to read the "flag.txt" file while we can't. May as well look at the source file. Your most interesting two lines are:
```C
file = fopen("/problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/flag.txt" , "r");
file = fopen( "./permission.txt" , "r");
```
It's notable that this program uses both absolute and relative paths to open different files, and it's also interesting that there isn't even a "permissions.txt" file in the same directory as "flag.txt". It's like they're asking for us to write our own.

What should we be writing? Several other lines in the code tell us:
```C
const char *yes = "yes";
if (!strncmp(permission, yes, yes_len)) {
```
So I guess they want us to write "yes" in the "permission.txt" file.

Take note of the directory where this program is and go back home.
```
$ cd ~
$ echo "yes" >permission.txt
$ /problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/absolutely-relative
You have the write permissions.
picoCTF{3v3r1ng_1$_r3l3t1v3_befc0ce1}
```

picoCTF{3v3r1ng_1$_r3l3t1v3_befc0ce1}

In Out Error
============
Navigate to the problem:
```
$ cd /problems/in-out-error_3_9eb10797d687f70cfce62e7c9c2bdea6
$ ls -l
total 20
-r--r----- 1 hacksports in-out-error_3    36 Sep 28 07:52 flag.txt
-rwxr-sr-x 1 hacksports in-out-error_3 13456 Sep 28 07:52 in-out-error
```
Running the "in-out-error" program and asking nicely yields us garbage. We need to separate the primary output (1) stream from the error output (2) stream. So one of the following will do:
```
$ ./in-out-error >/dev/null
$ ./in-out-error 2>/dev/null
```
Well it turns out the latter gives us the same dead meme the web buttons problem gave us, so the first one is right, and the flag is coming out of the error stream.

picoCTF{p1p1ng_1S_4_7h1ng_437b5c88}











Store
=====
```
# nc 2018shell3.picoctf.com 53220
```
This takes us to a cute shop where we can buy 1 imitation flag before going broke, unless we overflow the integers the program uses.
```C
int total_cost = 0;
total_cost = 1000*number_flags;
```
Based on the maximum positive value of an integer, we can overflow the cost by buying at least 2147484 flags, but we'll need to buy more to prevent our actual cash from also overflowing into the negative. 3000000 flags should do the trick.
```
Imitation Flags cost 1000 each, how many would you like?
3000000

Your total cost is: -1294967296

Your new balance: 1294968396
```
Then buy the real flag like normal.

picoCTF{numb3r3_4r3nt_s4f3_cbb7151f}


