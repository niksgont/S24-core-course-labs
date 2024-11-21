$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-7f7b696cc7-kn8sf   1/1     Running   0          12m

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/python-app   NodePort    10.105.232.12   <none>        8000:31511/TCP   12m
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          8d
