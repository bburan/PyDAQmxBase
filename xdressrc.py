package = 'nidaqmx'
packagedir = 'nidaqmx'

stlcontainers = [
    ('vector', 'str'),
    ('set', 'uint'),
    ('map', 'int', 'float'),
]

functions = [('*', 'include/NIDAQmxBase.*')]
classes = [('*', 'include/NIDAQmxBase.*')]
