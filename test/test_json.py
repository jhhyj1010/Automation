#!/usr/bin/env python3
import json

print("jesson")
data = [{'id': 'PR_kwDODqIrMc47c1bY', 'title': 'Creating repo visualization-helm-chart', 'body': '', 'author': {'login': 'kudupax'}, 'number': 63583, 'mergeable': 'UNKNOWN', 'commits': {'nodes': [{'commit': {'statusCheckRollup': None}}]}, 'timelineItems': {'nodes': []}, 'reviewDecision': None, 'createdAt': '2022-07-15T06:43:50Z', 'updatedAt': '2022-07-15T06:43:50Z', 'reviews': {'nodes': []}, 'reviewRequests': {'nodes': []}, 'assignees': {'nodes': []}, 'labels': {'nodes': []}}, {'id': 'PR_kwDODqIrMc47c02v', 'title': 'request for gvp observability', 'body': 'We need new inner source repo for developing Observability stack for GVP (Grand View Point project).', 'author': {'login': 'AbhijitKuma'}, 'number': 63582, 'mergeable': 'MERGEABLE', 'commits': {'nodes': [{'commit': {'statusCheckRollup': {'state': 'PENDING', 'contexts': {'nodes': [{}]}}}}]}, 'timelineItems': {'nodes': []}, 'reviewDecision': None, 'createdAt': '2022-07-15T06:40:27Z', 'updatedAt': '2022-07-15T06:41:56Z', 'reviews': {'nodes': []}, 'reviewRequests': {'nodes': []}, 'assignees': {'nodes': [{'login': 'AbhijitKuma'}]}, 'labels': {'nodes': []}}, {'id': 'PR_kwDODqIrMc47c1bY', 'title': 'Creating repo visualization-helm-chart', 'body': '', 'author': {'login': 'kudupax'}, 'number': 63583, 'mergeable': 'UNKNOWN', 'commits': {'nodes': [{'commit': {'statusCheckRollup': {'state': 'PENDING', 'contexts': {'nodes': [{}]}}}}]}, 'timelineItems': {'nodes': []}, 'reviewDecision': None, 'createdAt': '2022-07-15T06:43:50Z', 'updatedAt': '2022-07-15T06:45:50Z', 'reviews': {'nodes': []}, 'reviewRequests': {'nodes': []}, 'assignees': {'nodes': []}, 'labels': {'nodes': []}}]

print(type(data))
for i in range(len(data)):
    print(data[i]['number'])

for i, j in enumerate(data):
    print(i,j)

#data = '''{'id': 'PR_kwDODqIrMc47cIus', 'title': 'create repo install-gpu-driver', 'body': 'create repo install-gpu-driver for oneAPI CI PV\r\nSigned-off-by: Lin, Ginno <ginno.lin@intel.com>', 'author': {'login': 'ginno-lin'}, 'number': 63563, 'mergeable': 'MERGEABLE', 'commits': {'nodes': [{'commit': {'statusCheckRollup': {'state': 'FAILURE', 'contexts': {'nodes': [{}, {}]}}}}]}, {'state': 'SUCCESS', 'context': 'full-validation'}, 'timelineItems': {'nodes': [{'__typename': 'LabeledEvent', 'createdAt': '2022-07-15T00:26:07Z', 'label': {'name': 'verification failed'}}]}, 'reviewDecision': None, 'createdAt': '2022-07-15T00:16:35Z', 'updatedAt': '2022-07-15T05:55:06Z', 'reviews': {'nodes': []}, 'reviewRequests': {'nodes': []}, 'assignees': {'nodes': []}, 'labels': {'nodes': [{'name': 'verification failed'}]}}'''

#print(json.loads(data))
