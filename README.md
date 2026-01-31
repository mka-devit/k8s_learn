
```bash
kubectl get pods
```
> Получение списка всех подов (Pods),
```bash
kubectl get nodes
```
> Получение списка всех узлов (Nodes).
```bash
kubectl get deployments
```
> Получение списка всех Deployment’ов.
```bash
kubectl get rs
```
> Просмотр ReplicaSet’ов.
```bash
kubectl get hpa
```
> Просмотр horizontalpodautoscaler.autoscaling или AutoScaling.
```bash
kubectl get services
```
> Просмотр всех Service.
```bash
helm list
```
> Просмотр всех релизов Helm в кластере.
```bash
helm install app . 
```
> Используется для установки Helm-чарта.
```bash
helm uninstall app
```
> Ипользуется для удаления релиза Helm.
