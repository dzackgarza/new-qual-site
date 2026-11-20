---
schema: qual/card@1
id: P-LQEAV
kind: problem
title: $\norm{a}_{\ell^q}\le\norm{a}_{\ell^p}$ for $0<p<q\le\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Norms
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Thirteen of the fifteen steps asserted their claim with no justification and each now carries one:
    the degenerate cases $\norm{a}_{\ell^p} = 0$ and $= \infty$ on the extended real line, the
    term-at-most-the-sum step and the monotonicity of $t \mapsto t^{1/p}$ that turn it into the bound
    $\abs{a_k} \le \norm{a}_{\ell^p}$, the definition of the supremum used in the $\ell^\infty$ case, and
    in the finite case the normalization, the equality $\norm{b}_{\ell^p} = 1$, the inequality
    $\abs{b_j} \le 1$, the exponent comparison $\abs{b_j}^q \le \abs{b_j}^p$ valid because $q > p$ and
    $\abs{b_j} \le 1$, and the two final monotone operations. The argument is unchanged and correct:
    the inequality holds for every $0 < p < q \le \infty$, with equality of the two cases covered by
    the closing qed. The card stands alone, with no collection provenance and no retained published
    solution, so the argument is the card's own. The statement is unchanged.
---

::: {.problem}
Show that for $0 < p < q \le \infty$,
$$
\norm{a}_{\ell^q} \le \norm{a}_{\ell^p}
$$
for any sequence $a = (a_j)_{j=1}^\infty \in \CC^\NN$, where $\norm{a}_{\ell^\infty} \coloneqq \sup_j \abs{a_j}$ and $\norm{a}_{\ell^r} \coloneqq \left(\sum_{j=1}^\infty \abs{a_j}^r\right)^{1/r}$ for $r < \infty$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
If $q = \infty$, then $\norm{a}_{\ell^\infty} \le \norm{a}_{\ell^p}$.

::: pf-proof

::: pf-step
If $\norm{a}_{\ell^p} = \infty$, then the right-hand side of $\norm{a}_{\ell^\infty} \le \norm{a}_{\ell^p}$ is $\infty$, and every extended real number is $\le \infty$, so the inequality holds.


::: pf-proof
The inequality is asserted between extended real numbers, since the right-hand side may be $+\infty$; $+\infty$ is the largest extended real, so the left-hand side is at most it whatever its value.
:::

:::

::: pf-step
Assume $\norm{a}_{\ell^p} < \infty$. For every fixed index $k \ge 1$:
$$\abs{a_k}^p \le \sum_{j=1}^\infty \abs{a_j}^p = \norm{a}_{\ell^p}^p.$$


::: pf-proof
The sum defining the $\ell^p$ norm consists of nonnegative terms, so each single term is at most the whole sum, and the sum is finite by the assumption in force in this step; the whole sum is $\norm{a}_{\ell^p}^p$ by definition.
:::

:::

::: pf-step
Taking the $(1/p)$-th power of both sides (since $t \mapsto t^{1/p}$ is strictly increasing on $[0, \infty)$):
$$\abs{a_k} \le \norm{a}_{\ell^p} \quad \text{for all } k \ge 1.$$


::: pf-proof
For $p > 0$ the map $t \mapsto t^{1/p}$ is strictly increasing on $[0,\infty)$, so applying it to the inequality of the previous step preserves the inequality, and $\left(\norm{a}_{\ell^p}^p\right)^{1/p} = \norm{a}_{\ell^p}$.
:::

:::

::: pf-step
Taking the supremum over all $k \ge 1$:
$$\norm{a}_{\ell^\infty} = \sup_{k \ge 1} \abs{a_k} \le \norm{a}_{\ell^p}.$$


::: pf-proof
The right-hand side is an upper bound for the set $\{\abs{a_k} : k \ge 1\}$ by the previous step, and a supremum is the least upper bound, so it is at most that bound; $\norm{a}_{\ell^\infty}$ is the supremum by definition.
:::

:::

:::

:::

::: {.pf-step #s2}
If $q < \infty$, then $\norm{a}_{\ell^q} \le \norm{a}_{\ell^p}$.

::: pf-proof

::: pf-step
If $\norm{a}_{\ell^p} = 0$, then $a_j = 0$ for all $j$, so $\norm{a}_{\ell^q} = 0 = \norm{a}_{\ell^p}$.


::: pf-proof
A sum of nonnegative terms is zero only when every term is zero, so $\abs{a_j}^p = 0$ and hence $a_j = 0$ for every $j$. Then every term of the $\ell^q$ sum vanishes too, so $\norm{a}_{\ell^q} = 0$, and $\norm{a}_{\ell^p} = 0$ is the hypothesis.
:::

:::

::: pf-step
If $\norm{a}_{\ell^p} = \infty$, the inequality holds.


::: pf-proof
The right-hand side is $+\infty$, the largest extended real, so the inequality holds whatever the left-hand side is.
:::

:::

::: pf-step
Assume $0 < \norm{a}_{\ell^p} < \infty$. Define the normalized sequence $b = (b_j)_{j=1}^\infty$ by $b_j = \frac{a_j}{\norm{a}_{\ell^p}}$.


::: pf-proof
The denominator is a positive finite real number by the assumption of this case, so the quotient is defined for every $j$; dividing by the norm is the normalization that makes the $\ell^p$ norm of $b$ equal to $1$, which the next step computes.
:::

:::

::: {.pf-step #normalized-norm}
The normalized sequence satisfies
$$\norm{b}_{\ell^p}^p = \sum_{j=1}^\infty \abs{b_j}^p = \sum_{j=1}^\infty \frac{\abs{a_j}^p}{\norm{a}_{\ell^p}^p} = 1.$$


::: pf-proof
Substituting $b_j = a_j/\norm{a}_{\ell^p}$ gives $\abs{b_j}^p = \abs{a_j}^p/\norm{a}_{\ell^p}^p$, since $\norm{a}_{\ell^p}$ is a positive scalar, and summing over $j$ gives the middle expression; the last equality is the definition of the $\ell^p$ norm, divided by itself.
:::

:::

::: pf-step
In particular, for every index $j \ge 1$, $\abs{b_j}^p \le \sum_{k=1}^\infty \abs{b_k}^p = 1$, which implies $\abs{b_j} \le 1$.


::: pf-proof
Each term of the $\ell^p$ sum is nonnegative and therefore at most the sum, which equals $1$ by step [](#normalized-norm){.pf-ref}; applying the increasing map $t \mapsto t^{1/p}$ to $\abs{b_j}^p \le 1$ gives $\abs{b_j} \le 1$.
:::

:::

::: {.pf-step #exponent-comparison}
Since $q > p > 0$ and $\abs{b_j} \le 1$, the exponent comparison gives
$$\abs{b_j}^q = \abs{b_j}^{q-p} \abs{b_j}^p \le 1^{q-p} \abs{b_j}^p = \abs{b_j}^p \quad \text{for every } j \ge 1.$$


::: pf-proof
The identity $\abs{b_j}^q = \abs{b_j}^{q-p}\abs{b_j}^p$ holds because $q = (q-p) + p$. Since $q - p > 0$ and $0 \le \abs{b_j} \le 1$, one has $\abs{b_j}^{q-p} \le 1$, and multiplying that by the nonnegative factor $\abs{b_j}^p$ gives the inequality.
:::

:::

::: {.pf-step #summed-bound}
Summing over all $j \ge 1$:
$$\norm{b}_{\ell^q}^q = \sum_{j=1}^\infty \abs{b_j}^q \le \sum_{j=1}^\infty \abs{b_j}^p = \norm{b}_{\ell^p}^p = 1.$$


::: pf-proof
Summing the inequality of step [](#exponent-comparison){.pf-ref} over $j$ preserves it because the terms are nonnegative and the sums may be infinite, and the right-hand side is $\norm{b}_{\ell^p}^p = 1$ by step [](#normalized-norm){.pf-ref}.
:::

:::

::: {.pf-step #root-bound}
Taking the $(1/q)$-th power gives $\norm{b}_{\ell^q} \le 1^{1/q} = 1$.


::: pf-proof
For $q > 0$ the map $t \mapsto t^{1/q}$ is increasing on $[0,\infty)$, so applying it to the inequality of step [](#summed-bound){.pf-ref} gives $\norm{b}_{\ell^q} \le 1^{1/q} = 1$.
:::

:::

::: pf-step
Multiplying both sides by the positive scalar $\norm{a}_{\ell^p}$:
$$\norm{a}_{\ell^q} = \norm{a}_{\ell^p} \norm{b}_{\ell^q} \le \norm{a}_{\ell^p} \cdot 1 = \norm{a}_{\ell^p}.$$


::: pf-proof
Dividing $\norm{b}_{\ell^q}^q = \sum_j \abs{a_j}^q/\norm{a}_{\ell^p}^q$ by the positive number $\norm{a}_{\ell^p}^q$ and taking $q$-th roots gives $\norm{a}_{\ell^q} = \norm{a}_{\ell^p}\norm{b}_{\ell^q}$, which is the displayed equality; multiplying the bound of step [](#root-bound){.pf-ref} by the positive scalar $\norm{a}_{\ell^p}$ gives the inequality.
:::

:::

:::

:::

::: pf-qed
Either $q = \infty$ or $p < q < \infty$, and steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the inequality in the two cases.
:::

:::

:::
