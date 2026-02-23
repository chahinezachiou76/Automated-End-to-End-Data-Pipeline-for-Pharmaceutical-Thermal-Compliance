module "my_storage" {
  source = "./modules/storage"
}

module "my_streaming" {
  source        = "./modules/streaming"
  target_s3_arn = module.my_storage.bucket_arn  
}

module "my_processing" {
  source             = "./modules/processing"
  bucket_arn         = module.my_storage.bucket_arn
  bucket_name        = module.my_storage.bucket_id
  dynamodb_table_arn = module.my_storage.alerts_table_arn
}

module "my_analytics" {
  source     = "./modules/analytics"
  bucket_id  = module.my_storage.bucket_id
  bucket_arn = module.my_storage.bucket_arn
}