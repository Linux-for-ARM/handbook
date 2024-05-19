# Скачивание пакетов

Перейдите в директорию `src/`, которую вы создали ранее:

```bash
cd src/
```

Скачайте файлы `wget-list` и `md5sums`, которые будут использованы для скачивания исходного кода компонентов системы:

```bash
wget https://raw.githubusercontent.com/Linux-for-ARM/handbook/v1.0/wget-list
wget https://raw.githubusercontent.com/Linux-for-ARM/handbook/v1.0/md5sums
```

И скачайте системные компоненты:

```bash
wget --input-file=wget-list --continue
```

Для проверки корректности скачивания пакетов вам нужно воспользоваться файлом `md5sums`:

```bash
md5sum -c md5sums
```
