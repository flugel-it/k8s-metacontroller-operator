from sync import sync

def fake_parent(**overrides):
    parent = {'apiVersion': 'exampleoperator.flugel.it/v1alpha1',
              'kind': 'ImmortalContainer',
              'metadata': {'annotations': {'kubectl.kubernetes.io/last-applied-configuration': '{"apiVersion":"exampleoperator.flugel.it/v1alpha1","kind":"ImmortalContainer","metadata":{"annotations":{},"name":"example-immortal-container","namespace":"immortalcontainers"},"spec":{"image":"nginx:latest"}}\n'},
                           'creationTimestamp': '2019-02-27T14:42:50Z',
                           'generation': 1,
                           'name': 'example-immortal-container',
                           'namespace': 'immortalcontainers',
                           'resourceVersion': '45812',
                           'selfLink': '/apis/exampleoperator.flugel.it/v1alpha1/namespaces/immortalcontainers/immortalcontainers/example-immortal-container',
                           'uid': 'f4dda463-3a9d-11e9-9d52-0800271209bf'},
              'spec': {'image': 'nginx:latest'}}
    return {**parent, **overrides}

def fake_children(empty=False):
    if empty:
        return {'Pod.v1': {}}
    children = {'Pod.v1': {'example-immortal-container-immortalpod': {'apiVersion': 'v1',
                                                                      'kind': 'Pod',
                                                                      'metadata': {'annotations': {'metacontroller.k8s.io/last-applied-configuration': '{"apiVersion":"v1","kind":"Pod","metadata":{"labels":{"controller-uid":"f4dda463-3a9d-11e9-9d52-0800271209bf"},"name":"example-immortal-container-immortalpod","namespace":"immortalcontainers"},"spec":{"containers":[{"image":"nginx:latest","name":"acontainer"}],"restartPolicy":"OnFailure"}}'},
                                                                                   'creationTimestamp': '2019-02-27T14:42:50Z',
                                                                                   'labels': {'controller-uid': 'f4dda463-3a9d-11e9-9d52-0800271209bf'},
                                                                                   'name': 'example-immortal-container-immortalpod',
                                                                                   'namespace': 'immortalcontainers',
                                                                                   'ownerReferences': [{'apiVersion': 'exampleoperator.flugel.it/v1alpha1',
                                                                                                        'blockOwnerDeletion': True,
                                                                                                        'controller': True,
                                                                                                        'kind': 'ImmortalContainer',
                                                                                                        'name': 'example-immortal-container',
                                                                                                        'uid': 'f4dda463-3a9d-11e9-9d52-0800271209bf'}],
                                                                                   'resourceVersion': '45827',
                                                                                   'selfLink': '/api/v1/namespaces/immortalcontainers/pods/example-immortal-container-immortalpod',
                                                                                   'uid': 'f4e36550-3a9d-11e9-9d52-0800271209bf'},
                                                                      'spec': {'containers': [{'image': 'nginx:latest',
                                                                                               'imagePullPolicy': 'Always',
                                                                                               'name': 'acontainer',
                                                                                               'resources': {},
                                                                                               'terminationMessagePath': '/dev/termination-log',
                                                                                               'terminationMessagePolicy': 'File',
                                                                                               'volumeMounts': [{'mountPath': '/var/run/secrets/kubernetes.io/serviceaccount',
                                                                                                                 'name': 'default-token-cqslh',
                                                                                                                 'readOnly': True}]}],
                                                                               'dnsPolicy': 'ClusterFirst',
                                                                               'enableServiceLinks': True,
                                                                               'nodeName': 'minikube',
                                                                               'priority': 0,
                                                                               'restartPolicy': 'OnFailure',
                                                                               'schedulerName': 'default-scheduler',
                                                                               'securityContext': {},
                                                                               'serviceAccount': 'default',
                                                                               'serviceAccountName': 'default',
                                                                               'terminationGracePeriodSeconds': 30,
                                                                               'tolerations': [{'effect': 'NoExecute',
                                                                                                'key': 'node.kubernetes.io/not-ready',
                                                                                                'operator': 'Exists',
                                                                                                'tolerationSeconds': 300},
                                                                                               {'effect': 'NoExecute',
                                                                                                'key': 'node.kubernetes.io/unreachable',
                                                                                                'operator': 'Exists',
                                                                                                'tolerationSeconds': 300}],
                                                                               'volumes': [{'name': 'default-token-cqslh',
                                                                                            'secret': {'defaultMode': 420,
                                                                                                       'secretName': 'default-token-cqslh'}}]},
                                                                      'status': {'conditions': [{'lastProbeTime': None,
                                                                                                 'lastTransitionTime': '2019-02-27T14:42:50Z',
                                                                                                 'status': 'True',
                                                                                                 'type': 'Initialized'},
                                                                                                {'lastProbeTime': None,
                                                                                                 'lastTransitionTime': '2019-02-27T14:42:55Z',
                                                                                                 'status': 'True',
                                                                                                 'type': 'Ready'},
                                                                                                {'lastProbeTime': None,
                                                                                                 'lastTransitionTime': '2019-02-27T14:42:55Z',
                                                                                                 'status': 'True',
                                                                                                 'type': 'ContainersReady'},
                                                                                                {'lastProbeTime': None,
                                                                                                 'lastTransitionTime': '2019-02-27T14:42:50Z',
                                                                                                 'status': 'True',
                                                                                                 'type': 'PodScheduled'}],
                                                                                 'containerStatuses': [{'containerID': 'docker://4ac6a60eb65f410d027dd2a7a9e74da3a6327efd12d8988d7a0a04535b977e90',
                                                                                                        'image': 'nginx:latest',
                                                                                                        'imageID': 'docker-pullable://nginx@sha256:dd2d0ac3fff2f007d99e033b64854be0941e19a2ad51f174d9240dda20d9f534',
                                                                                                        'lastState': {},
                                                                                                        'name': 'acontainer',
                                                                                                        'ready': True,
                                                                                                        'restartCount': 0,
                                                                                                        'state': {'running': {'startedAt': '2019-02-27T14:42:54Z'}}}],
                                                                                 'hostIP': '10.0.2.15',
                                                                                 'phase': 'Running',
                                                                                 'podIP': '172.17.0.8',
                                                                                 'qosClass': 'BestEffort',
                                                                                 'startTime': '2019-02-27T14:42:50Z'}}}}

    return children

def test_sets_current_pod():
    parent = fake_parent()
    children = fake_children()
    synced = sync(parent, children)
    desired_status = synced["status"]
    desired_children = synced["children"]
    assert 'currentPod' in desired_status
    assert desired_status['currentPod'] == list(children['Pod.v1'])[0]


def test_create_pod():
    children = {'Pod.v1': {}}
    parent = fake_parent(spec={'image': 'exampleimg:latest'})

    synced = sync(parent, children)
    desired_status = synced["status"]
    desired_children = synced["children"]
    assert len(desired_children) == 1
    pod = desired_children[0]
    assert pod['apiVersion'] == 'v1' and pod['kind'] == 'Pod'
    assert pod['metadata']['name'] == parent["metadata"]["name"]+"-immortalpod"
    assert pod['spec']['containers'][0]['image'] == 'exampleimg:latest'


def test_unset_current_pod():
    children = fake_children(empty=True)
    parent = fake_parent(status={'currentPod': 'example-immortal-container-immortalpod'})

    synced = sync(parent, children)
    desired_status = synced["status"]
    assert desired_status['currentPod'] == ''
