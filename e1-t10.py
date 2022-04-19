# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.
import tkinter
from tkinter import StringVar
from tkinter import ttk

# Creamos una ventana
window = tkinter.Tk()               # Instancia de Tk
window.title( 'Ejericicio 1 - Tema 10' )

default_msg = 'Selecciona una opción'

selected_language = tkinter.StringVar()
msg = tkinter.StringVar( value = default_msg )
print( selected_language.get() )
print( msg.get() )

def on_radiobutton_change( *args ) :
    msg.set( f'Has seleccionado { selected_language.get() }!' )
    print( msg.get() )

def send_answer( event ) :
     print( f' > { selected_language.get() }' )

def reset( event ) :
    selected_language.set( '' )
    msg.set( default_msg )
    label_answer.config( text = msg.get() )

def set_label_answer_text() :
    # Establece nuevo texto al Componente Label
    label_answer.config( text = msg.get() )

# Escucha por cambios en el valor de la variable
selected_language.trace_add( 'write', on_radiobutton_change )


# Crea Componente Label
label_question = ttk.Label( window, text = 'El lenguaje que mas te gusta es:' )
label_question.grid(
    column = 0,
    row = 0,
    sticky = tkinter.W,
    pady = 3,
)

languages = [ 'JavaScript', 'PHP', 'Python', 'Ruby' ]
rb_options = []

for idx, language in enumerate( languages ):
    rb_options.append( 
        ttk.Radiobutton(
            window,
            text = language,
            value = language.lower(),
            variable = selected_language,
            command = set_label_answer_text
        ) 
    )
    rb_options[ idx ].grid(
        column = 0,
        row = idx + 1,
        sticky = tkinter.W,
        pady = 3,
        padx = 15
    )

#print( rb_options )

# Crea Componente Label
label_answer = ttk.Label( window, text = msg.get() )
label_answer.grid(
    column = 0,
    row = len( languages ) + 1,
    sticky = tkinter.W,
    pady = 3,
)

# Crea Componente Boton
button_send = ttk.Button( window, text = 'Responder' )
button_send.grid(
    column = 0,
    row = len( languages ) + 2,
    sticky = tkinter.E,
    padx = 5,
    pady = 5
)
button_send.bind(
    '<Button-1>',
    send_answer         # Callback
)

# Crea Componente Boton
button_reset = ttk.Button( window, text = 'Reset' )
button_reset.grid(
    column = 1,
    row = len( languages ) + 2,
    sticky = tkinter.W,
    padx = 5,
    pady = 5
)
button_reset.bind(
    '<Button-1>',
    reset         # Callback
)


if __name__ == "__main__" :
    window.mainloop()   