# Kubernetes Scheduler sp20-516-231 Brian Kegerreis

## Description

The Kubernetes Scheduler (`kube-scheduler`) is a component of the Kubernetes Control Plane that assigns newly created Pods to available Nodes. Each Pod has its own requirements, as do the containers within that Pod. In order to assign a given Pod to a Node, `kube-scheduler` first searches the cluster for "feasible" Nodes, calculates scores for each feasible Node, and then assigns the Pod to the Node with the highest score.

### Filtering

Filtering is the process by which `kube-scheduler` determines whether each Node in the cluster is considered "feasible," or able to meet all of a Pod's hard requirements. Filtering factors (predicates) include:

* Whether a Pod has requested specific Nodes
* Whether a Pod has requested Nodes with certain characteristics, such as dev Nodes or Production nodes.
* Whether each node can accommodate the Pod's memory and CPU requirements
* Whether each noe can mount the Volumes requested by the Pod

### Scoring

Scoring is the process by which `kube-scheduler` selects one Node from a list of feasible Nodes. Scoring factors (priority functions) include:

* Whether a node has cached the image(s) needed to host the Pod. This means the Node will not have to download the 
image(s) and may be able to start the Pod faster.
* Whether a node is hosting Pods that are part of the same Service as the Pod being scheduled. It may be preferable to spread a Service's Pods across multiple Nodes to make it more resilient to the failure of a single Node.
* The number of Pods and allocated resources on a Node. It may be preferable to select relatively empty nodes, but on the other hand, selecting nearly more full nodes could allow a set of Services to run on as few Nodes as possible, which could save money.

## Examples

### Customizing the Scheduler

The functionality of `kube-scheduler` can be augmented with new predicates and priority functions, although this is rarely necessary in practice. Some options for customizing `kube-scheduler` include running multiple schedulers in a cluster and running a "scheduler extender" http(s) process, both of which are poorly documented and exceedingly difficult to implement on Windows machines. The most straightforward method to customize `kube-scheduler` is to write a JSON file containing desired predicates and priority functions and pass this file to `kube-scheduler` when the cluster is launched. When using a custom config file, `kube-scheduler` will only call the functions named in the file as opposed to all default functions. The Kubernetes team recommends installing minikube and kubectl, which would allow you to execute `minikube start --extra-config=scheduler.AlgorithmSource.Policy.File.Path=$FILE`. However, setting up minikube and kubectl is an arduous process on Windows, and not even suggested sandbox tools like <labs.play-with-k8s.com> and <katacoda.com/courses/kubernetes/playground> provide the necessary functionality. Since multipass is expected for this course, we will use mircok8s running on a multipass instance.

#### Installing microk8s

This assumes you have already installed multipass on your machine. Follow these steps to install microk8s on a multipass VM.
```
$ multipass launch --name microk8s-vm --mem 2G --disk 40G
$ multipass shell microk8s-vm
$ sudo snap install microk8s --classic
# check microk8s status
$ sudo microk8s.status --wait-ready
$ sudo microk8s.enable dns dashboard registry
```

####  Setting up a Custom Config File

microk8s starts its version of `kube-scheduler` by calling snap.microk8s.daemon-scheduler with the arguments in /var/snap/microk8s/current/args/kube-scheduler. To point it to a custom config file, run the following command.
```
$ echo '--policy-config-file=$HOME/my_cfg/k8s-sched-cfg.json | sudo tee -a /var/snap/microk8s/current/args/kube-scheduler
```

Write a custom config file.
```
$ mkdir $HOME/my_cfg
# If you aren't familiar with vim, press "i" to start INSERT mode.
# When you are done typing, press ESC, then type ":wq" to write changes and quit. 
# To quit without saving changes, type ":q!"
$ vim k8s-sched-cfg.json
```

> example

> json

> goes

> right

> here

Restart `kube-scheduler`.
```
$ sudo systemctl restart snap.microk8s.daemon-scheduler.service
```

`kube-scheduler` will now use the predicates and priority functions listed in the custom config file. To revert to default scheduler behavior, delete the last line from /var/snap/microk8s/current/args/kube-scheduler and restart `kube-scheduler` again.

## Sources

<https://kubernetes.io/docs/concepts/overview/components/>

<https://kubernetes.io/docs/concepts/configuration/scheduling-framework/>

<https://kubernetes.io/docs/concepts/scheduling/kube-scheduler/>

<https://kubernetes.io/docs/concepts/scheduling/scheduler-perf-tuning/>

<https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/>

<https://kubernetes.io/docs/tasks/administer-cluster/configure-multiple-schedulers/>

<https://developer.ibm.com/technologies/containers/articles/creating-a-custom-kube-scheduler/>

<https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/scheduler_extender.md>

<https://microk8s.io/>
