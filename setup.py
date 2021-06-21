from setuptools import setup

setup(
    name='rss_parser',
    version='1.0',
    author='disp1air',
    install_requires=[
        'pdfkit==0.6.1',
        'requests=2.25.1'
    ],
    py_modules=['main'],
    entry_points='''
        [console_scripts]
        rss_parser=main:main
    '''
)
