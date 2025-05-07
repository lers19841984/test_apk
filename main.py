from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HolaMundoApp(App):
    def build(self):
        # Crear un layout vertical
        self.layout = BoxLayout(orientation='vertical')
        
        # Crear botón
        self.boton = Button(text='¡Presióname!')
        self.boton.bind(on_press=self.mostrar_mensaje)
        
        # Añadir botón al layout
        self.layout.add_widget(self.boton)
        return self.layout

    def mostrar_mensaje(self, instance):
        # Crear y añadir nueva etiqueta con el mensaje
        self.layout.add_widget(Label(text='Hola mundo'))

if __name__ == '__main__':
    HolaMundoApp().run()