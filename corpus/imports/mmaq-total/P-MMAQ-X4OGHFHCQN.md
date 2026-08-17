---
schema: qual/card@1
id: P-MMAQ-X4OGHFHCQN
kind: problem
title: The $4$-free decimals in $[0,1]$ form a compact nowhere-dense perfect null set
classification:
  areas:
  - real-analysis
  topics:
  - cantor-set
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
Let $K$ be the set of numbers in $[0, 1]$ whose decimal expansions do not use the digit $4$.

> We use the convention that when a decimal number ends with 4 but all other digits are different from 4, we replace the digit $4$ with $399\cdots$.
> For example, $0.8754 = 0.8753999\cdots$.

Show that $K$ is a compact, nowhere dense set without isolated points, and find the Lebesgue measure $m(K)$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that $K$, the set of numbers in $[0,1]$ whose decimal expansions avoid the digit $4$ (under the stated convention), is compact, nowhere dense, has no isolated points, and has Lebesgue measure $0$.

<1>1. $K$ is closed, hence compact.
<2>1. For each $n \geq 1$, the set $D_n$ of points whose canonical $n$-th decimal digit is $4$ is a union of $9^{n-1}$ disjoint open intervals of length $10^{-n}$.
Proof: fix any string of $n-1$ initial digits avoiding $4$ ($9^{n-1}$ choices); inside the corresponding block of length $10^{-(n-1)}$, the numbers whose $n$-th digit is $4$ form an open interval of length $10^{-n}$.
Its endpoints are assigned by the convention to the $399\cdots$ expansion, so they lie in $K$, not in $D_n$.
<2>2. $K = [0,1] \setminus \bigcup_{n=1}^\infty D_n$.
Proof: by definition, $x \in K$ iff its canonical expansion (via the convention) uses no digit $4$, i.e. iff no $D_n$ contains $x$.
<2>3. $K$ is closed, and being a closed subset of the compact set $[0,1]$, it is compact.
Proof: by <2>1 each $D_n$ is open, so $\bigcup_n D_n$ is open and its complement $K$ (by <2>2) is closed.

<1>2. $m(K) = 0$.
<2>1. For each $N$, $m\!\left(\bigcup_{n=1}^N D_n\right) = \sum_{n=1}^N 9^{n-1} 10^{-n}$.
Proof: by <1>1<2>1 each $D_n$ is a union of $9^{n-1}$ disjoint intervals of length $10^{-n}$, so $m(D_n) = 9^{n-1} 10^{-n}$.
The $D_n$'s are pairwise disjoint: in the canonical expansion a point has a definite digit in each position, so it belongs to exactly one $D_n$.
<2>2. $m(K) = 1 - \sum_{n=1}^\infty 9^{n-1} 10^{-n} = 1 - \frac{1}{10} \sum_{n=1}^\infty \left(\frac{9}{10}\right)^{n-1} = 1 - \frac{1}{10} \cdot \frac{1}{1 - 9/10} = 0$.
Proof: by continuity of measure from below, $m(\bigcup_n D_n) = \lim_N m(\bigcup_{n=1}^N D_n) = \sum_{n=1}^\infty 9^{n-1} 10^{-n}$; the geometric series sums to $1$, so $m(K) = 1 - 1 = 0$ by <1>1<2>2.

<1>3. $K$ is nowhere dense.
<2>1. $K$ has empty interior.
Proof: the interior $K^\circ$ is an open set contained in $K$, so $m(K^\circ) \leq m(K) = 0$ by <1>2; the only open set of measure zero is the empty set.
<2>2. Q.E.D. Proof: by <1>1<2>3 and <2>1, $K$ is closed with empty interior, i.e. nowhere dense.

<1>4. $K$ has no isolated points.
<2>1. Given $x \in K$ and $\delta > 0$, choose $n$ with $9 \cdot 10^{-n} < \delta$, let $d$ be the $n$-th digit of the canonical expansion of $x$ (so $d \neq 4$), and pick a digit $d'$ with $d' \neq d$ and $d' \neq 4$.
Let $y$ be the number obtained from $x$ by replacing its $n$-th digit by $d'$.
Then $y \in K$, $y \neq x$, and $|x - y| < \delta$.
Proof: the expansion of $y$ avoids $4$, so $y \in K$; $y \neq x$ since the expansions differ in the $n$-th digit; changing one digit moves the value by at most $9 \cdot 10^{-n} < \delta$.
(The convention only replaces terminating-$4$ expansions by $399\cdots$; a number already possessing a $4$-free expansion is in $K$.)
<2>2. Q.E.D. Proof: <2>1 shows every punctured neighborhood of $x$ meets $K$, so $x$ is not isolated.
:::
