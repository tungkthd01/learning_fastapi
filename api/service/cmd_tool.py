from click_shell import shell


@shell(prompt="neural-shell > ", intro="""Welcom to the Neural shell""")
def neural_shell():
    pass



@neural_shell.command()
def help():
    print("You've been cheated")
    
# @neural_shell.command
# def exit():


neural_shell()