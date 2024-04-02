from scrapy import Selector

html_sample = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        p {
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>

    <div id="div1">
        aaaa
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About Us</a></li>
            <li><a href="#services">Our Services</a></li>
            <li><a href="#contact">Contact Us</a></li>
        </ul>
        <div>hhhhhh</div> 
    </div>

    <section id="home-96644" class="name1 name2">
        <h2 class='home-page'>Home Page</h2>
        <h2 class='home-page'>Home Page2</h2>
        <h2 class='home-page'>Home Page3</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget justo nec ipsum venenatis ultricies.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget justo nec ipsum venenatis ultricies.</p>
    </section>

    <section class="about">
        <h2>About Us</h2>
        <p>Nulla facilisi. Cras ultricies lacus non nisl scelerisque, eu dapibus nunc mollis.</p>
    </section>

    <section id="services">
        <h2>Our Services</h2>
        <ul>
            <li>Service 1</li>
            <li>Service 2</li>
            <li>Service 3</li>
        </ul>
    </section>

    <footer>
        <p>&copy; 2024 My Website. All rights reserved.</p>
    </footer>
</body>
</html>
"""

selector = Selector(text=html_sample)
# 获取全部id为div1的div，并取其路径下/ul/li的全部a元素
# extract()方法将对象转换成列表
div_tag = selector.xpath('//div[@id="div1"]/ul/li/a').extract()[1]
print(div_tag)
div_tag = selector.xpath('//div[@id="div1"]/ul/li/a/text()').extract()[0]
print(div_tag)

# 只通过一个属性值查找元素：contains方法
section_tag = selector.xpath('//*[contains(@class, "name1")]/h2[last() - 1]/text()').extract()
print(section_tag)

# 获取目标的属性值
section_tag = selector.xpath('//*[contains(@class, "name1")]/@class').extract()
print(section_tag)

# 同时获取两个元素
sections_tag = selector.xpath('//section[@class="about"]/h2/text()|//section[@id="services"]/h2/text()').extract()
print(sections_tag)