---
schema: qual/card@1
id: E-AMD-3MQL7TPB
kind: problem
title: $O_p(G)$ is the unique maximal normal $p$-subgroup of $G$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
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
Let $O_p(G)$ be the intersection of all Sylow $p$-subgroups of $G$.
Show that $O_p(G) \normal G$, and that it is the unique maximal normal $p$-subgroup of $G$ (containing all other normal $p$-subgroups).
:::

::: {.solution}
Let
\[
O_p(G)=\bigcap_{P\in\Syl_p(G)}P.
\]

<1>1. The subgroup \(O_p(G)\) is normal in \(G\) and is a \(p\)-group.
::: {.proof}
Conjugation by any \(g\in G\) permutes the Sylow \(p\)-subgroups, so
\[
gO_p(G)g^{-1}
=\bigcap_{P\in\Syl_p(G)}gPg^{-1}
=O_p(G).
\]
Thus \(O_p(G)\trianglelefteq G\). Since it is contained in every Sylow \(p\)-subgroup, it is itself a \(p\)-group.
:::

<1>2. Every normal \(p\)-subgroup of \(G\) is contained in \(O_p(G)\).
::: {.proof}
Let \(N\trianglelefteq G\) be a \(p\)-subgroup. Choose a Sylow \(p\)-subgroup \(P\) with \(N\le P\). For every \(g\in G\), normality gives
\[
N=gNg^{-1}\le gPg^{-1}.
\]
Every Sylow \(p\)-subgroup is conjugate to \(P\), hence \(N\) lies in every Sylow \(p\)-subgroup. Therefore
\[
N\le\bigcap_{Q\in\Syl_p(G)}Q=O_p(G).
\]
:::

Thus \(O_p(G)\) is the unique largest normal \(p\)-subgroup of \(G\).
:::
