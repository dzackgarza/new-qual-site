---
schema: qual/card@1
id: P-5IAA5
kind: problem
title: 'A function weighting an enumeration of the rationals by $1/n$ is discontinuous exactly at the rationals'
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-30
  note: 'Split from P-4FH62, where it was part (h).'
---

::: {.problem}
Let $\theset{r_n}_{n=1}^\infty$ be any enumeration of all the rationals in $[0,1]$ and define $f : [0,1] \to \RR$ by setting
$$
f(x) = \begin{cases} \frac{1}{n} & \text{if } x = r_n \\ 0 & \text{if } x \in [0,1] \setminus \QQ. \end{cases}
$$
Prove that $\lim_{x \to c} f(x) = 0$ for every $c \in [0,1]$ and conclude that the set of all points at which $f$ is discontinuous is precisely $[0,1] \cap \QQ$.
:::

::: {.solution}

::: pf

::: pf-step

$\lim_{x\to c}f(x)=0$ for every $c\in[0,1]$, and $f$ is discontinuous exactly on $[0,1]\cap\QQ$.

::: pf-proof

Given $\varepsilon>0$, choose $N$ with $1/N<\varepsilon$. Only the finitely many points $r_1,\ldots,r_N$ can have value at least $\varepsilon$. For a fixed $c$, choose a punctured neighborhood of $c$ in $[0,1]$ that contains none of those points. Then $\abs{f(x)}<\varepsilon$ throughout that punctured neighborhood, so $\lim_{x\to c}f(x)=0$. Hence $f$ is continuous at $c$ exactly when $f(c)=0$: at an irrational $c$, $f(c)=0$, and at $c=r_n$, $f(c)=1/n\neq0$.

:::

:::

:::

:::
