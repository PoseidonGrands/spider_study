import re
import lxml

from bs4 import BeautifulSoup
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

bs = BeautifulSoup(html_sample, 'html.parser')
# 获取标签：bs.标签名
print(bs.title)
# 获取标签内容：bs.标签名.string
title_tag = bs.title.string
print(bs.title.string)

# 通过id查找目标元素
div_tag = bs.find('div', id='div1')
print(div_tag)

# 通过正则找目标元素
section_tag = bs.find('section', id=re.compile('home-\d{5}'))
print(section_tag)

# 找标签的子元素
childrens = div_tag.contents
for child in childrens:
    if child.name:
        print(child.name, type(child.name))

# 找标签的子孙元素（全部元素
childrens = div_tag.descendants
for child in childrens:
    if child.name:
        print(child.name)

# 通过class找标签的父元素
h2_tag = bs.find('h2', {'class': 'home-page'})
print(h2_tag.parent)

print('--------')

# 找标签的全部兄弟元素
div_siblings = bs.find('section', id=re.compile('home-\d{5}')).next_siblings
div_siblings_pre = bs.find('section', id=re.compile('home-\d{5}')).previous_siblings
for sibling in div_siblings:
    print(sibling)

print('--------')

# 获取标签的属性(单值属性(id)或未知属性返回字符串，多值属性(class)返回列表
section_tag = bs.find('section', id=re.compile('home-\d{5}'))
print(section_tag['id'])
print(section_tag.get('id'))
print(section_tag.get('class'))


