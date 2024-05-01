# Rockchip: TPL

Для некоторых SoC в U-Boot отсутствует поддержка инициализации DRAM. В этих случаях для получения полнофункционального образа загрузчика выполните следующие действия:

1. [**Упакуйте образ U-Boot TPL/SPL**](https://docs.u-boot.org/en/latest/board/rockchip/rockchip.html#packagewithtplandspl) (<https://docs.u-boot.org>), используйте бинарник DDR из репозитория `rkbin` как `ROCKCHIP_TPL` при сборке U-Boot, либо следуйте следующему пункту №2:
2. [**Упакуйте образ при помощи Rockchip `miniloader`**](https://docs.u-boot.org/en/latest/board/rockchip/rockchip.html#packagewithtplandspl) (<https://docs.u-boot.org>);

## Установка

Для RK3308:

```bash
export ROCKCHIP_TPL="$PWD/rkbin/bin/rk33/rk3308_ddr_589MHz_uartX_mY_v2.07.bin"
```

Для RK3568:

```bash
export ROCKCHIP_TPL="$PWD/rkbin/bin/rk35/rk3568_ddr_1560MHz_v1.13.bin"
```

Для RK3588:

```bash
export ROCKCHIP_TPL="$PWD/rkbin/bin/rk35/rk3588_ddr_lp4_2112MHz_lp5_2736MHz_v1.09.bin"
```
