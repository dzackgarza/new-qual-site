---
schema: qual/card@1
id: P-PRACT20-W6-01
kind: problem
title: Continuity of the function equal to $x/2$ on $\QQ$ and $x/3$ off $\QQ$
classification:
  areas:
  - prelim
  topics:
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the two branches agree only at x = 0, which the solution proves together with continuity at 0 and failure at every other point
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. Density of the rationals and irrationals for the failure, and the bound abs f(x) <= abs x / 2 for continuity at 0
---

::: {.problem}
Where is the function
$$
f(x)=\begin{cases}x/2,&x\in\QQ,\\x/3,&x\in\RR\setminus\QQ\end{cases}
$$
continuous?
:::

::: {.solution}

Let $f(x)=x/2$ for $x\in\QQ$ and $f(x)=x/3$ for $x\in\RR\setminus\QQ$.

::: pf

::: {.pf-step #notcontinuous}

$f$ is discontinuous at every $x_0\ne0$.

::: pf-proof

Take $x_0\ne0$ and sequences $q_n\in\QQ$, $r_n\notin\QQ$ with $q_n\to x_0$ and
$r_n\to x_0$, possible since both $\QQ$ and its complement are dense. Then
$f(q_n)=q_n/2\to x_0/2$ and $f(r_n)=r_n/3\to x_0/3$, and these two limits
differ because $x_0\ne0$. So the limit of $f$ at $x_0$ does not exist, and $f$
is not continuous there.

:::

:::

::: {.pf-step #continuous}

$f$ is continuous at $0$.

::: pf-proof

For every $x$, $\abs{f(x)}\le\abs x/2$, since either $x$ is rational and
$\abs{f(x)}=\abs x/2$, or irrational and $\abs{f(x)}=\abs x/3\le\abs x/2$.
Given $\varepsilon>0$ take $\delta=2\varepsilon$; then $\abs x<\delta$ gives
$\abs{f(x)-f(0)}=\abs{f(x)}\le\abs x/2<\varepsilon$. So $f$ is continuous at
$0$, and this is the only point of continuity.

:::

:::

:::


:::
