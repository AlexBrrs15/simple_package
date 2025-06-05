from setuptools import setup, find_packages

setup(
    name='simple_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Seu Nome',
    author_email='seu@email.com',
    description='Um pacote simples de exemplo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/simple_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
