from setuptools import setup

required = [
    "flask==2.2.5"
    "flask-sqlalchemy==3.0.3"
    "psycopg2-binary==2.9.6"
    "flask-login==0.6.2"
    "python-slugify==8.0.1"
    "flask-wtf==1.1.1"
    "email-validator==2.0.0"
]

setup(
    name="Flask-Mead",
    version="0.0.1",
    url="https://github.com/peef-dev/mead",
    license="ISC",
    author="Abdou Nasser",
    description="""[Work In Progress] Flask-Mead is a Flask extension that let's you
    build custom components for your web application.""",
    long_description=__doc__,
    long_description_content_type="text/markdown",
    platforms="any",
    packages=["flask_mead"],
    zip_safe=False,
    include_package_data=True,
    test_suite="tests",
    install_requires=required,
    keywords="flask extension for web component",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
