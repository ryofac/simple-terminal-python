import os
from abc import ABC, abstractmethod

from exceptions import InterruptionException


class Command(ABC):
    def __init__(self, name, description, usage=None):
        self._name = name
        self._description = description
        self._usage = usage

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def usage(self):
        return self._usage

    @abstractmethod
    def execute(self, args):
        pass

    def print_description(self):
        print("\n" + self.description)

        if self.usage:
            print("uso: " + self.usage)

        print()


class ClearCommand(Command):
    name = "clear"
    description = "usado para limpar o terminal"
    usage = "clear"

    def __init__(self):
        super().__init__(self.name, self.description)

    def execute(self, args):
        os.system("cls" if os.name == "nt" else "clear")


class ExitCommand(Command):
    name = "exit"
    description = "usado para sair do terminal"
    usage = "exit"

    def __init__(self):
        super().__init__(self.name, self.description)

    def execute(self, args):
        raise InterruptionException


class ManualCommand(Command):
    name = "manual"
    description = "exibe ajuda e mostra os comandos disponíveis"
    usage = "manual, manual <NOME_DO_COMANDO>"

    def __init__(self):
        super().__init__(self.name, self.description)

    def execute(self, args):
        from commands_repo import avaliable_commands, search_command_by_name

        if len(args) <= 0:  # Chamado sem argumentos
            self.print_description()
            print("\nComandos disponíveis: ")
            for command in avaliable_commands:
                # Pega os 40 primeiros caracteres
                shortDescription: str = command.description[:41] + "..."
                print(f"* {command.name} - {shortDescription}")
            print("\n")
            return

        elif len(args) == 1:  # Chamado com exatamente um argumento
            command_name = args[0]
            command: Command = search_command_by_name(command_name)
            if command:
                command.print_description()
            else:
                print(f"Comando {command_name} não encontrado")

        else:
            raise SyntaxError


class PrintCommand(Command):
    name = "print"
    description = "retorna os valores dados como string"
    usage = "print <VALOR>"

    def __init__(self):
        super().__init__(self.name, self.description)

    def execute(self, args):
        if not args or len(args) == 0:
            self.print_description()
            return

        print(str.join(" ", args))
