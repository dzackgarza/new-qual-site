---
schema: qual/card@1
id: P-F07LM
kind: problem
title: $\delta$-$\varepsilon$ definition of a limit, and $\lim_{x\to 1} 1/(1+x^2)=1/2$
classification:
  areas:
  - prelim
  topics:
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
a. Complete the $\delta$-$\varepsilon$ definition of a limit: Given a function $f: \RR \to \RR$ and $a, L \in \RR$, $\lim_{x \to a} f(x) = L$ means ...

b. Using the definition, prove that $\lim_{x \to 1} \frac{1}{1 + x^2} = \frac{1}{2}$.
:::

::: {.solution}
The statement
$$
\lim_{x\to a}f(x)=L
$$
means that for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
0<\abs{x-a}<\delta\implies \abs{f(x)-L}<\varepsilon.
$$

For $f(x)=1/(1+x^2)$ at $a=1$,
$$
\abs{\frac1{1+x^2}-\frac12}
=\frac{\abs{1-x^2}}{2(1+x^2)}
=\frac{\abs{x-1}\abs{x+1}}{2(1+x^2)}.
$$
If $\abs{x-1}<1$, then $0<x<2$, hence $\abs{x+1}<3$ and $1+x^2\ge1$. Therefore
$$
\abs{\frac1{1+x^2}-\frac12}\le \frac32\abs{x-1}.
$$
Given $\varepsilon>0$, choose
$$
\delta=\min\left\{1,\frac{2\varepsilon}{3}\right\}.
$$
Then $0<\abs{x-1}<\delta$ implies the desired error is less than $\varepsilon$.
:::
