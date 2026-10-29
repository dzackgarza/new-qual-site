---
schema: qual/card@1
id: P-LARQ14
kind: problem
title: Evaluation at $2$ identifies $\RR[x]/(x-2)$ with $\RR$
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the quotient by (x-2) with Lerman practice problem 14."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used evaluation at 2, the factor theorem and the first isomorphism theorem."
---

::: {.problem}
Prove that $\RR[x]/(x-2)\cong\RR$ as rings.
:::

::: {.solution}

::: pf

::: pf-step

Evaluation at $2$ has kernel $(x-2)$ and is surjective.

::: pf-proof

Define
$$
\Phi:\RR[x]\to\RR,
\qquad
\Phi(f)=f(2).
$$
Evaluation preserves addition and multiplication, so $\Phi$ is a ring homomorphism. It is surjective because every $c\in\RR$ is the image of the constant polynomial $c$.

By the factor theorem,
$$
f(2)=0
\quad\Longleftrightarrow\quad
(x-2)\mid f.
$$
Hence
$$
\ker\Phi=(x-2).
$$

:::

:::

::: pf-step

The first isomorphism theorem gives the desired ring isomorphism.

::: pf-proof

Since $\operatorname{im}\Phi=\RR$ and $\ker\Phi=(x-2)$,
$$
\RR[x]/(x-2)
=\RR[x]/\ker\Phi
\cong\operatorname{im}\Phi
=\RR.
$$

:::

:::

:::

:::
