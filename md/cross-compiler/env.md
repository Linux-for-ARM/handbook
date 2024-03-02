# Объявление дополнительных переменных

Теперь вам нужно объявить переменную `$LFA_SYS`, которая будет содержать путь до директории, в которой будет находиться собираемая базовая система LFA:

```bash
export LFA_SYS=$LFA/baseOS
echo "export LFA_SYS=\$LFA/baseOS" >> ~/.bashrc
```

Объявите переменные, содержащие пути до собранных компилятора, компоновщика и иных инструментов:

```bash
cat >> ~/.bashrc << EOF
export CC="$LFA_TGT-gcc --sysroot=$LFA_SYS"
export CXX="$LFA_TGT-g++ --sysroot=$LFA_SYS"
export AR="$LFA_TGT-ar"
export AS="$LFA_TGT-as"
export LD="$LFA_TGT-ld --sysroot=$LFA_SYS"
export RANLIB="$LFA_TGT-ranlib"
export READELF="$LFA_TGT-readelf"
export STRIP="$LFA_TGT-strip"
EOF
```

И примените изменения:

```bash
source ~/.bashrc
```
