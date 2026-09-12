---
schema: qual/card@1
id: E-AMD-4M7MSCEI
kind: problem
title: $H\operatorname{char} K\operatorname{char} G$ implies $H\operatorname{char}
  G$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that $H \operatorname{char} K \operatorname{char} G \implies H \operatorname{char} G$.

> So "characteristic" is a transitive relation for subgroups.
:::

::: {.solution}
Let \(\phi\in\Aut(G)\). Since \(K\operatorname{char}G\),
\[
\phi(K)=K,
\]
so the restriction
\[
\phi|_K:K\longrightarrow K
\]
is an automorphism of \(K\). Since \(H\operatorname{char}K\), every automorphism of \(K\) preserves \(H\); hence
\[
\phi(H)=(\phi|_K)(H)=H.
\]
As this holds for every \(\phi\in\Aut(G)\), we have
\[
H\operatorname{char}G.
\]
Thus characteristicity is transitive.
:::
