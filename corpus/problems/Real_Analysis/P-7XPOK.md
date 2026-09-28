---
schema: qual/card@1
id: P-7XPOK
kind: problem
title: Countable disjoint intervals, open sets in $\RR$ and $\RR^n$, the Cantor set,
  and Borel–Cantelli
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Cantor Set
  - Borel-Cantelli
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- Show that any disjoint intervals is countable.

- Show that every open $U \subseteq \RR$ is a countable union of disjoint open intervals.

- Show that every open $U \subseteq \RR^n$ is a countable union of *almost* disjoint closed cubes.

- Show that that Cantor middle-thirds set is compact, totally disconnected, and perfect, with outer measure zero.

- Prove the Borel-Cantelli lemma.
:::

::: {.solution}
<1>1. A family of pairwise disjoint intervals in $\RR$, each with nonempty interior, is countable.

::: {.proof}
Each interval contains a rational number; choosing one for each interval gives an injection into $\QQ$, because the intervals are disjoint. See [[E-MFCCS]], which also shows that the family of singletons $\theset{x}$, $x \in \RR$, is an uncountable disjoint family of degenerate intervals.
:::

<1>2. Every open $U \subseteq \RR$ is a countable union of disjoint open intervals.

::: {.proof}
The connected components of $U$ partition $U$. Each is open, because $\RR$ is locally connected, and connected, hence an open interval. By step <1>1 there are countably many. See [[E-EJN4Q]].
:::

<1>3. Every open $U \subseteq \RR^n$ is a countable union of almost disjoint closed cubes.

::: {.proof}
Let $\mathcal F$ be the set of closed dyadic cubes $Q \subseteq U$ of side $2^{-k}$, $k \geq 0$, such that $k = 0$ or the dyadic cube of side $2^{-k+1}$ containing $Q$ is not contained in $U$. Every $x \in U$ lies in a dyadic cube inside $U$, and the one of largest side among the dyadic cubes containing $x$ of side at most $1$ and contained in $U$ lies in $\mathcal F$. Two dyadic cubes are nested or have disjoint interiors, and the defining condition rules out strict nesting within $\mathcal F$. There are countably many dyadic cubes. See [[E-M3CGY]].
:::

<1>4. The Cantor set $C = \bigcap_n C_n$, with $C_n$ the union of the $2^n$ closed intervals of length $3^{-n}$ remaining at stage $n$, is compact, of outer measure zero, totally disconnected, and perfect.

::: {.proof}
$C$ is a closed subset of $[0,1]$, hence compact, and $m^*(C) \le m(C_n) = (2/3)^n$ for every $n$. A connected subset of $\RR$ with two points contains an interval of positive length, which would have positive measure, so every connected subset of $C$ has at most one point. For $x \in C$ and each $n$, the stage-$n$ interval containing $x$ has two endpoints in $C$ at distance $3^{-n}$ apart, so one of them is a point of $C \setminus \theset{x}$ within $3^{-n}$ of $x$. See [[E-L3F4O]].
:::

<1>5. If $(E_n)$ are measurable with $\sum_n \mu(E_n) < \infty$, then $\mu(\limsup_n E_n) = 0$.

::: {.proof}
$\limsup_n E_n = \bigcap_N\bigcup_{n \ge N}E_n$ is measurable and contained in $\bigcup_{n \ge N}E_n$ for every $N$, so countable subadditivity gives $\mu(\limsup_n E_n) \le \sum_{n \ge N}\mu(E_n)$. The right side is the tail of a convergent series and tends to $0$.
:::
:::
