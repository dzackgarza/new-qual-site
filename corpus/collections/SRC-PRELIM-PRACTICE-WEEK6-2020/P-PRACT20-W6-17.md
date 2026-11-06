---
schema: qual/card@1
id: P-PRACT20-W6-17
kind: problem
title: Probability that neither of two numbers from $1$ to $10$ is the square of the other
classification:
  areas:
  - prelim
  topics:
  - Probability
  - Combinatorics
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
    on the card: the statement was read and the count redone: the ordered pairs with one entry the square of the other are (1,1), (2,4), (4,2), (3,9), (9,3), five of the hundred, leaving 19/20
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The 10 x 10 sample space, the enumeration of the five bad ordered pairs with the overlap at (1,1) accounted for, and the complementary count
---

::: {.problem}
Two random numbers are drawn uniformly and independently from $\{1, \ldots, 10\}$. What is the probability that neither is the square of the other?
:::

::: {.solution}

Take the sample space $\Omega=\{1,\dots,10\}\times\{1,\dots,10\}$ of ordered
pairs of draws, with all $100$ outcomes equally likely.

::: pf

::: {.pf-step #bad}

The pairs for which one entry is the square of the other are
$(1,1),(2,4),(4,2),(3,9),(9,3)$.

::: pf-proof

The condition is $y=x^2$ or $x=y^2$. Both entries lie in $\{1,\dots,10\}$, so
$y=x^2$ forces $x\in\{1,2,3\}$, giving $(1,1),(2,4),(3,9)$; and $x=y^2$ gives
the transposes $(1,1),(4,2),(9,3)$. The two lists overlap only in $(1,1)$, so
the union has $3+3-1=5$ ordered pairs.

:::

:::

::: {.pf-step #count}

The probability that neither is the square of the other is
$\frac{100-5}{100}=\boxed{\frac{19}{20}}$.

::: pf-proof

The complement of the bad set has $100-5=95$ outcomes, and since the $100$
outcomes of the sample space are equally likely, its probability is
$\frac{95}{100}=\frac{19}{20}$. Equivalently, the probability that at least
one is the square of the other is $\frac{5}{100}=\frac1{20}$.

:::

:::

:::


:::
