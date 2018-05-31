import cmd
class Rotation(cmd.Cmd):
    intro = 'Rotation'
    def do_hello(self, arg):
        print('Hello')
    def do_close(self, arg):
        print('Bye')
        return True