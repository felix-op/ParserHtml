from datetime import datetime
import string

class ParserHtml:
    def __init__(self, title):
        self.articles = {}
        self.title = title
    
    def add_article(self, article):
        autor_id = article.autor_how_id()
        if autor_id not in self.articles:
            self.articles[autor_id] = []
        self.articles[autor_id].append(article)


    def filter_articles(self, key):
        filtrados = {}
        for autor, articles in self.articles.items():
            for article in articles:
                if key in article.text:
                    if autor in filtrados:
                        filtrados[autor].append(article)
                    else:
                        filtrados[autor] = [article]
        return filtrados

    def footer(self):
        return f"""
    <footer class="bg-dark text-white text-center py-3 mt-5">
        Fecha de creación: {datetime.now()}
    </footer>"""

    def to_html(self):
        autores_js = ",".join(
            f'"{articles[0].autor_how_id()}"'
            for autor, articles in self.articles.items())
        apellidos_js = ",".join(
            f'"{articles[0].autor_how_id().split("-")[1]}"'
            for autor, articles in self.articles.items())
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
    <link rel="stylesheet" href="./colores.css">
</head>
<body>
    <header class="bg-dark pt-3">
        <h1 class="m-0 px-3">Artículos de Roma</h1>
    </header>
    <section class="py-4 px-3 bg-dark text-secondary">
        <h2 class="h4 mb-4">Índice de autores</h2>
        <div class="d-flex flex-wrap gap-2 justify-content-around">{"".join(f"""
            <a class="boton-indice btn btn-sm d-flex" href="#{autor}">{articles[0].autor_normalize()} <span>- articulos: {len(articles)}</span></a>"""
            for autor, articles in self.articles.items())}
        </div>
    </section>
    <section class="bg-dark text-secondary">
        <h2 class="px-3 h4">Buscar por inicial</h2>
        <div class="d-flex px-3 py-3 flex-wrap gap-2">
            <button onclick="mostrarTodosAutores()" class="btn btn-outline-success">Todos</button>
            {"".join(
                f'''<button onclick="filtrarPorInicial('{letter.lower()}')" class="btn btn-outline-success">{letter}</button>'''
                for letter in string.ascii_uppercase)}
        </div>
    </section>
    <main>{"".join(f"""
        <section id="{autor}" class="container my-5">
            <h3 class="mb-4">{articles[0].autor_normalize()}</h3>
            <div class="row g-4">{f"".join(article.to_label(index) for index, article in enumerate(articles))}
            </div>
        </section>""" for autor, articles in self.articles.items())}
    </main>
    {self.footer()}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js" integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq" crossorigin="anonymous"></script>
    <script>
        function mostrarTodosAutores() {{
            document.querySelectorAll("section[id]").forEach(section => {{
                section.style.display = "";
            }});
        }}

        function filtrarPorInicial(letra) {{
            let autores = [{autores_js}];
            let apellidos = [{apellidos_js}];
            
            let idsMostrados = autores.filter((_, i) => apellidos[i].startsWith(letra));
            document.querySelectorAll("section[id]").forEach(section => {{
                section.style.display = idsMostrados.includes(section.id) ? "" : "none";
            }});
        }}
    </script>
</body>
</html>
"""