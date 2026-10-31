---
schema: qual/card@1
id: P-SHON-HW4-06
kind: problem
title: A group is isomorphic to its opposite group
classification:
  areas: [algebra]
  topics:
  - Opposite Group
  - Group Isomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 1 following exercise 3.5.10 in the retained Algebra HW 4 solution packet.
---

::: {.problem}
Let $G^{\mathrm{op}}$ be the group with the same underlying set as $G$ and multiplication
$$
\mu^{\prime}(x,y)=\mu_G(y,x).
$$
Prove that $G^{\mathrm{op}}\cong G$.
:::

::: {.solution}

Define
$$
\phi:G\to G^{\mathrm{op}}
$$
by
$$
\boxed{
\phi(g)=g^{-1}}.
$$

::: pf

::: pf-step

The map $\phi$ is well defined.


::: pf-proof

The groups $G$ and $G^{\mathrm{op}}$ have the same underlying set, and $g^{-1}\in G$ for every $g\in G$.

:::

:::

::: {.pf-step #s1-2}

Let $\star$ denote multiplication in $G^{\mathrm{op}}$. Then
$$
\boxed{
a\star b=ba}
$$
where the product on the right is taken in $G$.


::: pf-proof

This is the definition of the opposite group.

:::

:::

::: {.pf-step #s1-3}

For $x,y\in G$,
$$
\phi(xy)
=
(xy)^{-1}
=
y^{-1}x^{-1}.
$$


::: pf-proof

Use the inverse-of-a-product identity in $G$.

:::

:::

::: {.pf-step #s1-4}

Also,
$$
\phi(x)\star\phi(y)
=
x^{-1}\star y^{-1}
=
y^{-1}x^{-1}.
$$


::: pf-proof

Apply the reversed multiplication from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\phi(xy)=\phi(x)\star\phi(y)}.
$$


::: pf-proof

Compare steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Hence $\phi$ is a group homomorphism
$$
G\to G^{\mathrm{op}}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} is exactly the homomorphism condition.

:::

:::

::: {.pf-step #s1-7}

The map $\phi$ is injective.


::: pf-proof

If
$$
\phi(x)=\phi(y),
$$
then
$$
x^{-1}=y^{-1}.
$$
Taking inverses gives
$$
x=y.
$$

:::

:::

::: {.pf-step #s1-8}

The map $\phi$ is surjective.


::: pf-proof

Given $z\in G^{\mathrm{op}}$, choose
$$
g=z^{-1}\in G.
$$
Then
$$
\phi(g)=g^{-1}=z.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
G\cong G^{\mathrm{op}}}.
$$


::: pf-proof

The map $\phi$ is a bijective homomorphism by steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required isomorphism.

:::

:::

:::
