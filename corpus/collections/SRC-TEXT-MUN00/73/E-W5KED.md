---
schema: qual/card@1
id: E-W5KED
kind: problem
title: Spaces with prescribed finite abelian and free-product fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Products
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §73 Exercise 1, printed p. 445. Proof transcribed from Takumi Murayama, Selected Solutions to
    Munkres's Topology, 2nd Ed. (MAT365, Princeton, Fall 2012), §73 Exercise 1, which uses Theorem 60.1 for products and the wedge formula for free products. Checked
    against Theorem 73.4 (printed p. 444, the fundamental group of the n-fold dunce cap is cyclic of order n),
    Theorem 60.1 (printed p. 371, $\pi_1$ of a product) and Exercise 1 of §71 (printed p. 438), whose
    hypotheses are checked in step 1.
---

::: {.exercise}

Find spaces whose fundamental groups are isomorphic to the following groups.
(Here $\ZZ/n$ denotes the additive group of integers modulo $n$.)

(a) $\ZZ/n \times \ZZ/m$

(b) $\ZZ/n_1 \times \ZZ/n_2 \times \cdots \times \ZZ/n_k$

(c) $\ZZ/n * \ZZ/m$.
(See [[E-5DDIL]].)

(d) $\ZZ/n_1 * \ZZ/n_2 * \cdots * \ZZ/n_k$
:::

::: {.solution}

Write $D_n$ for the $n$-fold dunce cap, $n>1$ (defined on printed p. 443), a compact path-connected space with $\pi_1(D_n)\cong\ZZ/n$ by Theorem 73.4 (printed p. 444).

::: pf

::: pf-step

$\pi_1(D_n\times D_m)\cong\ZZ/n\times\ZZ/m$, and $\pi_1(D_n\vee D_m)\cong\ZZ/n*\ZZ/m$.

::: pf-proof

For the product, Theorem 60.1 (printed p. 371) gives $\pi_1(X\times Y,x_0\times y_0)\cong\pi_1(X,x_0)\times\pi_1(Y,y_0)$, so the fundamental group of $D_n\times D_m$ is $\ZZ/n\times\ZZ/m$. For the wedge, let $p$ be the common point. In $D_n$ the point $p$ is a deformation retract of an open neighbourhood: the dunce cap is a quotient of $B^2$ that identifies only points of $S^1$, so the image of the open ball of radius $1/2$ about the centre is an open set $W\subseteq D_n$ homeomorphic to a ball with a point of its boundary, which is star-shaped and hence retracts onto $p$; the same holds in $D_m$. Exercise 1 of §71 (printed p. 438) then gives $\pi_1(D_n\vee D_m,p)\cong\pi_1(D_n,p)*\pi_1(D_m,p)\cong\ZZ/n*\ZZ/m$.

:::

:::

::: pf-step

(a) and (b).

::: pf-proof

(a) is the product case: $X=D_n\times D_m$. For (b), take $X=D_{n_1}\times\cdots\times D_{n_k}$; induction on $k$ with Theorem 60.1 gives $\pi_1(X)\cong\ZZ/n_1\times\cdots\times\ZZ/n_k$.

:::

:::

::: pf-step

(c) and (d).

::: pf-proof

(c) is the wedge case: $X=D_n\vee D_m$. For (d), take $X=D_{n_1}\vee\cdots\vee D_{n_k}$; induction on $k$ with Exercise 1 of §71 at each step, the hypotheses being those checked in step 1, gives $\pi_1(X)\cong\ZZ/n_1*\cdots*\ZZ/n_k$.

:::

:::

::: pf-qed

The products answer (a) and (b), the wedges answer (c) and (d).

:::

:::
:::
