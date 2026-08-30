---
schema: qual/card@1
id: P-YCLOT
kind: problem
title: Groups of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
- (**Important**) Classify all groups of order $p^2$.

  > Must be abelian since quotient is cyclic.
  > If there's an element of order $p^2$, cyclic, done.
  > Else every element $a\neq 1$ must have order $p$.
  > Then $\gens{a}\neq G$, so pick $b$ in its complement, it has order $p$.
  > Call these two subgroups $H, K$ Recognize direct products: abelian implies both are normal, $H \intersect K = \ts{1}$.
  > and $\size HK = \size H \size K / \size(H \intersect K) = p\cdot p/1 = p^2$
:::

::: solution
**Goal:** Classify all groups of order $p^2$ for prime $p$.

<1>1. Let $G$ be a group of order $p^2$ and let $x\in G$.
    *Proof:*
    <2>1. By Lagrange, every element has order $1,p,$ or $p^2$.
    <2>2. If there exists $a$ with order $p^2$, then $G=\langle a\rangle\cong C_{p^2}$.

<1>2. Assume now no element has order $p^2$.
    <2>1. Choose $1\ne a\in G$, so $o(a)=p$ and $H:=\langle a\rangle$ has order $p$.
    <2>2. Choose $b\in G\setminus H$, then $o(b)=p$ and $K:=\langle b\rangle$ has order $p$.
    <2>3. Both $H$ and $K$ are nontrivial subgroups of prime order, hence maximal proper subgroups.

<1>3. Show $H\cap K=\{e\}$ and $HK=G$.
    <2>1. If $h\in H\cap K$, then $h$ has order dividing $p$ and $p$, so either $h=e$ or $h$ has order $p$.
    <2>2. But then $H=K$, contradicting $b\notin H$.
    <2>3. Therefore $H\cap K=\{e\}$.
    <2>4. By the product formula,
    $$|HK|=\frac{|H|\,|K|}{|H\cap K|}=\frac{p\cdot p}{1}=p^2,$$
    so $HK=G$.

<1>4. Establish a direct-product structure.
    <2>1. For $|H|$ prime, every subgroup of order $p$ is normal in $G$, so $H,K\triangleleft G$.
    <2>2. Define
    $$\psi:H\times K\to G,\qquad \psi(h,k)=hk.$$
    Then $\psi$ is surjective because $HK=G$ and injective because $H\cap K=\{e\}$.
    <2>3. Since domain and codomain have $p^2$ elements, $\psi$ is an isomorphism and
    $$G\cong H\times K\cong C_p\times C_p.$$

<1>5. Combine the two cases.
    The only possibilities are
    $$G\cong C_{p^2}\quad\text{or}\quad G\cong C_p\times C_p.$$
    Both are abelian and exhaustive.
:::
