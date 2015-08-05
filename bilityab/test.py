from htmldom import htmldom

with open("sample.html", "r") as sample:
    data = sample.read()

dom = htmldom.HtmlDom().createDom(data)

print(dom.find('div').first().children().contains('1').first().next().attr('class'))
