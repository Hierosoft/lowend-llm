# Define the parameters
$model = "deepseek-ai/DeepSeek-R1"
# $message = "$args?"
# ^ not working (blank)
# $message = ($args).join(' ')
$message = "$($args -join " ")"
Write-Host "query=$args?"
Write-Host "message=$message"
# Create the JSON body
# $body = @{
#     model = $model
#     messages = @(
#         @{
#             role = "user"
#             content = $message
#         }
#     )
# } | ConvertTo-Json | % { [System.Text.RegularExpressions.Regex]::Unescape($_) }
$body = @{
    input = $message
} | ConvertTo-Json | % { [System.Text.RegularExpressions.Regex]::Unescape($_) }

# Invoke-WebRequest -Uri "http://localhost:8000/v1/chat/completions" -Method Post -ContentType "application/json" -Body $body
Write-Output $body
Write-Output "Sending request..."
Invoke-WebRequest -Uri "http://localhost:5000/generate" -Method Post -ContentType "application/json" -Body $body
