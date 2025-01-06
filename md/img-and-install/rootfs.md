Смонтируйте полученный образ и скопируйте в неё файлы нашей системы (саму систему, ядро, Devicetree и сценарий загрузки):

```bash
mkdir -pv /tmp/lfa_rootfs
sudo mount -v rootfs.img /tmp/lfa_rootfs

sudo cp -rfv $LFA_SYS/* /tmp/lfa_rootfs
sync
```

> Все действия здесь выполняются от имени пользователя `lfa`. Поскольку здесь используется программа `sudo`, вам нужно добавить пользователя `lfa` в группу `wheel` или `sudo`.

После копирования файлов размонтируйте образ:

```bash
sudo umount /tmp/lfa_rootfs
```
