---
schema: qual/card@1
id: P-RI3ZA
kind: problem
title: Normality of field extensions is not transitive
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Counterexamples
relations: []
review: draft
---

::: problem
Give a tower $K\subset L\subset M$ such that $L/K$ and $M/L$ are normal, but $M/K$ is not normal.
:::

::: solution
Take
\[
\QQ\subset \QQ(\sqrt2)\subset \QQ(\sqrt[4]2).
\]
The extension $\QQ(\sqrt2)/\QQ$ is quadratic, hence normal. Also $\sqrt[4]2$ satisfies
\[
x^2-\sqrt2\in \QQ(\sqrt2)[x],
\]
so $\QQ(\sqrt[4]2)/\QQ(\sqrt2)$ is quadratic and therefore normal.

However, $\QQ(\sqrt[4]2)/\QQ$ is not normal. The minimal polynomial of $\sqrt[4]2$ over $\QQ$ is $x^4-2$, whose roots are
\[
\pm\sqrt[4]2,\qquad \pm i\sqrt[4]2.
\]
The field $\QQ(\sqrt[4]2)$ is contained in $\RR$, so it does not contain the nonreal roots. Hence $x^4-2$ does not split there, and the extension is not normal.
:::
