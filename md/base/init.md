# lfa_init

{{#include pkgs/lfa_init.md}}

## Сборка пакета

```bash
cargo build --release
```

## Установка пакета

Скопируйте скомпилированные файлы в директорию `/sbin`:

```bash
cp -v ./target/release/{init,service,poweroff,reboot} $LFA_SYS/sbin
```

Далее вам нужно создать директорию с конфигурационными файлами и сервисами системы инициализации. Рекомендуем вам использовать стандартные конфиги и сервисы, которые находятся в директории `./data/`.

Для того, чтобы установить конфигурационные файлы и сервисы в систему, выполните:

```bash
mkdir -pv $LFA_SYS/etc/init.d
cp -rv ./data/* $LFA_SYS/etc/init.d
```

> Подробную информацию о работе lfa_init см. в [3-й части статьи о строении ОС Linux](../additional/os-structure3.md).

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные программы:** `init`, `poweroff`, `reboot`, `service`
- **Установленные директории:** `/etc/init.d`

### Описание компонентов

- **Программы:**
  - `init` - программа, запускающаяся с **`PID`** = `1` и стартующая остальные компоненты LFA.
  - `poweroff` - завершает работу системы.
  - `reboot` - перезагружает системы.
  - `service` - программа для запуска, остановки или перезагрузки сервисов.
- **Директории:**
  - `/etc/init.d` - содержит конфигурационные файлы системы инициализации и сервисы для загрузки.
~~~
