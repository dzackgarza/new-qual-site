---
schema: qual/card@1
id: E-1VSTU
kind: problem
title: Net convergence generalizes sequence convergence
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    No published set for this exercise was located. The sources searched, the pages they
    cover and the conclusion are recorded in COMPLAINTS.md under the entry for the net
    exercises of §29; the card's own proof is kept. The statement was read against Munkres,
    Topology (2000), §29 supplementary exercises on nets, printed pp. 187-188.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 3 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-3-solution/,
    read 2026-11-15, with the page text kept at
    tmp/sources/dbfin/supplementary-exercises-nets/problem-3.md. That answer gives the reduction
    itself: with J = Z_+ the net is the sequence (x_n) and convergence means that for each
    neighborhood U of x there is N with n >= N implying x_n in U. It quotes Exercise 1 for the
    directedness of Z_+ and says nothing about a net on Z_+ being a sequence, so the card proves
    both (steps 1 and 2); nothing else is changed. This supersedes the 2026-11-10 note above that
    no published set had been located: dbFin carries a page for each of the twelve exercises of
    the Nets supplement, which the earlier search of the retained files had missed.
---

::: {.exercise}

Let $X$ be a topological space.
A net in $X$ is a function $f$ from a directed set $J$ into $X$.
If $\alpha \in J$, we usually denote $f(\alpha)$ by $x_\alpha$.
We denote the net $f$ itself by the symbol $(x_\alpha)_{\alpha \in J}$, or merely by $(x_\alpha)$ if the index set is understood.

The net $(x_\alpha)$ is said to converge to the point $x$ of $X$ (written $x_\alpha \to x$) if for each neighborhood $U$ of $x$, there exists $\alpha \in J$ such that

$$
\alpha \preceq \beta \implies x_\beta \in U.
$$

Show that these definitions reduce to familiar ones when $J = \ZZ_+$.
:::

::: {.solution}

Write $(\ZZ_+, \le)$ for the positive integers with their usual order, and say that a sequence $(x_n)$ in $X$ converges to $x$ if for each neighborhood $U$ of $x$ there is $N \in \ZZ_+$ such that $x_n \in U$ whenever $n \ge N$.

::: pf

::: pf-step
$(\ZZ_+, \le)$ is a directed set.

::: pf-proof
The relation $\le$ is reflexive and transitive, and $m \le n$ with $n \le m$ gives $m = n$; so it is a partial order, which is condition (1)--(3) of the definition. For $m, n \in \ZZ_+$ the integer $\max\{m, n\}$ lies in $\ZZ_+$ and satisfies $m \le \max\{m,n\}$ and $n \le \max\{m,n\}$, so each pair of elements has an upper bound in $\ZZ_+$.
:::

:::

::: pf-step
A net with index set $\ZZ_+$ is the same object as a sequence in $X$.

::: pf-proof
A net is a function $f : \ZZ_+ \to X$, its value at $n$ being written $x_n$; a sequence in $X$ is a function from $\ZZ_+$ into $X$, written $(x_n)$. These are one notion under two names, and the notation for the values agrees.
:::

:::

::: pf-step
For $J = \ZZ_+$ the net definition of convergence is the sequence definition of convergence.

::: pf-proof
The net definition says: for each neighborhood $U$ of $x$ there is $\alpha \in \ZZ_+$ such that $\alpha \le \beta$ implies $x_\beta \in U$. The sequence definition says: for each neighborhood $U$ of $x$ there is $N \in \ZZ_+$ such that $N \le n$ implies $x_n \in U$. Each condition is obtained from the other by renaming the bound index and the running index, and the order relation $\preceq$ of the net definition is the relation $\le$ of $\ZZ_+$; hence the two conditions hold for exactly the same nets and the same points $x$.
:::

:::

::: pf-step
Consequently the net definitions reduce, at $J = \ZZ_+$, to the definitions of a sequence and of its convergence, and the theory of nets on $\ZZ_+$ is the theory of sequences in $X$. $\square$

::: pf-proof
A net on $\ZZ_+$ is a sequence by step 2, and its convergence is the convergence of that sequence by step 3; the directedness used is that of step 1, which is the familiar order on $\ZZ_+$.
:::

:::

:::

:::
