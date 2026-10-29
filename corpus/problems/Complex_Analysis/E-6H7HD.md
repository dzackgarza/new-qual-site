---
schema: qual/card@1
id: E-6H7HD
kind: problem
title: No continuous square root on $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}
Show that there is no continuous square root function defined on all of $\CC$.

:::

::: {.solution}
Suppose toward a contradiction that $f:\CC\to\CC$ is continuous with $f(z)^2=z$ for all $z$, and let $p:\units{\CC}\to\units{\CC}$ be the covering map $p(z)=z^2$.

::: pf

::: {.pf-step #section}
$f$ restricts to a continuous map $\units{\CC}\to\units{\CC}$ with $p\circ f=\id$.

::: pf-proof
For $z\neq0$, $f(z)^2=z\neq0$, so $f(z)\neq0$ and $p(f(z))=z$.
:::

:::

::: pf-step
This is impossible.

::: pf-proof
Identify $\pi_1(\units{\CC})$ with $\ZZ$ by the winding number about $0$.
Then $p_*$ is multiplication by $2$, and $f_*$ is multiplication by some $n\in\ZZ$.
By functoriality and step [](#section){.pf-ref}, $p_*\circ f_*=\id$, so $2n=1$, which has no solution in $\ZZ$.
:::

:::

:::

:::
