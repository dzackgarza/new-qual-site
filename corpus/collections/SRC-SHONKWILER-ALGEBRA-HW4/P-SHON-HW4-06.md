---
schema: qual/card@1
id: P-SHON-HW4-06
kind: problem
title: A group is isomorphic to its opposite group
classification:
  areas: [algebra]
  topics: []
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
\[
\mu^{\prime}(x,y)=\mu_G(y,x).
\]
Prove that $G^{\mathrm{op}}\cong G$.
:::

Define
\[
\phi:G\to G^{\mathrm{op}}
\]
by
\[
\boxed{
\phi(g)=g^{-1}}.
\]

::: pf

::: pf-step

The map \(\phi\) is well defined.


::: pf-proof

The groups \(G\) and \(G^{\mathrm{op}}\) have the same underlying set, and \(g^{-1}\in G\) for every \(g\in G\).

:::

:::

::: pf-step

Let \(\star\) denote multiplication in \(G^{\mathrm{op}}\). Then
\[
\boxed{
a\star b=ba}
\]
where the product on the right is taken in \(G\).


::: pf-proof

This is the definition of the opposite group.

:::

:::

::: pf-step

For \(x,y\in G\),
\[
\phi(xy)
=
(xy)^{-1}
=
y^{-1}x^{-1}.
\]


::: pf-proof

Use the inverse-of-a-product identity in \(G\).

:::

:::

::: pf-step

Also,
\[
\phi(x)\star\phi(y)
=
x^{-1}\star y^{-1}
=
y^{-1}x^{-1}.
\]


::: pf-proof

Apply the reversed multiplication from step <1>2.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\phi(xy)=\phi(x)\star\phi(y)}.
\]


::: pf-proof

Compare steps <1>3--<1>4.

:::

:::

::: pf-step

Hence \(\phi\) is a group homomorphism
\[
G\to G^{\mathrm{op}}.
\]


::: pf-proof

Step <1>5 is exactly the homomorphism condition.

:::

:::

::: pf-step

The map \(\phi\) is injective.


::: pf-proof

If
\[
\phi(x)=\phi(y),
\]
then
\[
x^{-1}=y^{-1}.
\]
Taking inverses gives
\[
x=y.
\]

:::

:::

::: pf-step

The map \(\phi\) is surjective.


::: pf-proof

Given \(z\in G^{\mathrm{op}}\), choose
\[
g=z^{-1}\in G.
\]
Then
\[
\phi(g)=g^{-1}=z.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
G\cong G^{\mathrm{op}}}.
\]


::: pf-proof

The map \(\phi\) is a bijective homomorphism by steps <1>6--<1>8.

:::

:::

::: pf-qed

Step <1>9 is the required isomorphism.

:::

:::
