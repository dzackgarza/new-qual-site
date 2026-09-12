# Eval: google/gemma-4-26b-a4b-it:free

- Run timestamp (UTC): 20260912T071746Z
- Model timestamp (UTC): 20260912T072126Z
- Model: `google/gemma-4-26b-a4b-it:free`
- Provider: `google`
- Success: False
- Problem source: `HARD-PROOF-EVAL.md` verbatim (Koebe-Bieberbach)
- Prompt length: 8778 chars

---

## Error

```
HTTP 400: {"error":{"message":"Provider returned error","code":400,"metadata":{"raw":"{\n  \"error\": {\n    \"code\": 400,\n    \"message\": \"API key not valid. Please pass a valid API key.\",\n    \"status\": \"INVALID_ARGUMENT\",\n    \"details\": [\n      {\n        \"@type\": \"type.googleapis.com/google.rpc.ErrorInfo\",\n        \"reason\": \"API_KEY_INVALID\",\n        \"domain\": \"googleapis.com\",\n        \"metadata\": {\n          \"service\": \"generativelanguage.googleapis.com\"\n        }\n      },\n      {\n        \"@type\": \"type.googleapis.com/google.rpc.LocalizedMessage\",\n        \"locale\": \"en-US\",\n        \"message\": \"API key not valid. Please pass a valid API key.\"\n      }\n    ]\n  }\n}\n","provider_name":"Google AI Studio","is_byok":true,"provider_error_code":"400"}},"user_id":"user_2ywXSS9JCSz9EpQ8XNlg9GKBC0L"}
```
