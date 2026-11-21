---
schema: qual/card@1
id: P-SD42B
kind: problem
title: Bounds on alternating partial sums of a decreasing positive sequence
classification:
  areas:
  - prelim
  topics:
  - Series of Numbers
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $a_0, a_1, a_2, \ldots$ be a decreasing sequence of positive real numbers.
Prove that for every nonnegative integer $m$, $$0 \le \sum_{i=0}^{m}(-1)^i a_i \le a_0.$$ (Hint: $\sum_{i=0}^{m+1}(-1)^i a_i = a_0 - \sum_{i=0}^{m}(-1)^i a_{i+1}$.)
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper (`assets/attachments/grad_prelim_Fall05.pdf`) and no solutions sheet accompanies it, so the argument below is the card's own. It groups the alternating sum into nonnegative differences, which is quicker than the induction suggested by the problem's hint; both give the same two bounds.

Throughout, $(a_{i})_{i\geq0}$ is a decreasing sequence of positive reals, that is $a_{0}\geq a_{1}\geq a_{2}\geq\cdots>0$, and
$$
S_{m}\coloneqq\sum_{i=0}^{m}(-1)^{i}a_{i}.
$$

::: pf

::: {.pf-step #nonnegative-differences}
Every difference $a_{i}-a_{i+1}$ is nonnegative, and $a_{0}>0$.

::: pf-proof
The sequence is decreasing, so $a_{i}\geq a_{i+1}$ and the difference is $\geq0$; positivity of all terms gives $a_{0}>0$.
:::

:::

::: {.pf-step #lower}
$S_{m}\geq0$ for every $m\geq0$.

:::: pf-proof

::: {.pf-step #lower-odd}
If $m=2r+1$ is odd, $S_{m}=(a_{0}-a_{1})+(a_{2}-a_{3})+\cdots+(a_{2r}-a_{2r+1})\geq0$.

::: pf-proof
The terms of $S_{m}$ are paired as $\big(a_{2j}-a_{2j+1}\big)$ for $j=0,\dots,r$; each pair is a single difference $a_{2j}-a_{2j+1}$, and each such difference is nonnegative by step [](#nonnegative-differences){.pf-ref}, so the sum of the pairs is nonnegative.
:::

:::

::: {.pf-step #lower-even}
If $m=2r$ is even, $S_{m}=(a_{0}-a_{1})+\cdots+(a_{2r-2}-a_{2r-1})+a_{2r}\geq0$.

::: pf-proof
Here the summands are paired as $\big(a_{2j}-a_{2j+1}\big)$ for $j=0,\dots,r-1$ together with the unpaired last term $+a_{2r}$; the pairs are nonnegative by step [](#nonnegative-differences){.pf-ref} and $a_{2r}>0$, so the total is positive. For $r=0$, that is $m=0$, the display reads $S_{0}=a_{0}>0$.
:::

:::

::::

:::

::: {.pf-step #upper}
$S_{m}\leq a_{0}$ for every $m\geq0$.

:::: pf-proof

::: {.pf-step #upper-even}
If $m=2r$, $S_{m}=a_{0}-(a_{1}-a_{2})-\cdots-(a_{2r-1}-a_{2r})\leq a_{0}$.

::: pf-proof
Writing $S_{m}=a_{0}-\sum_{j=1}^{r}\big(a_{2j-1}-a_{2j}\big)$, each subtracted difference is nonnegative by step [](#nonnegative-differences){.pf-ref}, so subtracting their sum from $a_{0}$ cannot increase it. For $r=0$ the empty sum leaves $S_{0}=a_{0}$.
:::

:::

::: {.pf-step #upper-odd}
If $m=2r+1$, $S_{m}=a_{0}-(a_{1}-a_{2})-\cdots-(a_{2r-1}-a_{2r})-a_{2r+1}\leq a_{0}$.

::: pf-proof
Same decomposition as the even case, with the extra term $-a_{2r+1}$, which is negative because $a_{2r+1}>0$; subtracting nonnegative quantities and a positive one from $a_{0}$ gives a value at most $a_{0}$.
:::

:::

::::

:::

::: pf-step
Therefore $0\leq\sum_{i=0}^{m}(-1)^{i}a_{i}\leq a_{0}$ for every $m\geq0$.

::: pf-proof
Steps [](#lower){.pf-ref} and [](#upper){.pf-ref} give the two inequalities, each by the parity split of $m$; the upper and lower bounds hold simultaneously for every $m$, which is the claim.
:::

:::

:::

:::
