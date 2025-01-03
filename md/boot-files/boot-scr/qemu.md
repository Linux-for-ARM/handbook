# Создание `boot.scr` для QEMU

Создайте файл `$LFA_SYS/boot/boot.cmd`:

```bash
cat > $LFA_SYS/boot/boot.cmd << "EOF"
# higher load address; the default causes the initrd to be overwritten when the bzImage is unpacked....
#setenv ramdisk_addr_r 0x8000000

echo "KERNEL LOAD ADDRESS: kernel_addr_r : ${kernel_addr_r}"
echo "INITRD LOAD ADDRESS: ramdisk_addr_r: ${ramdisk_addr_r}"
echo "FDT LOAD ADDRESS   : fdt_addr      : ${fdt_addr}"

# /vmlinuz are standard LFA symlink to the "latest installed kernel"
load ${devtype} ${devnum}:${distro_bootpart} ${kernel_addr_r} /vmlinuz

#booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr}
booti ${kernel_addr_r}
EOF
```

Скомпилируйте этот файл:

```bash
mkimage -C none \
  -A arm \
  -T script \
  -d $LFA_SYS/boot/boot.cmd \
  $LFA_SYS/boot/boot.scr
```
