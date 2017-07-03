#!/bin/bash

# Set the name of your project environment
# That's the only thing you're have to change
PROJECT_ENV="sanic_user"

echo "Current environment:"
echo "$(conda info --envs | grep '*')"

echo "Environment required by this project:"
echo "${PROJECT_ENV}"

echo "Applying environment..."

{ # try
  source activate ${PROJECT_ENV} &&
} || { # catch
  conda create -n ${PROJECT_ENV} pip
  echo "Environment ${PROJECT_ENV} was created successfully."
  echo "Execute `source ./env.sh` again to switch the environment."
}

unset PROJECT_ENV
