# spider
 
**看了几本书之后写的第一个爬虫脚本，时间过去很久了，准备整理一下硬盘，然后写写阶段性的总结。**   

很明显在这个脚本中有许多不足的地方，诸如：
1. 网页的爬取是顺序进行的；
2. 如果爬取过程中遇到异常，譬如被服务器发现恶意爬取的时候，就会直接产生异常，被中断；

**下面说下这个脚本的思路，已备之后再爬取数据的时候参考，不至于全部忘完。** 
1. 添加webdriver，在webdriver中打开headless浏览器，这个浏览器在渲染动态页面的时候会非常给力。
基本上在我之后写脚本时不会因为页面抓不到而发愁；
2. 之后在代码中写的很清晰了，主要使用了driver.find_element_by_xpath这个方法，通过在浏览器中
按F12进入开发者模式，然后可以在html页面源码中右键选择xpath直接进行选择页面元素；
3. 查找元素操作页面主要用到了一个属性和一个方法：text(用来获取文本，这个和BeautifulSoup中也
是一样的，在写完这个脚本之后使用BS也是一样的感觉),click()(操作浏览器进行点击操作)
