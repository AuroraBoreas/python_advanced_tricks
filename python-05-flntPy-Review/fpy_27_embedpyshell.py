# method 01
def embed_py_shell1():
    import pyreadline
    import code
    variables = globals().copy()
    variables.update(locals())
    shell = code.InteractiveConsole(variables)
    shell.interact()

# method 02
def embed_py_shell2():
    from IPython import embed
    embed()

# method 03
var1 = 5      # command line variable
var2 = "Mike" # command line variable
def keyboard(banner=None):
    import code, sys
    # uses exceptio n trick to pick up the current frame
    try:
        raise None # it's the intension here
    except:
        frame = sys.exc_info()[2].tb_frame.f_back
    # evaluate commands in current namespace
    namespace = frame.f_globals.copy()
    namespace.update(frame.f_locals)
    code.interact(banner=banner, local=namespace)

if __name__ == "__main__":
    keyboard()