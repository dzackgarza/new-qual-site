---
schema: qual/card@1
id: P-IDMYK
kind: problem
title: Quotients of quadratic integer rings by nonzero prime ideals
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Number Theory
  - Commutative Algebra
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

::: {.problem}
Let $K=\QQ(\sqrt d)$ be a quadratic number field and let $\OO_K$ be its ring of integers.
What can you say about $\OO_K/\mathfrak p$ when $\mathfrak p\subset \OO_K$ is a nonzero prime ideal?
:::

::: {.solution}

::: pf

::: pf-step

Every nonzero prime ideal of $\OO_K$ is maximal.

::: pf-proof

The ring $\OO_K$ is a Dedekind domain. In a Dedekind domain every nonzero prime ideal is maximal. Hence $\OO_K/\mathfrak p$ is a field.

:::

:::

::: pf-step

The field $\OO_K/\mathfrak p$ is finite.

::: pf-proof

Because $\mathfrak p$ is nonzero, choose $0\ne\alpha\in\mathfrak p$. Since $\alpha$ is a nonzero algebraic integer, its norm satisfies
$$
N_{K/\QQ}(\alpha)\in\ZZ\setminus\{0\}.
$$
The principal ideal $(\alpha)$ has finite index in $\OO_K$, with
$$
\abs{\OO_K/(\alpha)}=\abs{N_{K/\QQ}(\alpha)}.
$$
Since $(\alpha)\subseteq\mathfrak p$, the quotient map
$$
\OO_K/(\alpha)\twoheadrightarrow\OO_K/\mathfrak p
$$
is surjective. Therefore $\OO_K/\mathfrak p$ is finite.

:::

:::

::: pf-step

$\OO_K/\mathfrak p$ is $\boxed{\text{a finite field isomorphic to } \FF_p \text{ or } \FF_{p^2}}$, where $p$ is the prime with $\mathfrak p\cap\ZZ=p\ZZ$.

::: pf-proof

The ideal $\mathfrak p\cap\ZZ$ is a prime ideal of $\ZZ$, and it is nonzero because it contains $N_{K/\QQ}(\alpha)=\alpha\overline\alpha$, where $\overline\alpha\in\OO_K$ is the Galois conjugate of $\alpha$. So $\mathfrak p\cap\ZZ=p\ZZ$ for a prime $p$, and $\OO_K/\mathfrak p$ is a field containing $\FF_p$.
Since $\OO_K\cong\ZZ^2$ as an abelian group, $\OO_K/p\OO_K$ has dimension $2$ over $\FF_p$, and $\OO_K/\mathfrak p$ is a quotient of it because $p\OO_K\subseteq\mathfrak p$. Hence $[\OO_K/\mathfrak p:\FF_p]\le2$.

:::

:::

:::

:::
