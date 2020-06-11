
import click
from tabulate import tabulate
from .core import CipherTools


@click.group()
def cli():
    """Encrypts files securely with your CLI"""
    pass


@cli.command()
def generate_key():
    """Generate a secure key for your files"""
    cipher = CipherTools()
    click.echo(
        'Your secure cipher key was generated successfully')
    print(
        tabulate([["Generated_key"], [cipher.generate_key()]], headers="firstrow"))
    click.echo(
        'Save your key in a secure place')


@cli.command()
def basic_init():
    """Generate a basic folders structure for your ciphers files"""
    click.echo(
        'Create a "files" folder for the files to be encrypted and a "cipher" folder for your processed files')
    file = CipherTools()
    file.init_paths()
    print(tabulate([["New folders", "Description"], ["files", "Your original files"],
                    ["cipher", "Procesing files"]], headers="firstrow"))


@cli.command()
@click.option('-f', '--filename',
              type=str,
              prompt=True,
              help='Filename with extension')
@click.option('-k', '--key',
              type=str,
              prompt=True,
              help='Key for cipher data')
def encrypt(filename, key):
    """Cypher a file"""
    file = CipherTools(filename)
    result = file.encrypt(key)
    if result:
        click.echo("Your file: "+filename+" has been encrypted")
    else:
        click.echo("Your key is not valid or the file does not exists")


@cli.command()
@click.option('-f', '--folder',
              type=str,
              prompt=True,
              help='Folder of your encrypted file')
@click.option('-k', '--key',
              type=str,
              prompt=True,
              help='Key for cipher data')
def decrypt(folder, key):
    """Decypher a file with a key"""
    file = CipherTools(folder)
    result = file.decrypt(key)
    if result:
        click.echo("Your file in: "+folder+" has been decrypted")
    else:
        click.echo("Your key is not valid or the file encrypted does not exists")


all = cli
