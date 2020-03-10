### Variables used in the Terraform configuration - override in terraform.tfvars
variable "do_token" {
    description = "API token for access to DigitalOcean (generate in API->Tokens/Keys)"
}

variable "do_sshkey_name" {
    description = "Name of the SSH public key (as present in DigitalOcean) to add to the VM"
}

### Resource and provider definitions for DigitalOcean
provider "digitalocean" {
    token = var.do_token
}

data "digitalocean_ssh_key" "sshkey" {
    name = var.do_sshkey_name
}

resource "digitalocean_droplet" "vm" {
    image       = "ubuntu-16-04-x64"
    name        = "test-vm01"
    region      = "fra1"
    size        = "s-1vcpu-1gb"
    ssh_keys    = [data.digitalocean_ssh_key.sshkey.id]

    provisioner "remote-exec" {
        inline = [
            "sleep 5",
            "apt -q update",
            "apt install -y python3 software-properties-common",
            "apt-add-repository --yes --update ppa:ansible/ansible",
            "apt install -y ansible",
        ]

        connection {
            type    = "ssh"
            host    = self.ipv4_address
            user    = "root"
            agent   = "true"
        }
    }
}

### Output definitions for DigitalOcean resources
output "ip" {
    description = "Returns IP addresses assigned to newly created droplets"
    value       = digitalocean_droplet.vm.ipv4_address
}
