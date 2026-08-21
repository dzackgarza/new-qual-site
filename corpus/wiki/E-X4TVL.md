---
schema: qual/card@1
id: E-X4TVL
kind: exercise
title: Rational and irrational anti-diagonals in the Sorgenfrey plane
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §31.9"}


Let $A$ be the set of all points of $\mathbb{R}_\ell^2$ of the form $x \times (-x)$, for $x$ rational; let $B$ be the set of all points of this form for $x$ irrational. If $V$ is an open set of $\mathbb{R}_\ell^2$ containing $B$, show there exists no open set $U$ containing $A$ that is disjoint from $V$, as follows:

(a) Let $K_n$ consist of all irrational numbers $x$ in $[0, 1]$ such that $[x, x + 1/n) \times [-x, -x + 1/n)$ is contained in $V$. Show that $[0, 1]$ is the union of the sets $K_n$ and countably many one-point sets.

(b) Use Exercise 5 of §27 to show that some set $\overline{K}_n$ contains an open interval $(a, b)$ of $\mathbb{R}$.

(c) Show that $V$ contains the open parallelogram consisting of all points of the form $x \times (-x + \epsilon)$ for which $a < x < b$ and $0 < \epsilon < 1/n$.

(d) Conclude that if $q$ is a rational number with $a < q < b$, then the point $q \times (-q)$ of $\mathbb{R}_\ell^2$ is a limit point of $V$.
:::
