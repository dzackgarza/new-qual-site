---
schema: qual/card@1
id: E-PLSGP
kind: problem
title: Epsilon-delta continuity implies open-set continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 1, printed p. 111, with the open set
    definition of continuity on printed p. 102; the stored statement is the printed one. Its
    epsilon glyph is lost in the text extraction, which the card records.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.1, PDF p. 11. The content is theirs: an
    epsilon-ball round f(x_0) inside the open set V, and the delta-ball round x_0 that the
    epsilon-delta condition supplies, which lies in the preimage. (tmp/sources/munkres-
    solutions-positron-ch2.pdf).
---

::: {.exercise}

Prove that for functions $f: \RR \to \RR$, the $\epsilon$-$\delta$ definition of continuity implies the open set definition.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.1, PDF p. 11** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs, and Whitman's printed p. 179 is the same proof phrased through Theorem 18.1(4). (The symbol for $\varepsilon$ in the stored statement of the exercise is a lost glyph in the extraction; it is $\varepsilon$.)

Let $f:\RR\to\RR$ be continuous in the $\varepsilon$-$\delta$ sense, that is: for every $x_{0}$ and every $\varepsilon>0$ there is $\delta>0$ such that $\abs{x-x_{0}}<\delta$ implies $\abs{f(x)-f(x_{0})}<\varepsilon$.

Let $V\subset\RR$ be open. If $f^{-1}(V)=\varnothing$ it is open; otherwise let $x_{0}\in f^{-1}(V)$, so $f(x_{0})\in V$. Since $V$ is open there is $\varepsilon>0$ with
$$
(f(x_{0})-\varepsilon,\ f(x_{0})+\varepsilon)\subset V .
$$
Choose $\delta>0$ as above for this $\varepsilon$. Then for every $x\in(x_{0}-\delta,x_{0}+\delta)$ we have $\abs{f(x)-f(x_{0})}<\varepsilon$, that is $f(x)\in V$, so
$$
x_{0}\in(x_{0}-\delta,x_{0}+\delta)\subset f^{-1}(V).
$$
Hence every point of $f^{-1}(V)$ is an interior point and $f^{-1}(V)$ is open. As $V$ was an arbitrary open set, $f$ is continuous in the open set definition.
:::
