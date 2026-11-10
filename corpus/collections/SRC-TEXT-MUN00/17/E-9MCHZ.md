---
schema: qual/card@1
id: E-9MCHZ
kind: problem
title: Closures and separation under five topologies on the line
classification:
  areas:
  - topology
  topics:
  - Closure
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 16, printed pp. 101-102, with the
    five topologies of Exercise 13.7 and Theorem 17.8; the stored statement is the printed
    one and the card states the ten answers as a table.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.16, printed pp.
    167-169. His are the table, the lemma that a finer topology inherits T1 and Hausdorff,
    all five closures - K, K, R, K and [0,infinity) in the five topologies - and the
    separation facts, including that the finite complement topology is T1 but not Hausdorff
    and the ray topology neither. positron0802 PDF p. 8 agrees on all ten entries.
    (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Consider the five topologies on $\RR$ given in Exercise 7 of §13.

(a) Determine the closure of the set $K = \theset{1/n \mid n \in \ZZ_+}$ under each of these topologies.

(b) Which of these topologies satisfy the Hausdorff axiom?
the $T_1$ axiom?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.16, printed pp. 167--169** (`tmp/sources/munkres-solutions-whitman.pdf`); the table, the closure computations of (a) and the separation arguments of (b) are his, with "positron0802", *Solutions to Topology, Chapter 2*, Exercise 17.16, PDF p. 8, agreeing on all ten entries.

The answer is

| topology | $\overline{K}$ | Hausdorff | $T_{1}$ |
| --- | --- | --- | --- |
| $\mathcal{T}_{1}$ standard | $K\cup\{0\}$ | yes | yes |
| $\mathcal{T}_{2}$ of $\RR_{K}$ | $K$ | yes | yes |
| $\mathcal{T}_{3}$ finite complement | $\RR$ | no | yes |
| $\mathcal{T}_{4}$ upper limit | $K$ | yes | yes |
| $\mathcal{T}_{5}$ rays $(-\infty,a)$ | $[0,\infty)$ | no | no |

**Lemma.** If $\mathcal{T}\subset\mathcal{T}'$ are topologies on $X$ and $\mathcal{T}$ is $T_{1}$, respectively Hausdorff, then so is $\mathcal{T}'$. Indeed a finite set closed in $\mathcal{T}$ has open complement in $\mathcal{T}$, hence in $\mathcal{T}'$; and disjoint $\mathcal{T}$-neighbourhoods of two points remain $\mathcal{T}'$-neighbourhoods.

(a) *Standard topology: $\overline{K}=K\cup\{0\}$.* The point $0$ is a limit point of $K$: a basis element $(a,b)$ with $0\in(a,b)$ has $b>0$, so $1/n\in(a,b)$ for all $n>1/b$. Every $x\notin K\cup\{0\}$ has a neighbourhood meeting $K$ in nothing: if $x<0$ then $(x-1,0)$ contains no element of $K$; if $x>1$ then $(1,x+1)$ contains none; and if $0<x\notin K$ then, choosing $n$ with $n<1/x<n+1$ (Exercise 4.9(b)), we get $1/(n+1)<x<1/n$ and the interval $(1/(n+1),1/n)$ contains $x$ and no element of $K$. So the only limit point of $K$ is $0$ and $\overline{K}=K\cup\{0\}$.

*$\RR_{K}$: $\overline{K}=K$.* The complement is open in $\RR_{K}$:
$$
\RR-K=(-\infty,0)\cup\bigcup_{n\in\ZZ_{+}}\Big(\tfrac1{n+1},\tfrac1n\Big)\cup(1,\infty),
$$
a union of basis elements. So $K$ is closed and $\overline{K}=K$. (Whitman argues the same pointwise: for $x\notin K$ the basis element $(x-1,x+1)-K$ contains $x$ and misses $K$.)

*Finite complement topology: $\overline{K}=\RR$.* A nonempty open set $U$ has finite complement, so $U\cap K$ is infinite, in particular it contains points other than any prescribed $x\in\RR$. Hence every point of $\RR$ is a limit point of $K$ and $\overline{K}=\RR$.

*Upper limit topology: $\overline{K}=K$.* Every $x\notin K$ has a basis element $(a,b]$ containing $x$ and meeting $K$ in nothing: if $x\le0$ take $(x-1,x]$; if $x>1$ take $(1,x]$; if $0<x\notin K$ choose $n$ with $1/(n+1)<x<1/n$ and take $(1/(n+1),x]$, whose points $y$ satisfy $1/(n+1)<y\le x<1/n$ and so are in no $\{1/m\}$. Hence no point outside $K$ is a limit point and $\overline{K}=K$.

*Rays: $\overline{K}=[0,\infty)$.* If $x\ge0$ and $(-\infty,a)$ is a basis element containing $x$, then $a>x\ge0$ and $1/n\in(-\infty,a)$ for $n>1/a$, so $x$ is a limit point of $K$; the point $0$ is included here. If $x<0$ then $(-\infty,0)$ is a neighbourhood of $x$ meeting $K$ in nothing. Hence $\overline{K}=[0,\infty)$.

(b) $\mathcal{T}_{1}$ is Hausdorff (it is induced by the metric of $\RR$), hence $T_{1}$. By Exercise 13.7, $\mathcal{T}_{1}\subset\mathcal{T}_{2}\subset\mathcal{T}_{4}$, so by the lemma $\mathcal{T}_{2}$ and $\mathcal{T}_{4}$ are Hausdorff and $T_{1}$.

$\mathcal{T}_{3}$ is $T_{1}$: a finite set $F$ has complement $\RR-F$, which is open in $\mathcal{T}_{3}$ because its own complement is $F$, finite; so every finite set, in particular every one-point set, is closed. It is not Hausdorff: if $U\ni0$ and $V\ni1$ are open, then $\RR-U$ and $\RR-V$ are finite (neither is all of $\RR$, since $U$ and $V$ are nonempty), so $\RR-(U\cap V)=(\RR-U)\cup(\RR-V)$ is finite and $U\cap V\ne\varnothing$.

$\mathcal{T}_{5}$ is not $T_{1}$: for $x<y$ every basis element $(-\infty,a)$ containing $y$ has $a>y>x$, so it contains $x$, and $y$ has no neighbourhood omitting $x$; by Exercise 17.15 the $T_{1}$ axiom fails. Hence $\mathcal{T}_{5}$ is not Hausdorff either (Theorem 17.8).
:::
