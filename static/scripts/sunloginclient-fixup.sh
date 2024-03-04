#!/bin/bash

echo "正在修正向日葵软件包配置脚本 ..."
echo -e "#\!/bin/bash\n/usr/bin/true" \
    > /var/lib/dpkg/info/sunloginclient.postinst
dpkg --configure -a

echo "正在安装与启用服务 ..."
cp -v /usr/local/sunlogin/scripts/runsunloginclient.service \
    /etc/systemd/system/runsunloginclient.service
systemctl enable runsunloginclient.service --now

<<<<<<< HEAD
echo "正在修正皮肤权限位 ..."
=======
echo "正在修正皮肤数据包权限位 ..."
>>>>>>> 0eadd18 (feat(scripts): add fix up script for sunloginclient)
chmod 666 /usr/local/sunlogin/res/skin/*
