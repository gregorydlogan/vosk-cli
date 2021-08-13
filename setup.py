from setuptools import setup

setup(name='vosk_cli',
      version='0.1',
      description='TODO',
      url='http://github.com/opencast',
      author='Martin Wygas',
      author_email='mwygas@uos.de',
      license='ECLv2',
      packages=['vosk_cli'],
      license_files = ('LICENSE.txt'),
      install_requires=[
		'vosk>=0.3.30',
		'webvtt-py>=0.4.6'
      ],
      include_package_data = True,
      zip_safe=False,
      entry_points = {
        'console_scripts': ['vosk-cli=vosk_cli.transcribe:main'],
    }
)
