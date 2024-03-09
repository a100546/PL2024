# TPC2: Conversor de MD para HTML

## 2024-02-16

## Autor
- **Nome:** Tomás Monteiro Sousa
- **Id:** A100546

## Enunciado
```
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:
- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
        In: # Exemplo
        Out: <h1>Exemplo</h1>
- Bold: pedaços de texto entre "**":
        In: Este é um **exemplo** ...
        Out: Este é um <b>exemplo</b> ...
- Itálico: pedaços de texto entre "*":
        In: Este é um *exemplo* ...
        Out: Este é um <i>exemplo</i> ...
- Lista numerada:
        In:
            1. Primeiro item
            2. Segundo item
            3. Terceiro item
        Out:
            <ol>
            <li>Primeiro item</li>
            <li>Segundo item</li>
            <li>Terceiro item</li>
            </ol>
- Link: [texto](endereço URL)
        In: Como pode ser consultado em [página da UC](http://www.uc.pt)
        Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
- Imagem: ![texto alternativo](path para a imagem)
        In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
        Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
```

## Solução
Para resolver o *TPC2* foi criado um conversor de Markdown para HTML em Python, conforme especificado no enunciado. Utilizei expressões regulares para fazer a conversão de diferentes elementos do Markdown para o formato HTML.

Decidi então fazer a conversão dos seguintes elementos:
- Cabeçalhos
- Itálico
- Negrito
- Listas Ordenadas
- Listas Desordenadas
- Links
- Imagens
- Blockquotes
- Linhas Horizontais

De modo a resolver o `TPC2` importei o módulo re (para operações com expressões regulares) e sys (para operações IO)

A função `sub_heading(md)` substitui os cabeçalhos `#,##,###,...` Markdown por elementos HTML `<h1>, <h2>, <h3>, etc..`: 
```py
def sub_heading(md):
    regex = r'^(#{1,6})\s+(.*)$'
    
    html_heading = re.sub(regex, lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>', md, flags=re.MULTILINE)

    return html_heading
```

A função `sub_italic_bold(md)` substitui o texto em negrito e itálico por elementos HTML `<b>` e `<i>`, respectivamente. Para todos os elementos que comecem e terminem com `"**"` ou `"__"` irá substituir para `<b></b>`, para os elementos que comecem e terminem com `"*"` ou `"_"` irá substituir para `<i></i>`:
```py
def sub_italic_bold(md):
    html_bi = re.sub(r'(\*\*|__)(.*?)\1', r'<b>\2</b>', md) # Negrito
    html_bi = re.sub(r'(\*|_)(.*?)\1', r'<i>\2</i>', html_bi) # Itálico

    return html_bi
```

A função `sub_list(md)` substitui listas numeradas e não numeradas por elementos HTML `<ol>` e `<ul>`, respectivamente, e os seus itens `<li>`. Dependendo se o primeiro elemento é `1.` será `<ol>`, caso seja `.`,`-` ou `*` será `<ul>`:
```py
def sub_list(md):
    html_list = re.sub(r'\n(\d\.(.+?)\n)+', lambda m: f"\n<ol>"+m.group(0)+"</ol>\n", md) # Para listas ordenadas /1. texto/
    html_list = re.sub(r'\n([\.\*\-](.+?)\n)+', lambda m: f"\n<ul>"+m.group(0)+"</ul>\n", html_list) # Para listas desordenadas /. texto/
    html_list = re.sub(r'(?<=\n)(\d*[\.\*\-]) (.+?)(?=\n)', r'<li>\2</li>', html_list)

    return html_list
```

A função `sub_link(md)` substitui os links Markdown por elementos HTML `<a>`. Os links Markdown contêm o formato `[nome](link)` que será tranformado em `<a href="link">nome</a>`: 
```py
def sub_link(md):
    regex = r'\[(.*?)\]\((.*?)\)'

    html_link = re.sub(regex, r'<a href="\2">\1</a>', md, flags=re.MULTILINE)

    return html_link
```

A função `sub_image(md)` substitui as imagens Markdown por elementos HTML `<img>`. As imagens em Markdown contêm o formato `![nome](link)` que será tranformado em `<img src="link" alt="nome">`: 
```py
def sub_image(md):
    regex = r'!\[(.*?)\]\((.*?)\)'

    html_img = re.sub(regex, r'<img src="\2" alt="\1"/>',  md, flags=re.MULTILINE)

    return html_img
```

A função `sub_blockquotes(md)` substitui as citações Markdown por elementos HTML `<blockquote>`. As blockquotes em Markdown são caracterizadas por começarem com `> texto`, sendo assim substituidas por `<blockquote>texto</blockquote>`:
```py
def sub_blockquotes(md):
    regex = r'^(?:> (.*))'
    
    html_bq = re.sub(regex, r'<br><blockquote>\1</blockquote>', md, flags=re.MULTILINE)

    return html_bq
```

A função `sub_horizontal(md)` que substitui linhas horizontais Markdown por elementos HTML `<hr>`. As linhas horizontais podem ser caracterizadas por `___`,`---` ou `***`:
```py
def sub_horizontal(md):
    regex = r'^___|---|\*\*\*$'

    html_horizontal = re.sub(regex, r'<br><hr><br>', md, flags=re.M)

    return html_horizontal
```

A função `parse_md(md)` que processa o Markdown completo e substitui todas as ocorrências pelos elementos HTML correspondentes:
```py
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
```

A função `main()` lê a entrada padrão (stdin) e escreve o HTML resultante num arquivo newHtml.html:
```py
def main():
    with open("newHtml.html", "w", encoding="utf-8") as html:
            html.write(parse_md(sys.stdin.read()))

if __name__ == "__main__":
    main()
```

# Como executar o código
Para executar o código é necessário ter um ficheiro Markdown e executar o código da seguinte forma:
```bash
$ cat <ficheiro Markdown> | python3 mdToHtml.py
```

# Resultados

Foi utilizado o seguinte ficheiro para testar o programa:
```txt
# Titulo 1

Um texto em **Negrito** e __Negrito__

## Titulo 2

Um texto em *Italico* e _Italico_

### Titulo 3

Um link para o [Youtube](https://www.youtube.com)

#### Titulo 4

![teste](https://aealtodosmoinhos.pt/wp-content/uploads/2016/05/teste.jpg)

##### Titulo 5

Uma lista ordenada:

1. Ordenada 1
1. Ordenada 2
1. Ordenada 3
1. Ordenada 4

###### Titulo 6

Uma lista desordenada:

- Desordenada 1
- Desordenada 2
- Desordenada 3
- Desordenada 4

---

> Um blackquote
> Outro blackquote

---

Uma palavra em ***negrito e italico***

```

Como resultado obteve-se o seguinte ficheiro html:
```txt

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Html</title>
        </head>
        <body>
            <h1>Titulo 1</h1>

Um texto em <b>Negrito</b> e <b>Negrito</b>

<h2>Titulo 2</h2>

Um texto em <i>Italico</i> e <i>Italico</i>

<h3>Titulo 3</h3>

Um link para o <a href="https://www.youtube.com">Youtube</a>

<h4>Titulo 4</h4>

<img src="https://aealtodosmoinhos.pt/wp-content/uploads/2016/05/teste.jpg" alt="teste"/>

<h5>Titulo 5</h5>

Uma lista ordenada:

<ol>
<li>Ordenada 1</li>
<li>Ordenada 2</li>
<li>Ordenada 3</li>
<li>Ordenada 4</li>
</ol>

<h6>Titulo 6</h6>

Uma lista desordenada:

<ul>
<li>Desordenada 1</li>
<li>Desordenada 2</li>
<li>Desordenada 3</li>
<li>Desordenada 4</li>
</ul>

<br><hr><br>

<br><blockquote>Um blackquote</blockquote>
<br><blockquote>Outro blackquote</blockquote>

<br><hr><br>

Uma palavra em <i></i>*negrito e italico<br><hr><br>

        </body>
        </html>
    
```