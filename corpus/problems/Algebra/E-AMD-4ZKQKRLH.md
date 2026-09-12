---
schema: qual/card@1
id: E-AMD-4ZKQKRLH
kind: problem
title: A normal $p$-subgroup is contained in every Sylow $p$-subgroup
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
Show that any normal $p$-subgroup of a finite group $G$ is contained in every Sylow $p$-subgroup of $G$.
:::

::: {.solution}
Let \(N\trianglelefteq G\) be a normal \(p\)-subgroup and let \(P\in\Syl_p(G)\). Since \(N\trianglelefteq G\), the product \(NP\) is a subgroup of \(G\). Moreover,
\[
|NP|=\frac{|N||P|}{|N\cap P|}
\]
is a power of \(p\), so \(NP\) is a \(p\)-subgroup containing \(P\).

By maximality of the Sylow \(p\)-subgroup \(P\), we must have \(NP=P\). Therefore \(N\le P\). Since \(P\) was arbitrary, \(N\) is contained in every Sylow \(p\)-subgroup of \(G\).
:::
