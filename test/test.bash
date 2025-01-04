#!/bin/bash
#SPDX-FileCopyrightText: 2024 Rikuto Nozaki
#SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg sin_publisher_sub.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '17, 0.29237'
