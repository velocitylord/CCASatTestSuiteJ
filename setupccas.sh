#!/bin/bash
#  !run as sudo!
# Add all the names you need, like below
# sysctl net.ipv4.tcp_congestion_control=bbr
#
# 
#
# 
ccas=("bbr" "bic" "hybla" "yeah" "doesnotexist" "yeah")
failedcca=()
for cca in "${ccas[@]}"; do
  sysctl net.ipv4.tcp_congestion_control=$cca
  if [[ $? -ne 0 ]]; then
    failedcca+=($cca)
  fi
done
if [[ ${#failedcca[@]} != 0 ]]; then
  echo "The following CCA's are not present or go by a different name"
  for failed in "${failedcca[@]}"; do
     echo $failed
  done
fi

#echo "Existing ccas"
#ls /lib/modules/$(uname -r)/kernel/net/ipv4 | grep tcp

echo "Availabel CCAs"
sysctl net.ipv4.tcp_available_congestion_control
