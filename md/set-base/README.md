# Настройка базовой системы

В данной части пойдёт речь о настройке базовой системы. Мы только собрали ряд нужных программ, но на этом всё. Однако для корректной работы только что собранной системы (как минимум для обеспечения её загрузки) нужно создать ряд конфигурационных файлов. Среди этих файлов будут `/etc/fstab`, содержащий информацию о монтировании файловых систем при загрузке, `/etc/mdev.conf` с информацией для `mdev`, предназначенного для динамического управления устройствами в диретории `/dev`, `/etc/profile` с настройками командной оболочки ash и ряд других конфигов, необходимых для работы системы.

Конечно, в более продвинутых и функциональных системах конфигурационных файлов куда больше, но в данном руководстве перечислен минимально возможный список кнфигов, подходящий для корректной работы LFA.
