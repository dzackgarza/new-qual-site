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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.6, PDF pp. 17--18** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all five parts are theirs. Part (a) below adds the step their sentence omits: that the complement of an interval of $A_{n}$ is a finite union of closed sets of $C$, so the interval's trace is clopen in $C$.

Let $A_{0}=[0,1]$ and let $A_{n}$ be obtained from $A_{n-1}$ by deleting the open middle third of each of its closed intervals, so that $A_{n}$ is a finite disjoint union of closed intervals of length $3^{-n}$; let $C=\bigcap_{n}A_{n}$.

::: pf

::: {.pf-step #clopen}
For $x\in C$ and $n\ge0$, if $I$ is the interval of $A_{n}$ containing $x$, then $I\cap C$ is both open and closed in $C$, and it contains no point of $C$ at distance more than $3^{-n}$ from $x$.

::: pf-proof
$I$ is closed in $\RR$, so $I\cap C$ is closed in $C$. The other intervals $J$ of $A_{n}$ are finitely many closed sets, so $C\setminus I=\bigcup_{J}\big(J\cap C\big)$ is a finite union of closed subsets of $C$, hence closed in $C$; therefore $I\cap C$ is also open in $C$. It contains $x$, and every point of $I$ lies within $3^{-n}$ of $x$ because $I$ has length $3^{-n}$.
:::

:::

::: {.pf-step #totally-disconnected}
(a) $C$ is totally disconnected.

::: pf-proof
Let $B\subseteq C$ be connected and let $x,y\in B$ with $x<y$. Choose $n$ with $3^{-n}<y-x$; then $x$ and $y$ lie in different intervals of $A_{n}$, because any two points of one interval are at distance at most $3^{-n}$. Let $I$ be the interval of $A_{n}$ containing $x$. By step [](#clopen){.pf-ref} the sets $B\cap I=B\cap(I\cap C)$ and $B\setminus I=B\cap(C\setminus I)$ are open in $B$ and closed in $B$; they are nonempty, as $x$ and $y$ lie in them respectively, and they are disjoint with union $B$. That is a separation, contradicting the connectedness of $B$. So no connected $B\subseteq C$ has two points.
:::

:::

::: {.pf-step #compact}
(b) $C$ is compact.

::: pf-proof
Each $A_{n}$ is a finite union of closed intervals, hence closed in $\RR$; so $C=\bigcap_{n}A_{n}$ is closed in $\RR$, and being a closed subset of the compact space $[0,1]$ it is compact (Theorem 26.2).
:::

:::

::: {.pf-step #intervals}
(c) Each $A_{n}$ is a union of finitely many disjoint closed intervals of length $3^{-n}$, and the endpoints of all these intervals lie in $C$.

::: pf-proof
Induction on $n$: $A_{0}=[0,1]$ is one closed interval of length $1=3^{0}$; if $A_{n-1}$ is a disjoint union of intervals of length $3^{-(n-1)}$, then $A_{n}$ is obtained by removing from each such interval its open middle third, leaving two disjoint closed intervals, each of length $\tfrac13\cdot3^{-(n-1)}=3^{-n}$; so $A_{n}$ is such a union, and it has $2^{n}$ intervals. At every step only an open interval is removed, so a point of $A_{n}$ that has been present in $A_{0},A_{1},\ldots,A_{n-1}$ as an endpoint of an interval remains in all later sets: each deletion removes no endpoint of any interval, hence every endpoint of every $A_{m}$ lies in $A_{n}$ for all $n$, and so in $C$.
:::

:::

::: {.pf-step #no-isolated}
(d) $C$ has no isolated points.

::: pf-proof
Let $x\in C$ and $n\in\ZZ_{+}$, and let $I$ be the interval of $A_{n}$ containing $x$. An endpoint $x_{n}$ of $I$ other than $x$ exists unless $I=\{x\}$, which is impossible since $I$ has length $3^{-n}>0$; that endpoint lies in $C$ by step [](#intervals){.pf-ref} and satisfies $0<\abs{x_{n}-x}\le3^{-n}$. So every neighbourhood of $x$ contains a point of $C$ different from $x$.
:::

:::

::: {.pf-step #uncountable}
(e) $C$ is uncountable.

::: pf-proof
$C$ is nonempty, since by step [](#intervals){.pf-ref} it contains the endpoints of the intervals of $A_{1}$, for instance $0,1/3,2/3,1$. It is compact Hausdorff by step [](#compact){.pf-ref}, and it has no isolated points by step [](#no-isolated){.pf-ref}; a nonempty compact Hausdorff space with no isolated points is uncountable (Theorem 27.7).
:::

:::

::: {.pf-qed}
Parts (a)--(e) are steps [](#totally-disconnected){.pf-ref}, [](#compact){.pf-ref}, [](#intervals){.pf-ref}, [](#no-isolated){.pf-ref} and [](#uncountable){.pf-ref}.
:::

:::

:::
