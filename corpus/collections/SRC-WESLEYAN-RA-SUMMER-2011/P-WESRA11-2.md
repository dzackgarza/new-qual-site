---
schema: qual/card@1
id: P-WESRA11-2
kind: problem
title: 'Almost-everywhere continuity versus equality almost everywhere to a continuous function'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $f:\RR\to\RR$ be Lebesgue measurable.
Compare the following conditions:

(i) $f$ is continuous at almost every point of $\RR$.

(ii) There is a continuous $g:\RR\to\RR$ such that $f=g$ almost everywhere.

Does either imply the other?
Give proofs or counterexamples.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Condition (i) does not imply condition (ii).


::: pf-proof

Define
$$
f(x)=\begin{cases}
0,&x<0,\\
1,&x\ge0.
\end{cases}
$$
This function is Lebesgue measurable and is continuous at every $x\ne0$, so it satisfies (i).

Suppose there were a continuous $g:\RR\to\RR$ with $f=g$ almost everywhere. On $(-\infty,0)$, the continuous function $g$ is equal to $0$ almost everywhere. It must therefore be identically $0$ there: if $g(x_0)\ne0$ at some $x_0<0$, continuity would make $g\ne0$ on an open interval of positive measure. Similarly, $g\equiv1$ on $(0,\infty)$. Continuity at $0$ would then require simultaneously $g(0)=0$ and $g(0)=1$, a contradiction. Thus (ii) fails.

:::

:::

::: {.pf-step #s1-2}

Condition (ii) does not imply condition (i).


::: pf-proof

Let
$$
f=\mathbf 1_{\QQ}
\qquad\text{and}\qquad
g\equiv0.
$$
The rationals are countable and hence have Lebesgue measure zero, so $f=g$ almost everywhere. Thus (ii) holds.

However, every open interval contains both rational and irrational points. Consequently every neighborhood of every $x\in\RR$ contains points where $f=1$ and points where $f=0$. Hence $f$ is discontinuous at every point, so (i) fails.

:::

:::

::: {.pf-step #s1-3}

Therefore $\boxed{\text{neither (i) nor (ii) implies the other}}$.


::: pf-proof

Step [](#s1-1){.pf-ref} disproves (i)$\Rightarrow$(ii), and step [](#s1-2){.pf-ref} disproves (ii)$\Rightarrow$(i).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required comparison.

:::

:::

:::
