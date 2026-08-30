---
schema: qual/card@1
id: P-QCF34
kind: problem
title: The annihilator of a module is an ideal, every ideal is an annihilator, and
  a faithful module of torsion elements
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $R$ be a commutative ring with unit and let $M$ be an $R$-module.
Define the annihilator of $M$ to be
\[
\operatorname{Ann}(M):=\{r \in R \mid r \cdot m=0 \text { for all } m \in M\}
\]

a. Prove that $\operatorname{Ann}(M)$ is an ideal in $R$.

b. Conversely, prove that every ideal in $R$ is the annihilator of some $R$-module.

c. Give an example of a module $M$ over a ring $R$ such that each element $m \in M$ has a nontrivial annihilator $\operatorname{Ann}(m):=\{r \in R \mid r \cdot m=0\}$, but $\operatorname{Ann}(M)=\{0\}$
:::

::: solution
**Goal:** Record the three standard annihilator facts and one example with trivial total annihilator.

<1> For (a), let $r\in\operatorname{Ann}(M)$. Then
    $r\cdot(m+n)=r\cdot m+r\cdot n=0$ and
    $r\cdot (s m)= (rs)\cdot m=s\cdot(r\cdot m)=0$ for all $m,n\in M, s\in R$.
    So $\operatorname{Ann}(M)$ is a subgroup of $R$ and is closed under multiplication by any $s\in R$.
    Therefore it is an ideal.

<1> For (b), take any ideal $I\subset R$ and the quotient module $M=R/I$.
    Then $r\in\operatorname{Ann}(R/I)$ iff $r\cdot (s+I)=0$ for all $s\in R$,
    equivalently $rs\in I$ for all $s\in R$, equivalently $r\in I$ (since $1\in R$).
    Hence $\operatorname{Ann}(R/I)=I$.

<1> For (c), let $R=\mathbb Z$ and $M=\mathbb Q/\mathbb Z$.
    For nonzero $m\in\mathbb Q/\mathbb Z$, write $m=\frac ab+\mathbb Z$ in lowest terms.
    Then $\operatorname{Ann}(m)=b\mathbb Z\neq\{0\}$, so every element has nontrivial annihilator.
    But if $r\in\operatorname{Ann}(M)$, then $r m=0$ for all $m$, so $r=0$ because $\frac1n+\mathbb Z\in M$ has order $n$ for every $n$.
    Thus $\operatorname{Ann}(M)=\{0\}$.

Authored by **Codex 5.3 Spark Extra High**.
:::
