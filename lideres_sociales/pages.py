from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Player


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(self):

        self.player.payoff = Constants.endowment - self.player.contribution

        
    

class Consent(Page):
    form_model = 'player' 
    form_fields = ['num_temporal','genero', 'accepts_terms']

class Survey(Page):
    form_model = 'player'    
    form_fields = ['frase_1', 'frase_2', 'frase_3', 'frase_4', 'frase_5', 'frase_6', 'frase_7', 'calidad_noticia', 'informacion_noticia', 'noticia_incompleta', 'noticia_credibilidad', 'noticia_tiempo',
    'noticia_calidad', 'noticia_imagenes', 'noticia_publico_general', 'noticia_informacion_importante',
    'noticia_informacion_importante_politicos', 'noticia_lenguaje', 'noticia_lideres_similar',
    'noticia_impactante', 'noticia_angustiante', 'noticia_violenta', 'lider_necesario', 
    'gobierno_responsable_lideres', 'conflicto_armado_cesado',
    'victima_responsable', 'siente_compasion']

class SurveyEMP(Page):
    form_model = 'player'    
    form_fields = ['entristece_persona_solitaria', 'importancia_sentimientos',
    'muestras_afecto', 'molestan_personas_infelices', 'ponerse_nervioso', 'llorar_felicidad', 'involucrarse_emocionalmente', 
    'cancion_conmueve', 'perder_control_malas_noticias', 'gente_influencia_estado_animo', 'extrajeros_geniales', 'trabajador_social',
    'enfado_amigo', 'abrir_regalos', 'gente_solitaria_no_amistosa', 'llorar_molesta', 'canciones_feliz', 'sentimientos_personajes_novela',
    'enfado_maltrato', 'mantener_calma', 'amigo_problemas', 'risa_otro', 'llanto_divierte', 'decisiones_sin_sentimientos', 'gente_deprimida_alrededor', 
    'irritar_gente', 'disgusto_animal_sufriendo', 'involucrarse_libros_tonto', 'ancianos_indefensos', 'irrita_lagrimas_otros', 'involucrar_pelicula', 
    'mantener_calma_emocion', 'ninos_lloran_sin_razon']


class SocioDemSurvey(Page):
    form_model = 'player'
    form_fields = ['edad', 'ciudad', 'estrato', 'estado_civil', 'numero_hijos', 'identifica_cultura',
    'identifica_religion',"identifica_partido",'nivel_estudios', 'tendencia_politica', 'disposicion_riesgos']

class Socio1(Page):
    form_model = 'player'
    form_fields = ['victima_violencia_farc_eln', 
    'victima_violencia_auc_otros', 'victima_violencia_otros_delicuencia', 'victima_no_violencia', 'familia_victima_farc_eln', 
    'familia_victima_auc_otros', 'familia_victima_otros_delincuencia', 'familia_victima_no_violencia']

class Socio2(Page):
    form_model = 'player'
    form_fields = ['conseguir_esfuerzo','planes_termino', 'juego_suerte', 'propongo_aprender', 'mayores_logros', 'establecer_metas', 'competencia_excelencia',
    'salir_adelante', 'comparar_calificaciones', 'empeno_trabajo']

class Socio3(Page):
    form_model = 'player'
    form_fields = ['alcanzar_objetivos', 'cumplir_tareas', 'obtener_resultados',
    'exito_esfuerzo','superar_desafios', 'confianza_tareas', 'tareas_excelencia', 'tareas_dificiles']

class Invitation(Page):
    form_model = 'player'
    form_fields = ['firma_acta', 'firma_acta1']

class Donation(Page):
    form_model = 'player'
    form_fields = ['contribution', 'correo_contribution']

class Piloto(Page):
    form_model = 'player'
    form_fields = ['afirmacion_1EMP', 'afirmacion_2EMP', "afirmacion_3EN", "afirmacion_4EN", "afirmacion_5EEmp", "afirmacion_6EEmp",
    "afirmacion_7Inf", "afirmacion_8Inf", "afirmacion_9LB", "afirmacion_10LB"]

class Video(Page):
    form_model = 'player'
    
    def vars_for_template(self):

        link = ""

        print(self.session.config['tipo'] == 'Empatia')

        if self.session.config['tipo'] == 'Empatia':
            self.player.tratamiento = "Empatia"
            link = "https://drive.google.com/file/d/17rSnZmdJel1yJlJuKLEQjUpcKXPUrkA7/preview"
        
        elif self.session.config['tipo'] == 'Empirico':
            self.player.tratamiento = "Empirico"
            link = "https://drive.google.com/file/d/1i3nQTwchHvWBEodL40cih6X211OoBXei/preview"
        elif self.session.config['tipo'] == 'Informacional':
            self.player.tratamiento = "Informacional"
            link = "https://drive.google.com/file/d/19xw56Bwt9Ea8Fhy_M88nTsj5YHZutbWp/preview"
        elif self.session.config['tipo'] == 'Linea_base':
            self.player.tratamiento = "Linea_base"
            link = "https://drive.google.com/file/d/13Hy0YaEkpqCnhn1U7qQVDQzoUUP5Fr4D/preview"
    
        
        return {
            
            'genero': self.player.genero,
            'link' : link
        }


class Final(Page):
    form_model = 'player'
    form_fields = ['contribution']


page_sequence = [Consent, Video, Piloto, Survey, SurveyEMP, SocioDemSurvey, Socio1, Socio3, Invitation, Donation,  Results]
