---
schema: qual/card@1
id: E-JSSPA
kind: problem
title: Directness of sums via vanishing of finite sums
classification:
  areas:
  - topology
  topics:
  - Free Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §67 Exercise 1, printed p. 411. Proof transcribed from dbFin, Munkres (2000) Topology with Solutions,
    §67 Problem 1 (https://dbfin.com/topology/munkres/chapter-11/section-67-direct-sums-of-abelian-groups/problem-1-solution/,
    read 2026-11-11), which has no printed pagination. Checked against the definition of the direct sum on
    Munkres p. 407 and Lemma 67.1 on p. 408: dbFin's "regroup and combine" step is written out here as the
    substitution x_alpha - y_alpha in G_alpha, since a term x_{alpha_i} and a term y_{alpha_i} with the same
    index must be combined before the hypothesis applies. Nothing else on the card needed correction.
---

::: {.exercise}

Suppose that $G = \sum G_\alpha$.
Show this sum is direct if and only if the equation

$$
x_{\alpha_1} + \dots + x_{\alpha_n} = 0
$$

implies that each $x_{\alpha_i}$ equals 0. (Here $x_{\alpha_i} \in G_{\alpha_i}$ and the indices $\alpha_i$ are distinct.)
:::

::: {.solution}

Write $G=\sum_{\alpha\in J}G_\alpha$, so that by the definition on p. 407 every $x\in G$ is a finite sum $x=\sum_{\alpha}x_\alpha$ with $x_\alpha\in G_\alpha$ and $x_\alpha=0$ for all but finitely many $\alpha$; the sum is direct when this $J$-tuple is unique for each $x$.

::: pf

::: pf-step

If the sum is direct, then $x_{\alpha_1}+\cdots+x_{\alpha_n}=0$ forces every $x_{\alpha_i}=0$.

::: pf-proof

The zero element has the representation $0=\sum_\alpha 0$ with every coordinate $0$. The displayed equation gives another: the tuple with $x_\alpha=x_{\alpha_i}$ for $\alpha=\alpha_i$ and $x_\alpha=0$ otherwise. Uniqueness of the representation in a direct sum gives $x_{\alpha_i}=0$ for each $i$.

:::

:::

::: pf-step

If the vanishing condition holds, the sum is direct.

::: pf-proof

Since the $G_\alpha$ generate $G$, each $x\in G$ has at least one representation. Let $x=\sum_\alpha x_\alpha=\sum_\alpha y_\alpha$ be two, with $x_\alpha,y_\alpha\in G_\alpha$, both coordinates zero off a finite set. Put $z_\alpha=x_\alpha-y_\alpha$, which lies in $G_\alpha$ and is zero off a finite set, and let $\alpha_1,\dots,\alpha_n$ be the distinct indices at which $z_\alpha\neq0$. Then

$$
z_{\alpha_1}+\cdots+z_{\alpha_n}=\sum_{\alpha}x_\alpha-\sum_{\alpha}y_\alpha=x-x=0,
$$

so the hypothesis gives $z_{\alpha_i}=0$ for every $i$, that is, $x_\alpha=y_\alpha$ for all $\alpha$. Hence the representation is unique and $G$ is the direct sum of the $G_\alpha$.

:::

:::

::: pf-qed

The two implications are steps 1 and 2.

:::

:::
:::
