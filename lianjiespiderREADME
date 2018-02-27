这个爬虫和yemianspider.py的思路是一样，但在获取图片网页链接的时候不一样，我们发现各个图片的地址有规律，所以我们就可以通过这个规律来得到各个图片的地址。
首先是图片首页的地址是"https://www.1102d.com/Html/63/index.html"，其他的地址都是"https://www.1102d.com/Html/63/index-%d.html"%i，i为2-181，
这样我们可以将所有的地址存在一个列表里，通过遍历列表来获取地址。具体的方式如下：
    list=[]
    url1=r"https://www.1102d.com/Html/63/index.html"
    list.append(url1)
    for i in range(2,182):
        url=r"https://www.1102d.com/Html/63/index-%d.html"%i
        list.append(url)
    for i in list[::-1]:
        frist(i)
具体代码见lianjiespider.py
其他的代码原理在yemianspider.py上。
