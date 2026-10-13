---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-08
kind: problem
title: Continuity and uniform continuity of a rational function
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Uniform Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(June 2009 #1) Give an $\epsilon$-$\delta$ proof that $$f(x)=\frac{x^2}{1-x^2}$$ is continuous on $(0,1)$.
Is $f$ uniformly continuous on $(0,1)$?
Prove your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $f(x)=x^2/(1-x^2)$ is continuous at each $a\in(0,1)$.

::: pf-proof

Fix $a\in(0,1)$ and $\varepsilon>0$, and write $d=1-a^2>0$. Choose
\[
\delta=\min\left\{\frac d4,\frac{\varepsilon d^2}{4}\right\}.
\]
For $x\in(0,1)$ with $|x-a|<\delta$, the inequality $x+a<2$ gives $|x^2-a^2|<2\delta\leq d/2$. Therefore $1-x^2>d/2$, and
\[
|f(x)-f(a)|
=\frac{|x^2-a^2|}{(1-x^2)(1-a^2)}
<\frac{4|x-a|}{d^2}\leq\frac{4\delta}{d^2}\leq\varepsilon.
\]
This establishes continuity by the $\varepsilon$-$\delta$ criterion.

:::

:::

::: {.pf-step #s2}

The function $f$ is not uniformly continuous on $(0,1)$.

::: pf-proof

For integers $n\geq2$, put $x_n=1-1/n$ and $y_n=1-1/(2n)$. Then $0<x_n<y_n<1$ and $|x_n-y_n|=1/(2n)\to0$. Rewriting $f(t)=1/(1-t^2)-1$ gives
\[
f(y_n)-f(x_n)
=\frac{4n^2}{4n-1}-\frac{n^2}{2n-1}
=\frac{n^2(4n-3)}{(4n-1)(2n-1)}.
\]
For $n\geq2$, this difference is at least $n/4$, since $4n-3\geq2n$ and $(4n-1)(2n-1)\leq8n^2$. In particular it exceeds $1/2$ for all $n\geq3$. Given any $\delta>0$, choosing $n\geq3$ with $1/(2n)<\delta$ violates uniform continuity with $\varepsilon=1/2$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives continuity at every point of the domain, and step [](#s2){.pf-ref} disproves uniform continuity.

:::

:::

:::
