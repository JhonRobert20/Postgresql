from persona import Persona
from conexion import Conexion
from prueba_basededatos import logger

class PersonaDao:
  '''
  DAO (Data Access Object)
  CRUD: Create-Read-Update-Delete
  '''

  __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
  __INSERTAR = 'INSERT INTO persona(nombre, apellido) VALUES(%s, %s)'
  __ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s WHERE id_persona=%s'
  __ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

  @classmethod
  def seleccionar(cls):
    cursor = Conexion.obtenerCursor()
    logger.debug(cursor.mogrify(cls.__SELECCIONAR))
    cursor.execute(cls.__SELECCIONAR)
    registros = cursor.fetchall()
    personas = []
    for registro in registros:
      persona = Persona(registro[0], registro[1], registro[2 ])
      personas.append(persona)
    return personas
  
  @classmethod
  def insertar(cls, persona):
    try:
      conexion = Conexion.obtenerConexion()
      cursor = conexion.cursor()
      logger.debug(cursor.mogrify(cls.__INSERTAR))
      logger.debug(f'Persona a insertar: {persona}')
      valores = (persona.get_nombre(), persona.get_apellido())

      cursor.execute(cls.__INSERTAR, valores)
      conexion.commit()
      return cursor.rowcount

    except Exception as e:
      conexion.rollback()
      logger.error(f'Excepción al insertar persona : {e}')
    
  @classmethod
  def actualizar(cls, persona):
    try:
      conexion = Conexion.obtenerConexion()
      cursor = conexion.cursor()
      logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
      logger.debug(f'Persona a actualizar: {persona}')
      valores = (persona.get_nombre(), persona.get_apellido(), persona.get_id_persona())

      cursor.execute(cls.__ACTUALIZAR, valores)
      conexion.commit()

      return cursor.rowcount

    except Exception as e:
      conexion.rollback()
      logger.error(f'Excepción al actualizar persona : {e}')

  @classmethod
  def eliminar(cls, persona):
    try:
      conexion = Conexion.obtenerConexion()
      cursor = conexion.cursor()
      logger.debug(cursor.mogrify(cls.__ELIMINAR))
      logger.debug(f'Persona a eliminar: {persona}')

      valor = (persona.get_id_persona(),)
      cursor.execute(cls.__ELIMINAR, valor)

      conexion.commit()
      return cursor.rowcount
    
    except Exception as e:
      conexion.rollback()
      logger.error(f'Excepción al insertar persona: {e}')

if __name__ == '__main__':
  # personas = PersonaDao.seleccionar()
  # for persona in personas:
  #   logger.debug(persona.get_nombre())

  #Insertamos un nuevo registro
  # persona = Persona( 
    # nombre = 'Pedro',
    # apellido = 'Naranja' )
  # personas_insertadas = PersonaDao.insertar(persona)

  #logger.debug(f'Personas Insertadas: {personas_insertadas}')

  #Actualizar un registro
  persona = Persona(3, 'Se', 'Cambio')

  personas_actualizadas = PersonaDao.actualizar(persona)
  logger.debug(f'Personas actualizadas: {personas_actualizadas}')

  persona_eliminar = Persona(id_persona = 15)
  personas_eliminadas = PersonaDao.eliminar(persona_eliminar)

  logger.debug(f'Personas eliminadas: {personas_eliminadas}')