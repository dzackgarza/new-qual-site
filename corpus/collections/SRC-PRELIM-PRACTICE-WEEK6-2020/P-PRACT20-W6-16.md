---
schema: qual/card@1
id: P-PRACT20-W6-16
kind: problem
title: Maximum of two independent geometric random variables
classification:
  areas:
  - prelim
  topics:
  - Probability
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray brace and restored the question mark, checked against Week6_solns.pdf (Problem 16).
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
    on the card: the statement was read and the computation redone from the weights: P(X<=3) = 7/8 and independence give the complement 49/64, so the answer is 15/64
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The sample space N x N with product weights, the geometric sum for P(X<=3), and the complementary event with independence
---

::: {.problem}
Suppose $X, Y$ are i.i.d. random variables taking value $n \in \NN$ with probability $\frac{1}{2^n}$. What is the probability that $\max\{X, Y\} > 3$?
:::

::: {.solution}

Take the sample space $\Omega=\NN\times\NN$ with the product weights
$P(X=m,Y=n)=2^{-m}2^{-n}$, which sum to $1$ over $\Omega$; the event is
$\{X>3\}\cup\{Y>3\}$.

::: pf

::: {.pf-step #complement}

$P(X\le3)=P(Y\le3)=\frac12+\frac14+\frac18=\frac78$.

::: pf-proof

The events $\{X=n\}$ for $n\in\NN$ are disjoint with total probability $1$,
since $\sum_{n\ge1}2^{-n}=1$. So
$P(X\le3)=\sum_{n=1}^{3}2^{-n}=2^{-1}+2^{-2}+2^{-3}=\frac78$, and the same
computation gives $P(Y\le3)=\frac78$.

:::

:::

::: {.pf-step #count}

$P(\max\{X,Y\}>3)=\left(1-\frac78\right)+\left(1-\frac78\right)-\left(1-\frac78\right)^2=\frac1{64}+\frac{16}{64}\cdot\ldots=\boxed{\frac{15}{64}}$;
equivalently $1-\left(\frac78\right)^2=\frac{64-49}{64}$.

::: pf-proof

$\{\max\{X,Y\}\le3\}=\{X\le3\}\cap\{Y\le3\}$, and $X,Y$ are independent
because the product weights factor, so its probability is
$\frac78\cdot\frac78=\frac{49}{64}$. The event in question is the complement,
with probability $1-\frac{49}{64}=\frac{15}{64}$. Counting directly over the
$3\times3$ rectangle would give the same: the complement consists of the
$64-49=15$ unit cells of the $8\times8$ weighted square outside the $7\times7$
sub-square when the masses $2^{-n}$ are viewed as dividing the unit interval
into lengths $2^{-n}$.

:::

:::

:::


:::
