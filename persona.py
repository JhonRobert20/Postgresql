from prueba_basededatos import logger

class Persona:
  def __init__(self, id_persona = None, nombre = None, apellido = None):
    self.__id_persona = id_persona
    self.__nombre = nombre
    self.__apellido = apellido

  def __str__(self):
    return(
      f'Id Persona: {self.__id_persona}, '
      f'Nombre: {self.__nombre}, '
      f'Apellido: {self.__apellido}'
    )
  
  def get_id_persona(self):
    return(self.__id_persona)

  def get_nombre(self):
    return(self.__nombre)
  
  def get_apellido(self):
    return(self.__apellido)
  
  def set_id_persona(self, id_persona):
    self.__id_persona = id_persona
  
  def set_nombre(self, nombre):
    self.__nombre = nombre

  def set_apellido(self, apellido):
    self.__apellido = apellido
  

if __name__ == '__main__':
  persona1 = Persona(3, "Juan", "Perez")
  logger.info(persona1)

  #Simulando un objeto a insertar de tipo persona
  persona2 = Persona(nombre =  "Juan", apellido = "Perez")
  logger.debug(persona2)

  #Simulando el caso de eliminar un objeto de tipo persona
  persona3 = Persona(id_persona = 3)
  logger.info(persona3)