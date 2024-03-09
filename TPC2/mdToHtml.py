import re
import sys

def sub_heading(md):
    regex = r'^(#{1,6})\s+(.*)$'
    
    html_heading = re.sub(regex, lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>', md, flags=re.MULTILINE)

    return html_heading

def sub_italic_bold(md):
    html_bi = re.sub(r'(\*\*|__)(.*?)\1', r'<b>\2</b>', md) # Negrito
    html_bi = re.sub(r'(\*|_)(.*?)\1', r'<i>\2</i>', html_bi) # Itálico

    return html_bi

def sub_list(md):
    html_list = re.sub(r'\n(\d\.(.+?)\n)+', lambda m: f"\n<ol>"+m.group(0)+"</ol>\n", md) # Para listas ordenadas /1. texto/
    html_list = re.sub(r'\n([\.\*\-](.+?)\n)+', lambda m: f"\n<ul>"+m.group(0)+"</ul>\n", html_list) # Para listas desordenadas /. texto/
    html_list = re.sub(r'(?<=\n)(\d*[\.\*\-]) (.+?)(?=\n)', r'<li>\2</li>', html_list)

    return html_list

def sub_link(md):
    regex = r'\[(.*?)\]\((.*?)\)'

    html_link = re.sub(regex, r'<a href="\2">\1</a>', md, flags=re.MULTILINE)

    return html_link

def sub_image(md):
    regex = r'!\[(.*?)\]\((.*?)\)'

    html_img = re.sub(regex, r'<img src="\2" alt="\1"/>',  md, flags=re.MULTILINE)

    return html_img

def sub_blockquotes(md):
    regex = r'^(?:> (.*))'
    
    html_bq = re.sub(regex, r'<br><blockquote>\1</blockquote>', md, flags=re.MULTILINE)

    return html_bq

def sub_horizontal(md):
    regex = r'^___|---|\*\*\*$'

    html_horizontal = re.sub(regex, r'<br><hr><br>', md, flags=re.M)

    return html_horizontal

def parse_md(md):

    page ="""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Html</title>
        </head>
        <body>
            {MARKDOWN}
        </body>
        </html>
    """

    html = sub_heading(md)
    html = sub_horizontal(html)
    html = sub_italic_bold(html)
    html = sub_list(html)
    html = sub_image(html)
    html = sub_link(html)
    html = sub_blockquotes(html)
    
    page = re.sub(r'\{MARKDOWN\}',html,page)
    
    return page

def main():
    with open("newHtml.html", "w", encoding="utf-8") as html:
            html.write(parse_md(sys.stdin.read()))

if __name__ == "__main__":
    main()