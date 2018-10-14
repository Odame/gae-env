from setuptools import setup


def readme():
    """ Read the content of the README.md file as the long description """
    with open('README.md') as readme_file:
        return readme_file.read()


setup(
    name='gae_env',
    version='0.1.2',
    description='Google Appengine environment variables stored in Cloud Datastore (and/or system environment variables)',
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='google appengine env var environment variable cloud datastore',
    url='https://github.com/Odame/gae-env',
    author='Prince Odame',
    author_email='opodame@gmail.com',
    license='MIT',
    packages=['gae_env'],
    zip_safe=False
)
