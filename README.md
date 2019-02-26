# Example Kubernetes operator using metacontroller.app

This repository implements an example Kubernetes operator using http://metacontroller.app and Python 3, called "ImmortalContainers". This operator enables the user to define, using custom resources, containers that must run and if terminated must be restarted.

## Installing and trying the operator

```bash
make
```

Try it running
```bash
make example
```

Then run `kubectl get pods -n immortalcontainers` and check the pod is created. If you kill the pod it will be recreated.

## Remove the operator

Run the following command to remove operator, metacontroller.app, namespaces and CRD.

```bash
make remove_all
```