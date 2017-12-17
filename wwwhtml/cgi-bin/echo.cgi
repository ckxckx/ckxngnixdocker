#!/bin/bash

echo -ne 'Status: 200\r\n'
echo -ne 'Content-Type: text/plain\r\n'
echo -ne '\r\n'

echo 'PATH_INFO: ' $PATH_INFO
echo 'QUERY_STRING: ' $QUERY_STRING

echo "ccccccccccccc"
exit 0
