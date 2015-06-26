#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Utility functions'''

import pkg_resources

def example_audio_file():
    '''Get the included example file'''
    path = 'examples/audio/amen.wav'
    return pkg_resources.resource_filename(__name__, path)

