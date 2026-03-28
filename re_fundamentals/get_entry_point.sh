#!/bin/bash

file_name=$1

if [ -z "$file_name" ]; then
    echo "Usage: $0 <elf_file>"
    exit 1
fi

if [ ! -f "$file_name" ]; then
    echo "Error: File '$file_name' not found."
    exit 1
fi

magic_number=$(readelf -h "$file_name" | grep "Magic:" | sed 's/Magic://' | xargs)
class=$(readelf -h "$file_name" | grep "Class:" | awk '{print $2}')
byte_order=$(readelf -h "$file_name" | grep "Data:" | awk -F', ' '{print $2}')
entry_point_address=$(readelf -h "$file_name" | grep "Entry point address:" | awk '{print $4}')

source messages.sh

display_elf_header_info