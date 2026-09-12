# Grades for Hard Proof Eval — Koebe–Bieberbach (E-SS3.PR-1) — Run 20260912T085503Z (per-model max, no timeout)

Rubric: `RUBRIC.md` (100 points: (a)5 + (b)5 + (c)20 + (d)15 + (e)20 + (f)15 + (g)10 + overall10). Graded blind.

Problem ID: `E-SS3.PR-1`
Run: `20260912T085503Z` per-model `max_completion_tokens` saturated, `timeout None`, 17 free non-BYOK non-safety, 13 success, 4 fail.

| Model | Provider | Max tokens | Problem ID | Score /100 | Notes |
| --- | --- | --- | --- | --- | --- |
| `cohere/north-mini-code:free` | `cohere` | 64000 | `E-SS3.PR-1` | 62 | Full solution now present (3369 content + 184895 reasoning) with (a)–(g) proofs; (a)5 (b)5 (c)8 area formula stated without full Green derivation (d)12 ψ existence ok (e)14 bound correct but equality hand-waved (f)9 (g)7 overall 2 — truncated previously at 6000, now complete but still gaps in (c) |
| `dots-studio/dots-3-note-preview:free` | `dots-studio` | 460800 | `E-SS3.PR-1` | 0 | Provider error 400 `bad request` on `tools` array (AtlasCloud); no solution |
| `inclusionai/ling-3.0-flash-fin:free` | `inclusionai` | 32768 | `E-SS3.PR-1` | 58 | Full solution with 78720 reasoning, 0 content? Actually content 0 but reasoning contains proofs for (a)–(g) with area theorem via `H(w)=h(1/w)`; (a)5 (b)5 (c)10 derivation via `H(w)` but still hand-waves Jordan curve (d)12 (e)12 (f)8 (g)6 overall 0 — COT only, no final content, but reasoning is now present and substantial |
| `inclusionai/ling-3.0-flash-sante:free` | `inclusionai` | 32768 | `E-SS3.PR-1` | 62 | 8085 content + 53471 reasoning, substantial proofs for all parts, similar gaps as fin but with content present |
| `inclusionai/ling-3.0-flash-vl:free` | `inclusionai` | 32768 | `E-SS3.PR-1` | 62 | 8596 content + 35514 reasoning, similar to sante |
| `liquid/lfm-2.5-2.6b:free` | `liquid` | 8192 | `E-SS3.PR-1` | 15 | 0 content + 26142 reasoning, only COT, minimal proof fragments for (a)(b) only |
| `nex-agi/nex-n2.5-mini:free` | `nex-agi` | 235929 | `E-SS3.PR-1` | 60 | 9822 content + 52978 reasoning, full (a)–(g) with correct area via `H(w)` and `g` construction, but (f) coefficient arithmetic still off |
| `nex-agi/nex-n2.5-pro:free` | `nex-agi` | 235929 | `E-SS3.PR-1` | 60 | 9346 content + 40609 reasoning, same as mini |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | `nvidia` | 65536 | `E-SS3.PR-1` | 45 | 8062 content + 27531 reasoning, has (a)–(d) correct, (c) area formula asserted, (e)–(g) incomplete |
| `nvidia/nemotron-3-super-120b-a12b:free` | `nvidia` | 235929 | `E-SS3.PR-1` | 55 | 10162 content + 16264 reasoning, substantial but (c) derivation still hand-waved, (f) not fully proved |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | `nvidia` | 65536 | `E-SS3.PR-1` | 58 | 7592 content + 24209 reasoning, similar to super, (a)(b)(d) correct, (c) 8, (e)12 |
| `nvidia/nemotron-3.5-lightning:free` | `nvidia` | 65536 | `E-SS3.PR-1` | 10 | 0 content + 103519 reasoning, only COT, no final solution (content null) |
| `openrouter/free` | `openrouter` | None | `E-SS3.PR-1` | 55 | 7173 content + 56587 reasoning, full (a)–(g) with area theorem via `H(w)`, but equality case hand-waved |
| `poolside/laguna-s-2.1:free` | `poolside` | 32768 | `E-SS3.PR-1` | 70 | 29349 content, no reasoning (0), substantial proofs for all parts, best of this run, (c) still stated without full Green derivation but better than 071746Z run |
| `poolside/laguna-xs-2.1:free` | `poolside` | 32768 | `E-SS3.PR-1` | 0 | Provider error 429 rate-limited upstream (Poolside); no solution |
| `thinkingmachines/inkling-small:free` | `thinkingmachines` | 262144 | `E-SS3.PR-1` | 0 | 403 harness-only |
| `thinkingmachines/inkling:free` | `thinkingmachines` | 262144 | `E-SS3.PR-1` | 0 | 403 harness-only |

*Run 085503Z graded. Compared to 071746Z (max 68), per-model saturation raised most 0s to 55–62 where content now present, but 4 still fail at provider and 1 truncated only COT.*
