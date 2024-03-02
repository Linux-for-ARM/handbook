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
```

## Создание ряда системных файлов

Обычно системы Linux хранят список смонтированных файловых систем в `/etc/mtab`. С учётом того, как устроена наша система, в качестве `/etc/mtab` в ней будет выступать ссылка на `/proc/mounts`:

```bash
ln -svf ../proc/mounts $LFA_SYS/etc/mtab
```

Для того, чтобы пользователь `root` мог войти в систему и чтобы имя `root` было распознано, создайте в файлах `/etc/passwd` и `/etc/group` соответствующие записи:

```bash
cat > $LFA_SYS/etc/passwd << "EOF"
root::0:0:root:/root:/bin/ash
EOF

cat > $LFA_SYS/etc/group << "EOF"
root:x:0:
EOF
```

Программы `login`, `agetty` и `init` используют файл `lastlog` для записи информации о том, кто и когда вошёл в систему. Однако они не будут ничего туда записывать, если этого файла нет. Создайте файл `lastlog` и дайте ему соответствующие разрешения:

```bash
touch $LFA_SYS/var/log/lastlog
chmod -v 664 $LFA_SYS/var/log/lastlog
```
