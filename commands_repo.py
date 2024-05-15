from commands import ClearCommand, ExitCommand, ManualCommand, PrintCommand

avaliable_commands = [
    PrintCommand(),
    ExitCommand(),
    ClearCommand(),
    ManualCommand(),
]


def search_command_by_name(name: str):
    commands_found = list(filter(lambda x: x.name == name, avaliable_commands))

    # Ponto de melhoria:
    # Assume-se que o commands_found só vai encontrar um commando com
    # o mesmo nome.
    # O ideal seria levantar uma exceção em caso de duplicata
    return None if len(commands_found) <= 0 else commands_found[0]
