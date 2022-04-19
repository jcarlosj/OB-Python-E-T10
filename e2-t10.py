# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
import tkinter
from tkinter import StringVar
from tkinter import ttk

# Creamos una ventana
window = tkinter.Tk()               # Instancia de Tk
window.title( 'Ejericicio 2 - Tema 10' )

# Define dimensiones
window.columnconfigure( 0, weight = 1 )
window.rowconfigure( 0, weight = 3 )

default_msg = 'Selecciona una opción'

languages = ( 'JavaScript', 'PHP', 'Python', 'Ruby', 'Dart', 'Rush', 'Perl', 'Go', 'Java', 'C', 'C++' )
lista_items = StringVar( value = languages )

msg = tkinter.StringVar( value = default_msg )
print( msg.get() )

def send_answer( event ) :
    for i in listbox_languages.curselection():
        print( f' > { listbox_languages.get( i ) }' )

def selected_item( event ):
     
    # curselection: retorna una tupla con los items del listbox
    for i in listbox_languages.curselection():
        print( listbox_languages.get( i ) )
        msg.set( f'Has seleccionado { listbox_languages.get( i ) }!' )
    
    print( msg.get() )
    label_answer.config( text = msg.get() )     # Establece nuevo texto al Componente Label

    

# Crea Componente Label
label_question = ttk.Label( window, text = 'El lenguaje que mas te gusta es:' )
label_question.grid(
    column = 0,
    row = 0,
    sticky = tkinter.W,
    pady = 3,
)

# Crea el Componente Listbox
listbox_languages = tkinter.Listbox(
    window,
    selectbackground = 'gray',
    listvariable = lista_items,    # lista que se desea mostrar
    height = 5,    # altura
)
listbox_languages.bind(
    '<<ListboxSelect>>',
    selected_item
)
listbox_languages.grid(
    column = 0,
    row = 1,
    sticky = tkinter.W,
    pady = 2,
    padx = 5
)

# Crea Componente Label
label_answer = ttk.Label( window, text = default_msg )
label_answer.grid(
    column = 0,
    row = 2,
    sticky = tkinter.W,
    pady = 3,
)

# Crea Componente Boton
button_send = ttk.Button(
    window,
    text = 'Responder',
    # command = selected_item
)
button_send.grid(
    column = 0,
    row = 3,
    sticky = tkinter.E,
    padx = 5,
    pady = 5
)
button_send.bind(
    '<Button-1>',
    send_answer         # Callback
)

if __name__ == "__main__" :
    window.mainloop()   