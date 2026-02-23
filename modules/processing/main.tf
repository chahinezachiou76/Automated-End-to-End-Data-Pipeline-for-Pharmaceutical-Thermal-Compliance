# 1. تعريف الـ IAM Role (الهوية التي ستعمل بها اللامبدا)
resource "aws_iam_role" "lambda_coldchain_role" {
  name = "coldchain_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# 2. إعطاء الصلاحيات للامبدا (Policy)
resource "aws_iam_role_policy" "lambda_policy" {
  name = "coldchain_lambda_policy"
  role = aws_iam_role.lambda_coldchain_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:GetObject"]
        Effect   = "Allow"
        Resource = "${var.bucket_arn}/*"
      },
      {
        Action   = ["dynamodb:PutItem"]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  # path.root تعني المجلد الرئيسي للمشروع مباشرة
  source_file = "${path.root}/lambda/process_coldchain.py"
  output_path = "${path.root}/lambda/process_coldchain.zip"
}

# 4. إنشاء وظيفة اللامبدا (Lambda Function)
resource "aws_lambda_function" "coldchain_processor" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "ColdChainProcessor"
  role             = aws_iam_role.lambda_coldchain_role.arn # هنا كان الخطأ لأنه لم يجد الـ Role أعلاه
  handler          = "process_coldchain.lambda_handler"
  runtime          = "python3.9"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
}