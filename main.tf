provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "ml_rg" {
  name     = "ml-resource-group"
  location = "East US"
}

resource "azurerm_kubernetes_cluster" "ml_aks" {
  name                = "ml-aks-cluster"
  location            = azurerm_resource_group.ml_rg.location
  resource_group_name = azurerm_resource_group.ml_rg.name
  dns_prefix          = "mlaks"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_container_registry" "ml_acr" {
  name                = "mlacrregistry"
  resource_group_name = azurerm_resource_group.ml_rg.name
  location            = azurerm_resource_group.ml_rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_machine_learning_workspace" "ml_workspace" {
  name                = "ml-workspace"
  location            = azurerm_resource_group.ml_rg.location
  resource_group_name = azurerm_resource_group.ml_rg.name
}

resource "azurerm_key_vault" "ml_kv" {
  name                        = "mlkeyvault"
  location                    = azurerm_resource_group.ml_rg.location
  resource_group_name         = azurerm_resource_group.ml_rg.name
  tenant_id                   = "REPLACE_WITH_YOUR_TENANT_ID"
  sku_name                    = "standard"
  soft_delete_enabled         = true
  purge_protection_enabled    = false
}
