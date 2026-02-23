resource "aws_s3_bucket" "coldchain_bucket" {
  bucket = "coldchain-vaccine-data-lake"
}

resource "aws_dynamodb_table" "alerts_table" {
  name         = "VaccineAlerts"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "BatchID"
  range_key    = "Timestamp"

  attribute {
    name = "BatchID"
    type = "S"
  }

  attribute {
    name = "Timestamp"
    type = "S"
  }
}