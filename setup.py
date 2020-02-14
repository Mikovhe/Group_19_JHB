from setuptools import setup, find_packages

setup(
    name='group_19_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='statistical utility functions',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/Mikovhe/Group_19_JHB.git',
    author='Mukwevho Mukovhe, Jed Chonowitz, Tumelo Mokubi, Percy Mokone, Thabo Ntsekhe ',
    author_email='<Your Email>'
)