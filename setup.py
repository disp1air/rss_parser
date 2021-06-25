from setuptools import setup

setup(
    name='rss_parser',
    version='1.0',
    author='disp1air',
    install_requires=[
        'pdfkit',
        'requests'
    ],
    py_modules=['main'],
    entry_points='''
        [console_scripts]
        rss_parser=main:main
    '''
)
