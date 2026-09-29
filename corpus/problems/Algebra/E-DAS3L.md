---
schema: qual/card@1
id: E-DAS3L
kind: problem
title: Cyclic groups, Euler's totient, and $\operatorname{Aut}(\mathbb{Z}/n\mathbb{Z})$
classification:
  areas:
  - algebra
  topics:
  - Cyclic Groups
  - Automorphisms
  - Number Theory
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.exercise}
\envlist

- Show that any cyclic group is abelian.

- Show that every subgroup of a cyclic group is cyclic.

- Show that $$\phi(n) = n \prod_{p\mid n}\qty{1 - {1\over p}}.$$

- Compute $\aut(\ZZ/n\ZZ)$ for $n$ composite.

- Compute $\aut(\qty{\ZZ/p\ZZ}^n)$.
:::

::: {.solution}

::: pf

::: pf-step
A cyclic group $G=\langle g\rangle$ is abelian.

::: pf-proof
Any two elements are $g^a,g^b$, and $g^ag^b=g^{a+b}=g^bg^a$.
:::

:::

::: pf-step
Every subgroup $H$ of $G=\langle g\rangle$ is cyclic.

::: pf-proof
If $H=\{e\}$, then $H=\langle e\rangle$.
Otherwise $H$ contains some $g^k$ with $k\neq0$, hence also $g^{|k|}$, so let $m$ be the least positive integer with $g^m\in H$.
For $g^k\in H$, write $k=qm+r$ with $0\le r<m$; then $g^r=g^k(g^m)^{-q}\in H$, so $r=0$ by minimality.
Hence $H=\langle g^m\rangle$.
:::

:::

::: {.pf-step #phi-n-formula}
$\phi(n)=|(\ZZ/n\ZZ)^\times|=n\prod_{p\mid n}\left(1-\frac1p\right)$.

::: pf-proof
For $n=\prod_i p_i^{a_i}$, the Chinese remainder theorem gives $(\ZZ/n\ZZ)^\times\cong\prod_i(\ZZ/p_i^{a_i}\ZZ)^\times$.
The nonunits of $\ZZ/p^a\ZZ$ are the $p^{a-1}$ multiples of $p$, so $|(\ZZ/p^a\ZZ)^\times|=p^a-p^{a-1}=p^a(1-1/p)$.
Multiplying over the prime powers dividing $n$ gives the formula.
:::

:::

::: pf-step
$\Aut(\ZZ/n\ZZ)\cong(\ZZ/n\ZZ)^\times\cong\prod_i(\ZZ/p_i^{a_i}\ZZ)^\times$, where
$$(\ZZ/2^a\ZZ)^\times\cong\begin{cases}1,&a=1,\\ C_2,&a=2,\\ C_2\times C_{2^{a-2}},&a\ge3,\end{cases}$$
and $(\ZZ/p^a\ZZ)^\times$ is cyclic of order $p^{a-1}(p-1)$ for $p$ odd.

::: pf-proof
An endomorphism of $\ZZ/n\ZZ$ is multiplication by $u=\varphi(1)$, and it is bijective exactly when $u$ is a unit; composition corresponds to multiplication of the units.
The product decomposition is step [](#phi-n-formula){.pf-ref}, For odd $p$ there is a primitive root modulo $p^a$; for $a\ge3$, the class of $5$ has order $2^{a-2}$ modulo $2^a$ and $(\ZZ/2^a\ZZ)^\times=\langle-1\rangle\times\langle5\rangle$.
For composite $n$ the group need not be cyclic, e.g. $\Aut(\ZZ/8\ZZ)\cong C_2\times C_2$.
:::

:::

::: pf-step
$\Aut((\ZZ/p\ZZ)^n)\cong\operatorname{GL}_n(\FF_p)$, of order $\prod_{i=0}^{n-1}(p^n-p^i)$.

::: pf-proof
A group homomorphism of $(\ZZ/p\ZZ)^n=\FF_p^n$ is additive, hence $\FF_p$-linear, so the automorphisms are the invertible $\FF_p$-linear maps.
An invertible matrix is a choice of columns $v_1,\dots,v_n$ with $v_{i+1}\notin\operatorname{span}(v_1,\dots,v_i)$, which leaves $p^n-p^i$ choices for $v_{i+1}$.
:::

:::

:::

:::
