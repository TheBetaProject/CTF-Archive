# Strong Password
### `Submitted by SpiderPig`

we have a password protected zip.

we can use john the ripper (with hashcat not necceraly) (using dictionary attack with rockyou.txt)
to extract the password.

```
John the Ripper password cracker.
John the Ripper is a fast password cracker, currently available for many flavors of Unix, macOS, Windows, DOS, BeOS, and OpenVMS (the latter requires a contributed patch). Its primary purpose is to detect weak Unix passwords. Besides several crypt(3) password hash types most commonly found on various Unix flavors, supported out of the box are Kerberos/AFS and Windows LM hashes, as well as DES-based tripcodes, plus hundreds of additional hashes and ciphers in "-jumbo" versions.
```
first of all we need to extract the password hash from the zip:
```
➜  Strong password ~/JohnTheRipper/run/zip2john strong_password.zip > hash.txt
```
and now we can just crack the password:
```
➜  Strong password ~/JohnTheRipper/run/john hash.txt --wordlist=rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:16 8.60% (ETA: 15:02:43) 0g/s 85694p/s 85694c/s 85694C/s princess-samy..polly1960
0g 0:00:00:18 9.73% (ETA: 15:02:41) 0g/s 85682p/s 85682c/s 85682C/s luv4bobby..lovence
0g 0:00:00:19 10.27% (ETA: 15:02:42) 0g/s 85620p/s 85620c/s 85620C/s keikeasher..karenkim
0g 0:00:00:20 10.87% (ETA: 15:02:41) 0g/s 85630p/s 85630c/s 85630C/s iloveathena..hutchinson1
0g 0:00:00:21 11.41% (ETA: 15:02:40) 0g/s 85617p/s 85617c/s 85617C/s fish211..farinella
0g 0:00:00:22 12.01% (ETA: 15:02:40) 0g/s 85626p/s 85626c/s 85626C/s cucciola1..coreybear
0g 0:00:00:23 12.56% (ETA: 15:02:40) 0g/s 85614p/s 85614c/s 85614C/s bobby010..bird000
0g 0:00:00:24 13.10% (ETA: 15:02:40) 0g/s 85425p/s 85425c/s 85425C/s alikaynuevaalianza..aizamar
0g 0:00:00:25 13.62% (ETA: 15:02:40) 0g/s 85456p/s 85456c/s 85456C/s GY4317..Daisuke15
0g 0:00:00:27 14.64% (ETA: 15:02:41) 0g/s 85497p/s 85497c/s 85497C/s 250839..23122388
0g 0:00:00:29 15.84% (ETA: 15:02:40) 0g/s 85533p/s 85533c/s 85533C/s zozoraide..zoeefatboy
0g 0:00:00:30 16.46% (ETA: 15:02:39) 0g/s 85543p/s 85543c/s 85543C/s young_g_shay_1..yonsokyen
0g 0:00:00:31 17.03% (ETA: 15:02:39) 0g/s 85536p/s 85536c/s 85536C/s xxxrocks..xtian317
0g 0:00:00:32 17.60% (ETA: 15:02:38) 0g/s 85423p/s 85423c/s 85423C/s winternighter1..wilmarck
0g 0:00:01:09 40.49% (ETA: 15:02:27) 0g/s 85619p/s 85619c/s 85619C/s machia906090..ma9971
0g 0:00:01:33 53.66% (ETA: 15:02:30) 0g/s 83354p/s 83354c/s 83354C/s guia29..gtluvsst
0g 0:00:01:34 54.25% (ETA: 15:02:30) 0g/s 83357p/s 83357c/s 83357C/s gocreds1..gm4il777
0g 0:00:01:35 54.89% (ETA: 15:02:30) 0g/s 83384p/s 83384c/s 83384C/s geass89..gayhubby
0g 0:00:01:36 55.42% (ETA: 15:02:30) 0g/s 83327p/s 83327c/s 83327C/s fundipss1..fucku516
Bo38AkRcE600X8DbK3600 (strong_password.zip/lorem_ipsum.txt)
1g 0:00:02:16 DONE (2021-05-17 15:01) 0.007311g/s 83069p/s 83069c/s 83069C/s Bobo64..Bernie00
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

and we get the password:
`Bo38AkRcE600X8DbK3600`
we unlock the zip and get the flag in the txt file:
`dctf{r0cKyoU_f0r_tHe_w1n}`
=======

>>>>>>> 6f318d3f929f43ea5b6ff1301e3811924212136d
