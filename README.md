# Fortigateobject

This simple python module allow you to generate a Fortigate script to create addresses objects (ipv4 addresses with CIDR masks). 

As it is, this module will read a txt file as an agurment (The file must have the IP adresses or subnets, one entry per line), creating a script output with the commands to create the objects on most versions of Fortigate Firewall. 

Using this module will allow you to save time, automating the creation of objects. This script does not consider enviroments that uses VDOMs. 
