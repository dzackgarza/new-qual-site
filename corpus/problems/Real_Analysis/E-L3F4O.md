---
schema: qual/card@1
id: E-L3F4O
kind: problem
title: Middle-thirds Cantor set is compact, totally disconnected, perfect, and null;
  Borel–Cantelli lemma
classification:
  areas:
  - real-analysis
  topics:
  - Cantor Set
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that that Cantor middle-thirds set is compact, totally disconnected, and perfect, with outer measure zero.

- Prove the Borel-Cantelli lemma.
:::

::: {.solution}
Let $C_0 = [0,1]$, let $C_n$ be obtained from $C_{n-1}$ by deleting the open middle third of each of its intervals, and let $C = \bigcap_{n \ge 0} C_n$. By induction, $C_n$ is the disjoint union of $2^n$ closed intervals of length $3^{-n}$, the stage-$n$ intervals.

<1>1. $C$ is compact.

::: {.proof}
Each $C_n$ is a finite union of closed intervals, hence closed, so $C$ is a closed subset of the compact set $[0,1]$.
:::

<1>2. $m^*(C) = 0$.

::: {.proof}
$C \subseteq C_n$ and $m^*(C_n) = 2^n 3^{-n}$, so monotonicity gives $m^*(C) \le (2/3)^n$ for every $n$.
:::

<1>3. $C$ is totally disconnected.

::: {.proof}
A connected subset of $\RR$ is an interval. If a connected $S \subseteq C$ contained points $x < y$, then $[x,y] \subseteq C$ and $m^*(C) \geq y - x > 0$, contradicting step <1>2. So every connected subset of $C$ has at most one point.
:::

<1>4. $C$ is perfect: every point of $C$ is a limit point of $C$.

<2>1. Every endpoint of a stage-$k$ interval lies in $C$.

::: {.proof}
Deleting an open middle third from a closed interval keeps both endpoints, and each endpoint of a stage-$k$ interval is an endpoint of a stage-$j$ interval for every $j \geq k$. So it lies in every $C_j$.
:::

<2>2. For $x \in C$ and $n \geq 0$ there is $y \in C$ with $0 < \abs{x - y} \leq 3^{-n}$.

::: {.proof}
Let $I$ be the stage-$n$ interval containing $x$. $I$ has two endpoints at distance $3^{-n}$ from each other, so at least one of them differs from $x$; it lies in $C$ by step <2>1 and in $I$, so its distance from $x$ is at most $3^{-n}$.
:::

<2>3. Q.E.D.

::: {.proof}
Step <2>2 gives points of $C \setminus \theset{x}$ within $3^{-n}$ of $x$ for every $n$. Since $C$ is closed by step <1>1, $C$ is perfect.
:::

<1>5. Borel--Cantelli lemma: if $(E_n)$ is a sequence of measurable sets in a measure space $(X, \mu)$ with $\sum_n \mu(E_n) < \infty$, then $\mu(\limsup_n E_n) = 0$.

::: {.proof}
$\limsup_n E_n = \bigcap_N \bigcup_{n \ge N} E_n$ is measurable. For every $N$, $\limsup_n E_n \subseteq \bigcup_{n \ge N} E_n$, so monotonicity and countable subadditivity give $\mu(\limsup_n E_n) \le \sum_{n \ge N} \mu(E_n)$. The right-hand side is the tail of a convergent series and tends to $0$ as $N \to \infty$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove compactness, outer measure zero, total disconnectedness, and perfectness of $C$; step <1>5 proves the Borel--Cantelli lemma.
:::
:::
