#!/bin/bash

# Set the name of project environment
# By comnvention it's an `env`
PROJECT_ENV="env"

echo "Current environment:"
echo "$(conda info --envs | grep '*')"

echo "Environment required by project:"
echo "${PROJECT_ENV}"

{ # try
  source activate ${PROJECT_ENV} &&
} || { # catch
  conda create -p ./${PROJECT_ENV} pip -y
}

echo "Activation shortcut:"
echo "> source ./env.sh"
echo "Name of current environment should appear in parenthesises."

unset PROJECT_ENV
