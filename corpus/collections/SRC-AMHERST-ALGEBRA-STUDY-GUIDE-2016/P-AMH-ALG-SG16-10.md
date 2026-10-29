---
schema: qual/card@1
id: P-AMH-ALG-SG16-10
kind: problem
title: Cosets of the preimage of a subgroup under a homomorphism
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(March 2015) Let $G_1,G_2$ be groups, let $H_2\subseteq G_2$ be a subgroup, and let $\varphi:G_1\to G_2$ be a homomorphism.
Define
$$
H_1=\{x\in G_1\mid \varphi(x)\in H_2\}.
$$
It is a fact, which you may assume, that $H_1$ is a subgroup of $G_1$.
Prove that for any $x,y\in G_1$, $H_1x=H_1y$ if and only if $H_2\varphi(x)=H_2\varphi(y)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
If $H_1x=H_1y$, then
$$
H_2\varphi(x)=H_2\varphi(y).
$$

::: pf-proof
By the right-coset criterion,
$$
H_1x=H_1y
\iff
xy^{-1}\in H_1.
$$
Thus
$$
\varphi(xy^{-1})\in H_2.
$$
Since $\varphi$ is a homomorphism,
$$
\varphi(xy^{-1})
=\varphi(x)\varphi(y)^{-1}.
$$
Hence
$$
\varphi(x)\varphi(y)^{-1}\in H_2,
$$
and another application of the right-coset criterion gives
$$
H_2\varphi(x)=H_2\varphi(y).
$$
:::

:::

::: {.pf-step #s1-2}
If
$$
H_2\varphi(x)=H_2\varphi(y),
$$
then $H_1x=H_1y$.

::: pf-proof
By the right-coset criterion,
$$
\varphi(x)\varphi(y)^{-1}\in H_2.
$$
Since
$$
\varphi(x)\varphi(y)^{-1}
=\varphi(xy^{-1}),
$$
the definition of $H_1$ gives
$$
xy^{-1}\in H_1.
$$
Therefore
$$
H_1x=H_1y.
$$
:::

:::

::: pf-step
Therefore
$$
\boxed{H_1x=H_1y\iff H_2\varphi(x)=H_2\varphi(y)}.
$$

::: pf-proof
Step [](#s1-1){.pf-ref} proves the forward implication and step [](#s1-2){.pf-ref} proves the reverse implication.
:::

:::

:::

:::
