Packaging and distributing:
    package was created by:
        python setup.py sdist
    install package:
        pip install -e
    now the package is available via:
        rss_parser ... 

TESTS:
    How to run a unit test:
        coverage run -m unittest test_convert_module.py 
    How to check its coverage:
        coverage report -m