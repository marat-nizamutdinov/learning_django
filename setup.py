import codecs
import os
import re
from distutils.core import setup


version = '0.0.0'  # stub for lint

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'learning_django', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


setup(
    name='learning_django',
    version=version,
    packages=['learning_django'],
    url='https://github.com/marat-nizamutdinov/learning_django',
    license='Beer license',
    author='Marat Nizamutdinov',
    author_email='shimizuu86@gmail.com',
    description='Test project and test documentation',
    install_requires=[
        'Django',
        'psycopg2-binary',
        'sorl-thumbnail',
        'Pillow',
    ]
)