from flask import Flask, render_template,  request, make_response, send_file, send_from_directory, abort
from fpdf import FPDF, HTMLMixin #para el pdf
from datetime import date

app = Flask(__name__)
#pdf = FPDF('P', 'mm', 'letter') #

# @app.route('/')
# def index():
#     title = 'HC4A - Codext'
#     return render_template("index.html", title=title)

@app.route('/about')
def about():
    names = ['Peter','Emma','Juan','Chipss']
    return render_template("about.html", names=names)

@app.route('/', methods=['GET', 'POST'])  #ruta inicial y el metodo post es una forma de recibir la información
def casa():
    #datoshabeas = formulario.Datos(request.form)
    #if request.method == 'POST' and datoshabeas.validate():


    return render_template('main.html')

@app.route('/form', methods=['POST'])
def form():

    title = 'Todo listo!'
    #datoshabeas = formulario.Datos(request.form)

    nom_solicitante = request.form.get('nom_solicitante').upper()
    fecha = date.today()
    ciudad = request.form.get('ciudad').upper()
    condi_solici = request.form.get('condi_solici')
    direccion_solicitante = request.form.get('direccion_solicitante')
    email_solicitante = request.form.get('email_solicitante').lower()
    ced_solicitante = request.form.get('ced_solicitante')
    id_solicitante = request.form.get('id_solicitante')
    num_solicitante =  request.form.get('num_solicitante')

    #gen_poder = datoshabeas.genero_dante.data
    #gen_poder = 'o' if gen_poder == 'm' else 'a'

    ### AFECTADO
    nom_afectado = request.form.get('nom_afectado').upper()
    nom_autoridad = request.form.get('nom_autoridad').upper()
    fecha_hechos = request.form.get('fecha_hechos')

    #ape_apo = datoshabeas.apellido_rado.data.upper()
    #correo_poderado = datoshabeas.correo_rado.data.lower()
    sujeto_ordeno = request.form.get('sujeto_ordeno').upper()
    if sujeto_ordeno == None or len(sujeto_ordeno)< 3:
        sujeto_ordeno = 'alguien desconocido.'
    cargo_txt = request.form.get('cargo_txt').capitalize()
    ced_afectado = request.form.get('ced_afectado')
    id_afectado = request.form.get('id_afectado')

    num_dias = request.form.get('num_dias')
    gen_afectado = request.form.get('gen_afectado')
    gen_afectado = 'o' if gen_afectado == 'm' else 'a'
    sitio = request.form.get('sitio')
    hechos = request.form.get('hechos')
    if hechos == None or len(hechos)<3:
        hechos='Actualmente no se cuenta con información adicional.'

    texto = f"""
<p style="text-align: justify;"><b><span>Señor</span><br><span>Juez competente</span></b><br>{ciudad}<br>
{fecha}
<br><br>
Yo, {nom_solicitante} en mi condición de {condi_solici}, acudo ante usted, señor juez a fin de solicitarle se sirva dar trámite a la petición de hábeas corpus en favor de {nom_afectado},
identificado con {id_afectado} No. {ced_afectado}, con fundamento en lo siguiente:</p>
<br>
<p style="text-align: justify;"><span><b>HECHOS</b></span></p>
<p style="text-align: justify;">{nom_afectado} fue aprehendid{gen_afectado} por la {nom_autoridad} el pasado {fecha_hechos} por orden de {sujeto_ordeno}. Desde entonces, hasta la fecha han transcurrido {num_dias} días sin que haya sido indagada o resuelta su situación jurídica.<br>{nom_afectado}
se encuentra recluid{gen_afectado} en {sitio}, desde el día {fecha_hechos} y el funcionario que ordenó su aprehensión es {sujeto_ordeno} {cargo_txt}.</p>
<p style="text-align: justify;">{hechos}</p>
<br>
<p style="text-align: justify;"><span><b>JURAMENTO</b></span></p>
<p style="text-align: justify;">Bajo la gravedad del juramento, manifiesto que ningún otro funcionario conoce o ha decidido sobre esta acción.</p>
<br>
<p style="text-align: justify;"><span><b>FUNDAMENTOS DE DERECHO</b></span></p>
<p >Esta petición está fundamentada, señor juez, en los artículos 30 y 85 de la Constitución Nacional referidos a la privación ilegal de la libertad y a la aplicación inmediata de los derechos consagrados en la Constitución Política. Sumado a ello, la Convención
Americana de Derechos Humanos establece en su artículo 7 el derecho a la libertad personal, ante lo cual, nadie puede ser sometido a detención arbitraria ni mucho menos puede ser privado de la libertad, salvo por causas y condiciones fijadas por la
Constitución y la Ley. En el artículo 8 de este instrumento también se plasma como garantía judicial el derecho que tiene toda persona a ser oída en un plazo razonable y por la autoridad competente para la determinación de sus derechos.</p>
<br>
<p style="text-align: justify;">Bien se dispuso por parte de la Corte Constitucional en Sentencia C 187 de 2006 que:</p>
<br>
<p style="text-align: justify;">'Una interpretación acorde con la Constitución Política supone que, después de invocado el hábeas corpus, la autoridad judicial encargada de conocer, deberá verificar la existencia de las condiciones que conducen a ordenar que el peticionario sea puesto
en libertad. Tales condiciones son: i) que la persona esté privada de la libertad, y ii) que la privación de la libertad o la prolongación de la misma se haya dado con violación o quebrantamiento del orden constitucional y legal. Una vez demostrado
que la privación de la libertad personal o la prolongación de la privación de la libertad son el resultado de actos contrarios a lo dispuesto por el ordenamiento constitucional o legal, la autoridad judicial competente deberá ordenar que la persona
sea puesta inmediatamente en libertad'<br>
<br>
<b>SOLICITUD</b><br>Efectuada la verificación de la violación de las garantías constitucionales y legales, solicito a usted ordenar la libertad inmediata de {nom_afectado} y compulsar copias para que se
inicien las investigaciones a que hubiere lugar.</p>
<br>
<p style="text-align: justify;">
Del señor juez,</p>
<br>
<p style="text-align: justify;">{nom_solicitante}<br>
{id_solicitante} {ced_solicitante}<br>Dirección de notificación: {direccion_solicitante}<br>
Email: {email_solicitante} <br>
Teléfono: {num_solicitante}</p>
"""
    class MyFPDF(FPDF, HTMLMixin):
        pass

    pdf = MyFPDF()
    pdf.set_margins(left= 15.0, top=12.5, right=15.0)
    pdf.add_page()
    pdf.write_html(texto)
    pdf.output('habeas_'+nom_solicitante[:4]+ced_solicitante[:-3]+'.pdf', 'F')


    return render_template("form.html", id_solicitante=id_solicitante, id_afectado=id_afectado, fecha= fecha, title = title, texto=texto, nom_solicitante = nom_solicitante, ciudad = ciudad, condi_solici = condi_solici, direccion_solicitante = direccion_solicitante , email_solicitante = email_solicitante, ced_solicitante = ced_solicitante, num_solicitante = num_solicitante, nom_afectado = nom_afectado, nom_autoridad = nom_autoridad, fecha_hechos = fecha_hechos, sujeto_ordeno = sujeto_ordeno, cargo_txt = cargo_txt, ced_afectado = ced_afectado, num_dias = num_dias, gen_afectado = gen_afectado, sitio = sitio , hechos = hechos)#, datoshabeas=datoshabeas.ciudad.data)

@app.route('/download/<pdf_name>')
def download_file(pdf_name):
    path = r'/static/client/pdf'
    try:
        return send_file(pdf_name, as_attachment=True)
    except FileNotFoundError:
        abort(404, description=path+pdf_name+"Not Found")

#=====================================PODER AUTOMATIZADO========================================
@app.route('/poder', methods=['GET', 'POST'])  #ruta inicial y el metodo post es una forma de recibir la información
def poder():
    return render_template('poder.html')
@app.route('/form_poder',methods=['POST'])
def poder_automatizado():
    title = 'Poder Automatizado'
    def info_poder(parte_procesal):
        parte = parte_procesal
        num_car = None
        #---------------poderdante
        nom_poder = request.form.get('nom_poder').upper()
        email = request.form.get('email').lower()
        gen_poder = request.form.get('gen_poder')
        gen_poder = 'o' if gen_poder == 'm' else 'a'
        ced_poder = request.form.get('ced_poder').replace('.','').replace(",","")
        #----------------------------------------------------------------------------------------------
        if parte_procesal == 'apoderado':
                nom_apo = request.form.get('nom_apo'),upper()
                num_car = request.form.get('num_car').replace('.','')
                gen_apo = request.form.get('gen_apo')
                gen_apo = 'o' if gen_poder == 'm' else 'a'
                portadore = '' if gen_poder == 'm'else 'a'
                email_apo = request.form.get('email_apo').lower()

        return nom_poder,gen_poder,ced_poder,num_car,gen_apo,email,email_apo,nom_apo

    #portadore = ''

    nom_poder,gen_poder,ced_poder,_,_,email,_,_ = info_poder('poderdante')
    nom_apo,gen_apo,ced_apo,gen_apo,num_car,_,email_apo,nom_apo = info_poder('apoderado')
    nom_contra,gen_contra,ced_contra,_,_,email_2,_,_ = info_poder('contraparte')
    if email_apo == 'civil':
        email_apo = 'conjurcivil@uexternado.edu.co'
    elif email_apo == 'comercial':
        email_apo = 'Lorem ipmsum'
    elif email_apo == 'penal':
        email_apo = 'Lorem ipmsum'
    elif email_apo == 'administrativo':
        email_apo='Lorem ipmsum'
    elif email_apo = 'laboral':
        email_apo ='lorem ipsum'
    elif email_apo_otro:
        if email_apo != '':
            email_apo= email_apo_otro
    #---------------------------TEXTO--------------------------------------------

    poder =  f"""{nom_poder}, mayor de edad, domiciliad{gen_poder} en la ciudad de Bogotá D.C.,
    identificad{gen_poder} con cédula de ciudadanía número {id_poder} {ced_poder}, y dirección de notificación electrónica {email},
    por medio del presente escrito, otorgo PODER ESPECIAL, AMPLIO Y SUFICIENTE a {nom_apo},
    mayor de edad, domiciliad{gen_apo} en Bogotá D.C., identificad{gen_apo} con
    Cédula de Ciudadanía No. {id_apo} {ced_apo}, miembro activo del Consultorio Jurídico de la
    Universidad Externado de Colombia, portador{portadore} del carné No.{num_car} , con dirección de notificación electrónica {email_apo}.
    Con la finalidad de que en mi nombre y representación, inicie y lleve
    hasta su terminación el PROCESO DE SEPARACIÓN DE BIENES contra el señor {nom_contra} ,
    mayor de edad, domiciliad{gen_contra} en Bogotá D.C.,
    identificad{gen_contra} con cédula de ciudadanía número{id_contra} {ced_contra}, con dirección de notificación electrónica
    {email_2}.
    Mi apoderad{gen_apo} queda facultad{gen_apo} para solicitar medidas cautelares,
    desistir, renunciar, sustituir, recibir, transigir,
    asumir el presente poder y demás facultades en los términos del artículo 77 del
    Código General del Proceso.

    Sírvase, Señor Juez, reconocerle personería jurídica a mi apoderad{gen_apo}, en los términos y para los efectos del presente poder.

    Señor Juez,

    {nom_poder}
    {ced_poder} No. {ced_poder}


    Acepto,


    {nom_apo}
    {id_apo} No. {ced_apo}
    Carné No.{num_car}  del Consultorio Jurídico.
    Universidad Externado de Colombia - Sala Civil.


     """
    return  num_carced_poderrender_template("form_poder.html",nom_poder=nom_poder,gen_poder=gen_pode,email=email,nom_apo=nom_apo,gen_apo=gen_apo,ced_apo=ced_apo,
    email_apo=email_apo,nom_contra=nom_contra,gen_contra=gen_contra,ced_contra=ced_contra,email_2=email_2)



if __name__ == '__main__':
    app.run(debug = True)
