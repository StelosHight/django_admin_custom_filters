from io import open
from setuptools import setup, find_packages


def read(f):
    return open(f, "r").read()


setup(
    name='django_admin_custom_filters',
    version='0.1.0',
    description='Custom filters for Django Admin',
    url='https://github.com/StelosHight/django_admin_custom_filters',
    author='StelosHight',
    author_email='stanislav.khansu@gmail.com',
    license='GPL',
    packages=find_packages(exclude=("img", "examples")),
    install_requires=['Django>=2.1.2,<3.0.4', ],
    python_requires=">=3.6",

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
