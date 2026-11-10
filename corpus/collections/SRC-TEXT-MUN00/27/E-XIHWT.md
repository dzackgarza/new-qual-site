---
schema: qual/card@1
id: E-XIHWT
kind: problem
title: Distance to a set in a metric space
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 2, printed p. 177, with Theorem
    27.4, Lemma 26.4 and the Lebesgue number lemma; the five parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.2, PDF p. 16. The distance to A vanishes
    exactly on the closure, is attained when A is compact, and its sublevel sets are unions
    of balls; compactness of A gives a Lebesgue number for a finite cover of A by balls
    inside U, and the tangent graph shows the compactness cannot be dropped.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $X$ be a metric space with metric $d$; let $A \subset X$ be nonempty.

(a) Show that $d(x, A) = 0$ if and only if $x \in \overline{A}$.

(b) Show that if $A$ is compact, $d(x, A) = d(x, a)$ for some $a \in A$.

(c) Define the $\epsilon$-neighborhood of $A$ in $X$ to be the set

$$
U(A, \epsilon) = \theset{x \mid d(x, A) < \epsilon}.
$$

Show that $U(A, \epsilon)$ equals the union of the open balls $B_d(a, \epsilon)$ for $a \in A$.

(d) Assume that $A$ is compact; let $U$ be an open set containing $A$.
Show that some $\epsilon$-neighborhood of $A$ is contained in $U$.

(e) Show the result in (d) need not hold if $A$ is closed but not compact.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.2, PDF p. 16** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all five parts are theirs.

(a) $d(x,A)=0$ iff $x\in\overline A$: if $d(x,A)=\delta>0$ then $B_{d}(x,\delta)\cap A=\varnothing$, so $x\notin\overline A$; conversely if $x\notin\overline A$ there is a ball $B_{d}(x,\delta)$ meeting $A$ in nothing, and then $d(x,A)\ge\delta/2>0$.

(b) $d:A\times A\to\RR$ is continuous (Exercise 20.3(a)), so for fixed $x$ the map $d_{x}(a)=d(x,a)$ is continuous on $A$ (Exercise 18.11); since $A$ is compact, the extreme value theorem gives $a\in A$ with $d_{x}(a)\le d_{x}(a')$ for all $a'$, i.e. $d(x,A)=d(x,a)$.

(c) $U(A,\varepsilon)=\{x\mid d(x,A)<\varepsilon\}=\bigcup_{a\in A}B_{d}(a,\varepsilon)$: if $d(y,A)<\varepsilon$ pick $a$ with $d(y,a)<\varepsilon$; conversely $y\in B_{d}(a,\varepsilon)$ gives $d(y,A)\le d(y,a)<\varepsilon$.

(d) For $x\in A$ choose $\varepsilon_{x}$ with $B_{d}(x,\varepsilon_{x})\subset U$; the balls $B_{d}(x,\varepsilon_{x})$ cover the compact set $A$, so finitely many of them do, and their Lebesgue number $\delta$ satisfies: every subset of $A$ of diameter $<\delta$ lies in one of them. Take $\varepsilon=\delta/2$; then each ball $B_{d}(a,\varepsilon)$ with $a\in A$ has diameter $<\delta$ and so lies in some $B_{d}(x_{i},\varepsilon_{x_{i}})\subset U$. Hence $U(A,\varepsilon)\subset U$.

(e) Let $C=\{x\times\tan x\mid -\pi/2<x<\pi/2\}$, closed in $\RR^{2}$ but not compact (it is unbounded), and $U=(-\pi/2,\pi/2)\times\RR$, open. For every $\varepsilon>0$ some point of $C$ is within $\varepsilon$ of the complement of $U$, so $U(C,\varepsilon)\not\subset U$: the compactness of $A$ in (d) cannot be dropped.
:::
