#!/usr/bin/env python3
#  -*- encoding: utf-8 -*-
""" Some Hello World for testing purposes. """

def greeting(name):
    """
    Function to generate a greeting message.

    params name is the name used in the resulting greeting message

    returns a greeting message as a string
    """
    return f"Hello {name}"

if __name__ == "__main__":
    print(greeting("World"))
