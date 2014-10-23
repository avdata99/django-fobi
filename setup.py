import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    screenshots = open(os.path.join(os.path.dirname(__file__), 'SCREENSHOTS.rst')).read()
    screenshots = screenshots.replace('.. image:: _static', '.. figure:: https://github.com/barseghyanartur/django-fobi/raw/master/docs/_static')
except:
    readme = ''
    screenshots = ''

template_dirs = [
    "src/fobi/templates/fobi", # Core templates

    "src/fobi/contrib/themes/bootstrap3/templates/bootstrap3", # Bootstrap 3
    "src/fobi/contrib/themes/foundation5/templates/foundation5", # Foundation 5
    "src/fobi/contrib/themes/simple/templates/simple", # Simple

    #"src/fobi/contrib/apps/djangocms_integration/templates/djangocms_integration", # DjangoCMS integration
    #"src/fobi/contrib/apps/feincms_integration/templates/feincms_integration", # FeinCMS integration

    "src/fobi/contrib/plugins/form_elements/content/image/templates/image", # Content image

    "src/fobi/contrib/plugins/form_handlers/db_store/templates/db_store", # DB Store
    "src/fobi/contrib/plugins/form_handlers/mail/templates/mail", # Mail
    "src/fobi/contrib/plugins/form_handlers/http_repost/templates/http_repost", # Http repost
]
static_dirs = [
    "src/fobi/static", # Core static

    "src/fobi/contrib/themes/bootstrap3/static", # Bootstrap3
    "src/fobi/contrib/themes/foundation5/static", # Foundation5
    "src/fobi/contrib/themes/simple/static", # Simple

    "src/fobi/contrib/plugins/form_handlers/db_store/static", # DB Store

    "src/fobi/contrib/plugins/form_elements/content/dummy/static", # Content image
]

locale_dirs = [
    "src/fobi/locale/nl",
    "src/fobi/locale/ru",
]

templates = []
static_files = []
locale_files = []

for template_dir in template_dirs:
    templates += [os.path.join(template_dir, f) for f in os.listdir(template_dir)]

for static_dir in static_dirs:
    static_files += [os.path.join(static_dir, f) for f in os.listdir(static_dir)]

for locale_dir in locale_dirs:
    locale_files += [os.path.join(locale_dir, f) for f in os.listdir(locale_dir)]

version = '0.1.5'

install_requires = [
    'Pillow>=2.0.0',
    'requests>=1.0.0',
    'django-autoslug>=1.3.0',
    'django-tinymce>=1.5.3',
    'ordereddict>=1.1',
    'six>=1.4.1',
    'easy-thumbnails>=1.4,<2.0',
    'transliterate>=1.5,<2.0',
    'vishap>=0.1.1,<2.0'
]

tests_require = [
    'radar>=0.3,<1.0',
    'simple_timer>=0.2',
    'selenium',
]

try:
    PY2 = sys.version_info[0] == 2
    LTE_PY26 = PY2 and (7 > sys.version_info[1])
    PY3 = sys.version_info[0] == 3
    #if LTE_PY26:
    #    install_requires.append('ordereddict==1.1')
except:
    pass

setup(
    name = 'django-fobi',
    version = version,
    description = ("Customisable, modular user- and developer- friendly form builder application for Django"),
    long_description = "{0}{1}".format(readme, screenshots),
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords = 'django, forms, form builder, forms builder, form designer',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/django-fobi/',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    install_requires = install_requires,
    tests_require = tests_require,
    package_data = {
        'fobi': templates + static_files + locale_files
    },
    include_package_data = True,
)
