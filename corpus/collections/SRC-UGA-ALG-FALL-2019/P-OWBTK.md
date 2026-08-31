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

::: problem
Let $R$ be a ring (not assumed to have an identity) with the property that $x^2 = x$ for all $x \in R$ (a Boolean ring).

(a) Prove that $2x = 0$ for all $x \in R$ (that is, $R$ has characteristic 2).

(b) Prove that $R$ is commutative.
:::

::: solution
**Goal:** Prove that every Boolean ring has characteristic 2 in (a) and is commutative in (b) by evaluating the idempotent property on sums.

<1>1. Part (a): $2x = 0$ for all $x \in R$.
::: {.proof}
    <2>1. Let $x \in R$. By hypothesis, $x + x \in R$ satisfies the idempotent property $(x + x)^2 = x + x$.
    <2>2. Expand the left-hand side using the distributive laws of ring arithmetic:
    $$(x + x)^2 = (x + x)(x + x) = x^2 + x^2 + x^2 + x^2.$$
    <2>3. Since $x^2 = x$, the expansion simplifies to:
    $$(x + x)^2 = x + x + x + x = 4x.$$
    <2>4. Equating the two expressions gives
    $$4x = 2x.$$
    <2>5. Subtracting $2x$ from both sides in the abelian group $(R, +)$ yields
    $$2x = 0 \quad \text{for all } x \in R.$$
    <2>6. In particular, $x = -x$ for all $x \in R$.

:::

<1>2. Part (b): $R$ is commutative ($x y = y x$ for all $x, y \in R$).
::: {.proof}
    <2>1. Let $x, y \in R$. By hypothesis, the element $x + y \in R$ satisfies $(x + y)^2 = x + y$.
    <2>2. Expand the left-hand side using distributivity:
    $$(x + y)^2 = x^2 + x y + y x + y^2 = x + x y + y x + y.$$
    <2>3. Equating this to $x + y$ gives
    $$x + x y + y x + y = x + y.$$
    <2>4. Subtracting $x + y$ from both sides yields
    $$x y + y x = 0.$$
    <2>5. Rearranging gives $x y = -y x$.
    <2>6. By Part (a), $-z = z$ for every $z \in R$. Applying this to $z = y x$ gives
    $$x y = y x.$$
    <2>7. Since $x, y \in R$ were arbitrary, $R$ is commutative.

:::

<1>3. Conclusion:
::: {.proof}
    Every Boolean ring satisfies $2x = 0$ and $x y = y x$.
:::
:::
