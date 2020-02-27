## Introduction

A container is an abstraction that in a nutshell represents the local
environment where an application will execute.  It is very similar to a
physical server or VM but unique in that it does not represent actual
infrastructure but rather an abstraction of said infrastructure.  This
allows you to decouple your application needs from your infrastructure
needs.  This local environment has everything an app needs to run such
as programming language packages for example.  Once in a container the
application is portable to any infrastructure that can host it.  Kubernetes
at a high level is an orchestrator that allows you to place your container
on a given piece of infrastructure. It does this by first placing the
container in a pod and then deploying that pod to a physical or virtual node
(server).  Therefore, pods in Kubernetes are a packaged unit of work that
are in a runnable or executable state.  They represent the smallest unit of
work in Kubernetes that can be created or deployed.  A pod includes inside
of it one or more containers.  Kubernetes supports several different
container runtimes but Docker is the most commonly used [@kubernetes_pods2020
-sp20-516-237].  There is a one
to many relationship between pods and containers.  Meaning that you can
design your app to run across several containers within the same pod or you
can stick to one container in one pod, it's up to the developer.  See Fig 1
for a more detailed view of a pod.

:o2: image includsin wrong, if copied, citation is missing Fig 1 wrong, please see notation.md for proper citation
empty lines in document missing 

![Fig 1 - Pods in a Node](./images/node_pic.png)
TODO: check to see if figure is correctly referenced in Bibtex format

:o2: punctuation wrong

So how does Kubernetes determine how to assign a pod, it's smallest unit of
work, to a given node?  The main way is through the Kubernetes Scheduler
.  The Scheduler is responsible for identifying pods with no assigned pod and
then assigning those pods to a particular node to run on.  The scheduler uses
certain principles to make it's decision of where to assign pods.  These
principles and other scheduler details are described in the subsequent
section.

## Assigning Pods to Nodes - kube-scheduler

:o2: indentation messed up. please learn markdown

Pods can be assigned to specific nodes by administrators or deployment
 engineers but that means a lot of manual work to avoid unhealthy nodes or
 nodes with inadequate resources [@Goltsman2019-sp20-516-237].  That is where
  the scheduler comes in
 to play.  The scheduler in Kubernetes is called "kube-scheduler".  Kube
 -scheduler performs a 2 step operation when determining how to assign pods
 : Filtering and Scoring [@kubernetes_scheduler2020-sp20-516-237].
 
 1. Filtering - a node list is created in this step.  Any available node that
  matches what is being requested by the pod is added to this list. There are a
   number of default policies that kube-scheduler takes into account when
   determining if a node is a match. A couple examples of
     these below [@kubernetes_scheduler2020-sp20-516-237].  
    * > PodFitsResources - Checks if the Node has free resources (eg, CPU and
     Memory) to meet the requirement of the Pod
    * > NoVolumeZoneConflict - Evaluate if the Volumes that a Pod requests are
     available on the Node, given the failure zone restrictions for that
      storage 

 2. Scoring - Using the node list generated from the filtering step, kube
 -scheduler scores the nodes based on whatever active scoring rules are in
  place.  Kube-scheduler assigns the pod to the node with the highest score
  .  In the event of a tie a winner is chosen at random.  Some examples of
   scoring rules below [@kubernetes_scheduler2020-sp20-516-237]:
    * > SelectorSpreadPriority - Spreads Pods across hosts, considering Pods
      > that belong to the same Service, StatefulSet or ReplicaSet.
    * > NodeAffinityPriority - Prioritizes nodes according to node affinity
      > scheduling preferences indicated in
      > PreferredDuringSchedulingIgnoredDuringExecution.
  
 
 NOTE: For a full list of these policies see [here](https://kubernetes.io/docs/concepts/scheduling/kube-scheduler/)
  
## Assigning Pods to Nodes - pod configuration

A pod can be assigned to a node either via the scheduler or can be
 manually directed to a node via the nodeName field in the pod config file
 .  Using
  nodeName is the simplest form of selecting a node but is very limited and
   thus rarely used [@kubernetes_assignpod2020-sp20-516-237].  The nodeName
    field is used to list the exact node
    the pod should be executed on and it takes precedence above other node
     selection rules [@kubernetes_assignpod2020-sp20-516-237].  Given the limited nature of using nodeName the
      remaining sections focus on node selection constraints that integrate
       with the scheduler.
       
Node selection constraints that integrate with the scheduler can be placed
 into 3 categories or types: nodeSelector, node affinity, and taints/tolerations.
 
   ### nodeSelector
 
   This is the earliest feature Kubernetes used to allow developers or admins
    to assign pods to specific nodes [@Goltsman2019-sp20-516-237].  It makes use of key/value pair
     labels to do this.  The key/value pair label must first be tagged to the
      node (see example below).
   
    kubectl label nodes workernode1 preferred=true
   
   That same key/value pair label must then be added to your pod
    configuration (see example below).
   
     spec:
       containers:
       - name: <app name>
         image: <image name>
         imagePullPolicy: Always
         ports:
         - containerPort: <port number>
       nodeSelector:
         preferred: "true"
    
  With these two pre-requisites in place the scheduler will now be able to
   assign any requested pod with this label to the appropriate node.  
 
   ### Node Affinity
 
   The use of node affinity is a much more sophisticated
    way of pairing pods to nodes but it works in a similar fashion to
     nodeSelector.  Key/value label pairs are still used on pod and node but
      the 3
      key
      differences to
      nodeSelector per
      Kubernetes [@kubernetes_assignpod2020-sp20-516-237] are as follows:
   
   1. More options are provided in the language than simply "exact match
   " comparison and the use of "AND".  You can do comparisons such as "In
   ", "NotIn", "Gt" (greater than), and others. Example below:
   
   2. The label rule can be identified as being optional or a "soft
    preference".  Meaning that if the rule is not satisfied but the scheduler
     still finds this to be the best node to run on, the pod will still be
      scheduled on that node. Example below:  
      
   3. Inter-pod affinity is possible which allows for these label rules to be
    applied based on pods already running on a node.  Meaning, if my pod
     starts up
    , the
     scheduler will determine if actively running pods on a given node can
      run with my pod based on these label rules matching or not matching
       between new pod and existing pods.
 
   ##### Node affinity example:
    
  The goal is to have a pod scheduled on a rhel (os-type) node as a must AND
    preferrably on a node with disk-type of ssd.  In the below example, a pod
     would normally get scheduled on workernode3 given the pod configuration.
   
   Applying node label:
       
    kubectl label nodes workernode1 os-type=windows
    kubectl label nodes workernode1 disk-type=ssd
    kubectl label nodes workernode2 os-type=rhel
    kubectl label nodes workernode2 disk-type=ssd
    kubectl label nodes workernode3 os-type=rhel
    kubectl label nodes workernode3 disk-type=hdd
         
   Pod configuration:
       
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: os-type
                operator: In
                values:
                - "rhel"
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            preference:
              matchExpressions:
              - key: disk-type
                operator: In
                values:
                - "ssd" 
 
   ##### Inter-pod affinity example:
   
   Inter-pod affinity and anti-affinity are more powerful than node affinity
    because it allows you to create node selection rules based on pods that
     are already running on nodes.  However, because it requires a
      significantly higher amount of processing it can slow down scheduling
       and so per Kubernetes [@kubernetes_assignpod2020-sp20-516-237] it is not recommended on clusters larger
        than few hundred nodes.  Note that anti-affinity refers to the
         ability to define labels which your pod will avoid.
   
   In the example below taken from Kubernetes site [@kubernetes_assignpod2020-sp20-516-237] there is one pod affinity
    rule (required) and another
    anti-affinity rule (preferred) defined.  The goal of affinity rule is to
     only schedule this pod on a node that has the listed topologyKey (failure
     -domain
    .beta.kubernetes.io/zone) AND has a pod running on it with key/value pair
    : security=S1.  The goal of the anti-affinity rule is to preferrably
     AVOID scheduling this pod on a node that has the listed topologyKey
      (failure
     -domain
     .beta.kubernetes.io/zone) AND has a pod running on it with key/value pair
    : security=S2.
        
   Pod configuration:
       
    spec:
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: security
                operator: In
                values:
                - S1
            topologyKey: failure-domain.beta.kubernetes.io/zone
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: security
                  operator: In
                  values:
                  - S2
              topologyKey: failure-domain.beta.kubernetes.io/zone 

## Taints and tolerations 

When we submit workloads to run in a cluster, the scheduler determines where to place the Pods associated with the workload. The scheduler can place a Pod on any available node that satisfies the Pod's CPU, memory, or any other resource requirements. There must be some control over which workloads can run on a particular pool of nodes. Node affinity is one way of control by attracting Pod to Nodes. Taints are to refuse pod to be scheduled unless that pod has a matching toleration. Taints are more like blacklist so when there are many nodes and need to blacklist one then it is really easy to achieve this with Taints [@KubeShedule-sp20-516-232]. 

* A taint applied to a node indicates that only specific pods can be scheduled on them.
* A toleration is applied to a pod allows them to tolerate a node's taint.

Taints and tolerations consist of a key, value, effect and operator

1. **Key**: The key is any string, up to 253 characters. The key must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores.

2. **Value**: Value is any string, up to 63 characters. The value must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores. 

3. **Effect**: Effect can be 
    * NoSchedule: New pods that do not match the taint are not scheduled onto that node. Existing pods on the node remain.
    * PreferNoSchedule: New pods that do not match the taint might be scheduled onto that node, but the scheduler tries not to.Existing
                        pods on the node remain. 
    * NoExecute: New pods that do not match the taint cannot be scheduled onto that node.Existing pods on the node that do not have a                    matching toleration are removed.
 4. **Operator**:
    * Equal: The key/value/effect parameters must match. This is the default.
    * Exists: The key/effect parameters must match. You must leave a blank value parameter, which matches any.
    
## Customizing the Scheduler

The functionality of `kube-scheduler` can be augmented with new predicates and priority functions, although this is rarely necessary in practice. Some options for customizing `kube-scheduler` include running multiple schedulers in a cluster and running a "scheduler extender" http(s) process, both of which are poorly documented and exceedingly difficult to implement on Windows machines. The most straightforward method to customize `kube-scheduler` is to write a JSON file containing desired predicates and priority functions and pass this file to `kube-scheduler` when the cluster is launched. When using a custom config file, `kube-scheduler` will only call the functions named in the file as opposed to all default functions. The Kubernetes team recommends installing minikube and kubectl, which would allow you to execute `minikube start --extra-config=scheduler.AlgorithmSource.Policy.File.Path=$FILE`. However, setting up minikube and kubectl is an arduous process on Windows, and not even suggested sandbox tools like <https://labs.play-with-k8s.com> and <https://katacoda.com/courses/kubernetes/playground> provide the necessary functionality. Since multipass is expected for this course, we will use mircok8s running on a multipass instance.

