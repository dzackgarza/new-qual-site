---
schema: qual/card@1
id: P-PRACT20-W6-18
kind: problem
title: Probability that $X<Y$ for $X$ uniform on $[0,3]$ and $Y$ uniform on $[0,4]$
classification:
  areas:
  - prelim
  topics:
  - Probability
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
    on the card: the statement was read and the computation redone as the area of the triangle-like region x < y in the 3 x 4 rectangle, giving 15/2 over 12
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The rectangle sample space with uniform area measure, the slice computation of the area of the event, and the division by the total area
---

::: {.problem}
If $X$ is drawn uniformly from $[0, 3]$ and $Y$ is drawn independently and uniformly from $[0, 4]$, what is the probability that $X < Y$?
:::

::: {.solution}

Take the sample space $\Omega=[0,3]\times[0,4]$ with the uniform probability
given by area divided by $3\cdot4=12$, so that $(X,Y)$ is uniform on the
rectangle; the event is $E=\{(x,y)\in\Omega:x<y\}$.

::: pf

::: {.pf-step #area}

The area of $E$ is $\int_0^3(4-x)\,dx=\frac{15}{2}$.

::: pf-proof

For a fixed $x\in[0,3]$ the condition $x<y$ with $y\in[0,4]$ describes the
interval $(x,4]$ of length $4-x$, so by Cavalieri (or Fubini for the indicator
of $E$) the area is $\int_0^3(4-x)\,dx=12-\frac92=\frac{15}{2}$. Equivalently
the complement $\{y<x\}$ inside the rectangle has area
$\int_0^3x\,dx=\frac92$, and indeed $\frac{15}{2}+\frac92=12$.

:::

:::

::: {.pf-step #count}

$P(X<Y)=\frac{15/2}{12}=\boxed{\frac58}$.

::: pf-proof

Independence of the two uniform draws means the joint distribution is the
uniform measure on the rectangle, so the probability of $E$ is its area
divided by the total area $12$. Hence
$P(X<Y)=\frac{15}{2}\cdot\frac1{12}=\frac{15}{24}=\frac58$; the boundary
$\{x=y\}$ is a line, of area zero, so $X\le Y$ has the same probability.

:::

:::

:::


:::
