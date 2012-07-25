#!/bin/sh

command -v pypy >/dev/null 2>&1
PYPY_EXISTS=$?

if [ $PYPY_EXISTS != 0 ]; then
    pip install -r cpython_requirements.txt --use-mirrors
fi

pip install -r requirements.txt --use-mirrors

