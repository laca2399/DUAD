#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

#Usos comunes: reutilización de código, extender y combinar funcionalidades, patrones de diseño, jerarquía de usuario

class Admin:
    def manage_project(self):
        print("Managing the project")

class Editor:
    def edit_project(self):
        print("Editing the project")

class Consultor:
    def consulting_project(self):
        print("Consulting the project")

class User(Admin, Editor, Consultor):
    pass

user = User()
user.manage_project()
user.edit_project()
user.consulting_project()