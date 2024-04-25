# Создание основных каталогов

Создайте каталог, в котором будет содержаться файлы кросс-компилятора. Для того, чтобы постоянно не указывать путь до него при сборке пакетов, объявите новую переменную окружения `$LFA_CROSS`:

```bash
export LFA_CROSS=$LFA/tools/$LFA_TGT

mkdir -pv $LFA_CROSS
ln -svf . $LFA_CROSS/usr

echo "export LFA_CROSS=\$LFA/tools/\$LFA_TGT" >> ~/.bashrc
```

Кроме того, вам необходимо создать директорию, где будет храниться исходный код компонентов:

```bash
mkdir -v src
```

~~~admonish tip title="Проверьте себя" collapsible=true
В итоге в домашней папке пользователя `lfa` будет примерно такая структура файлов:

```
/home/lfa
|-- lfa/
|   `-- tools/
|       `-- aarch64-linux-musleabihf/
|           `-- usr/ -> .
`-- src/
```

И содержимое файла `~/.bashrc` после всех записей в него (в зависимости от выбранной вами архитектуры его содержимое может незначительно меняться):

```bash
set +h
umask 022
unset CFLAGS
LFA=$HOME/lfa
LC_ALL=C
PATH=$LFA/tools/bin:/bin:/usr/bin
export LFA LC_ALL PATH
export LFA_HOST="x86_64-cross-linux-gnu"
export LFA_TGT="aarch64-linux-musleabihf"
export LFA_ARCH="armv8-a"
export LFA_CROSS=$LFA/tools/$LFA_TGT
```
~~~
