---
schema: qual/card@1
id: P-F12LM
kind: problem
title: $\varepsilon$-$\delta$ proof that $\lim_{x\to 2} 1/(x^2+1)=1/5$
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
Give an $\varepsilon$-$\delta$ proof that $\lim_{x \to 2} \frac{1}{x^2 + 1} = \frac{1}{5}$.
:::

::: {.solution}
We have
$$
\abs{\frac1{x^2+1}-\frac15}
=\frac{\abs{4-x^2}}{5(x^2+1)}
=\frac{\abs{x-2}\abs{x+2}}{5(x^2+1)}.
$$
If $\abs{x-2}<1$, then $1<x<3$, so $\abs{x+2}<5$ and $x^2+1>2$. Hence
$$
\abs{\frac1{x^2+1}-\frac15}<\frac12\abs{x-2}.
$$
Given $\varepsilon>0$, choose
$$
\delta=\min\{1,2\varepsilon\}.
$$
Then $0<\abs{x-2}<\delta$ implies the desired error is $<\varepsilon$.
:::
