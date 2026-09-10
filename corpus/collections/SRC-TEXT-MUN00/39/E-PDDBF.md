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
---

::: {.exercise}

Find a point-finite open covering $\mathcal{A}$ of $\mathbb{R}$ that is not locally finite.
(The collection $\mathcal{A}$ is point-finite if each point of $\mathbb{R}$ lies in only finitely many elements of $\mathcal{A}$.)
:::

::: {.solution}
For \(n\ge2\), put
\[
U_n=\left(\frac1{n+1},\frac1{n-1}\right),
\]
and let
\[
\mathcal A=\{(-\infty,1),(0,\infty)\}\cup\{U_n:n\ge2\}.
\]
This is an open covering of \(\mathbb R\): the first two sets already cover \(\mathbb R\).

It is point-finite. If \(x\le0\), then \(x\) lies in none of the \(U_n\). If \(x>0\), choose \(N\) with \(1/(N-1)<x\). Then for every \(n\ge N\),
\[
U_n\subset\left(0,\frac1{N-1}\right),
\]
so \(x\notin U_n\). Hence each point belongs to only finitely many of the \(U_n\), and therefore to only finitely many members of \(\mathcal A\).

However, \(\mathcal A\) is not locally finite at \(0\). Every neighborhood \((-\varepsilon,\varepsilon)\) of \(0\) meets \(U_n\) for all sufficiently large \(n\), since \(1/n\to0\). Thus every neighborhood of \(0\) meets infinitely many members of \(\mathcal A\).
:::
