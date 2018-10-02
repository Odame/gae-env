from setuptools import setup

# the rst content from this function will be rendered as the lib 'homepage' on pypi


def readme():
    with open('README.rst') as readme_file:
        return readme_file.read()


setup(
    name='gae_env',
    version='0.1.0',
    description='Google Appengine environment variables stored in Cloud Datastore',
    long_description='Google Appengine environment variables stored in Cloud Datastore.' +
    'This enables easy access to edit variables in Developers Console, ' +
    'and prevents bad practice of storing environment variables in code ' +
    '(app.yaml or secrets.json files)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='google appengine env var environment variable cloud datastore',
    # url='http://github.com/Odame/gae_env',
    author='Prince Odame',
    author_email='opodame@gmail.com',
    license='MIT',
    packages=['gae_env'],
    zip_safe=False,
)
