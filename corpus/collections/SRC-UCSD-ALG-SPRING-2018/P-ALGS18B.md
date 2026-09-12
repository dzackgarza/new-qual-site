---
schema: qual/card@1
id: P-ALGS18B
kind: problem
title: "Normalizer of Sylow subgroup times normal subgroup equals the whole group"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $G$ is a finite group, $N \trianglelefteq G$ and $P$ is a Sylow $p$-subgroup of $N$.
Prove that $N_G(P) \cdot N = G$.
:::

::: {.solution}
<1>1. Fix \(g\in G\). Since \(N\trianglelefteq G\), the conjugate \(gPg^{-1}\) is a subgroup of \(N\).
::: {.proof}
Because \(P\le N\) and \(gNg^{-1}=N\), one has \(gPg^{-1}\le gNg^{-1}=N\).
:::

<1>2. The subgroup \(gPg^{-1}\) is a Sylow \(p\)-subgroup of \(N\).
::: {.proof}
Conjugation preserves order, so \(|gPg^{-1}|=|P|\). Since \(P\) has the largest possible \(p\)-power order among subgroups of \(N\), the same is true of \(gPg^{-1}\).
:::

<1>3. There exists \(n\in N\) such that
\[
n(gPg^{-1})n^{-1}=P.
\]
::: {.proof}
By <1>2, \(P\) and \(gPg^{-1}\) are Sylow \(p\)-subgroups of the finite group \(N\). Sylow conjugacy inside \(N\) gives such an element \(n\in N\).
:::

<1>4. The element \(ng\) lies in \(N_G(P)\).
::: {.proof}
By <1>3,
\[
(ng)P(ng)^{-1}=n(gPg^{-1})n^{-1}=P.
\]
Thus \(ng\) normalizes \(P\).
:::

<1>5. Hence \(G=N_G(P)N\).
::: {.proof}
From <1>4, \(g=n^{-1}(ng)\in N N_G(P)\). Since \(N\trianglelefteq G\), one has \(N N_G(P)=N_G(P)N\). Thus every \(g\in G\) belongs to \(N_G(P)N\). The reverse inclusion is automatic.
:::
:::
