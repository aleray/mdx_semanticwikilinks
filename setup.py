#! /usr/bin/env python


from setuptools import setup
import mdx_semanticwikilinks


setup(
    name='mdx_semanticwikilinks',
    version=mdx_semanticwikilinks.__version__,
    author='Alexandre Leray',
    author_email='alexandre@stdin.fr',
    description='Python-Markdown extension to add support for semantic (wiki)links (RDFa)..',
    url='http://activearchives.org/',
    py_modules=['mdx_semanticwikilinks'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
