import click
import signup


@click.group()
def main():
    pass

main.add_command(signup.main,"signup")

if __name__ == "__main__":
    main()

