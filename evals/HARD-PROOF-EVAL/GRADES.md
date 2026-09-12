# Grades for Hard Proof Eval — Koebe–Bieberbach (E-SS3.PR-1)

Rubric: `RUBRIC.md` (100 points: (a)5 + (b)5 + (c)20 + (d)15 + (e)20 + (f)15 + (g)10 + overall10). Graded blind to model name per file, one row at a time.

Problem ID: `E-SS3.PR-1` (Koebe–Bieberbach radius theorem, `HARD-PROOF-EVAL.md` verbatim).
Run: `20260912T071746Z` (UTC) — 17 live free OpenRouter models (BYOK and safety excluded), 13 success, 2 fail (harness gate).
4 BYOK models (`gemma-4-26b-a4b-it:free`, `gemma-4-31b-it:free`, `lyria-3-clip-preview`, `lyria-3-pro-preview`) are not free (require `is_byok:true`) and 1 safety model (`nemotron-3.5-content-safety:free`) is a classifier, not a generative model; both were not tested per correction.

| Model | Provider | Datetimestamp (UTC) | Problem ID | Score /100 | Notes |
| --- | --- | --- | --- | --- | --- |
| `cohere/north-mini-code:free` | `cohere` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | Hit max_tokens, no final solution (content null, only COT planning, truncated); no proof for (a)–(g) |
| `dots-studio/dots-3-note-preview:free` | `dots-studio` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT planning truncated |
| `inclusionai/ling-3.0-flash-fin:free` | `inclusionai` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT |
| `inclusionai/ling-3.0-flash-sante:free` | `inclusionai` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT |
| `inclusionai/ling-3.0-flash-vl:free` | `inclusionai` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT |
| `liquid/lfm-2.5-2.6b:free` | `liquid` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT (earlier 42 was based on COT, corrected to 0 per rubric which grades final proofs) |
| `nex-agi/nex-n2.5-mini:free` | `nex-agi` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT |
| `nex-agi/nex-n2.5-pro:free` | `nex-agi` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | `nvidia` | `20260912T071746Z` | `E-SS3.PR-1` | 5 | Minimal solution fragment `1/4 (a) Show...` only, truncated, no (c)–(g) proofs |
| `nvidia/nemotron-3-super-120b-a12b:free` | `nvidia` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content is planning `We need to produce...`, not proof) |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | `nvidia` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content is planning, truncated) |
| `nvidia/nemotron-3.5-lightning:free` | `nvidia` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (`Here's a thinking process:`), only COT |
| `openrouter/free` | `openrouter` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | No final solution (content null, max_tokens length); only COT |
| `poolside/laguna-s-2.1:free` | `poolside` | `20260912T071746Z` | `E-SS3.PR-1` | 68 | Substantial solution for (a)–(g) with proofs; (a)5 (b)5 (c)8 area formula stated without full derivation (d)12 ψ existence ok but oddness hand-waved (e)15 bound via 1/g but equality case hand-waved (f)10 second coeff arithmetic off by factor (g)8 incomplete sharpness, overall 5 — best of 22, but still major gaps in (c) |
| `poolside/laguna-xs-2.1:free` | `poolside` | `20260912T071746Z` | `E-SS3.PR-1` | 68 | Same as laguna-s, near-identical structure and gaps; 68/100 |
| `thinkingmachines/inkling-small:free` | `thinkingmachines` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | Provider error 403 harness-only `is only available on agentic harnesses`; no solution (raw probe) |
| `thinkingmachines/inkling:free` | `thinkingmachines` | `20260912T071746Z` | `E-SS3.PR-1` | 0 | Provider error 403 harness-only; no solution |

*All 17 free (non-BYOK, non-safety) graded, one row per commit loop completed.
Two models (laguna s/xs) produced full attempted proofs; 13 produced no final solution (truncated COT); 2 failed at provider (harness 403). 4 BYOK and 1 safety excluded as not relevant for agent harness.*
