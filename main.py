from commands_repo import avaliable_commands
from exceptions import InterruptionException, NoContentException


def parse(raw_text: str):
    values = raw_text.split()

    if len(values) <= 0:
        raise NoContentException

    command_text = values[0]

    for command in avaliable_commands:
        if command.name == command_text:
            args = values[1:]
            command.execute(args)
            return

    # Se não achou nenhum comando disponível levanta
    # um syntax error do python mesmo, por enquanto
    raise SyntaxError


def main():
    print(
        "Terminal de brinquedo, tente digitar 'manual' para ver os comandos disponíveis"
    )
    while True:
        try:
            raw_input = input("> ")
            parse(raw_input)

        except KeyboardInterrupt:
            raise InterruptionException

        except SyntaxError:
            print(f"Erro de sintaxe: {raw_input} não é valido")

        except NoContentException:
            pass

        except InterruptionException:
            print("Até mais!")
            break


main()
