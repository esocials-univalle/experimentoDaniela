from os import environ

SESSION_CONFIGS = [
     dict(
        name='lideres_sociales_empatia',
        display_name="desensibilización de la violencia - empatia",
        num_demo_participants=40,
        app_sequence=['lideres_sociales'],
        tipo = 'Empatia'
     ),
     dict(
        name='lideres_sociales_empirico',
        display_name="desensibilización de la violencia - empirico",
        num_demo_participants=40,
        app_sequence=['lideres_sociales'],
        tipo = 'Empirico'
     ),
     dict(
        name='lideres_sociales_informacional',
        display_name="desensibilización de la violencia - informacional",
        num_demo_participants=40,
        app_sequence=['lideres_sociales'],
        tipo = 'Informacional'
     ),
     dict(
        name='lideres_sociales_linea_base',
        display_name="desensibilización de la violencia - linea base",
        num_demo_participants=40,
        app_sequence=['lideres_sociales'],
        tipo = 'Linea_base'
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'k%9b3m7&0-yjbnu^ms&)vcr@#y3^qc%0lirxb+r-ipps)%r483'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
