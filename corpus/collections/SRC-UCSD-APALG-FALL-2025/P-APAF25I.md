---
schema: qual/card@1
id: P-APAF25I
kind: problem
title: Finite-dimensionality of $k[x,y]/I$ for a two-point variety; must $\dim<100$?
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $k$ be an algebraically closed field and let $I\subseteq k[x,y]$ be an ideal.
Suppose that the variety of $I$ is $V(I)=\{(1,0),(0,1)\}\subseteq k^2$.

(a) Prove that $k[x,y]/I$ is a finite-dimensional $k$-vector space.

(b) Do we necessarily have $\dim_k(k[x,y]/I)<100$?
:::

::: solution
**Goal:** Use zero-dimensionality from a finite variety and then show dimension is unbounded.

<1> Let $\mathfrak m_1=(x-1,y)$ and $\mathfrak m_2=(x,y-1)$, the maximal ideals of the two points.
    Since $V(I)=\{(1,0),(0,1)\}$ is finite, $I$ has radical equal to $\mathfrak m_1\cap\mathfrak m_2$ and hence is zero-dimensional.
    By Hilbert’s theorem on zero-dimensional affine algebras, $k[x,y]/I$ is Artinian, therefore finite-dimensional over $k$.

<1> For (b), define
    $$
    J_n:=\mathfrak m_1^n\cap\mathfrak m_2^n.
    $$
    Then $V(J_n)=\{(1,0),(0,1)\}$ for all $n$.
    Since $\mathfrak m_1^n+\mathfrak m_2^n=R$ is comaximal, Chinese remainder gives
    $$
    k[x,y]/J_n\cong k[x,y]/\mathfrak m_1^n\oplus k[x,y]/\mathfrak m_2^n.
    $$

<1> In two variables, $\dim_k k[x,y]/\mathfrak m^n=n(n+1)/2$.
    Therefore
    $$
    \dim_k k[x,y]/J_n = n(n+1),
    $$
    so choosing $n=11$ gives $132>100$.
    Hence no bound $\dim_k(k[x,y]/I)<100$ follows from the stated assumptions.

Authored by **Codex 5.3 Spark Extra High**.
:::
