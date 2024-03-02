# gcc (проход 1)

{{#include pkgs/gcc-p1.md}}

> Сейчас нам нужно собрать GCC со статической библиотекой `libgcc` и без поддержки многопоточности.

## Подготовка

GCC требует, чтобы пакеты GMP, MPFR и MPC либо присутствовали на хосте, либо представлены в виде исходных текстов в дереве исходного кода GCC. Распакуйте их:

```bash
tar -xf ../mpfr-*.tar.bz2
tar -xf ../mpc-*.tar.gz
tar -xf ../gmp-*.tar.xz

mv -v mpfr-* mpfr
mv -v mpc-* mpc
mv -v gmp-* gmp
```

## Настройка

Сборка пакета `gcc` должна происходить в отдельном каталоге. Создайте его:

```bash
mkdir -v build
cd build
```

Запустите скрипт `configure`:

```bash
../configure --prefix=$LFA/tools \
  --build=$LFA_HOST \
  --host=$LFA_HOST \
  --target=$LFA_TGT \
  --with-sysroot=$LFA_CROSS \
  --disable-nls \
  --disable-shared \
  --without-headers \
  --with-newlib \
  --disable-decimal-float \
  --disable-libgomp \
  --disable-libmudflap \
  --disable-libssp \
  --disable-libatomic \
  --disable-libquadmath \
  --disable-threads \
  --enable-languages=c \
  --disable-multilib \
  --with-arch=$LFA_ARCH \
  --with-float=$LFA_FLOAT \
  --with-fpu=$LFA_FPU
```

> **Значения новых параметров:**
>
> `--host=$LFA_HOST` - указывает `configure` триплет машины, на которой будет выполняться GCC при кросс-компиляции. `$LFA_HOST` содержит название архитектуры хоста, на которой будем производить кросс-компиляцию для архитектуры `$LFA_TGT`.
>
> `--disable-shared` - этот переключатель заставляет GCC связывать свои внутренние библиотеки статически.
>
> `--without-headers` - указывает `configure` не использовать никаких заголовков из библиотек С. Это необходимо, поскольку мы ещё не собрали библиотеку С и чтобы предотвратить влияние окружения хоста.
>
> `--with-newlib` - собрать `libgcc` без использования библиотек С.
>
> `--disable-decimal-float` - отключить поддеркжу десятичной плавающей запятой (IEEE 754-2008). Нам это пока не нужно.
>
> `--disable-libgomp` - не собирать библиотеки времени выполнения GOMP.
>
> `--disable-libmudflap` - не собирать библиотеку `libmudflap` (библиотека, которая может быть использована для проверки правильности использования указателей).
>
> `--disable-libssp` - не собирать библиотеки времени выполнения для обнаружения разбиения стека.
>
> `--disable-libatomic` - не собирать атомарные операции.
>
> `--disable-libquadmath` - не собирать `libquadmath`.
>
> `--disable-threads` - не искать многопоточные заголовочные файлы, поскольку для этой архитектуры (`$LFA_TGT`) их ещё нет. GCC сможет найти их после сборки стандартной библиотеки С.
>
> `--enable-languages=c` - указывает `configure` собирать компилятр языка C.
>
> `--disable-multilib` - поддержка multilib нам не нужна.
>
> `--with-arch=$LFA_ARCH` - устанавливает выбранную ранее архитектуру ARM.
>
> `--with-float=$LFA_FLOAT` - устанавливает ранее выбранный режим работы с плавающей запятой.
>
> `--with-fpu=$LFA_FPU` - устанавливает тип аппаратной плавающей запятой. Если `$LFA_FPU="soft"`, это значение игнорируется.

## Сборка

```bash
make all-gcc all-target-libgcc
```

## Установка

```bash
make install-gcc install-target-libgcc
```

~~~admonish warning title="Внимание"
Если во время компиляции пакета у вас возникли ошибки, то, возможно, в вашем случае поможет перекомпиляция GCC: запустите снова скрипт `../configure` из этапа настройки со всеми указанными там опциями *кроме следующих:*

```bash
  --with-float=$LFA_FLOAT \
  --with-fpu=$LFA_FPU
```

Далее вновь выполните команду для сборки пакета (`make all-gcc all-target-libgcc`).
~~~

~~~admonish note title="Содержимое пакета" collapsible=true
На данный момент знать содержимое пакета GCC вам не требуется, поскольку сейчас мы собрали лишь небольшую его часть, предназначенную только для компиляции стандартной библиотеки С (`musl`). Информация о содержимом пакета GCC содержится [на втором проходе сборки GCC](gcc-p2.md)
~~~
