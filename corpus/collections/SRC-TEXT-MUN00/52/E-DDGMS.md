---
schema: qual/card@1
id: E-DDGMS
kind: problem
title: Change of base point along a composite path
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 52: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-52-the-fundamental-group/problem-2-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-52-the-fundamental-group/problem-2-solution.txt), and against Munkres, Topology (2000), Section 52
    Exercise 2, printed p. 334. dbFin's is the same chain of path-homotopy classes; the card writes the associativity step out. Nothing needed repair.
---

::: {.exercise}

Let $\alpha$ be a path in $X$ from $x_0$ to $x_1$; let $\beta$ be a path in $X$ from $x_1$ to $x_2$.
Show that if $\gamma = \alpha * \beta$, then $\hat{\gamma} = \hat{\beta} \circ \hat{\alpha}$.
:::

::: {.solution}
Recall that for a path $\delta$ from $u$ to $v$, the change-of-basepoint map is
$$
\widehat\delta([f])=[\bar\delta*f*\delta],
$$
with the convention that products of paths are traversed from left to right.

Let $\gamma=\alpha*\beta$. Then $\bar\gamma=\bar\beta*\bar\alpha$. Hence for a loop $f$ at $x_0$,
$$
\begin{aligned}
\widehat\gamma([f])
&=[\bar\gamma*f*\gamma]\\
&=[\bar\beta*\bar\alpha*f*\alpha*\beta]\\
&=\widehat\beta([\bar\alpha*f*\alpha])\\
&=(\widehat\beta\circ\widehat\alpha)([f]).
\end{aligned}
$$
Associativity here is associativity of path multiplication up to the standard reparametrization homotopy, which is enough on homotopy classes. Therefore
$$
\boxed{\widehat\gamma=\widehat\beta\circ\widehat\alpha}.
$$
:::
