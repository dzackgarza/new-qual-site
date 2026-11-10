---
schema: qual/card@1
id: E-BNX60
kind: problem
title: Locally finite interval collections in $\RR$ and in $(0,1)$
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 39 Exercise 1, printed p. 247, with Example 1 of §39, the definition of local finiteness, and the archimedean property of $\RR$ for the two collections that fail in $\RR$. No correction was needed; the card proves each of the three assertions of Example 1, including that $\mathcal B$ and $\mathcal C$ are locally finite in $(0,1)$ and not in $\RR$.
---

::: {.exercise}

Check the statements in Example 1 of §39: the collection

$$
\mathcal{A} = \theset{(n, n+2) \mid n \in \ZZ}
$$

is locally finite in $\RR$, while the collections

$$
\mathcal{B} = \theset{(0, 1/n) \mid n \in \ZZ_+} \quad \text{and} \quad \mathcal{C} = \theset{(1/(n+1), 1/n) \mid n \in \ZZ_+}
$$

are locally finite in $(0, 1)$ but not in $\RR$.
:::

::: {.solution}
For
$$
\mathcal A=\{(n,n+2):n\in\ZZ\},
$$
fix $x\in\RR$. Choose $0<\varepsilon<1/2$. If $(x-\varepsilon,x+\varepsilon)$ meets $(n,n+2)$, then
$$
n<x+\varepsilon,
\qquad
n>x-\varepsilon-2.
$$
Only finitely many integers $n$ satisfy these two inequalities. Hence $\mathcal A$ is locally finite in $\RR$.

Now let
$$
\mathcal B=\{(0,1/n):n\ge1\}.
$$
For $x\in(0,1)$, choose a neighborhood $V\subset(0,1)$ whose left endpoint is positive, say $V\subset(a,1)$ with $a>0$. If $n>1/a$, then $(0,1/n)\subset(0,a)$, so it misses $V$. Thus only finitely many members of $\mathcal B$ meet $V$, and $\mathcal B$ is locally finite in $(0,1)$. In $\RR$, however, every neighborhood of $0$ meets every sufficiently small interval $(0,1/n)$, hence infinitely many members of $\mathcal B$. So $\mathcal B$ is not locally finite in $\RR$.

Finally let
$$
\mathcal C=\{(1/(n+1),1/n):n\ge1\}.
$$
For each $x\in(0,1)$, choose a sufficiently small neighborhood avoiding all but the one or two adjacent intervals whose endpoints bracket $x$; equivalently, since $1/n\to0$, once a neighborhood of $x$ has positive lower endpoint, all sufficiently large members of $\mathcal C$ lie below it. Hence $\mathcal C$ is locally finite in $(0,1)$. But every neighborhood of $0$ in $\RR$ meets $(1/(n+1),1/n)$ for all sufficiently large $n$, so $\mathcal C$ is not locally finite in $\RR$.
:::
