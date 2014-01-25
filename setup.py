from setuptools import setup, find_packages

setup(
    name='django-moneybookers',
    version='0.2',
    author='Alex Aster',
    maintainer="GoTLiuM InSPiRiT",
    maintainer_email="gotlium@gmail.com",
    description=str('Moneyboookers gateway allows you to accept '
                    'payments on your website'),
    url='https://github.com/gotlium/django-moneybookers',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.4',
    ],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 2.7",
    ],
)
