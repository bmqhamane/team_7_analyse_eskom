from setuptools import setup, find_packages

setup(
    name='team_7_analyse_eskom_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA python Load-shedding package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/bmqhamane/team_7_analyse_eskom',
    author='<team_7_analyse>',
    author_email='<@gmail.com>'
)