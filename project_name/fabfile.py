# -*- coding: utf-8 -*-
from fabric.api import task
from fabric.api import run
from fabric.api import local
from fabric.api import env
from fabric.api import cd
from fabric.api import prefix
from fabric.api import hide

# Расположение зависимостей для проекта
REQUIREMENTS_NAME = 'reqs.txt'

# Расположение внешнего репозитория для верстки, если отсуствует в False
MARKUP_DIRECTORY = False

ENVIRONMENT = {
    # Окружение тестового сервера
    'staging': {
        # Хосты на которых расположен проект.
        'host': [],
        # Папка в котором располагается проект
        'branch': '',
        # Ветка по умолчанию для
        'root_dir': '',
        # Путь до virtualenv директории на серверах
        'venv': '',
    },
    # Окружение рабочего сервера
    'production': {
        'user': '',
        # Хосты на которых расположен проект.
        'host': [], # django@127.0.0.1
        # Папка в котором располагается проект
        'branch': 'master',
        # Ветка по умолчанию для
        'root_dir': '',
        # Путь до virtualenv директории на серверах
        'venv': '', # source /home/.venv/bin/activate
    },
}


def active_env(name):
    """
    Подготовка окружения
    """
    local_env = ENVIRONMENT.get(name, None)
    if not local_env:
        raise RuntimeError("Не найдено окружение")

    # env.user = local_env['user']
    env.hosts = local_env['host']
    env.root = local_env['root_dir']
    env.branch = local_env['branch']
    env.activate = local_env['venv']


@task
def staging():
    """
    Подготовка окружения тестового сервера
    """
    active_env('staging')


@task
def production():
    """
    Подготовка окружения рабочего сервера
    """
    active_env('production')


@task
def update(branch=None):
    """
    Обновление исходного кода из ветки

    Аргументы:
        - :branch: Ветка из которой берутся изменения, по умолчанию текущий для окружения
    """

    if branch is None:
        branch = env.branch

    # Отправляем локальные изменения в приложении на сервер
    local("git push origin " + branch)

    # Отправляем локальные изменения в верстке на сервер
    if MARKUP_DIRECTORY:
        with cd(MARKUP_DIRECTORY):
            local("git push origin master")

    with cd(env.root):
        # Обновляем бранчи если надо
        if branch != env.branch:
            run('git fetch --all')
            run('git checkout ' + branch)

        # Перемещаем изменения из репозитория в локальную папку
        run('git pull origin ' + branch)

        # Обновляем исходный код для статических файлов
        run('git submodule update --init')

        if MARKUP_DIRECTORY:
            with cd(MARKUP_DIRECTORY):
                run('git pull origin master')


@task
def install(branch=None):
    """
    Установка зависимостей

    Аргументы:
        - :branch: Ветка из которой берутся изменения, по умолчанию текущий для окружения
    """
    with cd(env.root):
        # Обновляем зависимости для проекта
        with prefix(env.activate):
            run('pip install -r ' + REQUIREMENTS_NAME)


@task
def migrate():
    """
    Миграция изменений схемы в БД
    """
    with cd(env.root):
        with prefix(env.activate):
            # Обновления БД в соответствии с джанго
            run('python manage.py syncdb')

            # Мигрируем изменения в БД
            run('python manage.py migrate')


@task
def collect():
    """
    Сборка и обновление статических файлов проекта
    """
    # Собираем статические файлы
    with cd(env.root):
        with prefix(env.activate):
            run('python manage.py collectstatic --noinput')


@task
def restart():
    """
    Перезапуск приложения
    """
    with cd(env.root):
        with prefix(env.activate):
            # Перезапуск приложения Django
            run('sudo supervisorctl restart project_name:* ')


@task
def flush_cache():
    """
    Сбросить кэш Reddis'а
    """
    run("echo 'FLUSHALL' | redis-cli")


@task
def deploy(branch=None, flush=False):
    """
    Выполнить полное развертывание приложения на сервере

    Аргументы:
        - :branch: Ветка из которой берутся изменения, по умолчанию текущий для окружения
        - :flush:  Сбросить кэш Reddis'а
    """
    update(branch)
    install()
    migrate()
    collect()
    restart()
    if flush:
        flush_cache()


@task(default=True)
def help():
    """
    Выводит эту справку
    """

    print """
Основные команды:

    fab --list                  список всех команд
    fab -d <команда>            информация о команде
    fab staging <команда>       выполнение команды на тестовом сервере
    fab production <команда>    выполнение команды на рабочем сервере

Обновить полностью тестовый сервер без сброса кэша:

    fab staging deploy:production

Обновить полностью тестовый сервер со сбросом кэша:

    fab staging deploy:production,flush:1

    """

    with hide('status', 'aborts', 'warnings', 'running', 'stderr', 'user'):
        local("fab --list")

    import fabric.state
    fabric.state.output.status = False
