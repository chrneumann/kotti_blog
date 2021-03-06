from setuptools import setup, find_packages
import sys, os

version = '0.2a1'

tests_require = [
    'pytest',
    'pytest-cov',
]

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
AUTHORS = open(os.path.join(here, 'AUTHORS.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

long_description = (
    README
    + '\n' +
    AUTHORS
    + '\n' +
    CHANGES
)

setup(name='kotti_blog',
      version=version,
      description="Kotti blog",
      long_description=long_description,
      classifiers=[],
      keywords='kotti blog',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Kotti>=0.7a4',
          'plone.batching',
          'AccessControl',  # this is actually a dependency of plone.batching
          'js.jquery_infinite_ajax_scroll',
      ],
      entry_points="""
      [fanstatic.libraries]
      kotti_blog = kotti_blog:library
      """,
      tests_require=tests_require,
      extras_require={
          'testing': tests_require,
          },
      message_extractors={'kotti_blog': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
