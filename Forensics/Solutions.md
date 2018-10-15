Warmup 1
========
If you don't have some archive program I can't help you.

picoCTF{welcome_to_forensics}

Warmup 2
========
Yeah yeah Windows Photo Viewer will bitch at you for this one, but look at this...
```
# file flag.png
flag.png: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 909x190, frames 3
```
Right. Just rename the extension.

picoCTF{extensions_are_a_lie}

Desrouleaux
===========
Just some 2 + 2 = 4, 4 - 1 = 3 quick maths. As usual, these values will be unique for each user.
```
# nc 2018shell3.picoctf.com 40952
```

Example:

Most common src:
189.230.108.137

Unique dests:
189.230.108.137: 3
196.222.158.128: 1
200.151.133.181: 1
208.10.169.130: 2
221.20.104.205: 2

File uniques:
27b42b2ca046b607: 1
6ce1b25511b09e68: 2
7e09e3669f4ff472: 1
a71a2bd84ee0fd4c: 1
cefffcb6651bfac0: 2
cf17e710b1a850c7: 2
fc5f9561bc2e42b2: 1
Average: 1.43

picoCTF{J4y_s0n_d3rUUUULo_b6cacd6c}

Recovering From the Snap
========================
I used testdisk for this one. This appears to be a simple disk image that isn't really corrupted.
```
# testdisk animals.dd

>Disk animals.dd - 10 MB / 10 MiB

>[None   ] Non partitioned media

>[ Analyse  ] Analyse current partition structure and search for lost partitions

>[Quick Search]

Disk animals.dd - 10 MB / 10 MiB - CHS 10 64 32
     Partition               Start        End    Size in sectors
>P FAT16                    0   0  1     9  63 32      20480 [NO NAME]

Keys T: change type, P: list files,
```
At this point hit the 'P' key and look what we have here. Half of the files are marked in red. Perfectly balanced, as all things should be. Navigate down to the flag file ("theflag.jpg") and hit the c key to copy it to whatever directory you want.
```
   P FAT16                    0   0  1     9  63 32      20480 [NO NAME]
Directory /

 -rwxr-xr-x     0     0    632333 25-Jul-2018 00:01 dachshund.jpg
 -rwxr-xr-x     0     0    493564 25-Jul-2018 00:01 fox.jpg
 -rwxr-xr-x     0     0    389187 25-Jul-2018 00:01 frog.jpg
 -rwxr-xr-x     0     0    254837 25-Jul-2018 00:01 giraffe.jpg
 -rwxr-xr-x     0     0    321758 25-Jul-2018 00:01 music.jpg
 -rwxr-xr-x     0     0    469105 25-Jul-2018 00:01 rabbit2.jpg
 -rwxr-xr-x     0     0    393003 25-Jul-2018 00:01 rabbit.jpg
>-rwxr-xr-x     0     0     40384 25-Jul-2018 00:01 theflag.jpg
```

picoCTF{th3_5n4p_happ3n3d}

Admin Panel
===========
Download the file and open it in Wireshark. Search for the login POST event.

You'll find something along the lines of:
```
Host: 192.168.3.128
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.3.128/
Content-Type: application/x-www-form-urlencoded
Content-Length: 53
Connection: keep-alive
Upgrade-Insecure-Requests: 1

user=admin&password=picoCTF{n0ts3cur3_13597b43}
```
picoCTF{n0ts3cur3_13597b43}

Hex Editor
==========
Lemme be honest. They shouldn't have put the flag at the end. Of course, first download cat picture because that's what the internet is for: cats, not porn.

Now look here. I know there are a lot of hex editors out there, but I'm lazy and the system knows it... so...
```
# strings hex_editor.jpg | tail -n 1
Your flag is: "picoCTF{and_thats_how_u_edit_hex_kittos_8BcA67a2}"
```
(For brevity purposes I chained it to tail.)

picoCTF{and_thats_how_u_edit_hex_kittos_8BcA67a2}

What's My Name?
===============
Download the file and open it in Wireshark. We are looking for information regarding websites identifying themselves... namely DNS stuff.

picoCTF{w4lt3r_wh1t3_2d6d3c6c75aa3be7f42debed8ad16e3b}



Truly an Artist
===============
Treat this image like any ARG image. Man I loved Ingress in its first year even though I was in high school without a driver's license and couldn't go anywhere.

Download the image file and peek into any metadata viewer, like http://exif.regex.info/exif.cgi

As the title says, the flag is in the artist field.

picoCTF{look_in_image_7e31505f}

Now You Don't
=============
Download the image that seems to be all red. Use GIMP or Photoshop to use the magic wand with 0 threshold/tolerance. Color the selected area for clarity if needed.

picoCTF{n0w_y0u_533_m3}


