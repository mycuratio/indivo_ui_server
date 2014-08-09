# the two places where we point to apps are:
# 1. in TEMPLATE_DIRS
# 2. through hardcoded URL routes in the file ref'd by ROOT_URLCONF

SERVER_ROOT_DIR = '/indivo/indivo_ui_server'
INDIVO_UI_SERVER_BASE = 'http://localhost5151'
INDIVO_SERVER_LOCATION = 'http://localhost:8000'
CONSUMER_KEY='curatehealth'
CONSUMER_SECRET='curatehealth'
SECRET_KEY = 'curatehealth'

# we need to put absolute paths here for the UI server's template AND
# each app's /jmvc/ directory otherwise the UI server will not load the jmvc
# start page. The django.template.loaders.app_directories.Loader is no help
# to us since it looks for a statically named /templates/ directory.
TEMPLATE_DIRS = (
    SERVER_ROOT_DIR + "/templates",
    SERVER_ROOT_DIR + '/apps/allergies/jmvc/',
    SERVER_ROOT_DIR + '/apps/immunizations/jmvc/',
    SERVER_ROOT_DIR + '/apps/labs/jmvc/',
    SERVER_ROOT_DIR + '/apps/labs/templates/',
    SERVER_ROOT_DIR + '/apps/medications/jmvc/',
    # SERVER_ROOT_DIR + '/apps/problems/templates',
    SERVER_ROOT_DIR + '/apps/'  # the problems app is a non-jmvc app and has a different template path
)

DEBUG = True
TEMPLATE_DEBUG = True
HIDE_HEALTHFEED = False
HIDE_INBOX = False
DISABLE_APP_SETTINGS = False
HIDE_SHARING = False
ROOT_URLCONF = 'urls'

# allow to signup via web?
REGISTRATION = {
	'enable': True,						# True or False
	'set_primary_secret': 1,			# 0 or 1. If 0, administrators will have to approve accounts. If set to 1, make sure the server has SEND_MAIL enabled!
	'set_secondary_secret': 1,			# 0 or 1. Can only be 1 if primary is also 1
	'min_password_length': 8,
	'autocreate_record': True			# if True creates a first record based on account name and email automatically
}

# allow user to add records?
ALLOW_ADDING_RECORDS = True

# handling of user secrets
PASSWORD_RESET_REQUIRE_SECONDARY = True

#  quick and dirty private labeling (optional)
#BRANDING = {
#   'short_name': 'Indivo&trade;',
#   'pretty_name': 'Indivo&trade;',
#   'pretty_name_prepend': '',
#   'header_template': 'ui/header.html',
#   'footer_template': 'ui/footer_sandbox.html',
#   'logo_image_src': '/jmvc/ui/resources/images/branding/gpp_three_loop_96x31.png',
#   'logo_image_big_src': '/jmvc/ui/resources/images/branding/gpp_three_loop_big.png'
#}

TIME_ZONE = 'UTC'
SESSION_COOKIE_NAME = "indivo_ui_sessionid"
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

# don't forget comma here. just love the python tuple!
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'ui'
)
# use file based sessions for now - fixme: security?
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = SERVER_ROOT_DIR + "/sessions"

# Use the following when not in development, and adjust accordingly:
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# ALLOWED_HOSTS = ['www.yoursite.com']
