---
schema: qual/card@1
id: P-BKS08-6A
kind: problem
title: A finite group with one automorphism has order at most two
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the reduction from trivial inner automorphisms to an
    elementary abelian 2-group and the nontrivial coordinate-swap automorphism
    in dimension at least two.
---

::: {.problem}
Suppose $G$ is a finite group with only one automorphism.
Show that
$$
|G|\le2.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #g-abelian}
The group $G$ is abelian.

::: pf-proof
For every $g\in G$, conjugation
$$
c_g(h)=ghg^{-1}
$$
is an automorphism of $G$. Since $G$ has only one automorphism and the
identity map is an automorphism, every $c_g$ must be the identity.
Thus every $g$ commutes with every $h$, so $G$ is abelian.
:::

:::

::: {.pf-step #elements-order-two}
Every element of $G$ has order dividing $2$.

::: pf-proof
By step [](#g-abelian){.pf-ref}, inversion
$$
\iota(g)=g^{-1}
$$
is an automorphism of $G$. It must therefore be the identity
automorphism. Hence $g=g^{-1}$ for every $g\in G$, so $g^2=e$.
:::

:::

::: {.pf-step #g-elementary-abelian}
The group $G$ is isomorphic to $(\ZZ/2\ZZ)^r$ for some
integer $r\ge0$.

::: pf-proof
Step [](#g-abelian){.pf-ref} makes $G$ abelian, and step [](#elements-order-two){.pf-ref} says every element is
annihilated by $2$. Therefore $G$ is a finite-dimensional vector space
over $\FF_2$, hence has the displayed form.
:::

:::

::: {.pf-step #r-at-most-one}
One has $r\le1$.

::: pf-proof
If $r\ge2$, choose a basis $e_1,\ldots,e_r$ of the
$\FF_2$-vector space $G$. The linear map exchanging $e_1$ and $e_2$
and fixing all other basis vectors is a nonidentity automorphism of
$G$, contradicting the hypothesis. Thus $r\le1$.
:::

:::

::: {.pf-step #order-bound}
Therefore
$$
\boxed{\abs{G}\le2}.
$$

::: pf-proof
By steps [](#g-elementary-abelian){.pf-ref} and [](#r-at-most-one){.pf-ref},
$$
\abs{G}=2^r
$$
with $r\le1$, so $\abs{G}\le2$.
:::

:::

::: pf-qed
Step [](#order-bound){.pf-ref} is the required conclusion.
:::

:::

:::
