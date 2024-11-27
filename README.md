# Linux for ARM

Linux for ARM (LFA) - руководство по сборке из исходного кода системы, использующей ядро Linux, для компьютеров на архитектуре ARM. Данное руководство использует наработки проекта [CLFS](https://www.clfs.org), а также ряд других источников, полный список которых приведён в списке литературы в самом руководстве.

## Мотивация

- Есть руководство [CLFS Embedded](http://clfs.org/view/clfs-embedded/arm/), но оно устарело.
- Для ARM-девайсов существуют дистрибутивы GNU/Linux, но далеко не все из них могут считаться пригодными к использованию.
- Отсутствие подобных русскоязычных руководств. Существуют разве что русские переводы LFS и [LX4U](https://lx4u.ru), но они не описывают процесс сборки системы для ARM-процессоров.
- Желание систематизировать сведения об ARM-девайсах в одном руководстве.
- Желание спровоцировать развитие дистрибутивов для ARM-девайсов. Для тех же Repka Pi, которые появились пару лет назад.

## Локальная сборка

### Требования

- `rustc` для сборки и установки программы `mdbook`;

### Установка зависимостей

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
export PATH=$PATH:$HOME/.cargo/bin

cargo install mdbook mdbook-pdf mdbook-admonish mdbook-variables
```

### Сборка руководства

```bash
mdbook build # генерирует также PDF-версию руководства
mdbook serve --open
```

<details>
  <summary><b>Донат</b></summary>
  <p>Вы можете отблагодарить автора за проделанную работу:</p>
  <blockquote><a href="https://boosty.to/linux-for-arm/donate">https://boosty.to/linux-for-arm</a></blockquote>
</details>
