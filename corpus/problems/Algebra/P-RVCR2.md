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
(1) Show that there exist $n \in \mathbb{N}$ with $1 \le n \le d$ and coefficients $c_0, c_1, \dots, c_{n-1} \in k$ such that:
$$a^n + c_{n-1}a^{n-1} + \cdots + c_1 a + c_0 = 0.$$
(2) Suppose such a relation holds. Show that if $c_0 \ne 0$, then $a$ is a unit in $R$.
(3) Show that if $a$ is not a zero-divisor in $R$, then $a$ is invertible in $R$.
:::

::: {.solution}
Since $\dim_kR=d$, the $d+1$ elements
\[
1,a,a^2,\dots,a^d
\]
are linearly dependent over $k$. Thus there is a nonzero polynomial of degree at most $d$ annihilating $a$. Choosing one of minimal degree and dividing by its leading coefficient gives
\[
a^n+c_{n-1}a^{n-1}+\cdots+c_0=0,
\qquad 1\le n\le d,
\]
with $c_i\in k$.

If $c_0\ne0$, then
\[
a\bigl(a^{n-1}+c_{n-1}a^{n-2}+\cdots+c_1\bigr)=-c_0,
\]
so
\[
a^{-1}=-c_0^{-1}\bigl(a^{n-1}+c_{n-1}a^{n-2}+\cdots+c_1\bigr).
\]
Hence $a$ is a unit.

Finally suppose $a$ is not a zero-divisor. Multiplication by $a$,
\[
m_a:R\to R,\qquad x\mapsto ax,
\]
is an injective $k$-linear endomorphism of the finite-dimensional vector space $R$. Therefore it is surjective. In particular there exists $b\in R$ with $ab=1$, so $a$ is invertible.
:::
