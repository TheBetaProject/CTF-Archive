#!/bin/bash
chown pilot:pilot /app/pwn_sanity_check
chmod +x /app/pwn_sanity_check
while true; do
    su pilot -c 'timeout -k 30s 1d socat TCP-LISTEN:7480,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./pwn_sanity_check"'
done