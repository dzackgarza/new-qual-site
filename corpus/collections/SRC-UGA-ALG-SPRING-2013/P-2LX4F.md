---
schema: qual/card@1
id: P-2LX4F
kind: problem
title: Galois group of $x^6+x^3+1$ over $\FF_2$ and its intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $F$ be the field with 2 elements and $K$ a splitting field of $f(x) = x^6 + x^3 + 1$ over $F$.
You may assume that $f$ is irreducible over $F$.

a. Show that if $r$ is a root of $f$ in $K$, then $r^9 = 1$ but $r^3\neq 1$.

b. Find $\gal(K/F)$ and express each intermediate field between $F$ and $K$ as $F(\beta)$ for an appropriate $\beta \in K$.
:::

::: {.solution}
Let $r$ be a root of $f$. Since
\[
r^6+r^3+1=0,
\]
put $u=r^3$. Then
\[
u^2+u+1=0.
\]
Multiplying by $u-1$ gives $u^3-1=0$, so $r^9=u^3=1$. Moreover $u\ne1$, because in characteristic $2$,
\[
1^2+1+1=1\ne0.
\]
Thus $r^3\ne1$. In fact $r$ has multiplicative order $9$.

Because $f$ is irreducible of degree $6$, $F(r)$ has $2^6=64$ elements. Every finite extension of a finite field is Galois, and all conjugates of $r$ are obtained by Frobenius powers, so the splitting field is
\[
K=F(r)\cong\mathbb F_{64}.
\]
Therefore
\[
\operatorname{Gal}(K/F)=\langle\sigma\rangle\cong C_6,
\qquad
\sigma(z)=z^2.
\]

A cyclic group of order $6$ has one subgroup of each order $1,2,3,6$, so there are exactly four intermediate fields, namely the unique finite subfields of orders $2^d$ for $d\mid6$:
\[
\mathbb F_2,
\quad
\mathbb F_4,
\quad
\mathbb F_8,
\quad
\mathbb F_{64}.
\]
They can be written explicitly as follows.

Since $r^3$ is a nontrivial cube root of unity, it satisfies $x^2+x+1$, which is irreducible over $\mathbb F_2$. Hence
\[
\mathbb F_4=F(r^3).
\]
Set
\[
\beta=r+r^8=r+r^{-1}.
\]
Because $r^{64}=r$,
\[
\beta^8=r^8+r^{64}=r^8+r=\beta,
\]
so $\beta\in\mathbb F_8$. It is not in $\mathbb F_2$: $\beta=0$ would imply $r^7=1$, and $\beta=1$ would imply $r^2+r+1=0$, hence $r^3=1$, both contradicting that $r$ has order $9$. Thus $F(\beta)$ is a proper extension of $F$ inside $\mathbb F_8$; since $[\mathbb F_8:F]=3$ is prime,
\[
\mathbb F_8=F(r+r^8).
\]
Finally,
\[
\mathbb F_{64}=F(r).
\]
So the intermediate fields are exactly
\[
F,
\qquad
F(r^3),
\qquad
F(r+r^8),
\qquad
F(r)=K.
\]
:::
