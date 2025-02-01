# Call the server using curl:
# curl -X POST "http://localhost:8000/v1/chat/completions" \
#     -H "Content-Type: application/json" \
#     --data "{
#         "model": "deepseek-ai/DeepSeek-R1",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "$@?"
#             }
#         ]
#     }"
curl -X POST "http://localhost:5000/generate" \
    -H "Content-Type: application/json" \
    --data "{
        \"input\": \"$@?\"
    }"