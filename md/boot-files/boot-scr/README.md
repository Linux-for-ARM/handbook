# Создание boot.scr

```admonish warning title="Внимание"
Это заготовка страницы. Здесь приведены общие инструкции, тестирование которых не производилось. Окончательная версия страницы войдёт во вторую версию руководства LFA.
```

В данном пункте приведены сведения о создании файла `boot.scr` для эмулятора QEMU и для реального оборудования. `boot.scr` — это загрузочный скрипт системы, предназначенный для U-Boot. Впоследствии мы скомпилируем его в `boot.cmd`, который и будет читать и исполнять загрузчик.

---

> **Смотрите также:**
>
> - [**How to boot Linux kernel from u-boot?**](https://stackoverflow.com/questions/30488942/how-to-boot-linux-kernel-from-u-boot) (<https://stackoverflow.com>)
> - [**How U-boot loads Linux kernel**](https://krinkinmu.github.io/2023/08/21/how-u-boot-loads-linux-kernel.html) (<https://krinkinmu.github.io>)
> - [**U-boot boot script**](https://krinkinmu.github.io/2023/11/19/u-boot-boot-script.html) (<https://krinkinmu.github.io>)
