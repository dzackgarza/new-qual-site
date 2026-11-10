---
schema: qual/card@1
id: E-QSI4Y
kind: problem
title: The Tietze extension theorem implies the Urysohn lemma
classification:
  areas:
  - topology
  topics:
  - Urysohn Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: "Doug's World", "Munkres - Topology - Chapter
    4 Solutions" (30 August 2017), Problem 35.1, printed p. 12
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 35: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-35-the-tietze-extension-theorem/problem-1-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-35-the-tietze-extension-theorem/problem-1-solution.txt); checked
    against Munkres, Topology (2000), Section 35 Exercise 1, printed p. 223, Theorem 35.1 and the
    pasting lemma (Theorem 18.3). The argument is the card's: on the closed union A cup B the
    function equal to 0 on A and 1 on B is continuous because A and B are disjoint closed, hence
    also open, in the union; Tietze extends it to X; truncation puts the values in [0,1]. No
    correction to the mathematics was needed.
---

::: {.exercise}

Show that the Tietze extension theorem implies the Urysohn lemma.
:::

::: {.solution}
Let $A,B\subset X$ be disjoint closed subsets of a normal space $X$. The union $A\cup B$ is closed. Define
$$
f:A\cup B\to[-1,1]
$$
by $f=0$ on $A$ and $f=1$ on $B$. This is continuous because $A$ and $B$ are disjoint closed-and-open subsets of the subspace $A\cup B$.

By the Tietze extension theorem, $f$ extends to a continuous
$$
F:X\to[-1,1].
$$
Composing with the continuous truncation
$$
t(s)=\min\{1,\max\{0,s\}\}
$$
gives $u=t\circ F:X\to[0,1]$, with $u(A)=0$ and $u(B)=1$. This is exactly the Urysohn lemma.
:::
