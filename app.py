import os
from flask import Flask, render_template
 
from prenda import Prenda
from inventario import Inventario
 
app = Flask(__name__)
 
# ---- Mismo modelo de siempre: ni Prenda ni Inventario se tocaron ----
inventario = Inventario()
if not inventario.prendas:
    inventario.agregar(Prenda("Camisa de lino", 900.0, "Camisa", "M", 10, "01/09/2026"))
    inventario.agregar(Prenda("Jean clásico", 900.0, "Pantalón", "L", 8, "02/09/2026", en_oferta=True))
    inventario.agregar(Prenda("Chaqueta de cuero", 900.0, "Chaqueta", "XL", 3, "03/09/2026"))
 
 
@app.route("/")
def inicio():
    return render_template(
        "index.html",
        prendas=inventario.prendas,
        valor_total=inventario.valor_total(),
        unidades=inventario.total_unidades(),
        en_oferta=inventario.total_en_oferta(),
    )
 
 
if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
