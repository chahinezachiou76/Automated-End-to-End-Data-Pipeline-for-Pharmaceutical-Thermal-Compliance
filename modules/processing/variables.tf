variable "bucket_arn" {
  description = "L'ARN du bucket S3 pour les notifications"
  type        = string
}

variable "bucket_name" {
  description = "Le nom du bucket S3"
  type        = string
}

variable "dynamodb_table_arn" {
  description = "L'ARN de la table DynamoDB pour les alertes"
  type        = string
}