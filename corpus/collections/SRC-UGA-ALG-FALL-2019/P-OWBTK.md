---
schema: qual/card@1
id: P-OWBTK
kind: problem
title: A ring of idempotents has characteristic $2$ and is commutative
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Characteristic
relations: []
review: draft
---

::: {.problem}
Let $R$ be a ring (not assumed to have an identity) with the property that $x^2 = x$ for all $x \in R$ (a Boolean ring).

(a) Prove that $2x = 0$ for all $x \in R$ (that is, $R$ has characteristic 2).

(b) Prove that $R$ is commutative.
:::

::: {.solution}
**Goal:** Prove that every Boolean ring has characteristic 2 in (a) and is commutative in (b) by evaluating the idempotent property on sums.

::: pf

::: pf-step
Part (a): $2x = 0$ for all $x \in R$.

::: pf-proof

::: pf-step
Let $x \in R$. By hypothesis, $x + x \in R$ satisfies the idempotent property $(x + x)^2 = x + x$.
:::

::: pf-step
Expand the left-hand side using the distributive laws of ring arithmetic:
$$(x + x)^2 = (x + x)(x + x) = x^2 + x^2 + x^2 + x^2.$$
:::

::: pf-step
Since $x^2 = x$, the expansion simplifies to:
$$(x + x)^2 = x + x + x + x = 4x.$$
:::

::: pf-step
Equating the two expressions gives
$$4x = 2x.$$
:::

::: pf-step
Subtracting $2x$ from both sides in the abelian group $(R, +)$ yields
$$2x = 0 \quad \text{for all } x \in R.$$
:::

::: pf-step
In particular, $x = -x$ for all $x \in R$.
:::

:::

:::

::: pf-step
Part (b): $R$ is commutative ($x y = y x$ for all $x, y \in R$).

::: pf-proof

::: pf-step
Let $x, y \in R$. By hypothesis, the element $x + y \in R$ satisfies $(x + y)^2 = x + y$.
:::

::: pf-step
Expand the left-hand side using distributivity:
$$(x + y)^2 = x^2 + x y + y x + y^2 = x + x y + y x + y.$$
:::

::: pf-step
Equating this to $x + y$ gives
$$x + x y + y x + y = x + y.$$
:::

::: pf-step
Subtracting $x + y$ from both sides yields
$$x y + y x = 0.$$
:::

::: pf-step
Rearranging gives $x y = -y x$.
:::

::: pf-step
By Part (a), $-z = z$ for every $z \in R$. Applying this to $z = y x$ gives
$$x y = y x.$$
:::

::: pf-step
Since $x, y \in R$ were arbitrary, $R$ is commutative.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
Every Boolean ring satisfies $2x = 0$ and $x y = y x$.
:::

:::

:::
:::
