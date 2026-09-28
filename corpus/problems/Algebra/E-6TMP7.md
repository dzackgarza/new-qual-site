---
schema: qual/card@1
id: E-6TMP7
kind: problem
title: Galois group of $x^2-2$ is $\mathbb{Z}/2\mathbb{Z}$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
---

::: {.exercise}
Compute the Galois group of $x^2-2$.
:::

::: {.solution}
Over $\QQ$, the roots of $x^2-2$ are $\pm\sqrt2$, and $\sqrt2\notin\QQ$, so $x^2-2$ is irreducible and its splitting field is $\QQ(\sqrt2)$, of degree $2$ over $\QQ$.
A group of order $2$ is cyclic, so
$$\Gal(\QQ(\sqrt2)/\QQ)=\{\mathrm{id},\ \sqrt2\mapsto-\sqrt2\}\cong\boxed{\ZZ/2\ZZ}.$$
:::
