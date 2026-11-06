---
schema: qual/card@1
id: P-PRACT20-W6-19
kind: problem
title: Probability that the first player tosses heads first
classification:
  areas:
  - prelim
  topics:
  - Probability
  - Geometric Series
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
    on the card: the statement was read and the geometric series redone: the first player wins on the disjoint events T^{2k}H with probabilities 2^{-(2k+1)}, summing to 2/3
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The product sample space, the disjoint cylinders of the first head at an odd toss, and the geometric sum with the complementary check
---

::: {.problem}
Two players take turns tossing a fair coin; the winner is the first who tosses heads.
What is the probability that the first player wins?
:::

::: {.solution}

Take the sample space $\Omega=\{H,T\}^{\NN}$ of infinite sequences of tosses
with the product measure giving each sequence of $n$ specified first tosses
probability $2^{-n}$. The first player wins exactly when the first head occurs
at an odd-numbered toss.

::: pf

::: {.pf-step #disjoint}

The event "first head at toss $2k+1$" is $T^{2k}H$, of probability
$2^{-(2k+1)}$, and these events for $k\ge0$ are pairwise disjoint.

::: pf-proof

$T^{2k}H$ is the cylinder of sequences whose first $2k$ tosses are tails and
whose $(2k+1)$-st is heads, and its probability is $2^{-(2k+1)}$ by the
definition of the product measure. Two such cylinders with different $k$
prescribe different $(2k+1)$-st tosses, so a sequence cannot lie in both.

:::

:::

::: {.pf-step #sum}

$P(\text{first player
wins})=\sum_{k\ge0}2^{-(2k+1)}=\frac12\cdot\frac{1}{1-\frac14}=\boxed{\frac23}$.

::: pf-proof

The first player wins exactly on the disjoint union of the events $T^{2k}H$,
so by countable additivity the probability is the sum of their probabilities,
a geometric series with ratio $\frac14$ and first term $\frac12$, whose sum is
$\frac{1/2}{1-1/4}=\frac23$. The second player's winning probability is the
complementary sum $\sum_k2^{-(2k+2)}=\frac13$, and the two sum to $1$ because
the game ends with probability $1$: the probability that the first $2n$ tosses
are all tails is $4^{-n}\to0$.

:::

:::

:::


:::
