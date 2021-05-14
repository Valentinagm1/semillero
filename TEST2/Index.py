from flask import Flask, render_template, request, make_response #framkework para html y python
import formulario
from fpdf import FPDF #para el pdf



app = Flask(__name__) #se crea el objeto flask
pdf = FPDF('P', 'mm', 'letter') #

@app.route('/', methods=['GET', 'POST'])  #ruta inicial y el metodo post es una forma de recibir la información

def casa():
    datospoder = formulario.Datos(request.form)
    if request.method == 'POST' and datospoder.validate():
        nom_poder = datospoder.nombre_dante.data.upper()
        ape_poder = datospoder.apellido_dante.data.upper() 
        email = datospoder.correo_dante.data.lower()
        ced_poder = datospoder.identidad_dante.data
        gen_poder = datospoder.genero_dante.data
        gen_poder = 'o' if gen_poder == 'm' else 'a'

        nom_apo = datospoder.nombre_rado.data.upper()
        ape_apo = datospoder.apellido_rado.data.upper()
        #correo_poderado = datospoder.correo_rado.data.lower()
        ced_apo = datospoder.identidad_rado.data
        num_car = datospoder.carnet.data
        gen_apo= datospoder.genero_rado.data
        gen_apo = 'o' if gen_apo== 'm' else 'a'
        portadore = 'o' if gen_apo == 'm' else 'a'

        nom_contra = datospoder.nombre_contra.data.upper()
        ape_contra= datospoder.apellido_contra.data.upper()
        email_2 = datospoder.correo_contra.data.lower()
        ced_contra = datospoder.identidad_contra.data
        gen_contra= datospoder.genero_contra.data
        gen_contra = 'o' if gen_contra == 'm' else 'a'

        texto = f"""{nom_poder} {ape_poder}, mayor de edad, domiciliad{gen_poder} en la ciudad de Bogotá D.C., 

identificad{gen_poder} con cédula de ciudadanía número {ced_poder}, y dirección de notificación electrónica {email}, 
por medio del presente escrito, otorgo PODER ESPECIAL, AMPLIO Y SUFICIENTE a {nom_apo} {ape_apo}, 
mayor de edad, domiciliad{gen_apo} en Bogotá D.C., identificad{gen_apo} con 
Cédula de Ciudadanía No. {ced_apo}, miembro activo del Consultorio Jurídico de la 
Universidad Externado de Colombia, portador{portadore} del carné No.{num_car} , para que, 
en mi nombre y representación, inicie y lleve 
hasta su terminación el PROCESO DE SEPARACIÓN DE BIENES contra el señor {nom_contra} {ape_contra}, 
mayor de edad, domiciliad{gen_contra} en Bogotá D.C., 
identificad{gen_contra} con cédula de ciudadanía número {ced_contra}, con dirección de notificación electrónica 
{email_2}.
Mi apoderad{gen_apo} queda facultad{gen_apo} para solicitar medidas cautelares, 
desistir, renunciar, sustituir, recibir, transigir, 
asumir el presente poder y demás facultades en los términos del artículo 77 del 
Código General del Proceso.

Sírvase, Señor Juez, reconocerle personería jurídica a mi apoderad{gen_apo}, en los términos y para los efectos del presente poder.
 
Señor Juez,

{nom_poder} {ape_poder}
C.C. No. {ced_poder}


Acepto, 


{nom_apo} {ape_apo}
C.C. {ced_apo}
Carné No.{num_car}  del Consultorio Jurídico.
Universidad Externado de Colombia - Sala Civil.


 """
        print(texto)

        pdf.add_page()
        pdf.set_font('Times', '', 10)
        pdf.multi_cell(0, 10, texto)
        pdf.ln()
        pdf.output('Poder.pdf', 'F')

    return render_template('main.html', form = datospoder)

@app.route('/poder', methods=['POST'])
def poder():
    if request.method == 'POST':
        return("hello")
            
if __name__ == '__main__':  
    app.run(debug = True)