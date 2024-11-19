provider "yandex" {
  token     = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

resource "yandex_compute_instance" "vm" {
  name = "terraform-vm"

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = "fd8q3ijh4lvqlh44tj6r"
    }
  }

  network_interface {
    subnet_id = var.subnet_id
    nat       = true
  }
}