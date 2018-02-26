# sihuspider
  四虎网站是一个成人网站，里面有很多的资源可以进行下载，本文将把网站的图片给下载下来。

一、获取图片网页的信息

  首先是获取图片网页的链接 ，我们在图片的主页面上有各个图片的链接和标题，我们可以爬取下载再进行分析

  我们首先通过requests.get（）的方法把网页给爬取下来，这时利用requests.get（）的content属性可以把网页的源代码给显示出来，也可以用text来显示，但content的一个优势就是返回的是二进制数据，而text返回的是unicode型数据。简单来说，就是content不容易乱码，而且也可以获取图片和文件。

    html=requests.get(firsturl)
    #soup=BeautifulSoup(html.text)
    soup = BeautifulSoup(html.content)
    try :
        topurl = soup.find(attrs={'class': 'next pagegbk'})["href"]
    except TypeError:
        return 0

  我们发现网页的最后一页的下一页没有，返回的是一个空值，所以我们直接将最后一个网页作为页面的异常值抛出.接下来我们直接利用BeautifulSoup类型的find_all找出所有的链接。其中有些链接不是图片页面的链接，我们又发现图片链接的地址长度都是一样的，我们可以通过将链接地址大小进行判断，取得图片地址链接。

for link in soup.find_all('a'):
        href=link.get('href')
        l=os.path.join("https://www.1102f.com/",href[1:])
        #title=link.get_text().encode("utf-8")
        title = link.get_text()
        print title
        if len(href) == 19:
            print keep(href,title)

我们还有一个任务就是取得下一页的链接地址。

topurl = soup.find(attrs={'class': 'next pagegbk'})["href"]
二、获取各个图片的链接

  我们现在可以通过上面取得网页的地址来获取各个图片的链接，我们发现图片的地址都是在img的src属性里，我们可以通过上面的方法来获得图片的链接

def single(url,title):
    time.sleep(2)
    html=requests.get(url)
    soup=BeautifulSoup(html.text)
    for link in soup.find_all('img'):
        print link.get（“src”）
三、下载图片

  图片可以通过urllib.urlretrieve(imgurl, path)来保存图片，但通过这种的方式保存的图片无法打开，所以还是要通过
f.write(h.content)的方式来保存图片。
还有将同一个标题下的图片存在一起，我们通过判断标题是否一样，如果一样就保存在这个文件夹下，
如果不一样就创建文件夹

    path=os.path.join(r"C:\Users\asus-pc\Desktop\beautifulgirl\555",title)
    if not os.path.exists(path):
        os.mkdir(path)
还有一点就是保存的图片文件名，我们通过时间的名字来保存
name=str(time.time())[-7:-3]
四、主函数

  我们利用下一页返回是否为空来判断是否爬取完成。如果返回的不是空，则会永远执行，我们还有一个计时功能，来计算执行时间。

if __name__ == "__main__":
    print "anction time :"
    print time.strftime("%Y-%m-%d %H:%M:%S")
    url = r"https://www.1102f.com/Html/63/"
    topurl = frist(url)
    while 1:
        time.sleep(3)
        if topurl!=0:
            topurl=frist(topurl)
        else:
            print "end time:"
            print time.strftime("%Y-%m-%d %H:%M:%S")
