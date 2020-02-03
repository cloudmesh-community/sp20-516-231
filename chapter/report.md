# 1 Kubernetes Scheduler

:o2: please learn markdown

:o2: use empty ilines

:o2: all http links are non valid markdown use <>

## 1.1 Description
The Kubernetes Scheduler (`kube-scheduler`) is a component of the Kubernetes Control Plane that assigns newly created Pods to available Nodes. Each Pod has its own requirements, as do the containers within that Pod. In order to assign a given Pod to a Node, `kube-scheduler` first searches the cluster for "feasible" Nodes, calculates scores for each feasible Node, and then assigns the Pod to the Node with the highest score.
### 1.1.1 Filtering
Filtering is the process by which `kube-scheduler` determines whether each Node in the cluster is considered "feasible," or able to meet all of a Pod's hard requirements. Filtering factors include:
* Whether a Pod has requested specific Nodes
* Whether a Pod has requested Nodes with certain characteristics, such as dev Nodes or Production nodes.
* Whether each node can accommodate the Pod's memory and CPU requirements
* Whether each noe can mount the Volumes requested by the Pod
### 1.1.2 Scoring
Scoring is the process by which `kube-scheduler` selects one Node from a list of feasible Nodes. Scoring factors include:
* Whether a node has cached the image(s) needed to host the Pod. This means the Node will not have to download the image(s) and may be able to start the Pod faster.
* Whether a node is hosting Pods that are part of the same Service as the Pod being scheduled. It may be preferable to spread a Service's Pods across multiple Nodes to make it more resilient to the failure of a single Node.
* The number of Pods and allocated resources on a Node. It may be preferable to select relatively empty nodes, but on the other hand, selecting nearly more full nodes could allow a set of Services to run on as few Nodes as possible, which could save money.
## 1.2 Example
idea - set up a custom scheduler for certain pods

rationale - can contain some rules for pods that you only have to define once and then send pods to the scheduler instead of copy-pasting whatever affinity rule to each pod


## Sources
https://kubernetes.io/docs/concepts/overview/components/

https://kubernetes.io/docs/concepts/configuration/scheduling-framework/

https://kubernetes.io/docs/concepts/scheduling/kube-scheduler/

https://kubernetes.io/docs/concepts/scheduling/scheduler-perf-tuning/

https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/

https://kubernetes.io/docs/tasks/administer-cluster/configure-multiple-schedulers/

https://developer.ibm.com/technologies/containers/articles/creating-a-custom-kube-scheduler/

https://github.com/kubernetes/community/blob/master/contributors/design-proposals/scheduling/scheduler_extender.md
