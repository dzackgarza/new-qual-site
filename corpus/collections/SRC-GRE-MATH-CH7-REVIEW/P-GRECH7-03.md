---
schema: qual/card@1
id: P-GRECH7-03
kind: problem
title: Number of lottery tickets needed to guarantee a jackpot
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 3 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
In a State Lottery, players choose 6 numbers from among the integers 1 through 51. The jackpot is awarded if the 6 numbers selected match the 6 numbers drawn. What's the minimum number of tickets someone would need to purchase in order to guarantee winning?

(A) 720
(B) 18,009,460
(C) 377,149,517
(D) 12,966,811,200
(E) 17,596,287,801
:::

::: pf

::: pf-step

A guaranteed win requires one ticket for every $6$-element subset of $\{1,\dots,51\}$.


::: pf-proof

The six numbers drawn form an unordered $6$-element subset. A ticket wins exactly for the one subset printed on it. If some $6$-element subset were omitted from the purchased tickets, that subset could be drawn and no purchased ticket would win. Conversely, purchasing one ticket for every possible subset guarantees that the drawn subset appears on one of the tickets.

:::

:::

::: pf-step

The number of such subsets is
$$
\binom{51}{6}=18{,}009{,}460.
$$


::: pf-proof

By the binomial-coefficient formula,
$$
\begin{aligned}
\binom{51}{6}
&=\frac{51\cdot50\cdot49\cdot48\cdot47\cdot46}{6!}\\
&=\frac{51\cdot50\cdot49\cdot48\cdot47\cdot46}{720}\\
&=18{,}009{,}460.
\end{aligned}
$$

:::

:::

::: pf-step

Therefore the minimum number of tickets is
$$
\boxed{18{,}009{,}460},
$$
so the answer is (B).


::: pf-proof

Step <1>1 shows that every possible $6$-element subset is both necessary and sufficient, and step <1>2 counts those subsets.

:::

:::

::: pf-qed

Step <1>3 gives the required minimum.

:::

:::
