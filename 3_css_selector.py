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
        <a href='www.baidu.com'>百度首页</a>
    </footer>
</body>
</html>
"""

selector = Selector(text=html_sample)
div_tag = selector.css('#div1')
print(div_tag)

# 获取id为services的元素下ul/的全部li元素
section_tag = selector.css('#services > ul > li::text').extract()
print(section_tag)

# 获取id为services的元素下ul/的第二个li元素
section_tag = selector.css('#services > ul > li:nth-child(2)::text').extract()
print(section_tag)

# 获取class为about的元素后的第一个section元素
section_tag = selector.css('.about + section > h2::text').extract()
print(section_tag)

# 获取class为about的相邻元素
section_tags = selector.css('.about ~ section').extract()
print(section_tags)

# 通过属性值获取元素
a_tag = selector.css('a[href="www.baidu.com"]::text').extract()
print(a_tag)

# 通过属性值的部分值匹配获取元素
a_tag = selector.css('a[href*="baidu"]::text').extract()
print(a_tag)