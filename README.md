# Cypher (CLI)<!-- omit in toc -->

> Cipher your files make simple

<div align="center">
  <img src="img/cipher.png">
</div>

## Content<!-- omit in toc -->
- [Features](#features)
- [How to run](#how-to-run)
- [Quick guide](#quick-guide)
  - [Create a basic structure for cipher and decipher](#create-a-basic-structure-for-cipher-and-decipher)
  - [Generate a secure key](#generate-a-secure-key)
  - [Cipher a file](#cipher-a-file)
  - [Decipher a file](#decipher-a-file)
- [How to contribute](#how-to-contribute)

## Features
* Command line interface
* Generate secure keys on base64
* Cipher files
* Decipher files

## How to run

* Create enviroment

`python -m venv env`

* Activate enviroment

`cd env/Scripts`
`activate`

* Install requirements

`pip install pycryptodome`

* Execute interface

`python cipher.py`

<div align="center">
  <img src="img/1.png">
</div>

## Quick guide

Only type a simple commands for start

> For this guide I use a simple file .txt with a "hello world" message

### Create a basic structure for cipher and decipher

`python cipher.py basic-init`

<div align="center">
  <img src="img/2.png">
</div>

When the command is run, two new folders have been created, the original files must be placed in the "files" folder

<div align="center">
  <img src="img/3.png">
</div>

### Generate a secure key

You need a secure key make on base64 for cipher and decipher your files, type next command:

<div align="center">
  <img src="img/4.png">
</div>

Save the key on your password manager or on other secure place

Move your file to "files" folder

<div align="center">
  <img src="img/5.png">
</div>


### Cipher a file

Type this:
Type your filename and your key generated
`python cipher.py encrypt`

<div align="center">
  <img src="img/6.png">
</div>

The file generated is

<div align="center">
  <img src="img/7.png">
</div>

### Decipher a file

Make sure you have a folder with an encrypt.txt file

Type this
``python cipher.py decrypt``

<div align="center">
  <img src="img/9.png">
</div>

Your file

<div align="center">
  <img src="img/10.png">
</div>

# How to contribute
Send me a pull request or contact me as eocode in social media

# License
GPL 3