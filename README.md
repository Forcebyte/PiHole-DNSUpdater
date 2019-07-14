# PiHole-DNSUpdater
Botched little script used to update DNS records from an inventory list in Pi-Hole

### Brief / Overview
This repo uses both a Ansible YAML file and a Python script to update entries onthe Pi-Hole. This, alongside the inventory.txt file are meant to run against multiple Pi-Hole or DNSMasq servers to coordinate updates to DNS files

Perferably, this is meant to run on a Jenkins box, however that can be customizable. Right now its labelled against my HomeLab but you can change the local git repo to point to your GitHub instead of my Gitea server if needed

### Requirements
- SSH Key access to Proxmox server (Preferrably root)
- Jenkins Server to run job on a timed basis

### Why not Ansible Tower DNS Module?
This is mostly for personal preference - I wanted more experience with Jenkins' Ansible extensions so I went with that. This will also work off of Ansible Tower if required (all I use Ansible for is propagating off of an inventory file)
