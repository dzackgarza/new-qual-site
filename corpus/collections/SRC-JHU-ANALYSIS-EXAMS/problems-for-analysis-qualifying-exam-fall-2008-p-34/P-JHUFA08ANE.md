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

::: {.problem}
5) (10 points) How many solutions does the equation

$$
e ^ { z } = 3 z ^ { 7 }
$$

have in the unit disk $D = \{ x \in \mathbb { C } : | z | < 1 \} ?$ Justify your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

On $\abs z=1$, $\abs{e^z}<\abs{-3z^7}$.

::: pf-proof

$\abs{e^z}=e^{\Re z}\le e<3=\abs{-3z^7}$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref} and Rouché's theorem, $e^z-3z^7$ has as many zeros in $\abs z<1$ as $-3z^7$, counted with multiplicity, namely $\boxed{7}$. Counted without multiplicity the answer is the same: at a zero, $e^z=3z^7$ and the derivative $e^z-21z^6=3z^7-21z^6=3z^6(z-7)$ is nonzero for $0<\abs z<1$, and $z=0$ is not a zero.

:::

:::

:::
