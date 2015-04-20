
from setuptools import setup

setup(name='servicemanager',
      version='0.0.24',
      description='A python tool to manage developing and testing with lots of microservices',
      url='https://github.com/hmrc/service-manager',
      author='vaughansharman',
      license='Apache Licence 2.0',
      packages=['servicemanager', 'servicemanager.actions', 'servicemanager.server', 'servicemanager.service', 'servicemanager.thirdparty'],
      install_requires=['requests==2.2.1','pymongo==2.6.3','bottle==0.12.4','pytest==2.5.2','argcomplete==0.8.1'],
      scripts=['bin/sm', 'bin/smserver'],
      zip_safe=False)
