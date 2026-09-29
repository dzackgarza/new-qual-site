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

::: {.problem}
Suppose $G$ is a finite group, $N \trianglelefteq G$ and $P$ is a Sylow $p$-subgroup of $N$.
Prove that $N_G(P) \cdot N = G$.
:::

::: {.solution}

::: pf

::: pf-step

Fix \(g\in G\). Since \(N\trianglelefteq G\), the conjugate \(gPg^{-1}\) is a subgroup of \(N\).

::: pf-proof

Because \(P\le N\) and \(gNg^{-1}=N\), one has \(gPg^{-1}\le gNg^{-1}=N\).

:::

:::

::: {.pf-step #s2}

The subgroup \(gPg^{-1}\) is a Sylow \(p\)-subgroup of \(N\).

::: pf-proof

Conjugation preserves order, so \(|gPg^{-1}|=|P|\). Since \(P\) has the largest possible \(p\)-power order among subgroups of \(N\), the same is true of \(gPg^{-1}\).

:::

:::

::: {.pf-step #s3}

There exists \(n\in N\) such that
\[
n(gPg^{-1})n^{-1}=P.
\]

::: pf-proof

By step [](#s2){.pf-ref}, \(P\) and \(gPg^{-1}\) are Sylow \(p\)-subgroups of the finite group \(N\). Sylow conjugacy inside \(N\) gives such an element \(n\in N\).

:::

:::

::: {.pf-step #s4}

The element \(ng\) lies in \(N_G(P)\).

::: pf-proof

By step [](#s3){.pf-ref},
\[
(ng)P(ng)^{-1}=n(gPg^{-1})n^{-1}=P.
\]
Thus \(ng\) normalizes \(P\).

:::

:::

::: pf-step

Hence \(G=N_G(P)N\).

::: pf-proof

From step [](#s4){.pf-ref}, \(g=n^{-1}(ng)\in N N_G(P)\). Since \(N\trianglelefteq G\), one has \(N N_G(P)=N_G(P)N\). Thus every \(g\in G\) belongs to \(N_G(P)N\). The reverse inclusion is automatic.

:::

:::

:::

:::
