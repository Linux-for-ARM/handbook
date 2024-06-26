# busybox

{{#include pkgs/busybox.md}}

## Настройка

> Процесс настройки пакета `busybox` схож с процессом настройки ядра Linux. Параметры сборки записываются в файл `.config`. Можно сконфигурировать сборку в псевдографическом режиме (`make menuconfig`), а можно использовать стандартный конфиг (`make defconfig`). Вы можете сохранить файл `.config` для того, чтобы в будущем (в случае пересборки этой версии BusyBox или в случае сборки новой версии этого пакета) не конфигурировать пакет вновь.

Убедитесь, что дерево исходного кода BusyBox чистое и не содержит лишних файлов:

```bash
make mrproper
```

> Далее требуется настроить пакет BusyBox, выбрав те опции, которые вам нужны, и убрать то, что вам не требуется. В зависимости от числа выбранных опций зависит в том числе и размер вашей системы, однако BusyBox — вещь довольно минималистичная, и на размер системы влияет больше ядро Linux, его модули и файлы [Device Tree](../additional/dtb.md).

```bash
make ARCH=arm64 menuconfig
```

### Процесс настройки

В разделах `Archival Utilities`, `Coreutils`, `Console Utilities`, `Debian Utilities`, `klibc-utils`, `Editors` и т.д. выберите сборку программ и утилит в зависимости от того, в каких сценариях должна использоваться ваша система LFA, а также в зависимости от её конечного размера. Конечно, на её размер куда больше будут влиять ядро и файлы, необходимые для загрузки системы, но инструкции по уменьшению размера, к примеру, ядра Linux, ищите сами на просторах интернета.

### Система инициализации

Поскольку чуть позже мы установим в LFA загрузочные скрипты, нам требуется система инициализации, которая эти скрипты будет исполнять. Для этого компилируйте BusyBox с поддержкой `init`, `halt`, `poweroff`, `reboot`. Кроме того, вам нужны программы `getty` и `login`.

```
Init Utilities  --->
  <*> halt      [CONFIG_HALT]
  <*> poweroff  [CONFIG_POWEROFF]
  <*> reboot    [CONFIG_REBOOT]
  <*> init      [CONFIG_INIT]
Login/Password Management Utilities  --->
  <*> getty     [CONFIG_GETTY]
  <*> login     [CONFIG_LOGIN]
```

### mdev

В данном руководстве рекомендуется использовать `mdev` для динамического управления устройствами в директории `/dev`. Включите следующие опции:

```
Linux System Utilities  --->
  <*> mdev                          [CONFIG_MDEV]
    <*> Support /etc/mdev.conf      [CONFIG_FEATURE_MDEV_CONF]
    <*> Support loading of firmware [CONFIG_FEATURE_MDEV_LOAD_FIRMWARE]
    <*> Support daemon mode         [CONFIG_FEATURE_MDEV_DAEMON]
```

### Отключение опций

После конфигурирования вам нужно отлючить ряд возможностей, с которыми мы не смогли бы корректно собрать этот пакет.

Во-первых, отключите сборку `ifplugd` и `inetd`, поскольку их сборка вместе с `musl` имеет проблемы:

```bash
sed -i 's/\(CONFIG_\)\(.*\)\(INETD\)\(.*\)=y/# \1\2\3\4 is not set/g' .config
sed -i 's/\(CONFIG_IFPLUGD\)=y/# \1 is not set/' .config
```

Отключите использование `utmp`/`wtmp`, поскольку `musl` их не поддерживает:

```bash
sed -i 's/\(CONFIG_FEATURE_WTMP\)=y/# \1 is not set/' .config
sed -i 's/\(CONFIG_FEATURE_UTMP\)=y/# \1 is not set/' .config
```

Отключите использование `ipsvd` для TCP и UDP, поскольку у него есть проблемы сборки вместе с `musl` (аналогично `inetd`):

```bash
sed -i 's/\(CONFIG_UDPSVD\)=y/# \1 is not set/' .config
sed -i 's/\(CONFIG_TCPSVD\)=y/# \1 is not set/' .config
```

Сборка компонента `tc` на ядрах Linux >= 6.8 вызывает ошибку. Отключите сборку `tc` если он вам не нужен:

```bash
sed -i 's/\(CONFIG_TC\)=y/# \1 is not set/' .config
```

~~~admonish tip title="Если вам нужен `tc`" collapsible=true
- Примените [**патч**](https://gitweb.gentoo.org/repo/gentoo.git/tree/sys-apps/busybox/files/busybox-1.36.1-kernel-6.8.patch?id=d8ad860a1ed9aa92adaa7dcf1c3fc78d0e2f80ce);
- [**Обсуждение на** *lists.busybox.net*](http://lists.busybox.net/pipermail/busybox-cvs/2024-January/041752.html);
~~~

Сборка BusyBox с поддержкой PAM (Pluggable Authentication Modules) не требуется, поскольку PAM'a в LFA нет. Убедитесь, что собираете BusyBox без PAM:

```bash
sed -i 's/\(CONFIG_PAM\)=y/# \1 is not set/' .config
```

Обычно в системах подобных LFA не требуются пакетные менеджеры типа того же `dpkg`. К тому же, в BusyBox предоставляется достаточно «обрезанная» версия dpkg с некоторыми ограничениями. Да и подобных LFS руководствах (в том числе и в LFA) не рекомендуется использовать подобные пакетные менеджеры во избежание проблем и поломок системы. Если вам не нужен `dpkg`, отключите его сборку, чем освободите около 73 Кб памяти:

```bash
sed -i 's/\(CONFIG_DPKG\)=y/# \1 is not set/' .config
sed -i 's/\(CONFIG_DPKG_DEB\)=y/# \1 is not set/' .config
```

Тоже самое сделайте и с версией пакетного менеджера `rpm`:

```bash
sed -i 's/\(CONFIG_RPM\)=y/# \1 is not set/' .config
sed -i 's/\(CONFIG_RPM2CPIO\)=y/# \1 is not set/' .config
```

## Сборка

```bash
make ARCH=arm64 CROSS_COMPILE=$LFA_TGT-
```

## Установка

Установите пакет:

```bash
make ARCH=arm64 CROSS_COMPILE=$LFA_TGT- \
  CONFIG_PREFIX=$LFA_SYS install
```

> Заметьте, что BusyBox содержит множество программ, но все они объединены в один файл. Однако для удобства (чтобы, например, вводить не `busybox mv file1 file2`, а просто `mv file1 file2` как в обычных системах) в каталогах `$LFA_SYS/bin` и `$LFA_SYS/sbin` создаются ссылки на `busybox` с именами программ, которые содержит этот пакет.

Если вы собираетесь собирать ядро с помощью модулей, вам нужно убедиться, что `depmod.pl` доступен для выполнения на вашем хосте:

```bash
cp -v examples/depmod.pl $LFA/tools/bin
chmod -v 755 $LFA/tools/bin/depmod.pl
```

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные программы:** `[`, `[[`, `arch`, `ascii`, `ash`, `awk`, `base32`, `base64`, `basename`, `bc`, `bunzip2`, `busybox` и другие[^1]

### Описание компонентов

- **Программы:**
  - `busybox` — реализация стандартных UNIX утилит.
  - все остальные — ссылки на `busybox`.

---

[^1]: Набор установленного ПО зависит от того, какие настройки вы указывали при конфигурировании пакета.
~~~
