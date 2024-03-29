# gcc (проход 2)

{{#include pkgs/gcc-p2.md}}

```admonish warning title="Внимание"
Сейчас мы собираем полноценную версию компилятора GCC для сборки остальной системы, используя уже готовую стандартную библиотеку С.
```

## Подготовка

```bash
tar -xf ../mpfr-*.tar.xz
tar -xf ../mpc-*.tar.gz
tar -xf ../gmp-*.tar.bz2

mv -v mpfr-* mpfr
mv -v mpc-* mpc
mv -v gmp-* gmp
```

## Настройка

~~~admonish warning title="Внимание"
Если вы собираете систему для AArch64, то **не используйте** переменные окружения `$LFA_FLOAT` и `$LFA_FPU`, а также пропускайте при вводе команд строки, содержащие эти переменные окружения. Например, если вы собираете систему для AArch64, то скрипту `configure` не следует передавать эти аргументы:

```bash
  --with-float=$LFA_FLOAT \
  --with-fpu=$LFA_FPU
```
~~~

```bash
mkdir -v build
cd build

../configure --prefix=$LFA/tools \
  --build=$LFA_HOST \
  --host=$LFA_HOST \
  --target=$LFA_TGT \
  --with-sysroot=$LFA_CROSS \
  --disable-nls \
  --enable-languages=c \
  --enable-c99 \
  --enable-long-long \
  --disable-libmudflap \
  --disable-multilib \
  --with-arch=$LFA_ARCH \
  --with-float=$LFA_FLOAT \
  --with-fpu=$LFA_FPU
```

## Сборка

```bash
make
```

## Установка

```bash
make install
```

~~~admonish note title="Содержимое пакета" collapsible=true
- **Установленные программы:** `gcc`, `gcov`
- **Установленные библиотеки:** `libgcc.a`, `libgcc_eh.a`, `libgcc_s.so`

### Описание компонентов

- **Программы:**
  - `gcc` - компилятор языка C.
  - `gcov` - инструмент для тестирования покрытия, используется для анализа программ, чтобы определить, где оптимизация даст наибольший эффект.
~~~
