# Загрузка DTBO

Оверлеи Devicetree — это почти те же Devicetree-файлы, но с несколько иным синтаксисом. Пожалуйста, обратитесь к файлу `dt-object-internal.txt` в исходном коде компилятора devicetree за информацией о внутреннем формате оверлеев: **<https://git.kernel.org/pub/scm/utils/dtc/dtc.git/tree/Documentation/dt-object-internal.txt>**

## Способы использования оверлеев в U-Boot

Существует два способа применения оверлеев:

1. Включить и определить оверлеи в FIT-образ и автоматически их применять;
2. Вручную применять оверлеи;

В оставшейся части документа будет рассмотрено использование оверлеев с помощью ручного подхода. Информацию об использовании оверлеев как части образа FIT можно найти в документе `doc/uImage.FIT/overlay-fdt-boot.txt` загрузчика U-Boot.

## Ручная загрузка и применение оверлеев

<ol>
  <li>Определите, где разместить базовый devicetree и оверлей к нему. Убедитесь, что у вас достаточно места для наложения оверлея.</li>
  <pre><code>=> setenv fdtaddr 0x87f00000
=> setenv fdtovaddr 0x87fc0000</code></pre>

  <li>Загрузите базовый devicetree и оверлей к нему:</li>
  <pre><code>=> load ${devtype} ${bootpart} ${fdtaddr} ${bootdir}/base.dtb
=> load ${devtype} ${bootpart} ${fdtovaddr} ${bootdir}/overlay.dtbo</code></pre>

  <li>Установите базовый devicetree как рабочее дерево FDT:</li>
  <pre><code>=> fdt addr $fdtaddr</code></pre>

  <li>Увеличте дерево FDT настолько, чтобы было возможно применить к нему все возможные (нужные для вас?) оверлеи:</li>
  <pre><code>=> fdt resize 8192</code></pre>

  <li>Примените оверлей:</li>
  <pre><code>=> fdt apply $fdtovaddr</code></pre>

  <li>Загрузите систему, как это делается с традиционным <code>dtb</code>.</li>
</ol>

Для `bootm`:

```bash
=> bootm ${kerneladdr} - ${fdtaddr}
```

Для `bootz`:

```bash
=> bootz ${kerneladdr} - ${fdtaddr}
```

Обратите внимание, что в случае ошибки и базовый devicetree, и его оверлеи будут аннулированы, поэтому сохраните копии, чтобы избежать их перезагрузки.
