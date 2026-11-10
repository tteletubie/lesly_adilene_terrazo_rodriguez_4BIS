
import csv
import json
from fpdf import FPDF


class Exporter:

    def export(self, productos):
        raise NotImplementedError(
            "Debe implementar export()"
        )

class CSVExporter(Exporter):

    def export(self, productos):

        with open(
            "productos.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            writer = csv.writer(archivo)

            writer.writerow(
                ["ID", "Nombre", "Precio", "Stock"]
            )

            writer.writerows(productos)

class TXTExporter(Exporter):

    def export(self, productos):

        with open(
            "productos.txt",
            "w",
            encoding="utf-8"
        ) as archivo:

            for p in productos:

                archivo.write(
                    f"ID: {p[0]} | "
                    f"Nombre: {p[1]} | "
                    f"Precio: {p[2]} | "
                    f"Stock: {p[3]}\n"
                )

class JSONExporter(Exporter):

    def export(self, productos):

        datos = []

        for p in productos:

            datos.append({
                "id": p[0],
                "nombre": p[1],
                "precio": float(p[2]),
                "stock": p[3]
            })

        with open(
            "productos.json",
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

class PDFExporter(Exporter):

    def export(self, productos):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=12
        )

        pdf.cell(
            200,
            10,
            txt="Lista de Productos",
            ln=True,
            align="C"
        )

        pdf.ln(10)

        for p in productos:

            texto = (
                f"ID:{p[0]}  "
                f"Nombre:{p[1]}  "
                f"Precio:{p[2]}  "
                f"Stock:{p[3]}"
            )

            pdf.cell(
                200,
                10,
                txt=texto,
                ln=True
            )

        pdf.output("productos.pdf")