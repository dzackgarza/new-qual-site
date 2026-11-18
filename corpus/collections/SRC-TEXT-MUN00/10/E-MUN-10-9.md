---
schema: qual/card@1
id: E-MUN-10-9
kind: problem
title: Antidictionary order on sequences ending in $1$'s
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 9, printed p. 67; the antidictionary
    order and both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.9, printed pp.
    113-114. From him: the identification of the section by a sequence with a single 2 at
    position n+1 with the set of sequences that are 1 beyond n, the order isomorphism onto
    (Z_+)^n given by reversing the first n coordinates, the well-ordering of (Z_+)^n by
    induction on n, and the least-index argument of (b). Whitman's case analysis for the
    section is replaced by the equivalent single comparison at the largest differing
    coordinate, and the order axioms are checked explicitly.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Munkres, *Topology* (2000), §10 Exercise 9, printed p. 67, the order relation and both parts matching the printed text. The argument is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.9, printed pp. 113--114. Checked: that two elements of $A$ differ in only finitely many coordinates; that $A_n$ is exactly the section below the element with $a_{n+1}=2$; that the reversal map is an order isomorphism; and the two-stage minimal-index argument in (b).
---

::: {.exercise}

Consider the subset $A$ of $(\ZZ_{+})^{\omega}$ consisting of all infinite sequences of positive integers $\mathbf{x} = (x_{1}, x_{2}, \ldots)$ that end in an infinite string of 1's. Give $A$ the following order: $\mathbf{x} < \mathbf{y}$ if $x_{n} < y_{n}$ and $x_{i} = y_{i}$ for $i > n$ . We call this the "antidictionary order" on $A$ .

(a) Show that for every $n$, there is a section of $A$ that has the same order type as $(\ZZ_+)^n$ in the dictionary order.

(b) Show $A$ is well-ordered.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.9, printed pp. 113--114** (`tmp/sources/munkres-solutions-whitman.pdf`); the identification of the section in (a) with an order isomorphism onto $(\ZZ_+)^{n}$, and the minimal-index argument of (b), are his. The statement is Munkres, *Topology* (2000), §10 Exercise 9, printed p. 67.

::: pf

::: {.pf-step #order}
The antidictionary relation is a simple order on $A$.

::: pf-proof
Two elements of $A$ differ in only finitely many coordinates, because both end in a string of $1$'s, so the set of indices at which $x\neq y$ has a largest element, and $x<y$ is decided by comparing the entries at that index. This gives irreflexivity, trichotomy for distinct elements, and transitivity: for $x<y<z$ the largest index at which $x$ and $z$ differ is the largest of the corresponding indices for the pairs $(x,y)$ and $(y,z)$, and the comparison there is the two-step comparison of integers.
:::
:::

::: {.pf-step #section}
(a) For $n\geq1$ the set $A_n=\{x\in A\st x_i=1\text{ for all }i>n\}$ is a section of $A$.

::: pf-proof
Let $a\in A$ have $a_{n+1}=2$ and $a_i=1$ for $i\neq n+1$. If $x\in A_n$ then $x_i=a_i=1$ for $i>n+1$ and $x_{n+1}=1<2=a_{n+1}$, so the largest differing index is $n+1$ and $x<a$. Conversely if $x\notin A_n$ there is $i>n$ with $x_i\neq1$; taking the largest such $i$, we have $x_i>1=a_i$ and $x_j=a_j=1$ for $j>i$, so $x>a$. Hence $A_n=\{x\st x<a\}$ is the section determined by $a$.
:::
:::

::: {.pf-step #iso}
(a) $A_n$ with the antidictionary order is isomorphic to $(\ZZ_+)^{n}$ with the dictionary order.

::: pf-proof
The map $f(x)=(x_n,\dots,x_1)$ is a bijection of $A_n$ onto $(\ZZ_+)^n$, with inverse $y\mapsto(y_n,\dots,y_1,1,1,\dots)$. If $x,x'\in A_n$ differ and $m\le n$ is the largest index at which they differ, then $x<x'$ exactly when $x_m<x'_m$; in the tuples $f(x),f(x')$ this is position $n-m+1$, and the earlier positions hold the common coordinates $x_n,\dots,x_{m+1}$. So $x<x'$ exactly when $f(x)<f(x')$ in the dictionary order.
:::
:::

::: {.pf-step #powers}
$(\ZZ_+)^{k}$ in the dictionary order is well ordered for every $k$.

::: pf-proof
For $k=1$ this is the well-ordering of $\ZZ_+$. If it holds for $k$ and $B\subset(\ZZ_+)^{k+1}$ is nonempty, the set of first coordinates of elements of $B$ is a nonempty subset of $\ZZ_+$ with a smallest element $a_0$; the set of tails $(b_1,\dots,b_k)$ with $(a_0,b_1,\dots,b_k)\in B$ is nonempty and, by the induction hypothesis, has a smallest element; the corresponding element of $B$ is its smallest.
:::
:::

::: {.pf-step #b}
(b) $A$ is well ordered.

::: pf-proof
Let $B\subset A$ be nonempty. If $\mathbf{1}=(1,1,\dots)\in B$ it is the smallest element of $A$. Otherwise each $x\in B$ has a largest index $n_x$ with $x_{n_x}>1$; the set $I=\{n_x\st x\in B\}$ is a nonempty subset of $\ZZ_+$ with smallest element $n$, and $B_n=\{x\in B\st n_x=n\}$ is nonempty and contained in $A_n$, which is well ordered by steps [](#section){.pf-ref} and [](#iso){.pf-ref}. Let $b$ be the smallest element of $B_n$. For $x\in B$: if $n_x=n$ then $b\le x$; if $n_x>n$ then $b_i=1=x_i$ for $i>n_x$ and $b_{n_x}=1<x_{n_x}$, so $b<x$, again using $b\in A_n$. Hence $b$ is the smallest element of $B$.
:::
:::

::: {.pf-step}
Both parts of the exercise hold: every section $A_n$ has the order type of $(\ZZ_+)^{n}$, and $A$ is well ordered.

::: pf-proof
Steps [](#section){.pf-ref} and [](#iso){.pf-ref} give (a) and steps [](#powers){.pf-ref} and [](#b){.pf-ref} give (b).
:::
:::

:::
:::
