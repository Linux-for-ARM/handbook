# Конец

Всё готово! Новая система LFA установлена! Мы желаем вам успехов в работе в новой системой Linux.

Не лишним будет создать файл `/etc/lfa-release`. Имея этот файл, вам (и, может быть, нам) будет легко узнать, какая версия LFA установлена. Создайте этот файл, выполнив команду:

```bash
echo "1.0" > /etc/lfa-release
```

И ещё один файл с информацией о системе:

```bash
cat > /etc/lsb-release << "EOF"
DISTRIB_ID="Linux for Arm"
DISTRIB_RELEASE="1.0"
DISTRIB_CODENAME="<ваше имя>"
DISTRIB_DESCRIPTION="Linux for ARM"
EOF
```
