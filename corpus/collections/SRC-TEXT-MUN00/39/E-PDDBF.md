---
schema: qual/card@1
id: E-PDDBF
kind: problem
title: A point-finite open covering that is not locally finite
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
    Checked against Munkres, Topology (2000), Section 39 Exercise 2, printed p. 247, with the definitions of point-finite and locally finite, and the fact that $1/n\to0$. No correction was needed.
---

::: {.exercise}

Find a point-finite open covering $\mathcal{A}$ of $\RR$ that is not locally finite.
(The collection $\mathcal{A}$ is point-finite if each point of $\RR$ lies in only finitely many elements of $\mathcal{A}$.)
:::

::: {.solution}
For $n\ge2$, put
$$
U_n=\left(\frac1{n+1},\frac1{n-1}\right),
$$
and let
$$
\mathcal A=\{(-\infty,1),(0,\infty)\}\cup\{U_n:n\ge2\}.
$$
This is an open covering of $\RR$: the first two sets already cover $\RR$.

It is point-finite. If $x\le0$, then $x$ lies in none of the $U_n$. If $x>0$, choose $N$ with $1/(N-1)<x$. Then for every $n\ge N$,
$$
U_n\subset\left(0,\frac1{N-1}\right),
$$
so $x\notin U_n$. Hence each point belongs to only finitely many of the $U_n$, and therefore to only finitely many members of $\mathcal A$.

However, $\mathcal A$ is not locally finite at $0$. Every neighborhood $(-\varepsilon,\varepsilon)$ of $0$ meets $U_n$ for all sufficiently large $n$, since $1/n\to0$. Thus every neighborhood of $0$ meets infinitely many members of $\mathcal A$.
:::
