---
schema: qual/card@1
id: P-5UQSK
kind: problem
title: Equicontinuity on $[a,b]$ of differentiable functions with $|f(a)|\le M$ and
  $|f'|\le M$
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $M<\infty$ and $\mathcal{F} \subseteq C[a,b]$.
Assume that each $f \in \mathcal{F}$ is differentiable on $(a,b)$ and satisfies $|f(a)| \leq M$ and $|f'(x)| \leq M$ for all $x \in (a,b)$.
Prove that $\mathcal{F}$ is equicontinuous on $[a,b]$.
:::

::: {.solution}
<1>1. Every $f \in \mathcal F$ is Lipschitz with constant $M$: $|f(x) - f(y)| \le M|x - y|$ for all $x, y \in [a,b]$.

::: {.proof}
The assertion is immediate if $\mathcal F$ is empty. Otherwise $|f'(x)|\le M$ implies $M\ge0$. For $a\le x<y\le b$, continuity on $[x,y]$ and differentiability on $(x,y)$ permit the mean value theorem: there is $c\in(x,y)$ such that $f(y)-f(x)=f'(c)(y-x)$. Taking absolute values proves the bound; the case $x=y$ is immediate.
:::

<1>2. $\mathcal F$ is equicontinuous on $[a,b]$.

<2>1. For every $\varepsilon>0$, the number $\delta=\varepsilon/(M+1)$ is positive and independent of $f\in\mathcal F$ and $x,y\in[a,b]$.

::: {.proof}
If $\mathcal F$ is nonempty, step <1>1 gives $M\ge0$, so $M+1>0$. If $\mathcal F$ is empty, equicontinuity is vacuous and any $\delta>0$ works.
:::

<2>2. Whenever $x,y\in[a,b]$ satisfy $|x-y|<\delta$, one has $|f(x)-f(y)|<\varepsilon$ for every $f\in\mathcal F$.

::: {.proof}
By step <1>1, $|f(x)-f(y)|\le M|x-y|<M\varepsilon/(M+1)<\varepsilon$ for $M>0$. If $M=0$, the bound in step <1>1 is zero, giving the same conclusion.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 establish the epsilon-delta criterion uniformly over the family.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 proves equicontinuity on $[a,b]$.
:::
:::

For every $f\in\mathcal F$, the same Lipschitz estimate also gives the uniform bound $|f(x)|\le M+M(b-a)$, using $|f(a)|\le M$.
:::
