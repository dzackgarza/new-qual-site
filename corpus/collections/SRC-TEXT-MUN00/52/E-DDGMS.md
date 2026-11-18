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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the reverse of a product, the two sides of the
    computation as the same product of four path classes, and the associativity up to
    reparametrization. The argument is the card's own; no retained set is cited. Munkres §52
    Exercise 6, printed p. 334. The printed statement needed no repair.
---

::: {.exercise}

Let $\alpha$ be a path in $X$ from $x_0$ to $x_1$; let $\beta$ be a path in $X$ from $x_1$ to $x_2$.
Show that if $\gamma = \alpha * \beta$, then $\hat{\gamma} = \hat{\beta} \circ \hat{\alpha}$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Munkres §52 Exercise 6, printed p. 334, with the definition of the change-of-basepoint map $\widehat\delta([f])=[\bar\delta*f*\delta]$ for a path $\delta$ from $u$ to $v$ and a loop $f$ at $u$.

::: pf

::: {.pf-step #reverse}
$\overline{\alpha*\beta}=\bar\beta*\bar\alpha$.

::: pf-proof
The reverse of a path is given by $\bar\delta(s)=\delta(1-s)$. For the product $\gamma=\alpha*\beta$, which traverses $\alpha$ on $[0,\tfrac12]$ and $\beta$ on $[\tfrac12,1]$, the reverse traverses first $\beta$ backwards and then $\alpha$ backwards, which is $\bar\beta*\bar\alpha$; formally the two parametrizations differ by the reparametrization $s\mapsto1-s$, so these paths are equal after reparametrization.
:::

:::

::: {.pf-step #computation}
For every loop $f$ at $x_{0}$, $\ \widehat\gamma([f])=\big(\widehat\beta\circ\widehat\alpha\big)([f])$.

::: pf-proof
$\gamma$ is a path from $x_{0}$ to $x_{2}$ and
$$
\widehat\gamma([f])=[\bar\gamma*f*\gamma]=[\bar\beta*\bar\alpha*f*\alpha*\beta],
$$
using step [](#reverse){.pf-ref}. On the other hand $\widehat\alpha([f])=[\bar\alpha*f*\alpha]$ is a loop class at $x_{1}$, a path from $x_{1}$ to $x_{2}$ is $\beta$, and
$$
\widehat\beta\big([\bar\alpha*f*\alpha]\big)=[\bar\beta*(\bar\alpha*f*\alpha)*\beta],
$$
which is the same product. The two expressions differ only in the bracketing of a product of four path classes, and path multiplication is associative up to the standard reparametrization homotopy, which is an equality of homotopy classes.
:::

:::

::: {.pf-step}
$\widehat\gamma=\widehat\beta\circ\widehat\alpha$.

::: pf-proof
Step [](#computation){.pf-ref} shows the two maps agree on every class $[f]$ of a loop at $x_{0}$, which is the whole domain $\pi_{1}(X,x_{0})$ of both.
:::

:::

:::
:::
