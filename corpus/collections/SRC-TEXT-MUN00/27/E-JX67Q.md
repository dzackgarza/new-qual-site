---
schema: qual/card@1
id: E-JX67Q
kind: problem
title: The Cantor set
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 6, printed p. 178, with Theorem 26.2
    and Theorem 27.7; the construction and all five parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.6, PDF pp. 17-18. The Cantor set is totally
    disconnected, closed and compact, contains the endpoints of all the deleted intervals,
    has no isolated points, and so is uncountable by Theorem 27.7. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $A_0$ be the closed interval $[0, 1]$ in $\RR$.
Let $A_1$ be the set obtained from $A_0$ by deleting its "middle third" $(\tfrac{1}{3}, \tfrac{2}{3})$.
Let $A_2$ be the set obtained from $A_1$ by deleting its "middle thirds" $(\tfrac{1}{9}, \tfrac{2}{9})$ and $(\tfrac{7}{9}, \tfrac{8}{9})$.
In general, define $A_n$ by the equation

$$
A_n = A_{n-1} - \bigcup_{k=0}^{\infty} \left( \frac{1+3k}{3^n}, \frac{2+3k}{3^n} \right).
$$

The intersection

$$
C = \bigcap_{n \in \ZZ_+} A_n
$$

is called the Cantor set; it is a subspace of $[0, 1]$.

(a) Show that $C$ is totally disconnected.

(b) Show that $C$ is compact.

(c) Show that each set $A_n$ is a union of finitely many disjoint closed intervals of length $1/3^n$; and show that the end points of these intervals lie in $C$.

(d) Show that $C$ has no isolated points.

(e) Conclude that $C$ is uncountable.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.6, PDF pp. 17--18** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all five parts are theirs.

The Cantor set is $C=\bigcap_{n}A_{n}$, where $A_{0}=[0,1]$ and $A_{n+1}$ is obtained from $A_{n}$ by deleting the open middle third of each of its closed intervals.

(a) $C$ is totally disconnected. If $B\subset C$ is connected and contains $x\ne y$, choose $n$ with $3^{-n}<\abs{x-y}$; then $x$ and $y$ lie in different closed intervals of $A_{n}$, and $B\cap I$, $B\cap(C-I)$ separate $B$ for the interval $I$ of $A_{n}$ containing $x$ — a contradiction.

(b) Each $A_{n}$ is a finite union of closed intervals, hence closed, so $C$ is closed; being a closed subspace of the compact space $[0,1]$, $C$ is compact (Theorem 26.2).

(c) At each step each closed interval of $A_{n}$ is replaced by two closed intervals, the middle third's interior being removed; so only interiors of intervals are deleted, and the endpoints of every interval of every $A_{n}$ survive in $C$.

(d) If $x\in C$ and $n\in\ZZ_{+}$, the interval $I_{n}$ of $A_{n}$ containing $x$ has length $3^{-n}$ and an endpoint $x_{n}\ne x$, which lies in $C$ by (c) and satisfies $\abs{x_{n}-x}\le3^{-n}$. So $x$ is a limit of points of $C$ and $C$ has no isolated points.

(e) $C$ is nonempty (it contains the endpoints of all the intervals), compact, Hausdorff and has no isolated points, so it is uncountable by Theorem 27.7.
:::
