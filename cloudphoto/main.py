import click

import cloudphoto.cloud_functions as cf


@click.group()
def main():
    print('=============================================================================================')
    print('Приложение CloudPhoto для отправки фотографий в облачное хранилище и загрузки их на компьютер')
    print('=============================================================================================')


# Отправка фотографий в облачное хранилище
@click.command()
@click.option('-p', help='путь к каталогу для отправки в облачное хранилище')
@click.option('-a', help='название альбома')
def upload(p, a):
    if (p is None) & (a is None):
        click.echo('Необходимо указать путь к каталогу(-p) и название альбома(-a)')
    else:
        cf.upload(p, a)


# Загрузка фотографий на компьютер
@click.command()
@click.option('-p', help='путь к каталогу для загрузки из облачного хранилища')
@click.option('-a', help='название альбома')
def download(p, a):
    if (p is None) & (a is None):
        click.echo('Необходимо указать путь к каталогу(-p) и название альбома(-a)')
    else:
        cf.download(p, a)


# Просмотр списка альбомов
# Просмотр списка фотографий в альбоме -a
@click.command()
@click.option('-a', help='название альбома')
def list(a):
    if a is None:
        cf.list_of_albums()
    else:
        cf.list_of_photo_in_album(a)


main.add_command(list)
main.add_command(download)
main.add_command(upload)

if __name__ == '__main__':
    main()
