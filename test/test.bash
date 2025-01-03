#!/bin/bash
#SPDX-FileCopyrightText: 2024 Rikuto Nozaki
#SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source /opt/ros/foxy/setup.bash
source $dir/ros2_ws/install/setup.bash

timeout 15 ros2 run mypkg sin_publisher > /tmp/mypkg.log

if cat /tmp/mypkg.log | grep -E 'Listen: 360,' /tmp/mypkg.log; then
	echo "Error: 360以上はないです"
	exit 1
else
        echo 'OK'
        exit 0
fi
