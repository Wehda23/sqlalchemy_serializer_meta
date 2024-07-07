from setuptools import setup, find_packages

setup(
    name="sqlalchemy_serializer_meta",
    version="0.1.0",
    description="A simple serializer for SQLAlchemy models and Flask Models",
    long_description="A simple serializer for SQLAlchemy models and Flask Models",
    long_description_content_type="text/markdown",
    url="https://github.com/sergey-sokolov/sqlalchemy_serializer_meta",
    author="Sergey Sokolov",
    author_email="sergey.sokolov@yandex.ru",
    license="MIT",
    packages=find_packages(),
    install_requires=["sqlalchemy", "pydantic==2.7.4", "pydantic_core==2.18.4"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        ],
    keywords="sqlalchemy serializer pydantic flask",
)