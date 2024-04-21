# Создание файлов и каталогов

## Директория базовой ОС

Создайте директорию, в которой будут находиться файлы собранной базовой ОС:

```bash
mkdir -pv $LFA_SYS
```

## Стандартные системные каталоги базовой ОС

Теперь пришло время создать некоторую структуру в целевой файловой системе базовой ОС. Создайте стандартное дерево каталогов, выполнив следующие команды:

```bash
mkdir -pv $LFA_SYS/{bin,boot,dev,etc,home}
mkdir -pv $LFA_SYS/lib/{firmware,modules}
mkdir -pv $LFA_SYS/{mnt,opt,proc,sbin,srv,sys}
mkdir -pv $LFA_SYS/var/{cache,lib,local,lock,log,opt,run,spool}
mkdir -pv $LFA_SYS/usr/{,local/}{bin,include,lib,sbin,share,src}

install -dv -m 0750 $LFA_SYS/root
install -dv -m 1777 $LFA_SYS/{var/,}tmp

if [ $LFA_TGT == "aarch64-linux-musleabihf" ]; then
    mkdir -pv $LFA_SYS/lib64
    mkdir -pv $LFA_SYS/usr/lib64
fi
```

~~~admonish tip title="Проверьте себя" collapsible=true
После исполнения данных команд в директории `$LFA_SYS` должна быть такая структура:

```
/home/lfa/lfa/baseOS
|-- bin
|-- boot
|-- dev
|-- etc
|-- home
|-- lib
|   |-- firmware
|   `-- modules
|-- mnt
|-- opt
|-- proc
|-- root
|-- sbin
|-- srv
|-- sys
|-- tmp
|-- usr
|   |-- bin
|   |-- include
|   |-- lib
|   |-- local
|   |   |-- bin
|   |   |-- include
|   |   |-- lib
|   |   |-- sbin
|   |   |-- share
|   |   `-- src
|   |-- sbin
|   |-- share
|   `-- src
`-- var
    |-- cache
    |-- lib
    |-- local
    |-- lock
    |-- log
    |-- opt
    |-- run
    |-- spool
    `-- tmp
```
~~~

## Создание ряда системных файлов

Обычно системы Linux хранят список смонтированных файловых систем в `/etc/mtab`. С учётом того, как устроена наша система, в качестве `/etc/mtab` в ней будет выступать ссылка на `/proc/mounts`:

```bash
ln -svf ../proc/mounts $LFA_SYS/etc/mtab
```

### Создание пользователей и групп

Для того, чтобы пользователь `root` мог войти в систему и чтобы имя `root` было распознано, создайте в файлах `/etc/passwd` и `/etc/group` соответствующие записи:

```bash
cat > $LFA_SYS/etc/passwd << "EOF"
root::0:0:root:/root:/bin/ash
EOF
```

> **Вы можете захотеть создать следующих пользователей:**
>
> `bin:x:1:1:bin:/bin:/bin/false` — может быть полезен для совместимости с устаревшими приложениями;
>
> `daemon:x:2:6:daemon:/sbin:/bin/false` — часто рекомендуется использовать непривилегированного пользователя для запуска демонов, чтобы ограничить их доступ к системе;
>
> `adm:x:3:16:adm:/var/adm:/bin/false` — используется программами, которые выполняют административные задачи;
>
> `lp:x:10:9:lp:/var/spool/lp:/bin/false` — используется в программах для печати;
>
> `mail:x:30:30:mail:/var/mail:/bin/false` — используется для почтовых программ;
>
> `news:x:31:31:news:/var/spool/news:/bin/false` — используется в программах для получения новостей;
>
> `uucp:x:32:32:uucp:/var/spool/uucp:/bin/false` — часто используется для копирования файлов Unix-to-Unix с одного сервера на другой;
>
> `operator:x:50:0:operator:/root:/bin/ash` — может быть использоан для предоставления операторам доступа к системе;
>
> `postmaster:x:51:30:postmaster:/var/spool/mail:/bin/false` —  обычно используется как учетная запись, которая получает всю информацию о проблемах с почтовым сервером;
>
> `nobody:x:65534:65534:nobody:/:/bin/false` — используется в NFS.

Создайте файл, в котором будут указаны группы пользователей:

```bash
cat > $LFA_SYS/etc/group << "EOF"
root:x:0:
bin:x:1:
sys:x:2:
kmem:x:3:
tty:x:4:
tape:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
usb:x:14:
cdrom:x:15:
EOF
```

> **Вы можете захотеть создать следующие группы:**
>
> - `adm:x:16:root,adm,daemon`
> - `console:x:17` — пользователи этой группы имеют доступ к консоли
> - `mail:x:30:mail`
> - `news:x:31:news`
> - `uucp:x:32:uucp`
> - `users:x:100:` — используется в программе `shadow` по умолчанию для новых пользователей
> - `nogroup:x:65533` — используется некоторыми программами, которым **специально** не требуется группа
> - `nobody:x:65534`

### Логи

Программы `login`, `agetty` и `init` используют файл `lastlog` для записи информации о том, кто и когда вошёл в систему. Однако они не будут ничего туда записывать, если этого файла нет. Создайте файл `lastlog` и дайте ему соответствующие разрешения:

```bash
touch $LFA_SYS/var/log/lastlog
chmod -v 664 $LFA_SYS/var/log/lastlog
```
