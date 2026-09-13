# Eval: poolside/laguna-xs-2.1:free

- Run timestamp (UTC): 20260912T085503Z
- Model timestamp (UTC): 20260912T095341Z
- Model: `poolside/laguna-xs-2.1:free`
- Provider: `poolside`
- Success: False
- Problem source: `HARD-PROOF-EVAL.md` verbatim (Koebe-Bieberbach)
- Prompt length: 8778 chars
- Max tokens: per-model saturated (32768), timeout: none

---

## Error

```
HTTP 429: {"error":{"message":"Provider returned error","code":429,"metadata":{"raw":"poolside/laguna-xs-2.1:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations","provider_name":"Poolside","is_byok":false,"limit_source":"upstream_provider_shared_pool","remedy_hint":"Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing"}},"user_id":"user_2ywXSS9JCSz9EpQ8XNlg9GKBC0L"}
```
