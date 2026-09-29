---
schema: qual/card@1
id: P-ALGS16I
kind: problem
title: Local vanishing at maximals over $I$ implies $M = IM$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Modules
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
Let $R$ be a commutative ring with unit, $M$ be an $R$-module and $I$ an ideal of $R$.
Suppose that $M_{\mathfrak{m}} = 0$ for all maximal ideals $\mathfrak{m}$ of $R$ that contain $I$.
Prove that $M = IM$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Set \(N=M/IM\). It is enough to prove \(N=0\).

::: pf-proof
The equality \(N=0\) is equivalent to \(M=IM\).
:::

:::

::: {.pf-step #s2}
If \(\mathfrak m\) is a maximal ideal containing \(I\), then \(N_{\mathfrak m}=0\).

::: pf-proof
Localization is exact, so
\[
N_{\mathfrak m}\cong M_{\mathfrak m}/I_{\mathfrak m}M_{\mathfrak m}.
\]
By hypothesis \(M_{\mathfrak m}=0\), hence the quotient is zero.
:::

:::

::: {.pf-step #s3}
If \(\mathfrak m\) is a maximal ideal not containing \(I\), then \(N_{\mathfrak m}=0\).

::: pf-proof
Choose \(a\in I\setminus\mathfrak m\). Then \(a/1\) is a unit in \(R_{\mathfrak m}\), so \(I_{\mathfrak m}=R_{\mathfrak m}\). Therefore
\[
N_{\mathfrak m}\cong M_{\mathfrak m}/I_{\mathfrak m}M_{\mathfrak m}=0.
\]
:::

:::

::: {.pf-step #s4}
Thus \(N_{\mathfrak m}=0\) for every maximal ideal \(\mathfrak m\) of \(R\).

::: pf-proof
Combine step [](#s2){.pf-ref} and step [](#s3){.pf-ref}.
:::

:::

::: {.pf-step #s5}
An \(R\)-module whose localization at every maximal ideal is zero must itself be zero.

::: pf-proof
Suppose \(0\neq n\in N\). Its annihilator \(\operatorname{Ann}*R(n)\) is a proper ideal, so it is contained in some maximal ideal \(\mathfrak m\). If \(n/1=0\) in \(N*{\mathfrak m}\), then there exists \(s\notin\mathfrak m\) with \(sn=0\). This puts \(s\in\operatorname{Ann}*R(n)\subseteq\mathfrak m\), a contradiction.
Hence \(N*{\mathfrak m}\neq0\), contrary to step [](#s4){.pf-ref}.
:::

:::

::: pf-step
Consequently \(N=0\), and therefore \(M=IM\).

::: pf-proof
Apply step [](#s5){.pf-ref} to step [](#s4){.pf-ref}, then use step [](#s1){.pf-ref}.
:::

:::

:::
:::
