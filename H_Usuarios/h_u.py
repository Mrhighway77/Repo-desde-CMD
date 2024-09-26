import pandas as pd

# Datos organizados por secciones con la información relevante
data = {
    "Sección": [
        "1. Antecedentes Personales", "1. Antecedentes Personales", "1. Antecedentes Personales", 
        "2. Descripción Proyecto APT", "3. Fundamentación Proyecto APT", "4. Objetivos",
        "4. Objetivo general", "4. Objetivos específicos", "4. Objetivos específicos", 
        "4. Objetivos específicos", "5. Metodología", "6. Evidencias", 
        "6. Evidencias", "6. Evidencias", "7. Plan de Trabajo", "7. Plan de Trabajo",
        "7. Plan de Trabajo", "7. Plan de Trabajo", "7. Plan de Trabajo", 
        "7. Plan de Trabajo", "7. Plan de Trabajo", "7. Plan de Trabajo", 
        "7. Plan de Trabajo", "8. Carta Gantt"
    ],
    "Información": [
        # Antecedentes personales
        "Nombre estudiante: Alex Baeza, Marco Puga, Constanza Vilaza",
        "Rut: 17316832-2, 18697880-3, 18546253-6", 
        "Carrera: Ingeniería en Informática",

        # Descripción del proyecto
        ("Nombre del proyecto: Proyecto inmobiliario con inteligencia artificial. Áreas de desempeño: "
         "Base de datos, programación web, calidad de software, minería de datos, machine learning. "
         "Competencias: Utilización de PostgreSQL, plataforma web conectada a una API y modelo predictivo."),

        # Fundamentación del proyecto
        ("Relevancia: El proyecto busca resolver la disminución de la demanda de compra de viviendas en "
         "la Región Metropolitana, mediante la digitalización inmobiliaria y una plataforma web."),

        # Objetivo general y específicos
        "Objetivo General: Desarrollar una plataforma digital de intermediación inmobiliaria.",
        "Realizar un estudio de las zonas con propiedades para compra disponibles.",
        "Evaluar y seleccionar propiedades para alojamiento según ubicación y disponibilidad.",
        "Desarrollar una aplicación web para búsqueda de propiedades con un valor aproximado.",

        # Metodología
        ("Metodología: Se utilizará Scrum, con sprints de 2 semanas y reuniones diarias (Dailys) "
         "a las 9 pm vía Google Meet."),

        # Evidencias
        "Tipo de evidencia: Dataset de zona oriente",
        "Tipo de evidencia: Notebook predictivo",
        "Tipo de evidencia: Plataforma web funcional",

        # Competencias
        ("Competencias: Programación de Software, Minería de Datos, Desarrollo de Modelos de Datos, "
         "Programación Web, Calidad de Software."),

        # Plan de trabajo
        "Actividad: Planificación del proyecto",
        "Actividad: Scraping de datos de propiedades en la zona oriente",
        "Actividad: Limpieza y preparación del dataset",
        "Actividad: Desarrollo del modelo predictivo",
        "Actividad: Desarrollo de la aplicación web",
        "Actividad: Pruebas y validación del sistema",
        "Actividad: Documentación técnica",
        "Actividad: Integración del modelo predictivo con la plataforma web y PostgreSQL.",

        # Carta Gantt (falta este elemento)
        "Se incluirá Carta Gantt de actividades planificadas."
    ]
}

# Comprobación de las longitudes de las listas
seccion_len = len(data['Sección'])
info_len = len(data['Información'])

print(f"Longitud de 'Sección': {seccion_len}")
print(f"Longitud de 'Información': {info_len}")

# Creación del DataFrame solo si las longitudes coinciden
if seccion_len == info_len:
    df = pd.DataFrame(data)
    
    # Guardando el DataFrame en un archivo Excel
    excel_path = "Proyecto_Titulo_Historias_Usuario.xlsx"
    df.to_excel(excel_path, index=False)

    print(f"Archivo Excel guardado en: {excel_path}")
else:
    print("Error: Las listas 'Sección' e 'Información' no tienen la misma longitud.")
