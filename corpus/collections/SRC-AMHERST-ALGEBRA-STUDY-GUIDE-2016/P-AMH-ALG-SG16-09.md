---
schema: qual/card@1
id: P-AMH-ALG-SG16-09
kind: problem
title: Homomorphisms from a group of order 144 to a group of order 25 are trivial
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
Let $G$ and $H$ be groups.
Recall that a homomorphism $\varphi:G\to H$ is said to be trivial if $\varphi(g)=e_H$ for all $g\in G$.
If $|G|=144$ and $|H|=25$, prove that any homomorphism $\varphi:G\to H$ is trivial.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
For every $g\in G$, the order of $\varphi(g)$ divides $144$.

::: pf-proof
By Lagrange's theorem in $G$,
$$
g^{144}=e_G.
$$
Applying the homomorphism $\varphi$ gives
$$
\varphi(g)^{144}
=\varphi(g^{144})
=\varphi(e_G)
=e_H.
$$
Hence
$$
\operatorname{ord}(\varphi(g))\mid144.
$$
:::

:::

::: {.pf-step #s1-2}
For every $g\in G$, the order of $\varphi(g)$ also divides $25$.

::: pf-proof
The element $\varphi(g)$ lies in the finite group $H$ of order $25$. Therefore Lagrange's theorem gives
$$
\operatorname{ord}(\varphi(g))\mid25.
$$
:::

:::

::: {.pf-step #s1-3}
Therefore $\varphi(g)=e_H$ for every $g\in G$.

::: pf-proof
By step [](#s1-1){.pf-ref} and step [](#s1-2){.pf-ref},
$$
\operatorname{ord}(\varphi(g))
\mid\gcd(144,25)=1.
$$
Thus
$$
\operatorname{ord}(\varphi(g))=1,
$$
so $\varphi(g)=e_H$.
:::

:::

::: pf-step
Hence
$$
\boxed{\varphi\text{ is trivial}}.
$$

::: pf-proof
Step [](#s1-3){.pf-ref} holds for arbitrary $g\in G$.
:::

:::

:::

:::
