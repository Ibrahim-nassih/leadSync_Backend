#!/usr/bin/env bash

TAG=${1}
NAME_SPACE=${2}

export BUILD_NAME=${TAG}
mkdir ./k8s/.generated/
for f in ./k8s/template/*.yaml
do
  envsubst < $f > "./k8s/.generated/$(basename $f)"
done

kubectl apply -f ./k8s/.generated/ --namespace=$NAME_SPACE
