Playground
----------

As the name states, this repository is an archive of small exercises or projects mostly used for personal reference.

Setting up a testing Ubuntu VM (DigitalOcean)
=============================================

	echo 'do_token = "DigitalOcean API TOKEN"' > terraform.tfvars
	echo 'do_sshkey_name = "Name of the SSH key from DigitalOcean account"' >> terraform.tfvars
	terraform init
	terraform apply
