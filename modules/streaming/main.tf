resource "aws_kinesis_firehose_delivery_stream" "vaccine_firehose" {
  name        = "coldchain-vaccine-firehose"
  destination = "extended_s3"

  extended_s3_configuration {
    role_arn   = aws_iam_role.firehose_role.arn
    bucket_arn = var.target_s3_arn

    buffering_size     = 1  # 1 MB
    buffering_interval = 60 # 60 ثانية
  }
}

resource "aws_iam_role" "firehose_role" {
  name = "sanofi_firehose_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "firehose.amazonaws.com" }
    }]
  })
}