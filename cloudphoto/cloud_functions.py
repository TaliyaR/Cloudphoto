from os import listdir
from os.path import isfile, join, exists, isdir

import boto3

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)
bucket_name = 'd05.itiscl.ru'
image_type = ['.jpg', '.jpeg']


def get_albums():
    albums = []
    for album in s3.list_objects(Bucket=bucket_name, Prefix='', Delimiter='/').get('CommonPrefixes', []):
        album_name = album.get('Prefix').split('/')[0]
        albums.append(album_name)
    return albums


def get_list_of_photo_name(a):
    photos = []
    prefix = f'{a}/'
    for album in s3.list_objects(Bucket=bucket_name, Prefix=prefix).get('Contents', []):
        name = album.get('Key')
        for type in image_type:
            if name.endswith(type):
                photos.append(name[len(prefix):])
    return photos


def upload(p, a):
    if exists(p):
        if isdir(p):
            if len(listdir(p)) != 0:
                files_from_path = {f for f in listdir(p) if isfile(join(p, f))}
                for file in files_from_path:
                    for type in image_type:
                        if (file.lower()).endswith(type):
                            s3.upload_file(f'{p}/{file}', bucket_name, f'{a}/{file.lower()}')
                            print(f"Файл {file.lower()} отправлен")
            else:
                print("Заданный каталог пуст")
        else:
            print("Заданный путь не является каталогом")
    else:
        print("Заданного пути не существует")


def download(p, a):
    if exists(p):
        if isdir(p):
            if a in get_albums():
                for file in get_list_of_photo_name(a):
                    s3.download_file(bucket_name, f'{a}/{file}', f'{p}/{file}')
                    print(f"Файл {file} загружен")
            else:
                print("Заданного альбома не существует")
        else:
            print("Заданный путь не является каталогом")
    else:
        print("Заданного пути не существует")


def list_of_albums():
    albums = get_albums()
    if not albums:
        print("Список альбомов пуст")
    else:
        for album_name in get_albums():
            print(album_name)


def list_of_photo_in_album(a):
    photos = get_list_of_photo_name(a)
    if not photos:
        print("В данном альбоме нет фотографий")
    else:
        for photo_name in photos:
            print(photo_name)
