---
schema: qual/card@1
id: P-ECG25
kind: problem
title: $F(\alpha)/F$ is finite iff $\alpha$ is algebraic over $F$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Show that $\alpha/F$ is algebraic $\iff F(\alpha)/F$ is a finite extension.
:::


::: {.solution}
<1>1. If $\alpha$ is algebraic over $F$, then $F(\alpha)/F$ is finite.
::: {.proof}
Let $m_\alpha(x)\in F[x]$ be the minimal polynomial of $\alpha$, of degree $n$. Evaluation induces an isomorphism
\[
F[x]/(m_\alpha)\xrightarrow{\sim}F(\alpha).
\]
Hence
\[
1,\alpha,\dots,\alpha^{n-1}
\]
is an $F$-basis of $F(\alpha)$, so $[F(\alpha):F]=n<\infty$.
:::

<1>2. If $F(\alpha)/F$ is finite, then $\alpha$ is algebraic over $F$.
::: {.proof}
If $[F(\alpha):F]=n$, then the $n+1$ vectors
\[
1,\alpha,\dots,\alpha^n
\]
are linearly dependent over $F$. Thus there exist coefficients, not all zero, such that
\[
c_0+c_1\alpha+\cdots+c_n\alpha^n=0.
\]
Therefore $\alpha$ is a root of a nonzero polynomial in $F[x]$, so it is algebraic.
:::

Hence
\[
\alpha/F\text{ is algebraic}
\iff
[F(\alpha):F]<\infty.
\]
:::
