# Importations nécessaires
import streamlit as st
import os

# Fonction principale pour l'exécution de Streamlit
def main():
    st.title("Générateur de template multicloud Terraform")
    
    # Sélection du cloud provider
    cloud_provider = st.selectbox(
        "Sélectionnez votre cloud provider:",
        ["AWS", "Azure", "Google Cloud", "DigitalOcean"]
    )
    
    # Configuration de base en fonction du cloud provider
    if cloud_provider == "AWS":
        st.write("Configuration pour AWS:")
        region = st.text_input("Région AWS:", "us-west-1")
        instance_type = st.text_input("Type d'instance EC2:", "t2.micro")
    elif cloud_provider == "Azure":
        st.write("Configuration pour Azure:")
        location = st.text_input("Location Azure:", "westus")
        vm_size = st.text_input("Taille de la VM:", "Standard_DS1_v2")
    elif cloud_provider == "Google Cloud":
        st.write("Configuration pour Google Cloud:")
        zone = st.text_input("Zone GCP:", "us-west1-a")
        machine_type = st.text_input("Type de machine:", "n1-standard-1")
    elif cloud_provider == "DigitalOcean":
        st.write("Configuration pour DigitalOcean:")
        droplet_region = st.text_input("Région du Droplet:", "nyc1")
        droplet_size = st.text_input("Taille du Droplet:", "s-1vcpu-1gb")
    
    # Bouton pour générer le template Terraform
    if st.button("Générer le template Terraform"):
        if cloud_provider == "AWS":
            st.code(f"""
provider "aws" {{
  region = "{region}"
}}

resource "aws_instance" "example" {{
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "{instance_type}"
}}
            """)
        elif cloud_provider == "Azure":
            st.code(f"""
provider "azurerm" {{
  features {{}}
}}

resource "azurerm_virtual_machine" "example" {{
  name                  = "myVM"
  location              = "{location}"
  resource_group_name   = "myResourceGroup"
  vm_size               = "{vm_size}"
  # ... d'autres configurations ...
}}
            """)
        elif cloud_provider == "Google Cloud":
            st.code(f"""
provider "google" {{
  project = "my-project-id"
  zone    = "{zone}"
}}

resource "google_compute_instance" "default" {{
  name         = "my-instance"
  machine_type = "{machine_type}"
  # ... d'autres configurations ...
}}
            """)
        elif cloud_provider == "DigitalOcean":
            st.code(f"""
provider "digitalocean" {{
  token = "YOUR_DO_TOKEN"
}}

resource "digitalocean_droplet" "web" {{
  name   = "my-droplet"
  size   = "{droplet_size}"
  image  = "ubuntu-20-04-x64"
  region = "{droplet_region}"
}}
            """)

if __name__ == "__main__":
    main()
