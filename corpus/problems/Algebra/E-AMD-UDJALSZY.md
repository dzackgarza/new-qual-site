---
schema: qual/card@1
id: E-AMD-UDJALSZY
kind: problem
title: $C_H(x)=H\cap C_G(x)$ for $H\leq G$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
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

::: {.exercise}
Let $G$ be a group, $H\leq G$, and $x\in G$. Show that $C_H(x) = H \intersect C_G(x)$.
:::


::: {.solution}

::: pf

::: pf-step
$C_H(x)=H\cap C_G(x)$.

::: pf-proof
By definition,
$$
h\in C_H(x)
\quad\Longleftrightarrow\quad
h\in H\text{ and }hx=xh.
$$
Also,
$$
h\in C_G(x)\quad\Longleftrightarrow\quad h\in G\text{ and }hx=xh.
$$
Since $H\le G$, for $h\in H$ the condition $h\in C_G(x)$ is exactly $hx=xh$. Therefore $h\in C_H(x)$ if and only if $h\in H\cap C_G(x)$, and the two subsets have the same elements.
:::

:::

:::

:::
