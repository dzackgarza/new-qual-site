---
schema: qual/card@1
id: E-8GBZO
kind: problem
title: The box topology implication in the maps-into-products theorem
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 5, printed p. 118, with Theorem 19.6
    on printed p. 117 and Example 19.2; the stored statement is the printed question and the
    card answers which implication holds.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.5, printed p. 192.
    His is the affirmative half: continuity of f gives continuity of each coordinate
    function, by pulling back the box basis element that is V in one coordinate and the
    whole space elsewhere. The failure of the converse is Munkres's Example 19.2, written
    out on the card with the box-open set whose preimage is the single point 0.
    (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

One of the implications stated in Theorem 19.6 holds for the box topology.
Which one?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.5, printed p. 192** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer and the proof are his.

**Continuity of $f$ implies continuity of each $f_{\alpha}$; the converse fails for the box topology.**

Let $f:A\to\prod_{\alpha\in J}X_{\alpha}$, $f(a)=(f_{\alpha}(a))_{\alpha\in J}$, where the product carries the box topology, and suppose $f$ is continuous. Fix $\beta\in J$ and let $V$ be open in $X_{\beta}$. Set
$$
B_{\alpha}=\begin{cases}V,&\alpha=\beta,\\ X_{\alpha},&\alpha\ne\beta,\end{cases}
\qquad B=\prod_{\alpha\in J}B_{\alpha}.
$$
Every $B_{\alpha}$ is open, so $B$ is a basis element of the box topology, hence open, and $U=f^{-1}(B)$ is open in $A$ because $f$ is continuous. For $a\in A$,
$$
a\in U\iff f(a)\in B\iff f_{\alpha}(a)\in B_{\alpha}\ \text{for all }\alpha\iff f_{\beta}(a)\in V,
$$
so $U=f_{\beta}^{-1}(V)$. As $V$ was arbitrary, $f_{\beta}$ is continuous; as $\beta$ was arbitrary, every coordinate function is.

The converse fails: Munkres's Example 2 of §19, the map $f:\RR\to\RR^{\omega}$, $f(t)=(t,2t,3t,\dots)$, has every coordinate function $t\mapsto nt$ continuous, but $f$ is not continuous for the box topology on $\RR^{\omega}$. Indeed
$$
B=(-1,1)\times\big(-\tfrac1{2^{2}},\tfrac1{2^{2}}\big)\times\cdots\times\big(-\tfrac1{n^{2}},\tfrac1{n^{2}}\big)\times\cdots
$$
is a box-open set containing $f(0)=\mathbf{0}$, while $f(t)\in B$ forces $\abs{nt}<1/n^{2}$, that is $\abs{t}<1/n^{3}$, for every $n$, which holds only for $t=0$; so $f^{-1}(B)=\{0\}$ is not open in $\RR$.
:::
