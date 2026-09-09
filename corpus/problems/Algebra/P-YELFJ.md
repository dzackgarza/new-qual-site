---
schema: qual/card@1
id: P-YELFJ
kind: problem
title: An ideal maximal among annihilators of nonzero elements of an $R$-module is
  prime
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a commutative ring and let $M$ be an $R$-module.
Recall that for $\mu \in M$, the *annihilator* of $\mu$ is the set:
$$\operatorname{Ann}(\mu) = \{ r \in R \mid r \mu = 0 \}.$$

Suppose that $I$ is an ideal in $R$ which is maximal among the set of annihilators of non-zero elements of $M$ (i.e. $I = \operatorname{Ann}(\mu)$ for some $\mu \in M \setminus \{0\}$, and if $\operatorname{Ann}(\nu) \supsetneq I$ for some $\nu \ne 0$, no such $\nu$ exists).

Prove that $I$ is a **prime** ideal in $R$.
:::

::: solution
Write
\[
I=\operatorname{Ann}(\mu),
\qquad \mu\ne0,
\]
and assume $I$ is maximal among annihilators of nonzero elements of $M$. Since $\mu\ne0$, we have $1\notin I$, so $I$ is proper.

Suppose
\[
ab\in I
\]
and $b\notin I$. Then
\[
b\mu\ne0.
\]
Moreover, for every $r\in I$,
\[
r(b\mu)=b(r\mu)=0,
\]
so
\[
I\subseteq\operatorname{Ann}(b\mu).
\]
By maximality and $b\mu\ne0$,
\[
I=\operatorname{Ann}(b\mu).
\]
But
\[
a(b\mu)=(ab)\mu=0,
\]
so $a\in\operatorname{Ann}(b\mu)=I$. Therefore
\[
ab\in I,\ b\notin I\implies a\in I,
\]
and hence
\[
\boxed{I\text{ is prime}}.
\]
:::
