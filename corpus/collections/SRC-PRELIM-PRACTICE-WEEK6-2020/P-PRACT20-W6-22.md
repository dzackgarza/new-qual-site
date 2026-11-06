---
schema: qual/card@1
id: P-PRACT20-W6-22
kind: problem
title: Factorials ending in exactly $99$ zeros
classification:
  areas:
  - prelim
  topics:
  - Number Theory
  - Factorials
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
    on the card: the statement was read and the count redone: v_5(399!) = 97, v_5(404!) = 99, the jump of two at 400 because 25 divides it, and the next jump at 405
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The trailing-zero formula through 5-adic valuations, the monotonicity and step behaviour, the determination of the interval 400 to 404, and the count of five
---

::: {.problem}
For how many positive integers $k$ does $k!$ end in exactly $99$ zeros?
:::

::: {.solution}

For a positive integer $k$ let $v_5(k!)=\sum_{i\ge1}\big\lfloor
k/5^i\big\rfloor$ be the exponent of $5$ in $k!$; the number of trailing zeros
of $k!$ is $\min(v_2(k!),v_5(k!))=v_5(k!)$, since $v_2\ge v_5$.

::: pf

::: {.pf-step #formula}

The number of trailing zeros of $k!$ is $v_5(k!)$, and $v_5$ is nondecreasing
in $k$, increasing by one exactly when $5^j\mid k$ for some $j$.

::: pf-proof

Trailing zeros are the factors $10=2\cdot5$, so the count is $\min(v_2,v_5)$;
each multiple of $5$ up to $k$ contributes at least one factor $5$, and the
multiples of $2$ are more numerous, so $v_2(k!)\ge v_5(k!)$ and the minimum is
$v_5(k!)$. The sum formula counts, for each $i$, the multiples of $5^i$ up to
$k$. Since $v_5((k+1)!)-v_5(k!)$ is the exponent of $5$ in $k+1$, the function
increases by one exactly at multiples of $5$ that are not multiples of $25$,
by two at multiples of $25$ not of $125$, and so on; in particular it never
decreases.

:::

:::

::: {.pf-step #value}

$v_5(k!)=99$ exactly for $k=400,401,402,403,404$.

::: pf-proof

$v_5(399!)=\lfloor\frac{399}5\rfloor+\lfloor\frac{399}{25}\rfloor+\lfloor\frac{399}{125}\rfloor=79+15+3=97$
and $v_5(404!)=80+16+3=99$, so on the way from $399$ to $404$ the count rises
from $97$ to $99$. It rises at multiples of $5$, and the only multiple of $5$
strictly between $399$ and $405$ is $400$; since $400$ is divisible by $25$
but not by $125$, it contributes two, so $v_5(400!)=99$ and $v_5$ stays at
$99$ until the next multiple of $5$, which is $405$, where
$v_5(405!)=81+16+3=100$.

:::

:::

::: {.pf-step #answer}

There are $\boxed{5}$ positive integers $k$ for which $k!$ ends in exactly
$99$ zeros, namely $400\le k\le404$.

::: pf-proof

By steps [](#formula){.pf-ref} and [](#value){.pf-ref} the set of $k$ with
$v_5(k!)=99$ is exactly $\{400,401,402,403,404\}$, a set of five integers; and
$v_5$ is nondecreasing, so no smaller or larger $k$ qualifies. Hence the
answer is $5$.

:::

:::

:::


:::
