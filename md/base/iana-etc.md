# iana-etc

{{#include pkgs/iana-etc.md}}

## Установка

Скопируйте файлы `services` и `protocols` в `$LFA_SYS/etc`:

```bash
cp -v services protocols $LFA_SYS/etc
```

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные файлы:** `/etc/protocols` и `/etc/services`

### Описание компонентов

- `/etc/protocols` - описывает различные интернет-протоколы DARPA, которые доступны из подсистемы TCP/IP.
- `/etc/services` - обеспечивает сопоставление между дружественными текстовыми именами интернет-сервисов и соответствующими им номерами портов и типами протоколов.
~~~
