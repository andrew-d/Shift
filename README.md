Shift
=====

A generic template library for Python.





Architecture
------------

The general architecture of Shift is as follows:

    - When the shift module is imported, a template registry class is created - this is the Shift class.
    - The shift.engines module is then imported, which imports each of the engine submodules.
    - After the submodules are imported, they are then registered with Shift.  TODO: Does the registration happen in the engine file, or in the main class after the rest are imported?

When you want to use Shift to register a template:

    - Shift.new will attempt to find the most specific mapping for the given file path, and return None if there's no defined mapping that matches.  TODO: should it raise?
    - The returned object is an instance of the individual engine class.
    - Each engine class exposes a render() function, which will render the given file.
    - For convenience, the engines also expose a render_from_string() function, which will render a template string.

Registration Process:

    - Each template class calls Shift.register_class(ClassName, 'mapping')
    - The class is added to a dict of lists for that mapping
    - The initialize() static method is called on the class.  This causes the base class to call on_initialize() if it hasn't already been called.  Note that the return value from this method is then assigned to the initialized static property.
    - When new() is called, for each mapping:
        - If it doesn't exist, go to the next one
        - If it does exist, loop through all template classes in the list.
        - If we find one that has the initialized property set to True, we instantiate it and return it.

