---
schema: qual/card@1
id: E-9IP2I
kind: problem
title: Free products of finite cyclic groups determine their factors
classification:
  areas:
  - topology
  topics:
  - Free Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §69 Exercise 3, printed p. 425. The printed theorem reads "Let G = G_1 * G_1, where G_1 and G_2
    are cyclic of orders m and n", which is a misprint: the same sentence names two groups G_1 and G_2, and
    parts (a)--(c) are not statements about G_1 * G_1. Read from the page image of printed p. 425. The
    statement on the card reproduces the printed words and the solution names the misprint. Proof transcribed
    from "Solutions to exercises for Mathematics 205A", University of California, Riverside, Part 9 (Fall
    2014), §69 Exercise 3, the set's printed p. 4. Checked against Exercise 1 of §69 (printed p. 425) for (a)
    and Exercise 2 of §68 (printed p. 421), whose part (c) restricts the finite-order elements, for (b). The
    sheet's (b) takes m >= n by symmetry of the free product, which the card states.
---

::: {.exercise}

Prove the following.

Theorem.
Let $G = G_1 * G_1$, where $G_1$ and $G_2$ are cyclic of orders $m$ and $n$, respectively.
Then $m$ and $n$ are uniquely determined by $G$.

(a) Show $G/[G, G]$ has order $mn$.

(b) Determine the largest integer $k$ such that $G$ has an element of order $k$.
(See [[E-175IG]].)

(c) Prove the theorem.
:::

::: {.solution}

The printed product "$G_1 * G_1$" is a misprint for $G_1 * G_2$: the same sentence calls $G_1$ and $G_2$ cyclic of orders $m$ and $n$, and the theorem is false for $G_1*G_1$ with one group named twice. Everything below is for $G=G_1*G_2$ with $G_1\cong\ZZ/m\ZZ$ and $G_2\cong\ZZ/n\ZZ$. Since $G_1*G_2\cong G_2*G_1$, we may also assume $m\ge n$, and then $m\ge1$.

::: pf

::: pf-step

(a) $G/[G,G]$ has order $mn$.

::: pf-proof

By Exercise 1 of §69, $G/[G,G]\cong \ZZ/m\ZZ\oplus\ZZ/n\ZZ$, which has $mn$ elements.

:::

:::

::: pf-step

(b) The largest order of an element of $G$ is $\max(m,n)=m$.

::: pf-proof

By Exercise 2(c) of §68 (printed p. 421), every element of finite order in $G$ is conjugate to an element of finite order in $G_1$ or in $G_2$, hence has order dividing $m$ or dividing $n$, so at most $m$. A generator of $G_1$ has order $m$, so the bound is attained.

:::

:::

::: pf-step

(c) $m$ and $n$ are determined by $G$.

::: pf-proof

The group $G$ determines the integers $\abs{G/[G,G]}=mn$ by (a) and $\max(m,n)=m$ by (b), since an isomorphism carries commutator subgroups to commutator subgroups and preserves element orders. Hence $m$ is known, and $n=(mn)/m$ is known too. If $m=n$ the two determinations agree, and the pair $\theset{m,n}$ is recovered in every case.

:::

:::

::: pf-qed

Parts (a), (b) and (c) are steps 1--3, and the theorem follows from step 3.

:::

:::
:::
