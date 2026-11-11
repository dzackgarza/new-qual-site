---
schema: qual/card@1
id: E-UZY87
kind: problem
title: A conjugate of one free factor meets the other trivially
classification:
  areas:
  - topology
  topics:
  - Free Products
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §68 Exercise 3, printed p. 421. Proof transcribed from "Solutions to exercises for Mathematics
    205A", University of California, Riverside, Part 9 (Fall 2014), §68 Exercise 3, the set's printed p. 3,
    whose argument is the homomorphism theta to G_1 x G_2; the card writes the conjugate of theta(c) out in
    coordinates, which is the step the sheet leaves to an induction. Checked against the extension condition
    of Lemma 68.3 (printed p. 418), which produces theta, and Lemma 68.1 (printed p. 414).
---

::: {.exercise}

Let $G = G_1 * G_2$.
Given $c \in G$, let $cG_1c^{-1}$ denote the set of all elements of the form $cxc^{-1}$, for $x \in G_1$.
It is a subgroup of $G$; show that its intersection with $G_2$ consists of the identity alone.
:::

::: {.solution}

That $cG_1c^{-1}$ is a subgroup: it is the image of the subgroup $G_1$ under the automorphism $x\mapsto cxc^{-1}$ of $G$.

::: pf

::: pf-step

There is a homomorphism $\theta:G_1*G_2\to G_1\times G_2$ with $\theta(g_1)=(g_1,1)$ and $\theta(g_2)=(1,g_2)$.

::: pf-proof

The projections $G_i\hookrightarrow G_i$ followed by the inclusions into $G_1\times G_2$ are homomorphisms $G_i\to G_1\times G_2$, so the extension condition of Lemma 68.3 (printed p. 418) for the free product $G_1*G_2$ produces $\theta$.

:::

:::

::: pf-step

If $c\in G$ has $\theta(c)=(u,v)$ and $a\in G_1$, then $\theta(cac^{-1})=(uau^{-1},1)$.

::: pf-proof

Because $\theta$ is a homomorphism and $\theta(a)=(a,1)$,

$$
\theta(cac^{-1})=\theta(c)\theta(a)\theta(c)^{-1}=(u,v)(a,1)(u,v)^{-1}=(uau^{-1},vv^{-1})=(uau^{-1},1),
$$

the multiplication in $G_1\times G_2$ being coordinatewise.

:::

:::

::: pf-step

$cG_1c^{-1}\cap G_2=\theset{1}$.

::: pf-proof

Let $cac^{-1}\in G_2$ with $a\in G_1$. Then $\theta(cac^{-1})=(1,cac^{-1})$, so step 2 gives $(uau^{-1},1)=(1,cac^{-1})$ and $uau^{-1}=1$, hence $a=u^{-1}\cdot1\cdot u=1$ and $cac^{-1}=1$. So the only element of the intersection is the identity.

:::

:::

::: pf-qed

Steps 1--3 prove the assertion.

:::

:::
:::
