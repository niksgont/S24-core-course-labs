# Ansible Deployment Output

## Deployment Command
```bash
ansible-playbook playbooks/dev/main.yaml
PLAY [Deploy Docker and Web Application] ***************************************

TASK [Gathering Facts] *********************************************************
ok: [vm1]

TASK [docker : Install prerequisites] ******************************************
changed: [vm1]

TASK [docker : Add Docker’s official GPG key] **********************************
changed: [vm1]

...

TASK [web_app : Pull the latest Docker image] **********************************
changed: [vm1]

TASK [web_app : Stop and remove any existing container] ************************
ok: [vm1]

TASK [web_app : Deploy the new container] **************************************
changed: [vm1]

PLAY RECAP *********************************************************************
vm1                        : ok=15   changed=10   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
