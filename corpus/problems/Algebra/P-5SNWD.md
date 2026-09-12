---
schema: qual/card@1
id: P-5SNWD
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $G$ be a group, and let $H \le K \le G$ be subgroups.
Prove that if $H$ is a characteristic subgroup of $K$ ($H \operatorname{char} K$) and $K$ is a characteristic subgroup of $G$ ($K \operatorname{char} G$), then $H$ is a characteristic subgroup of $G$ ($H \operatorname{char} G$).
:::

::: solution
Let $\varphi\in\operatorname{Aut}(G)$. Since $K\operatorname{char}G$,
\[
\varphi(K)=K.
\]
Therefore the restriction
\[
\varphi|_K:K\to K
\]
is an automorphism of $K$. Since $H\operatorname{char}K$, this restriction preserves $H$:
\[
\varphi(H)=(\varphi|_K)(H)=H.
\]
Because this holds for every automorphism $\varphi$ of $G$, we have
\[
H\operatorname{char}G.
\]
Thus characteristicity is transitive.
:::
