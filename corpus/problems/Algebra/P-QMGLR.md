---
schema: qual/card@1
id: P-QMGLR
kind: problem
title: $\alpha\pm\beta$ and $\alpha\beta^{\pm 1}$ are algebraic over $F$ whenever
  $\alpha$ and $\beta$ are
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $\alpha,\beta$ be algebraic over a field $F$. Prove that
$$
\alpha\pm\beta,
\qquad
\alpha\beta
$$
are algebraic over $F$, and if $\beta\ne0$, then so is
$$
\alpha\beta^{-1}.
$$
:::

::: {.solution}
::: pf

::: {.pf-step #finite}
$F(\alpha,\beta)/F$ is a finite extension.

::: pf-proof
Since $\alpha$ is algebraic over $F$, $[F(\alpha):F]<\infty$. Since $\beta$ is algebraic over $F$, it is algebraic over $F(\alpha)$, so $[F(\alpha,\beta):F(\alpha)]<\infty$. By the tower law, $[F(\alpha,\beta):F]<\infty$.
:::

:::

::: pf-step
$\alpha\pm\beta$, $\alpha\beta$, and, when $\beta\ne0$, $\alpha\beta^{-1}$ are algebraic over $F$.

::: pf-proof
All of these elements lie in the field $F(\alpha,\beta)$. Every element $\gamma$ of a finite extension $K/F$ is algebraic over $F$, because the powers $1,\gamma,\gamma^2,\ldots$ are linearly dependent over $F$. Step [](#finite){.pf-ref} applies with $K=F(\alpha,\beta)$.
:::

:::

:::
:::
