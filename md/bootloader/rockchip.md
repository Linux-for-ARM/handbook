# Rockchip

{{#include pkgs/u-boot.md}}

## Поддерживаемые платы

Выберите из списка ниже нужную вам материнскую плату. Алгоритм действий следующий: подставьте в аргумент системы сборки make вместо `<имя платы>_defconfig` имя вашей платы, указанное в столбце «`defconfig`», например, для платы Orange Pi 5, аргумент будет `orangepi-5-rk3588s_defconfig`.

| SoC        | Плата                                                | `defconfig`                   |
|------------|------------------------------------------------------|-------------------------------|
| **px30**   | **Rockchip Evb-PX30**                                | **`evb-px30`**                |
|            | Engicam PX30.Core C.TOUCH 2.0                        | `px30-core-ctouch2-px30`      |
|            | Engicam PX30.Core C.TOUCH 2.0 10.1                   | `px30-core-ctouch2-of10-px30` |
|            | Firefly Core-PX30-JD4                                | `firefly-px30`                |
|            | Theobroma Systems PX30-µQ7 SoM - Ringneck            | `ringneck-px30`               |
| **rk3288** | **Google Jerry**                                     | **`chromebook_jerry`**        |
|            | Google Mickey                                        | `chromebook_mickey`           |
|            | Google Minnie                                        | `chromebook_minnie`           |
|            | Google Speedy                                        | `chromebook_speedy`           |
| **rk3308** | **Radxa ROCK Pi S**                                  | **`rock-pi-s-rk3308`**        |
| **rk3326** | **Odroid-go Advance**                                | **`odroid-go2`**              |
| **rk3328** | **FriendlyElec NanoPi R2C**                          | **`nanopi-r2c-rk3328`**       |
|            | FriendlyElec NanoPi R2C Plus                         | `nanopi-r2c-plus-rk3328`      |
|            | FriendlyElec NanoPi R2S                              | `nanopi-r2s-rk3328`           |
|            | Pine64 Rock64                                        | `rock64-rk3328`               |
|            | Radxa ROCK Pi E                                      | `rock-pi-e-rk3328`            |
|            | Xunlong Orange Pi R1 Plus                            | `orangepi-r1-plus-rk3328`     |
|            | Xunlong Orange Pi R1 Plus LTS                        | `orangepi-r1-plus-lts-rk3328` |
| **rk3399** | **FriendlyElec NanoPC-T4**                           | **`nanopc-t4-rk3399`**        |
|            | FriendlyElec NanoPi M4                               | `nanopi-m4-rk3399`            |
|            | FriendlyElec NanoPi M4B                              | `nanopi-m4b-rk3399`           |
|            | FriendlyARM NanoPi NEO4                              | `nanopi-neo4-rk3399`          |
|            | Google Bob                                           | `chromebook_bob`              |
|            | Google Kevin                                         | `chromebook_kevin`            |
|            | Khadas Edge                                          | `khadas-edge-rk3399`          |
|            | Khadas Edge-Captain                                  | `khadas-edge-captain-rk3399`  |
|            | Khadas Edge-V                                        | `khadas-edge-v-rk3399`        |
|            | Orange Pi RK3399                                     | `orangepi-rk3399`             |
|            | Pine64 RockPro64                                     | `rockpro64-rk3399`            |
| **rk3566** | **Pine64 PineTab2**                                  | **`pinetab2-rk3566`**         |
|            | Pine64 Quartz64-A Board                              | `quartz64-a-rk3566`           |
|            | Pine64 Quartz64-B Board                              | `quartz64-b-rk3566`           |
| **rk3568** | **Banana Pi BPI-R2 Pro**                             | **`bpi-r2-pro-rk3568`**       |
|            | FriendlyElec NanoPi R5C                              | `nanopi-r5c-rk3568`           |
|            | FriendlyElec NanoPi R5S                              | `nanopi-r5s-rk3568`           |
|            | Hardkernel ODROID-M1                                 | `odroid-m1-rk3568`            |
|            | Radxa ROCK 3 Model A                                 | `rock-3a-rk3568`              |
|            | *Generic RK3566/RK3568*                              | *`generic-rk3568`*            |
| **rk3588** | **Edgeble Neural Compute Module 6A SoM - Neu6a**     | **`neu6a-io-rk3588`**         |
|            | Edgeble Neural Compute Module 6B SoM - Neu6b         | `neu6b-io-rk3588`             |
|            | FriendlyElec NanoPC-T6                               | `nanopc-t6-rk3588`            |
|            | Pine64 QuartzPro64                                   | `quartzpro64-rk3588`          |
|            | Radxa ROCK 5A                                        | `rock5a-rk3588s`              |
|            | Radxa ROCK 5B                                        | `rock5b-rk3588`               |
|            | Xunlong Orange Pi 5                                  | `orangepi-5-rk3588s`          |
|            | Xunlong Orange Pi 5 Plus                             | `orangepi-5-plus-rk3588`      |
|            | *Generic RK3588S/RK3588*                             | *`generic-rk3588`*            |
| **rv1126** | **Edgeble Neural Compute Module 2 SoM - Neu2/Neu2k** | **`neu2-io-r1126`**           |

<small>Таблица поддерживаемого оборудования в сокращённом виде. Выберите отсюда нужную вам плату. Если вашу плату, использующую Rockchip SoC, вы не нашли здесь, обратитесь к таблице из <a href="https://docs.u-boot.org/en/latest/board/rockchip/rockchip.html#rockchip-boards"><b>документации U-Boot</b></a>, где содержится полный список поддерживаемых плат.</small>
