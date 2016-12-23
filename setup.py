#!/usr/bin/env python2

from setuptools import setup

setup(
    name='calculator',
    version='0.2.0',
    description='Math expression calculator',
    author='Evgeny Zhurko',
    author_email='evgeny.zhurko@gmail.com',
    packages=['calculator', 'tests'],
    test_suite='tests.test',
    entry_points={
        'console_scripts':
            ['calc = calculator.calc:calculate_shell']
        }
    )
