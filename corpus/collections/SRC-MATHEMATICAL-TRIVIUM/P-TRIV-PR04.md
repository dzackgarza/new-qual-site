---
schema: qual/card@1
id: P-TRIV-PR04
kind: problem
title: Probability that the $j$th student draws a lucky ticket
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the broken range 1 <= j <= N against Probability Problem 4 on page 27 of the source PDF.
---

::: {.problem}
Among $N$ tickets for $N$ students there are $n$ happy tickets.
The students take the tickets one by one, each takes one random ticket.
What is the probability that $j$'s student gets a happy ticket, $1 \leqslant j \leqslant N$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Drawing the tickets sequentially without replacement produces a uniformly random permutation of the $N$ tickets.


::: pf-proof

For any prescribed ordered list of all $N$ tickets, the probability that the draws occur in that order is
$$
\frac1N\frac1{N-1}\cdots\frac11=\frac1{N!}.
$$
Thus every permutation is equally likely.

:::

:::

::: {.pf-step #s1-2}

Consequently, the ticket in position $j$ is uniformly distributed among the $N$ tickets.


::: pf-proof

Fix any ticket. Among the $N!$ permutations from step [](#s1-1){.pf-ref}, exactly $(N-1)!$ place that ticket in position $j$. Hence its probability of occupying position $j$ is $(N-1)!/N!=1/N$, independently of $j$.

:::

:::

::: {.pf-step #s1-3}

Since exactly $n$ tickets are happy, the probability that student $j$ receives one is
$$
\boxed{\frac nN}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, each of the $N$ tickets has probability $1/N$ of being drawn in position $j$. The $n$ favorable tickets are disjoint possibilities, so their probabilities sum to $n/N$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested probability for every $1\leq j\leq N$.

:::

:::

:::
