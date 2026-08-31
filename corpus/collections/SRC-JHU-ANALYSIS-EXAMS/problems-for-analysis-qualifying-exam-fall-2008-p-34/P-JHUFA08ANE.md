---
schema: qual/card@1
id: P-JHUFA08ANE
kind: problem
title: "Counting solutions of e^z = 3z^7 in the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

5) (10 points) How many solutions does the equation

$$
e ^ { z } = 3 z ^ { 7 }
$$

have in the unit disk $D = \{ x \in \mathbb { C } : | z | < 1 \} ?$ Justify your answer.

::: {.solution}
<1>1. Rewrite as $e^z - 3z^7 = 0$; let $f(z) = -3z^7$ and $g(z) = e^z$.
::: {.proof}
setup for Rouché's theorem.
:::

<1>2. On $|z| = 1$, $|f(z)| = 3|z|^7 = 3$ and $|g(z)| = |e^z| = e^{\operatorname{Re} z} \le e < 3$.
::: {.proof}
$|e^z| = e^{\operatorname{Re} z} \le e^1 = e < 3$.
:::

<1>3. Hence $|g(z)| < |f(z)|$ on $|z| = 1$.
::: {.proof}
<1>2.
:::

<1>4. By Rouché's theorem, $f + g = e^z - 3z^7$ and $f = -3z^7$ have the same number of zeros in $|z| < 1$.
::: {.proof}
Rouché's theorem.
:::

<1>5. $-3z^7$ has $7$ zeros in $|z| < 1$ (the zero at $z = 0$ with multiplicity $7$).
::: {.proof}
$-3z^7 = 0$ iff $z = 0$, with multiplicity $7$.
:::

<1>6. Hence $e^z = 3z^7$ has $7$ solutions in the unit disk.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
