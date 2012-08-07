from setuptools import setup, find_packages

from akanda import meta


setup(
    name=meta.display_name,
    version=meta.version,
    description=meta.description,
    author=meta.author,
    author_email=meta.author_email,
    url=meta.url,
    license=meta.license,
    install_requires=meta.requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'akanda-configure-ssh ='
            'akanda.tools.management:configure_ssh',
        ]
    },
)
