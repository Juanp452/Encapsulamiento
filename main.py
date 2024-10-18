from classWindows import Window

ventana = Window()
ventana.setDimesions(500, 500)
ventana.setTitulo("Mi primer amor")
ventana.setResize(False)

print(ventana.getDimensions())
print(ventana.getResize())
print(ventana.getTitulo())

ventana.crear_ventana()

