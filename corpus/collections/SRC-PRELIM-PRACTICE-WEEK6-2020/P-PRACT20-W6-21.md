---
schema: qual/card@1
id: P-PRACT20-W6-21
kind: problem
title: Surjections from a $4$-element set onto a $3$-element set
classification:
  areas:
  - prelim
  topics:
  - Combinatorics
  - Inclusion-Exclusion
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray brace and restored the question mark, checked against Week6_solns.pdf (Problem 21).
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
    on the card: the statement was read and the count redone twice, by inclusion-exclusion giving 36 and by partitions into three nonempty blocks giving 6 times 6
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The total 3^4, the inclusion-exclusion count of functions missing a value, and the subtraction, cross-checked with Stirling numbers
---

::: {.problem}
How many surjective functions are there from $\{1, 2, 3, 4\}$ to $\{1, 2, 3\}$?
:::

::: {.solution}

A function $\{1,2,3,4\}\to\{1,2,3\}$ is surjective exactly when its image is
all of the three-element target; count by inclusion-exclusion over the missing
values.

::: pf

::: {.pf-step #total}

There are $3^4=81$ functions from a four-element set to a three-element set.

::: pf-proof

A function is determined by its four values, each chosen freely among three
possibilities, so there are $3\cdot3\cdot3\cdot3=81$.

:::

:::

::: {.pf-step #inclusion}

The number missing at least one value is $3\cdot2^4-3\cdot1^4=48-3=45$.

::: pf-proof

For a fixed value $v$ of the target, the functions missing $v$ are the
functions into the remaining two values, of which there are $2^4=16$; summing
over the three choices of $v$ counts $3\cdot16=48$ pairs (function, missing
value). A function missing two values was counted twice, once for each missing
value, and there are $3$ such functions, each constant into one of the three
values, i.e. $1^4=1$ function for each of the $\binom32=3$ pairs of missing
values. So by inclusion-exclusion the number missing at least one value is
$48-3=45$.

:::

:::

::: {.pf-step #surjective}

The number of surjections is $81-45=\boxed{36}$.

::: pf-proof

A function is surjective iff it misses no value, so the count is the total
minus those missing at least one value: $81-45=36$. Equivalently, by Stirling
numbers of the second kind, $3!\cdot S(4,3)=6\cdot6=36$, since a surjection is
a partition of the four-element set into three nonempty blocks together with a
bijection of the blocks to the target, and $S(4,3)=6$.

:::

:::

:::


:::
