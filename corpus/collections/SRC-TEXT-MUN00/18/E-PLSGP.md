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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the prose solution as a Lamport proof against the retained set: positron0802, Solutions
    to Topology, Chapter 2 (1 January 2021), Exercise 18.1, PDF p. 11, re-read in its text version
    (tmp/sources/positron-ch2.txt). The steps are the set's argument: take a point of the preimage
    of an open set, use the openness of the target for an epsilon, use the epsilon-delta hypothesis
    for a delta, and conclude that the delta-interval lies in the preimage. The empty case and the
    conclusion that every point of the preimage is interior are stated as steps rather than left to
    the reader. The statement is unchanged, and the note on the lost glyph for epsilon in the stored
    statement is kept.
---

::: {.exercise}

Prove that for functions $f: \RR \to \RR$, the $\epsilon$-$\delta$ definition of continuity implies the open set definition.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.1, PDF p. 11** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs, and Whitman's printed p. 179 is the same proof phrased through Theorem 18.1(4). (The symbol for $\varepsilon$ in the stored statement of the exercise is a lost glyph in the extraction; it is $\varepsilon$.)

Write the $\varepsilon$-$\delta$ hypothesis as: for every $x_{0}\in\RR$ and every $\varepsilon>0$ there is $\delta>0$ such that $\abs{x-x_{0}}<\delta$ implies $\abs{f(x)-f(x_{0})}<\varepsilon$.

::: pf

::: {.pf-step #interior-point}
If $V\subset\RR$ is open and $x_{0}\in f^{-1}(V)$, then some open interval about $x_{0}$ lies in $f^{-1}(V)$.

::: pf-proof
Since $f(x_{0})\in V$ and $V$ is open, there is $\varepsilon>0$ with $(f(x_{0})-\varepsilon,f(x_{0})+\varepsilon)\subset V$. Apply the hypothesis at $x_{0}$ to this $\varepsilon$, obtaining $\delta>0$ such that $\abs{x-x_{0}}<\delta$ implies $\abs{f(x)-f(x_{0})}<\varepsilon$. Hence every $x\in(x_{0}-\delta,x_{0}+\delta)$ has $f(x)\in(f(x_{0})-\varepsilon,f(x_{0})+\varepsilon)\subset V$, that is $x\in f^{-1}(V)$, and $x_{0}\in(x_{0}-\delta,x_{0}+\delta)\subset f^{-1}(V)$.
:::

:::

::: {.pf-step #preimage-open}
For every open $V\subset\RR$ the preimage $f^{-1}(V)$ is open.

::: pf-proof
If $f^{-1}(V)$ is empty it is open. Otherwise every one of its points is an interior point by step [](#interior-point){.pf-ref}, and a subset of $\RR$ all of whose points are interior is open by definition.
:::

:::

::: {.pf-step #answer}
The $\varepsilon$-$\delta$ definition of continuity implies the open set definition.

::: pf-proof
Step [](#preimage-open){.pf-ref} shows that the preimage of each open set is open, which is the open set definition of continuity of $f:\RR\to\RR$, and the hypothesis of $\varepsilon$-$\delta$ continuity was the only input.
:::

:::

:::
:::
