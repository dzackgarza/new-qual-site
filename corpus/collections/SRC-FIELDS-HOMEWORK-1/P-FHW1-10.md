---
schema: qual/card@1
id: P-FHW1-10
kind: problem
title: A cubic whose splitting field has degree $3$ has three real roots
classification:
  areas: [algebra]
  topics: [Splitting Fields, Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $K\supset\QQ$ be a splitting field of a cubic polynomial $f(x)\in\QQ[x]$. Show that if $[K:\QQ]=3$, then $f(x)$ has $3$ real roots.
:::

::: {.solution}
The extension $K/\QQ$ is a splitting field in characteristic zero, so it is Galois and $|\Gal(K/\QQ)|=[K:\QQ]=3$; a splitting field over $\QQ$ is moreover stable under every automorphism of $\CC$.

::: pf

::: {.pf-step #conjugation}
Complex conjugation restricts to a $\QQ$-automorphism of $K$.

::: pf-proof
Conjugation $\sigma\colon\CC\to\CC$ fixes $\QQ$ and carries a root of $f$ to a root of $f$, since it fixes the coefficients of $f$.
The field $K$ is generated over $\QQ$ by the roots of $f$, so $\sigma(K)=K$, and $\sigma|_K$ is a $\QQ$-automorphism of $K$.
:::

:::

::: {.pf-step #has-three-real-roots}
$f$ has three real roots.

::: pf-proof
Suppose $f$ has a nonreal root $\omega$. Then $\sigma(\omega)=\overline{\omega}\ne\omega$, so the restriction $\sigma|_K$ is not the identity, and the subgroup it generates in $\Gal(K/\QQ)$ has order $2$.
By Lagrange's theorem $2$ divides $|\Gal(K/\QQ)|=3$, which is false.
Hence every root of $f$ is real, and a cubic has three roots counted with multiplicity.
:::

:::

:::

:::
