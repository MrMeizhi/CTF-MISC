# CTF-MISC

ctf-misc记录板

http://www.shiyanbar.com/ctf/53
broken.img
软盘扇区,FAT12


http://www.shiyanbar.com/ctf/22
这个日志审查了很久但是然并卵，又是看代码啥的，其实更多的时候应该把精力集中在日志上面，试图去分析行为吧，因为如果还要结合代码的话，可能时间会非常的长，一般的ctf做题时间都不会太长。
当然最后还是翻了writeup，想了一下收获还蛮多的。
如果日志量大的话，主要是针对敏感点就行：sql注入，文件遍历，任意文件读取，任意文件下载，敏感后台地址。
而这道ctf的分析中，可以发现，忽然间phpmyadmin被大量访问，再加上前面出现的任意文件读取，并且其状态码为200可以判断为某些文件被读取到了。
同样的道理，其实sql注入，及其注入之后的状态请求都可以关注的。


http://www.shiyanbar.com/ctf/742
又是这种数据包的问题，其实流量分析一直是我的弱项。这种类型的题以前也做过，但是记得不太清楚了，今天再次拿到这种题大概思路是要提取数据
感觉又是一个坑，又得编程写大量的代码。当然熟悉原理才是最重要的，编程只是一个工具而已。
哎呀 writeup也不想看了，代码逻辑写得太不清楚了，于是我决定用一下别人说的工具。Dshell，github地址是：https://github.com/USArmyResearchLab/Dshell
安装完成以后，运行:ecode -d rip-http data
可以得到一个文件，用winhex这类型工具打开发现，头部缺少格式，然后按照常规套路，我给它加上了png的头部0x89504E470D0A1A0A，然后重新打开，坑爹，居然不行????难道还有更加深的套路?emmmmmm，若有所思。然后实在不行再看了下writeup，发现writeup写的是89504E470D0A1A0A0000000D49，嗯? exo me?
