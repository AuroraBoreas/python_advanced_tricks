"""
P130-P133, copy: Duplicate Objects

! What is it?
https://docs.python.org/3/library/copy.html

# A: the copy module includes two functions, copy() and deepcopy() 
# for duplicating existing objects

! Why?

# A: Python refers everything as 'ByRef' in VB or '*pointer' in C/C++ by default
# in some situation, it's convenient to duplicate a copy of objects rather than referencing it directly

! how to use?

copy
|-- shallow copy
|-- deep copy
|-- custome copy behavior
|-- recursion in deep copy

"""