# Установка имени хоста

Во время загрузки система устанавливает имя хоста, на котором она работает (hostname). Имя хоста содержится в файле `/etc/hostname`. Создайте его:

```bash
echo "[lfa]" > $LFA_SYS/etc/hostname
```

Замените `[lfa]` на имя, присвоенное компьютеру. Не вводите здесь полное доменное имя (FQDN). Эта информация будет помещена в файл `/etc/hosts` в следующем разделе.
