---
schema: qual/card@1
id: E-VBWDH
kind: problem
title: Uniform boundedness principle
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The printed theorem asks for a nonempty open set, so the complete metric space X must be nonempty.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: Arthur Lei Qiu, MAT 327 Problem Set 4 solutions (the file
    327ps6sol.pdf on the course page https://www.math.toronto.edu/laithy/3272023/ of MAT327, Introduction to
    Topology, 2023; retrieved into tmp/sources/munkres-solutions-mat327-ps6sol.pdf), Question 1, Problem 1(b),
    PDF p. 1. That argument is the one on the card: the sets A_N of points at which every function of the family
    is bounded by N are closed, their union is the whole space by pointwise boundedness, and the Baire property
    of a complete metric space gives one of them a nonempty interior. The sheet proves the statement for a
    locally compact Hausdorff space or a complete metric space at once; the complete metric case is the
    exercise. Checked against Munkres, Topology (2000), §48 Exercise 10, printed p. 299, with Theorem 48.2. What
    was corrected: the printed hypothesis omits that X is nonempty, and the statement is false for the empty
    space, where there is no nonempty open set to find; the card states the exercise as printed and opens with
    the empty case and the assumption that X is nonempty.
---

::: {.exercise}

Prove the following.

Theorem (Uniform boundedness principle).
Let $X$ be a complete metric space, and let $\mathcal{F}$ be a subset of $\mathcal{C}(X, \RR)$ such that for each $a \in X$, the set

$$
\mathcal{F}_a = \theset{f(a) \mid f \in \mathcal{F}}
$$

is bounded.
Then there is a nonempty open set $U$ of $X$ on which the functions in $\mathcal{F}$ are uniformly bounded, that is, there is a number $M$ such that $\abs{f(x)} \leq M$ for all $x \in U$ and all $f \in \mathcal{F}$.
[Hint: Let $A_N = \theset{x \mid \abs{f(x)} \leq N \text{ for all } f \in \mathcal{F}}$.]
:::

::: {.solution}
As printed, the statement needs $X$ nonempty: for $X=\varnothing$ the space $\mathcal{C}(X,\RR)$ has one element, the pointwise boundedness hypothesis holds vacuously, and $X$ has no nonempty open subset, so the conclusion fails. Assume $X$ nonempty below, and note that then every $A_N$ for $N$ at least the bound at one point is nonempty.

For $N\in\ZZ_+$ set
$$
A_N=\{x\in X:\abs{f(x)}\le N\text{ for every }f\in\mathcal F\}.
$$
Each $A_N$ is closed, since
$$
A_N=\bigcap_{f\in\mathcal F}f^{-1}([-N,N]).
$$
Pointwise boundedness says every $x$ belongs to some $A_N$, so $X=\bigcup_NA_N$. A complete metric space is Baire; therefore some $A_N$ has nonempty interior. Choose a nonempty open $U\subset A_N$. Then for every $x\in U$ and every $f\in\mathcal F$, $\abs{f(x)}\le N$. Taking $M=N$ proves the assertion.
:::
