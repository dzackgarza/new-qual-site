---
schema: qual/card@1
id: P-FN7H4
kind: problem
title: Galois group of $x^2-2$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Irreducibility Criteria
  - Splitting Fields
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
What is the Galois group of $x^2 - 2$?
Why is $x^2 - 2$ irreducible?
:::


::: {.solution}
<1>1. The polynomial $x^2-2$ is irreducible over $\QQ$.
::: {.proof}
A reducible quadratic over $\QQ$ has a rational root. If $a/b$ in lowest terms satisfied $(a/b)^2=2$, then $a^2=2b^2$. Thus $a$ is even, say $a=2c$, giving $b^2=2c^2$, so $b$ is even, contradicting coprimality.
:::

<1>2. Its splitting field is $\QQ(\sqrt2)$.
::: {.proof}
The roots are $\pm\sqrt2$, both contained in $\QQ(\sqrt2)$, and irreducibility gives degree $2$.
:::

<1>3. Therefore
\[
\operatorname{Gal}(x^2-2/\QQ)\cong C_2.
\]
::: {.proof}
There are exactly two $\QQ$-automorphisms of the quadratic splitting field: the identity and conjugation $\sqrt2\mapsto-\sqrt2$.
:::
:::
