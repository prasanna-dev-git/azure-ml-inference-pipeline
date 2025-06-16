output "resource_group_name" {
  value = azurerm_resource_group.ml_rg.name
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.ml_aks.name
}

output "acr_name" {
  value = azurerm_container_registry.ml_acr.name
}
