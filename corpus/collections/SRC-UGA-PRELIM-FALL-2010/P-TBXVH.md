---
schema: qual/card@1
id: P-TBXVH
kind: problem
title: The $\varepsilon$-$\delta$ definition of $\lim_{x\to a}f(x)=\ell$, and $\lim_{x\to
  2}\frac{2x+1}{x^2+1}$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Suppose $f: \mathbb{R} \to \mathbb{R}$.

a. Give the $\delta$-$\varepsilon$ definition of $\lim_{x \to a} f(x) = \ell$.
b. Determine the limit and use the definition to prove your answer: $$\lim_{x \to 2} \frac{2x+1}{x^2+1} = ?$$
:::

::: {.solution}
The statement $\lim_{x\to a}f(x)=\ell$ means: for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
0<|x-a|<\delta\implies |f(x)-\ell|<\varepsilon.
\]

Here the candidate limit is
\[
\frac{2(2)+1}{2^2+1}=1.
\]
Moreover
\[
\left|\frac{2x+1}{x^2+1}-1\right|
=\frac{|x(2-x)|}{x^2+1}.
\]
If $|x-2|<1$, then $|x|<3$, while $x^2+1\ge1$. Thus
\[
\left|\frac{2x+1}{x^2+1}-1\right|\le3|x-2|.
\]
Given $\varepsilon>0$, choose
\[
\delta=\min\{1,\varepsilon/3\}.
\]
Then $0<|x-2|<\delta$ implies the displayed error is $<\varepsilon$. Hence the limit is $1$.
:::
