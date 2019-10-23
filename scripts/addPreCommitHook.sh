#!/bin/bash

PRE_COMMIT_PATH=.git/hooks/pre-commit
FORCE=0

while getopts ":f" opt; do
  case $opt in
    f)
      echo "Command invoked with -f flag, overwriting existing hook..." >&2
      FORCE=1
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

if [ $FORCE -eq 0 -a -e $PRE_COMMIT_PATH ]; then
  echo "Failed: $PRE_COMMIT_PATH exists"
  exit 1
fi

echo "Copying template pre-commit hook to $PRE_COMMIT_PATH..."
cp scripts/pre-commit.template $PRE_COMMIT_PATH
chmod +x $PRE_COMMIT_PATH

if [ $? -eq 0 ]; then
    echo "Success!"
else
    echo "Failed: pre-commit template was not copied to $PRE_COMMIT_PATH"
fi



