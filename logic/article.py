import re

def dividir_en_oraciones(texto: str) -> list[str]:
    oraciones = re.split(r'(?<!a)\. (?=[A-ZÁÉÍÓÚÑ])', texto)
    return [oracion.strip() + ('' if oracion.strip().endswith('.') else '.')
            for oracion in oraciones if oracion.strip()]

class Article:
    def __init__(self, title, autor, text):
        
        if len(title) < 10:
            raise ValueError("Error: la longitud del titulo debe ser mayor a 10")
        
        if len(text)<10:
            raise ValueError("Error: la longitud del texto debe ser mayor a 10")
        
        self.title = title
        self.autor = autor
        self.text = text

    def autor_normalize(self):
        return self.autor.strip().capitalize()
    
    def autor_how_id(self):
        return self.autor.strip().lower().replace(" ", "-");

    def to_label(self, index):
        return f"""
                <div class="col-md-4">
                    <article class="border p-3 h-100 d-flex flex-column align-items-start">
                        <h4>{self.title}</h4>
                        <p class="text-secondary">{self.text[:300] + "..."}</p>
                        <a class="btn btn-sm btn-outline-success mt-auto" href="./articulos/{self.autor_how_id()}-{index}.html">Leer más</a>
                    </article>
                </div>"""
    
    def to_html(self, prev=None, next=None):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Articulo de {self.autor_normalize()}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
    <link rel="stylesheet" href="./../colores.css">
</head>
<body class="min-vh-100 d-flex flex-column">
    <header class="bg-dark pt-3">
        <h1 class="m-0 px-3">Artículos de Roma - {self.autor_normalize()}</h1>
        <a href="./../index.html" class="btn btm-sm px-3 py-4 text-success fs-4 fw-semibold">← Volver a los Articulos</a>
    </header>
    <main class="d-flex align-items-center justify-content-around flex-grow-1 mt-5">{f"""
            <a href="{prev}" class="d-flex boton-indice btn btn-outline-success">← <span>Articulo anterior</span></a>
        """ if prev != None else ""}
        <div class="bg-dark rounded p-4" style="width: 70%">
            <h2 class="mb-4">{self.title}</h2>
            {"".join(f"<p>{text}</p>" for text in dividir_en_oraciones(self.text) if text != "")}
        </div>{f"""
            <a href="{next}" class="d-flex boton-indice btn btn-outline-success">→ <span>Articulo siguiente</span></a>
        """ if next != None else ""}
    </main>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js" integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq" crossorigin="anonymous"></script>
</body>
</html>"""
    
    def __str__(self):
        return f"{self.title + self.text}"