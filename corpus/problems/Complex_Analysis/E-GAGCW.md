---
schema: qual/card@1
id: E-GAGCW
kind: problem
title: Schwarz–Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
---

::: {.problem}
Suppose $f:\DD\to \DD$ is analytic.
Prove that
$$
\forall a\in \DD, \qquad {\abs{f'(a)} \over 1 - \abs{f(a)}^2 } \leq {1 \over 1 - \abs{a}^2}
.$$
:::

::: {.solution}
For $b\in\DD$, let $\psi_b(z)\coloneqq{b-z\over1-\bar bz}$, an automorphism of $\DD$ with $\psi_b(0)=b$, $\psi_b(b)=0$ and $\psi_b\circ\psi_b=\id$.

::: pf

::: {.pf-step #pick}
For $z,w\in\DD$,
$$
\abs{f(w) - f(z) \over 1 - \overline{f(w)}f(z)} \leq \abs{w-z \over 1-\bar{w} z}
,$$
that is, $\abs{\psi_{f(w)}(f(z))}\le\abs{\psi_w(z)}$.

::: pf-proof
Let $F\coloneqq\psi_{f(w)}\circ f\circ\psi_w$, a holomorphic map $\DD\to\DD$ with $F(0)=\psi_{f(w)}(f(w))=0$.
The Schwarz lemma gives $\abs{F(b)}\le\abs b$ for $b\in\DD$.
Put $b=\psi_w(z)$, so that $\psi_w(b)=z$ and $F(b)=\psi_{f(w)}(f(z))$.
:::

:::

::: pf-step
For $a\in\DD$, ${\abs{f'(a)}\over1-\abs{f(a)}^2}\le{1\over1-\abs a^2}$.

::: pf-proof
Take $w=a$ in step [](#pick){.pf-ref} and divide by $\abs{z-a}$ for $z\neq a$:
$$
{1\over\abs{1-\overline{f(a)}f(z)}}\cdot\abs{f(z)-f(a)\over z-a}\le{1\over\abs{1-\bar az}}
.$$
As $z\to a$, the difference quotient tends to $\abs{f'(a)}$, while $1-\overline{f(a)}f(z)\to1-\abs{f(a)}^2$ and $1-\bar az\to1-\abs a^2$.
:::

:::

:::

:::
