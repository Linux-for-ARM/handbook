# Allwinner

```admonish warning title="Внимание"
В данной части предоставлены *общие* инструкции, которые приведут к сборке работающего загрузчика U-Boot, пригодного для дальнейшего использования. Конечно, «кастомная» сборка U-Boot и ряда дополнительных компонентов с другими параметрами допускается, но на данный момент я не предоставляю иных инструкций кроме этих. Возможно, что в будущем я добавлю ряд советов по изменению параметров сборки, но сейчас у меня на это нет ни времени, ни сил, ни желания.
```

<!--
---

## Установка U-Boot

```admonish bug title="Under construction!"
Инструкции ниже я перепечатал из [**документации**](https://docs.u-boot.org/en/latest/board/allwinner/sunxi.html#installing-u-boot) загрузчика и не уверен, что они применимы в нашем случае. Если вы знаете, как правильно устанавливать загрузчик ОС на определённый носитель информации, с которого будет происходить загрузки собранной системы LFA (MicroSD или eMMC), то, пожалуйста, свяжитесь со мной одним из следующих способов:

- [Создайте issue в репозитории руководства](https://github.com/Linux-for-ARM/handbook/issues/new), где опишете шаги по сборке и установке загрузчика;
- [Напишите мне в личку в Telegram](https://t.me/brezhnev_zhiv)
- [Напишите в Telegram-чат руководства](https://t.me/lfa_chat)

Меня интересует следующее: в `img`-образах существующих дистрибутивов (Debian, Ubuntu, Manjaro ARM, Armbian) уже существуют какие-то файлы загрузчика (если я правильно понимаю). Но я не понимаю того, как скомпилированный образ U-Boot (`u-boot-sunxi-with-spl.bin`) "засунуть" в `img`-образ системы, чтобы после его записи на SD-карту или eMMC с помощью `dd` я мог бы загрузить свою систему.

На всякий случай: меня в первую очередь интересует сборка U-Boot для Orange Pi (например, для Orange Pi 3 LTS), поскольку сейчас я располагаю именно этим компьютером.
```

### Установка на MicroSD-карту

Все SoC Allwinner пытаются найти загрузочный образ в 16 секторе (8 КБ) карты, подключенной к первому MMC-контроллеру. Чтобы перенести скомпилированный ранее образ на SD-карту с любого устройства (как с того, на котором выполнялась сборка, так и с сам*о*й платы), оснащённого устройством чтения MicroSD-карт, введите от имени пользователя `root`:

```bash
dd if=boot-sunxi-with-spl.bin of=/dev/sdX bs=1k seek=8
```

где `X` — буква (`a`, `b`, `c`) устройства, например, `/dev/sdc`. Обратите внимание на то, что в некоторых случаях вместо `sdX` имя устройства может быть `mmcblkX`.

Новые SoC (начиная с 2014 г. и включая все ARM64 SoC) также ищут подпись в секторе 256 (128 КБ). Преимущество установки туда загрузчика в том, что он не пересекается с таблицей разделов GPT. Просто замените `seek=8` на `seek=128`.

---
-->

> **Смотрите также:**
>
> - [**Страница U-Boot на linux-sunxi WiKi**](https://linux-sunxi.org/U-Boot) (<https://linux-sunxi.org/>)
