---
schema: qual/card@1
id: E-SS1.EX-22
kind: problem
title: $\NN$ is not a finite disjoint union of arithmetic progressions with distinct steps
classification:
  areas:
    - complex-analysis
  topics: [Power Series, Generating Functions]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into numbered steps for issue #2: the generating-function identity, its extension to an
      identity of rational functions, the pole count at a primitive $D$-th root, and the conclusion $D=1$. No
      retained solution set covers this exercise (the collection retains the textbook, not a solutions manual),
      so the argument is the card's own; it was re-read for this pass.
---

::: {.exercise}
Let $\NN = \{1, 2, 3, \dots\}$ denote the set of positive integers. A subset $S \subset \NN$ is said to be in arithmetic progression if
$$
S = \{a, a+d, a+2d, a+3d, \dots\}
$$
where $a, d \in \NN$. Here $d$ is called the step of $S$.

Show that $\NN$ cannot be partitioned into a finite number of subsets that are in arithmetic progression with distinct steps (except for the trivial case $a = d = 1$).

[Hint: Write $\sum_{n \in \NN} z^n$ as a sum of terms of the type $\frac{z^a}{1 - z^d}$.]
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. A partition of $\NN$ into finitely many arithmetic progressions $S_{j}=\{a_{j}+kd_{j}:k\ge0\}$ with distinct positive steps $d_{1},\dots,d_{r}$ is supposed.

::: pf

::: {.pf-step #identity}
For $\abs{z}<1$, $\dfrac{z}{1-z}=\sum_{j=1}^{r}\dfrac{z^{a_{j}}}{1-z^{d_{j}}}$.

::: pf-proof
Since the $S_{j}$ partition $\NN$ and each is the progression with first term $a_{j}$ and step $d_{j}$,
$$
\frac{z}{1-z}=\sum_{n\ge1}z^{n}=\sum_{j=1}^{r}\sum_{k\ge0}z^{a_{j}+kd_{j}}=\sum_{j=1}^{r}z^{a_{j}}\sum_{k\ge0}\bigl(z^{d_{j}}\bigr)^{k}=\sum_{j=1}^{r}\frac{z^{a_{j}}}{1-z^{d_{j}}},
$$
the geometric series converging because $\abs{z^{d_{j}}}<1$.
:::

:::

::: {.pf-step #rational}
The identity holds as an identity of rational functions.

::: pf-proof
Both sides are rational functions of $z$: the left is $z/(1-z)$, and the right is a finite sum of quotients of polynomials. Their difference is a rational function vanishing on the open disc $\abs{z}<1$, which is infinite with an accumulation point, so it vanishes identically; hence the two rational functions are equal.
:::

:::

::: {.pf-step #pole}
If $D=\max_{j}d_{j}>1$, taking a primitive $D$-th root of unity $\zeta$ makes the right side of step [](#identity){.pf-ref} have a pole at $\zeta$ while the left side does not.

::: pf-proof
$\zeta\ne1$, so $1-\zeta\ne0$ and $z/(1-z)$ is regular at $\zeta$. On the right, the denominator $1-z^{d_{j}}$ vanishes at $\zeta$ exactly when $\zeta^{d_{j}}=1$, that is when $D\mid d_{j}$; since $1\le d_{j}\le D$, this holds exactly for the index $j$ with $d_{j}=D$, and the steps are distinct so there is just one such index. At that index the numerator $\zeta^{a_{j}}$ is nonzero, so the term has a pole at $\zeta$; the other terms are regular there. Summing, the right side has a pole at $\zeta$, contradicting the equality of rational functions.
:::

:::

::: {.pf-step}
The only such partition is the trivial one.

::: pf-proof
Step [](#pole){.pf-ref} rules out $D>1$, so $D=1$: every step equals $1$, and since the steps are distinct there is only one progression, $S_{1}=\{a_{1},a_{1}+1,a_{1}+2,\dots\}$. That set is all of $\NN$ exactly when $a_{1}=1$, which is the trivial case $a=d=1$. So no nontrivial partition of $\NN$ into finitely many arithmetic progressions with distinct steps exists.
:::

:::

:::
:::
