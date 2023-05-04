from django.shortcuts import render, HttpResponse
from facturas.models import Cliente, Helado, Topping, Factura, DetalleFactura

# Create your views here.


def index(request):
    return render(request,'index.html')

def tipo(request):

    if request.method == 'POST':

        tipo_de_helado=request.POST.get('tipo_helado')
        print(tipo_de_helado)
        if tipo_de_helado == 'cremoso':
            return render(request, 'tamano_cremoso.html')
        elif tipo_de_helado == 'hielo':
            return render(request, 'tamano_hielo.html')
        else:
            return render(request, 'index.html')

def sabor_cremoso(request):

  
    if request.method == 'POST':
        num_bolas=request.POST.get('cantidad')
        top=request.POST.get('topping')
        top_=topping_s(top)
        tipo='cremoso'
        sabor1=request.POST.get('sabor1')
        sabor2=request.POST.get('sabor2')
        sabor3=request.POST.get('sabor3')
        sabor=sabor1+' '+sabor2+' '+sabor3

        if num_bolas=='1':
            tam=15
            total= tam + top_
        elif num_bolas=='2':
            tam=20
            total= tam + top_ 
        elif num_bolas=='3':
            tam=24
            total= tam + top_
        else:
            return render(request, 'tamano_cremoso.html') 

    return render(request, 'total_cremoso.html', {
        'total': total,
        'top': top,
        'top_': top_,
        'tam': tam,
        'bolas': num_bolas,
        'tipo': tipo,
        'sabor': sabor
    })
 
def sabor_hielo(request):
 
  
    if request.method == 'POST':
        tamanio=request.POST.get('tamanio')
        top=request.POST.get('topping')
        top_=topping_s(top)
        tipo='hielo'
        sabor=request.POST.get('sabor[]')
        if tamanio=='pequeno':
            tam=15
            total= tam + top_
        elif tamanio=='mediano':
            tam=20
            total= tam + top_ 
        elif tamanio=='grande':
            tam=24
            total= tam + top_
        else:
            return render(request, 'tamano_hielo.html') 

    return render(request, 'total_hielo.html', {
        'total': total,
        'top': top,
        'top_': top_,
        'tam': tam,
        'tamanio': tamanio,
        'tipo': tipo,
        'sabor': sabor
    })

def topping_s(top):
    if top=='no aplica':
        return 0
    elif top== 'chispas de chocolate':
        return 5
    elif top== 'anillos':
        return 3
    elif top== 'crema batida':
        return 7
    elif top== 'chocolate líquido':
        return 5
    else:
        return 0

def registro(request):

    if request.method=='POST':
        top=request.POST.get('top')
        precio_top=request.POST.get('precio_top')
        tipo=request.POST.get('tipo')
        tamano=request.POST.get('tamano')
        precio=request.POST.get('tam')
        sabor=request.POST.get('sabor')


    return render(request, 'registro.html',{
        'top': top,
        'precio_top': precio_top,
        'tipo': tipo,
        'tamano': tamano,
        'precio': precio,
        'sabor': sabor
    })

def fin(request):
    if request.method == 'POST':
        nit_c=request.POST.get('nit')
        nombre_c =request.POST.get('nombre')
        correo_c=request.POST.get('correo')
        top=request.POST.get('top')
        precio_top=request.POST.get('precio_top')
       
        tipo=request.POST.get('tipo')
        tamano=request.POST.get('tamano')
        precio=request.POST.get('precio')
        sabor=request.POST.get('sabor')

        cantidad_helado=precio_top+precio

        cliente = Cliente(nit=nit_c,nombre=nombre_c, correo=correo_c)
        cliente.save()
        factura=Factura(cliente=cliente)
        factura.save()
        topping=Topping(nombre=top,precio=precio_top)
        topping.save()
        helado=Helado(tipo=tipo,sabor=sabor,tam=tamano,precio=precio)
        helado.save()
        # Crear un objeto DetalleFactura y guardarlo en la base de datos
        detalle_factura = DetalleFactura(factura=factura, helado=helado, topping=topping, cantidad=cantidad_helado)
        detalle_factura.save()
    return render(request, 'exito.html')