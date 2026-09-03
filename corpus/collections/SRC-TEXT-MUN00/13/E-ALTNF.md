---
schema: qual/card@1
id: E-ALTNF
kind: problem
title: Comparing five topologies on the real line
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the following topologies on $\mathbb{R}$:

$\mathcal{T}_1$ = the standard topology,

$\mathcal{T}_2$ = the topology of $\mathbb{R}_K$,

$\mathcal{T}_3$ = the finite complement topology,

$\mathcal{T}_4$ = the upper limit topology, having all sets $(a, b]$ as basis,

$\mathcal{T}_5$ = the topology having all sets $(-\infty, a) = \ts{x \mid x < a}$ as basis.

Determine, for each of these topologies, which of the others it contains.
:::

::: solution
**Goal:** Determine all inclusion relations among the five given topologies $\mathcal{T}_1, \mathcal{T}_2, \mathcal{T}_3, \mathcal{T}_4, \mathcal{T}_5$ on $\mathbb{R}$.

<1>1. Verification of pairwise inclusions:
    *Proof:*
    <2>1. **$\mathcal{T}_1 \supset \mathcal{T}_3$:** Every non-empty set in $\mathcal{T}_3$ is of the form $\mathbb{R} \setminus \{x_1, \dots, x_k\}$, which is a finite intersection of open sets in the standard topology $\mathcal{T}_1$. Thus $\mathcal{T}_3 \subset \mathcal{T}_1$.
    <2>2. **$\mathcal{T}_1 \supset \mathcal{T}_5$:** Every basis element $(-\infty, a) = \bigcup_{n=1}^\infty (a - n, a)$ of $\mathcal{T}_5$ is a union of standard open intervals, so $\mathcal{T}_5 \subset \mathcal{T}_1$.
    <2>3. **$\mathcal{T}_2 \supset \mathcal{T}_1$:** The basis for $\mathcal{T}_2$ includes all open intervals $(a, b)$, so $\mathcal{T}_1 \subset \mathcal{T}_2$.
    <2>4. **$\mathcal{T}_4 \supset \mathcal{T}_1$:** Every open interval $(a, b) = \bigcup_{n=1}^\infty (a, b - 1/n]$ is open in $\mathcal{T}_4$, so $\mathcal{T}_1 \subset \mathcal{T}_4$.
    <2>5. **$\mathcal{T}_4 \supset \mathcal{T}_2$:** The basis elements of $\mathcal{T}_2$ are $(a, b)$ and $(a, b) \setminus K$. Since $(a, b) \in \mathcal{T}_4$, we only check $(a, b) \setminus K$:
        - For any $x \in (a, b) \setminus K$:
            - If $x \le 0$, there exists $\varepsilon > 0$ such that $(x - \varepsilon, x] \subseteq (a, b) \setminus K$.
            - If $x > 0$ and $x \notin K$, choose $n$ such that $\frac{1}{n+1} < x < \frac{1}{n}$; then $(\frac{1}{n+1}, x] \subseteq (a, b) \setminus K$.
        - Thus $(a, b) \setminus K \in \mathcal{T}_4$, proving $\mathcal{T}_2 \subset \mathcal{T}_4$.

<1>2. Verification of strictness and non-inclusions:
    *Proof:*
    <2>1. $\mathcal{T}_5 \not\subset \mathcal{T}_3$ because $(-\infty, a)$ has infinite complement.
    <2>2. $\mathcal{T}_3 \not\subset \mathcal{T}_5$ because bounded cofinite open sets are not unions of rays $(-\infty, a)$.
    <2>3. $\mathcal{T}_1 \not\subset \mathcal{T}_3$ and $\mathcal{T}_1 \not\subset \mathcal{T}_5$ (e.g. $(0, 1) \notin \mathcal{T}_3, \mathcal{T}_5$).
    <2>4. $\mathcal{T}_2 \not\subset \mathcal{T}_1$ because $(-1, 1) \setminus K \in \mathcal{T}_2 \setminus \mathcal{T}_1$.
    <2>5. $\mathcal{T}_4 \not\subset \mathcal{T}_2$ because $(0, 1] \in \mathcal{T}_4 \setminus \mathcal{T}_2$.

<1>3. Complete containment summary for each topology:
    - **$\mathcal{T}_1$ contains:** $\mathcal{T}_1, \mathcal{T}_3, \mathcal{T}_5$.
    - **$\mathcal{T}_2$ contains:** $\mathcal{T}_1, \mathcal{T}_2, \mathcal{T}_3, \mathcal{T}_5$.
    - **$\mathcal{T}_3$ contains:** $\mathcal{T}_3$.
    - **$\mathcal{T}_4$ contains:** $\mathcal{T}_1, \mathcal{T}_2, \mathcal{T}_3, \mathcal{T}_4, \mathcal{T}_5$ (all five).
    - **$\mathcal{T}_5$ contains:** $\mathcal{T}_5$.

<1>4. Conclusion:
    The inclusion lattice is the total chain $\mathcal{T}_4 \supset \mathcal{T}_2 \supset \mathcal{T}_1$ branching below $\mathcal{T}_1$ to the two incomparable subtopologies $\mathcal{T}_3$ and $\mathcal{T}_5$. Q.E.D.
:::
