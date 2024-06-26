# Принятые обозначения

В руководстве используются следующие обозначения:

```bash
./configure --prefix=/usr --target=$LFA_TGT
```

Этот текст необходимо набрать в терминале в точности так, как указано, если иное не сказано в тексте.

Иногда строка разделяется до двух или более с использованием символа `\`:

```bash
ARCH=arm ./configure --prefix=/usr \
    --target=$LFA_TGT \
    --with-sysroot=$LFA_SYS \
    --disable-nls \
    --disable-threads
```

*Обратите внимание на то, что после `\` должен быть переход на новую строку (<kbd>Enter</kbd>). Другие символы приведут к некорректному результату и ошибкам.*

```
2024-02-27 18:58:13 [INFO] (mdbook::cmd::serve): Files changed: ["/home/admin/Work/lfa/src/typography.md"]
2024-02-27 18:58:13 [INFO] (mdbook::cmd::serve): Building book...
2024-02-27 18:58:13 [INFO] (mdbook::book): Book building has started
2024-02-27 18:58:13 [INFO] (mdbook::book): Running the html backend
```

Этот текст используется для отображения вывода в терминале.

*Используется, чтобы подчеркнуть важную информацию, на которую следует обратить внимание.*

[Используется для ссылок на страницы руководства.](typography.md)

[**Используется для ссылок на внешние ресурсы**](https://linux-for-arm.github.io/donate.html).

```admonish warning title="Важно"
Используется для указания на критически важную информацию. На неё следует обратить особое внимание.
```

> Используется для указания на информацию рекомендательного характера. Не рекомендуется пропускать эти указания и внимательно с ними ознакомиться.
