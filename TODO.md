Todo List
=========

List of stuff to do, in roughly priority order.

 - Work on how Shift loads templates from the filesystem
    - Loading the initial template, and also somehow pass to the template engine
 - Ability to pass various options to the actual template engine
 - Tests of the various template engines


Future plans for template loading:
 - Reorganize Shift class - classes still register with a static method, but you need to instantiate a copy of the class to call new().  On instantiation, can pass settings like, e.g. the template base directory, and so on
 - BaseTemplate shouldn't be reading files.  Perhaps have a render() from a file-like object function, and from a string?
 - Need to pass the template path to some of the engines so that including other templates works.  Test with Jinja2
 - Should look into whether it's worth it to seperate the logic for rendering from a file and rendering from a string.  Might be worth offering two hooks (on_render_file and on_render, and have the on_render_file hook default to simply reading the file path and then calling the on_render hook with the result).
 - Need to be sure that this is still easy to use!


 - New-ish plan:
    - Seperate loading the template from rendering it.  Specifically make initializing a template class be the 'load' operation, and the render() method actually render the template.
    - This lets us nicely seperate the 'how do we find the file/pass the file path to a loader' from 'how do we turn a template into a string'
    - Shift.new() will effectively dynamically pick a template class and then call TemplateClass.new(file_path, root_path)
    - Template classes should accept either as None.  This is handy for when we're, e.g. rendering Markdown from a string.

