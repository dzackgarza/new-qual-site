---
schema: qual/card@1
id: P-WESRA13A-II2
kind: problem
title: 'Sets of measure greater than $1/2$: a positive-measure set of points lying in more than half of them'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Direct inspection of the retained PDF page resolves the garbled extracted threshold as $\mu(B_i)>1/2$.
---

::: {.problem}
Let $(X,\mathcal B,\mu)$ be a measure space with $\mu(X)=1$, and let $B_1,\dots,B_N\in\mathcal B$ satisfy
$$
\mu(B_i)>\frac12\qquad(1\le i\le N).
$$
Show that there is $C\in\mathcal B$ of positive measure such that for every $x\in C$,
$$
\frac1N\sum_{i=1}^N\chi_{B_i}(x)>\frac12.
$$
:::

::: {.solution}

Define the measurable function
$$
g(x)=\frac1N\sum_{i=1}^N\chi_{B_i}(x).
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\int_X g\,d\mu>\frac12.
$$


::: pf-proof

By linearity of the integral,
$$
\begin{aligned}
\int_X g\,d\mu
&=\frac1N\sum_{i=1}^N\int_X\chi_{B_i}\,d\mu\\
&=\frac1N\sum_{i=1}^N\mu(B_i).
\end{aligned}
$$
Every term in the average is strictly greater than $1/2$, so the average is strictly greater than $1/2$.

:::

:::

::: {.pf-step #s1-2}

The set
$$
C=\left\{x\in X:g(x)>\frac12\right\}
$$
has positive measure.


::: pf-proof

Suppose instead that $\mu(C)=0$. Then
$$
g(x)\leq\frac12
$$
for almost every $x\in X$. Since $g\geq0$ and $\mu(X)=1$, this would imply
$$
\int_Xg\,d\mu
\leq\frac12\mu(X)
=\frac12,
$$
contradicting step [](#s1-1){.pf-ref}. Hence $\mu(C)>0$.

:::

:::

::: {.pf-step #s1-3}

Every $x\in C$ satisfies
$$
\frac1N\sum_{i=1}^N\chi_{B_i}(x)>\frac12.
$$


::: pf-proof

This is exactly the defining inequality for membership in $C$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives a measurable set $C$ of positive measure, and step [](#s1-3){.pf-ref} gives the required pointwise inequality on it.

:::

:::

:::
