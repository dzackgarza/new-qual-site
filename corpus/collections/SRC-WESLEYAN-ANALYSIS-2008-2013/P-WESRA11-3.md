---
schema: qual/card@1
id: P-WESRA11-3
kind: problem
title: 'Lebesgue outer measure and countable subadditivity'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
For $A\subset\RR$, define the Lebesgue outer measure $m^*(A)$.
Prove that for every sequence $(A_i)$ of subsets of $\RR$,
$$
m^*\!\left(\bigcup_{i=1}^\infty A_i\right)
\le \sum_{i=1}^\infty m^*(A_i).
$$
:::

::: {.solution}

For an interval $I\subset\RR$, write $\setmeasure{I}$ for its length.

::: pf

::: {.pf-step #s1-1}

For every $A\subseteq\RR$, its Lebesgue outer measure is
$$
\boxed{
m^*(A)
=\inf\left\{
\sum_{j=1}^\infty \setmeasure{I_j}:
A\subseteq\bigcup_{j=1}^\infty I_j,
\ I_j\text{ open intervals}
\right\}}.
$$

:::

::: {.pf-step #s1-2}

If $\sum_{i=1}^\infty m^*(A_i)=\infty$, then the required inequality holds.


::: pf-proof

The left side is nonnegative and takes values in $[0,\infty]$, so it is automatically at most $\infty$.

:::

:::

::: {.pf-step #s1-3}

Suppose $\sum_{i=1}^\infty m^*(A_i)<\infty$. For every $\varepsilon>0$ and every $i\ge1$, there is a countable family of open intervals $(I_{i,j})_{j\ge1}$ such that
$$
A_i\subseteq\bigcup_{j=1}^\infty I_{i,j}
$$
and
$$
\sum_{j=1}^\infty \setmeasure{I_{i,j}}
<m^*(A_i)+\frac{\varepsilon}{2^i}.
$$


::: pf-proof

Under the present assumption every $m^*(A_i)$ is finite. The assertion follows directly from the infimum in the definition in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

One has
$$
m^*\!\left(\bigcup_{i=1}^\infty A_i\right)
\le \sum_{i=1}^\infty m^*(A_i)+\varepsilon.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, the countable family $(I_{i,j})_{i,j\ge1}$ covers $\bigcup_i A_i$. Hence step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
m^*\!\left(\bigcup_{i=1}^\infty A_i\right)
&\le \sum_{i=1}^\infty\sum_{j=1}^\infty \setmeasure{I_{i,j}}\\
&<\sum_{i=1}^\infty\left(m^*(A_i)+\frac{\varepsilon}{2^i}\right)\\
&=\sum_{i=1}^\infty m^*(A_i)+\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
m^*\!\left(\bigcup_{i=1}^\infty A_i\right)
\le \sum_{i=1}^\infty m^*(A_i)}.
$$


::: pf-proof

If the right side is infinite, step [](#s1-2){.pf-ref} applies. Otherwise step [](#s1-4){.pf-ref} holds for every $\varepsilon>0$, so letting $\varepsilon\downarrow0$ gives the displayed inequality.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and step [](#s1-5){.pf-ref} proves countable subadditivity.

:::

:::

:::
