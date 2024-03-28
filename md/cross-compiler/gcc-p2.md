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

~~~admonish warning title="Внимание"
Если во время компиляции пакета у вас возникли ошибки, то, возможно, в вашем случае поможет перекомпиляция GCC: запустите снова скрипт `../configure` из этапа настройки со всеми указанными там опциями *кроме следующих:*

```bash
  --with-float=$LFA_FLOAT \
  --with-fpu=$LFA_FPU
```

Далее вновь выполните команду для сборки пакета (`make`).
~~~

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
