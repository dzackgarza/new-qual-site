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
---

::: {.exercise}

Consider the subset $A$ of $(\ZZ_{+})^{\omega}$ consisting of all infinite sequences of positive integers $\mathbf{x} = (x_{1}, x_{2}, \ldots)$ that end in an infinite string of 1's. Give $A$ the following order: $\mathbf{x} < \mathbf{y}$ if $x_{n} < y_{n}$ and $x_{i} = y_{i}$ for $i > n$ . We call this the "antidictionary order" on $A$ .

(a) Show that for every $n$, there is a section of $A$ that has the same order type as $(\ZZ_+)^n$ in the dictionary order.

(b) Show $A$ is well-ordered.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.9, printed pp. 113--114** (`tmp/sources/munkres-solutions-whitman.pdf`); the section identification and the order isomorphism of (a), and the minimal-index argument of (b), are his.

Write $\mathbf{1}=(1,1,1,\dots)$. Two elements of $A$ differ in only finitely many coordinates, since both end in a string of $1$'s, so the set of coordinates in which $x\ne y$ has a largest element; the relation of the exercise reads $x<y$ iff $x_{n}<y_{n}$ at that largest differing index $n$. It is a simple order on $A$: it is irreflexive, and for $x\ne y$ exactly one of $x<y$, $y<x$ holds according to the comparison of the entries at the largest differing index; transitivity holds because for $x<y<z$ the largest index at which $x$ and $z$ differ is the largest of the two largest indices at which $x,y$ and $y,z$ differ, and at that index $x<z$.

(a) Fix $n\ge1$ and let $a\in A$ have $a_{n+1}=2$ and $a_{i}=1$ for $i\ne n+1$. Put
$$
A_{n}=\{x\in A\mid x_{i}=1 \text{ for all } i>n\}.
$$
*Claim: the section $S_{a}=\{x\in A\mid x<a\}$ equals $A_{n}$.* If $x\in A_{n}$ then $x_{i}=a_{i}=1$ for $i>n+1$ and $x_{n+1}=1<2=a_{n+1}$, so the largest index at which $x$ and $a$ differ is $n+1$ (even if some coordinate $i\le n$ also differs, it is smaller than $n+1$), and $x_{n+1}<a_{n+1}$; hence $x<a$. Conversely, if $x_{i}\ne1$ for some $i>n$, let $m$ be the largest such index; then $x_{m}>1=a_{m}$ and $x_{i}=a_{i}=1$ for $i>m$, so $x>a$ and $x\notin S_{a}$. And if $x_{n+1}\ne1$ then $x_{n+1}\ge2=a_{n+1}$, and either $x_{n+1}>2$ and the largest differing index is $n+1$ with $x_{n+1}>a_{n+1}$, or $x_{n+1}=2$ and the largest differing index is some $m\le n$ where $x_{m}\ge1=a_{m}$, so $x\ge a$ (with $x=a$ when no such $m$ exists). So $x\in S_{a}$ exactly when $x\in A_{n}$, as claimed.

Now define
$$
f:A_{n}\longrightarrow(\ZZ_{+})^{n},\qquad f(x)=(x_{n},x_{n-1},\dots,x_{1}).
$$
This is a bijection onto $(\ZZ_{+})^{n}$: an inverse is $y\mapsto(y_{n},\dots,y_{1},1,1,\dots)$, which lies in $A_{n}$. For $x\ne x'$ in $A_{n}$ let $m\le n$ be the largest index at which they differ. In the antidictionary order $x<x'$ exactly when $x_{m}<x'_{m}$, and in the dictionary order on $(\ZZ_{+})^{n}$ the tuples $f(x),f(x')$ first differ in position $n-m+1$, where $f(x)$ has the entry $x_{m}$ and $f(x')$ the entry $x'_{m}$; the entries of positions $1,\dots,n-m$ are the common coordinates $x_{n},\dots,x_{m+1}$. Hence $x<x'$ iff $f(x)<_{\mathrm{dict}}f(x')$, and $f$ is an order isomorphism of $S_{a}=A_{n}$ onto $(\ZZ_{+})^{n}$ in the dictionary order.

(b) First, $(\ZZ_{+})^{k}$ in the dictionary order is well ordered for every $k$. For $k=1$ this is the usual well-ordering of $\ZZ_{+}$. If it holds for $k$ and $B\subset(\ZZ_{+})^{k+1}$ is nonempty, let $A'$ be the nonempty set of first coordinates of elements of $B$; it has a smallest element $a_{0}$, and the set of $b\in\ZZ_{+}$ with $(a_{0},b,\dots)\in B$ is nonempty and has a smallest element $b_{0}$ by the induction hypothesis, and $(a_{0},b_{0},\dots)$ is the smallest element of $B$.

Now let $B\subset A$ be nonempty. If $\mathbf{1}\in B$ then $\mathbf{1}$ is the smallest element of $A$, hence of $B$. Otherwise every $x\in B$ satisfies $x\ne\mathbf{1}$, and since $x$ ends in a string of $1$'s there is a largest index $n_{x}$ with $x_{n_{x}}>1$; put
$$
I=\{n_{x}\mid x\in B\},\qquad B_{n}=\{x\in B\mid n_{x}=n\}.
$$
$I$ is a nonempty subset of $\ZZ_{+}$ and has a smallest element $n$; $B_{n}$ is nonempty. Every $x\in B_{n}$ has $x_{i}=1$ for $i>n$, so $B_{n}\subset A_{n}=S_{a}$, and $S_{a}$ is well ordered by (a); let $b$ be the smallest element of the nonempty set $B_{n}$.

Then $b$ is the smallest element of $B$. For $x\in B$: if $n_{x}=n$ then $x\in B_{n}$ and $b\le x$. If $n_{x}>n$, then $b_{n_{x}}=1<x_{n_{x}}$ because $b\in A_{n}$ and $n_{x}>n$, and $b_{i}=1=x_{i}$ for all $i>n_{x}$; so the largest index at which $b$ and $x$ differ is $n_{x}$, where $b<x$, giving $b<x$. Hence $B$ has a smallest element and $A$ is well ordered.

Whitman notes that $(\ZZ_{+})^{n}$ has order type $\omega^{n}$, so the section $A_{n}$ of $A$ does too, and $A$ has order type $\omega^{\omega}$.
:::
