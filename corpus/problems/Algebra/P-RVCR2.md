---
schema: qual/card@1
id: P-RVCR2
kind: problem
title: Every element of a finite-dimensional $k$-algebra is integral over $k$, and
  a non-zero-divisor is a unit
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Integral Extensions
  - Integral Domains
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
Let $R$ be a commutative ring containing a field $k$ such that $\dim_k(R) = d < \infty$.
Let $a \in R$.

(a) Show that there exist $n \in \NN$ with $1 \le n \le d$ and coefficients $c_0, c_1, \ldots, c_{n-1} \in k$ such that
$$a^n + c_{n-1}a^{n-1} + \cdots + c_1 a + c_0 = 0.$$

(b) Suppose such a relation holds. Show that if $c_0 \ne 0$, then $a$ is a unit in $R$.

(c) Show that if $a$ is not a zero-divisor in $R$, then $a$ is invertible in $R$.
:::

::: {.solution}

::: pf

::: pf-step

(a) There is a monic relation $a^n+c_{n-1}a^{n-1}+\cdots+c_0=0$ with $c_i\in k$ and $1\le n\le d$.

::: pf-proof

The $d+1$ elements $1,a,\ldots,a^d$ of the $d$-dimensional $k$-space $R$ are linearly dependent, so a nonzero polynomial over $k$ of degree at most $d$ annihilates $a$. A nonzero constant does not annihilate $a$, since $1\neq0$ in $R$, so this polynomial has degree $n\ge1$. Dividing by its leading coefficient gives the monic relation.

:::

:::

::: pf-step

(b) If $c_0\neq0$, then $a$ is a unit.

::: pf-proof

The relation rearranges to
$$
a\bigl(a^{n-1}+c_{n-1}a^{n-2}+\cdots+c_1\bigr)=-c_0 ,
$$
so $a^{-1}=-c_0^{-1}\bigl(a^{n-1}+c_{n-1}a^{n-2}+\cdots+c_1\bigr)$.

:::

:::

::: pf-qed

(c) If $a$ is not a zero-divisor, the $k$-linear map $m_a\colon R\to R$, $x\mapsto ax$, is injective. An injective linear endomorphism of the finite-dimensional space $R$ is surjective, so $ab=1$ for some $b\in R$, and $a$ is invertible.

:::

:::

:::
