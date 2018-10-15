Warmup 1
========
The result is ``llkjmlmpadkkc`` and the key being ``thisisalilkey``, you need to use the table in reverse. For each character in the key, find the row with the right letter, then look to the left.

picoCTF{SECRETMESSAGE}

Warmup 2
========
Just use rot13.com for this. It's been here at least since the Enderdragon was added to Minecraft.
cvpbPGS{guvf_vf_pelcgb!}

picoCTF{this_is_crypto!}

HEEEEEEERE'S Johnny!
====================
*Screams and cuts his hand with a knife.*
This one needs John the Ripper and is a nice pun since Johnny is the GUI version of it.
You can very easily feed the provided shadow file (the provided passwd file has no useful information) into Johnny and he will crack it pretty damn quickly because it's one of those crappy passwords found in the infamous ``rockyou.txt`` list of bad passwords. In this case it's ``password1``.
Now just feed it into the netcat.
```
# nc 2018shell3.picoctf.com 40157
Username: root
Password: password1
```

picoCTF{J0hn_1$_R1pp3d_1b25af80}

Caesar Cipher 1
===============
Given: picoCTF{vgefmsaapaxpomqemdoubtqdxoaxypeo}
Shift by 14: picoCTF{justagoodoldcaesarcipherlcolmdsc}

