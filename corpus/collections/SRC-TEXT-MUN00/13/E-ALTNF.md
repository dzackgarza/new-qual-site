---
schema: qual/card@1
id: E-ALTNF
kind: problem
title: Comparing five topologies on the real line
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §13 Exercise 7, printed p. 83, with Lemma 13.3
    and Lemma 13.4 on printed pp. 81-82; the five topologies and their bases are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 13.7, printed pp.
    146-147. The answer (T_3 in T_1 in T_2 in T_4, T_5 in T_1, T_3 and T_5 incomparable) and
    every comparison are his: the interval decomposition of a finite complement, the ray
    inclusion, the two witnesses separating T_3 from T_5, and the case split showing every
    K-basis element is covered by an upper-limit basis element while (-2,-1] is not K-open.
    The inclusion T_1 in T_2 is the book's Lemma 13.4, which he quotes.
    (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Consider the following topologies on $\RR$:

$\mathcal{T}_1$ = the standard topology,

$\mathcal{T}_2$ = the topology of $\RR_K$,

$\mathcal{T}_3$ = the finite complement topology,

$\mathcal{T}_4$ = the upper limit topology, having all sets $(a, b]$ as basis,

$\mathcal{T}_5$ = the topology having all sets $(-\infty, a) = \theset{x \mid x < a}$ as basis.

Determine, for each of these topologies, which of the others it contains.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.7, printed pp. 146--147** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer and every comparison below are his, except that the inclusion $\mathcal{T}_{1}\subsetneq\mathcal{T}_{2}$ is Munkres's Lemma 13.4 (printed p. 82), which he quotes.

The answer is
$$
\mathcal{T}_{3}\subsetneq\mathcal{T}_{1}\subsetneq\mathcal{T}_{2}\subsetneq\mathcal{T}_{4},
\qquad
\mathcal{T}_{5}\subsetneq\mathcal{T}_{1},
$$
with $\mathcal{T}_{3}$ and $\mathcal{T}_{5}$ incomparable. Explicitly: $\mathcal{T}_{1}$ contains $\mathcal{T}_{3}$ and $\mathcal{T}_{5}$ and nothing else; $\mathcal{T}_{2}$ contains $\mathcal{T}_{1},\mathcal{T}_{3},\mathcal{T}_{5}$; $\mathcal{T}_{3}$ contains none of the others; $\mathcal{T}_{4}$ contains all four of them; $\mathcal{T}_{5}$ contains none of the others. Every inclusion asserted below is proper, so these containments are exhaustive by transitivity.

Write $\mathcal{B}_{1},\mathcal{B}_{2},\mathcal{B}_{4},\mathcal{B}_{5}$ for the bases of the standard, the $K$-topology, the upper limit and the ray topology, so $\mathcal{B}_{1}=\{(a,b)\}$, $\mathcal{B}_{2}=\{(a,b)\}\cup\{(a,b)-K\}$ with $K=\{1/n\mid n\in\ZZ_{+}\}$, $\mathcal{B}_{4}=\{(a,b]\}$ and $\mathcal{B}_{5}=\{(-\infty,a)\}$. The finite complement topology $\mathcal{T}_{3}$ is given directly. As in Exercise 13.6 we use Lemma 13.3 to compare two topologies given by bases.

*$\mathcal{T}_{3}\subsetneq\mathcal{T}_{1}$.* Let $U\in\mathcal{T}_{3}$, so $\RR-U$ is finite or all of $\RR$. In the second case $U=\varnothing\in\mathcal{T}_{1}$. In the first, list $\RR-U=\{x_{1},\dots,x_{n}\}$ with $x_{1}<\dots<x_{n}$; then
$$
U=(-\infty,x_{1})\cup\bigcup_{k=1}^{n-1}(x_{k},x_{k+1})\cup(x_{n},\infty),
$$
and the two unbounded pieces are unions of open intervals, $(-\infty,x_{1})=\bigcup_{k\ge1}(x_{1}-k-1,x_{1}-k+1)$ and similarly for $(x_{n},\infty)$. So $U$ is a union of elements of $\mathcal{B}_{1}$ and lies in $\mathcal{T}_{1}$. The inclusion is proper because $(-1,1)\in\mathcal{T}_{1}$ while $\RR-(-1,1)=(-\infty,-1]\cup[1,\infty)$ is neither finite nor all of $\RR$.

*$\mathcal{T}_{5}\subsetneq\mathcal{T}_{1}$.* Let $x\in(-\infty,a)\in\mathcal{B}_{5}$. Then $x\in(x-1,a)\in\mathcal{B}_{1}$ and $(x-1,a)\subset(-\infty,a)$, so $\mathcal{T}_{5}\subset\mathcal{T}_{1}$ by Lemma 13.3. It is proper: $-1\in(-2,0)\in\mathcal{B}_{1}$, but every element $(-\infty,a)$ of $\mathcal{B}_{5}$ containing $-1$ also contains $-3$, which is not in $(-2,0)$, so no basis element of $\mathcal{B}_{5}$ at $-1$ lies inside $(-2,0)$ and $\mathcal{T}_{1}\not\subset\mathcal{T}_{5}$.

*$\mathcal{T}_{3}$ and $\mathcal{T}_{5}$ are incomparable.* The set $U=\RR-\{0\}$ lies in $\mathcal{T}_{3}$ since $\RR-U=\{0\}$ is finite. Were $U\in\mathcal{T}_{5}$, the basis element $(-\infty,a)\in\mathcal{B}_{5}$ containing $1\in U$ and lying in $U$ would contain $0<1<a$, hence $0\in U$, a contradiction; so $U\notin\mathcal{T}_{5}$ and $\mathcal{T}_{3}\not\subset\mathcal{T}_{5}$. Conversely $(-\infty,0)\in\mathcal{T}_{5}$, while $\RR-(-\infty,0)=[0,\infty)$ is neither finite nor all of $\RR$, so $(-\infty,0)\notin\mathcal{T}_{3}$ and $\mathcal{T}_{5}\not\subset\mathcal{T}_{3}$.

*$\mathcal{T}_{1}\subsetneq\mathcal{T}_{2}$.* This is Lemma 13.4.

*$\mathcal{T}_{2}\subsetneq\mathcal{T}_{4}$.* Let $x\in B_{2}\in\mathcal{B}_{2}$. If $B_{2}=(a,b)$ then $(a,x]\in\mathcal{B}_{4}$ satisfies $x\in(a,x]\subset(a,b)$. If $B_{2}=(a,b)-K$ with $x\in B_{2}$, then $a<x<b$ and $x\notin K$. If $x\le0$, every $y\in(a,x]$ satisfies $a<y\le0$, so $y\notin K$ and $(a,x]\subset(a,b)-K$. If $x>0$, choose the smallest $n\in\ZZ_{+}$ with $n>1/x$, and let $a_{0}=\max(a,1/n)$; then $a_{0}\le1/n<x$, so $x\in(a_{0},x]$, and if $y\in(a_{0},x]$ then $a\le a_{0}<y\le x<b$, so $y\in(a,b)$; and $y\notin K$, because $y=1/m$ with $1/n\le a_{0}<1/m$ gives $m<n$, while $n$ is the least integer exceeding $1/x$, so $m\le1/x\le n-1$ and $1/m\ge x\ge y=1/m$, forcing $y=x$, contrary to $x\notin K$. So $(a_{0},x]\subset(a,b)-K$. In both cases Lemma 13.3 gives $\mathcal{T}_{2}\subset\mathcal{T}_{4}$.

The inclusion is proper. Take $x=-1\in(-2,-1]\in\mathcal{B}_{4}$ and let $B_{2}\in\mathcal{B}_{2}$ contain $-1$, so $B_{2}=(a,b)$ or $(a,b)-K$ with $a<-1<b$. If $b>0$ then $0\in B_{2}$ (as $0\notin K$), while $0\notin(-2,-1]$. If $b\le0$ then $y=(-1+b)/2$ satisfies $a<-1<y<b\le0$, so $y\notin K$ and $y\in B_{2}$, while $y>-1$, so $y\notin(-2,-1]$. Thus no basis element of $\mathcal{B}_{2}$ at $-1$ lies in $(-2,-1]$ and $\mathcal{T}_{4}\not\subset\mathcal{T}_{2}$.

Whitman remarks that it is therefore not the case that the $K$-topology is incomparable with every familiar topology on $\RR$: it is incomparable with the lower limit topology (Exercise 13.6) but comparable with the upper limit topology.
:::
