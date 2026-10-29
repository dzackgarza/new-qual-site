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
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: "The source statement was the bullet item 'Show that $\\alpha/F$ is algebraic $\\iff F(\\alpha)/F$ is a finite extension.', which declared neither $F$ nor $\\alpha$; the extension $K/F$ containing $\\alpha$ is now stated."
---

::: {.problem}
Let $K/F$ be a field extension and let $\alpha\in K$.
Show that $\alpha$ is algebraic over $F$ if and only if $F(\alpha)/F$ is a finite extension.
:::

::: {.solution}

::: pf

::: pf-step

If $\alpha$ is algebraic over $F$, then $F(\alpha)/F$ is finite.

::: pf-proof

Let $m_\alpha(x)\in F[x]$ be the minimal polynomial of $\alpha$, of degree $n$. Evaluation induces an isomorphism
$$
F[x]/(m_\alpha)\xrightarrow{\sim}F(\alpha).
$$
Hence $1,\alpha,\ldots,\alpha^{n-1}$ is an $F$-basis of $F(\alpha)$, so $[F(\alpha):F]=n<\infty$.

:::

:::

::: pf-step

If $F(\alpha)/F$ is finite, then $\alpha$ is algebraic over $F$.

::: pf-proof

If $[F(\alpha):F]=n$, then the $n+1$ vectors $1,\alpha,\ldots,\alpha^n$ are linearly dependent over $F$. Thus there exist $c_0,\ldots,c_n\in F$, not all zero, such that
$$
c_0+c_1\alpha+\cdots+c_n\alpha^n=0.
$$
Therefore $\alpha$ is a root of a nonzero polynomial in $F[x]$, so it is algebraic.

:::

:::

:::

:::
