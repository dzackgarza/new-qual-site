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

::: problem
Let $R$ be a commutative ring with unit, $M$ be an $R$-module and $I$ an ideal of $R$.
Suppose that $M_{\mathfrak{m}} = 0$ for all maximal ideals $\mathfrak{m}$ of $R$ that contain $I$.
Prove that $M = IM$.
:::

::: {.solution}
<1>1. Set \(N=M/IM\). It is enough to prove \(N=0\).
::: {.proof}
The equality \(N=0\) is equivalent to \(M=IM\).
:::

<1>2. If \(\mathfrak m\) is a maximal ideal containing \(I\), then \(N_{\mathfrak m}=0\).
::: {.proof}
Localization is exact, so
\[
N_{\mathfrak m}\cong M_{\mathfrak m}/I_{\mathfrak m}M_{\mathfrak m}.
\]
By hypothesis \(M_{\mathfrak m}=0\), hence the quotient is zero.
:::

<1>3. If \(\mathfrak m\) is a maximal ideal not containing \(I\), then \(N_{\mathfrak m}=0\).
::: {.proof}
Choose \(a\in I\setminus\mathfrak m\). Then \(a/1\) is a unit in \(R_{\mathfrak m}\), so \(I_{\mathfrak m}=R_{\mathfrak m}\). Therefore
\[
N_{\mathfrak m}\cong M_{\mathfrak m}/I_{\mathfrak m}M_{\mathfrak m}=0.
\]
:::

<1>4. Thus \(N_{\mathfrak m}=0\) for every maximal ideal \(\mathfrak m\) of \(R\).
::: {.proof}
Combine <1>2 and <1>3.
:::

<1>5. An \(R\)-module whose localization at every maximal ideal is zero must itself be zero.
::: {.proof}
Suppose \(0\neq n\in N\). Its annihilator \(\operatorname{Ann}*R(n)\) is a proper ideal, so it is contained in some maximal ideal \(\mathfrak m\). If \(n/1=0\) in \(N*{\mathfrak m}\), then there exists \(s\notin\mathfrak m\) with \(sn=0\). This puts \(s\in\operatorname{Ann}*R(n)\subseteq\mathfrak m\), a contradiction.
Hence \(N*{\mathfrak m}\neq0\), contrary to <1>4.
:::

<1>6. Consequently \(N=0\), and therefore \(M=IM\).
::: {.proof}
Apply <1>5 to <1>4, then use <1>1.
:::
:::
