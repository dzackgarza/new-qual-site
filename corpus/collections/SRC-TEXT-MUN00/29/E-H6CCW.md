---
schema: qual/card@1
id: E-H6CCW
kind: problem
title: Cofinal subsets of directed sets
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
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
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-2-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-2.md, and
    checked against Math StackExchange 4068934, answer 4068942 by Arturo Magidin (2021-03-20),
    https://math.stackexchange.com/questions/4068934, which is the same two-line argument.
    dbFin's page states the upper bound only; the card also states that the restricted order is a
    partial order, as Magidin's answer does. This supersedes the 2026-11-10 note above.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Munkres, Topology, 2nd ed. (2000), §29 Supplementary Exercises: Nets,
    Exercise 2 on printed p. 187, the page whose folio the retained extraction records:
    "A subset $K$ of $J$ is said to be cofinal in $J$ if for each $\alpha \in J$, there
    exists $\beta \in K$ such that $\alpha \preceq \beta$. Show that if $J$ is a directed set
    and $K$ is cofinal in $J$, then $K$ is a directed set." The card states it verbatim and
    uses the partial order and directed set printed on the same page. The three steps are
    sound: a restriction of a partial order is a partial order; for $a, b \in K$ directedness
    of $J$ gives $\alpha \in J$ above both and cofinality gives $\beta \in K$ above $\alpha$,
    so $\beta$ is an upper bound of $a$ and $b$ in $K$; the conclusion follows. dbFin's
    solution to this exercise proves the upper-bound half only, as the 2026-11-15 note says,
    and Arturo Magidin's answer 4068942 to Math StackExchange 4068934 states the restricted
    order as step 1 does. No defect found; nothing was changed. Not checked: no published set
    outside those two was read in this pass.
---

::: {.exercise}

A subset $K$ of $J$ is said to be cofinal in $J$ if for each $\alpha \in J$, there exists $\beta \in K$ such that $\alpha \preceq \beta$.
Show that if $J$ is a directed set and $K$ is cofinal in $J$, then $K$ is a directed set.
:::

::: {.solution}

::: pf

::: pf-step
The relation $\preceq$ restricted to $K$ is a partial order on $K$.

::: pf-proof
A restriction of a reflexive, transitive and antisymmetric relation has the same three properties, and for $a, b \in K$ the statements $a \preceq b$ and $b \preceq a$ still say what they said in $J$.
:::

:::

::: pf-step
Every pair of elements of $K$ has an upper bound in $K$.

::: pf-proof
Let $a, b \in K$. Since $J$ is directed, there is $\alpha \in J$ with $a \preceq \alpha$ and $b \preceq \alpha$. Since $K$ is cofinal in $J$, there is $\beta \in K$ with $\alpha \preceq \beta$. Transitivity gives $a \preceq \beta$ and $b \preceq \beta$, and $\beta$ lies in $K$.
:::

:::

::: pf-step
$K$ is a directed set. $\square$

::: pf-proof
Step 1 gives the partial order and step 2 gives the upper bound of every pair, which is the whole of the definition.
:::

:::

:::

:::
