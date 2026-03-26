output "bucket_id" {
  value = aws_s3_bucket.coldchain_bucket.id
}

output "bucket_arn" {
  value = aws_s3_bucket.coldchain_bucket.arn
}

output "alerts_table_arn" {
  value = aws_dynamodb_table.alerts_table.arn
}