---
schema: qual/card@1
id: P-WESRA12-2
kind: problem
title: 'Lebesgue-measure digit sets and a nearest-reciprocal function'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash renders the source interval as `{0,1}`; the decimal-expansion, Borel, and Lebesgue-measure context determines that the intended set is the interval $[0,1]$.
---

::: {.problem}
Let $X=[0,1]$ with its Borel $\sigma$-algebra and Lebesgue measure $\lambda$.

(a) Calculate the measure of each set:

1. $\{x\in X:\sin(2\pi/x)\le0\}$;

2. numbers $x=0.x_1x_2\cdots$ having no digit $x_i=7$;

3. numbers $x=0.x_1x_2\cdots$ for which $x_i=5$ and $x_{i+1}=6$ for some $i$.

(b) State the Dominated Convergence Theorem on $(X,\lambda)$.

(c) For $x\ne0$, choose a positive integer $n=n(x)$ for which the distance $d(x)$ from $x$ to $1/n$ is minimal, and define $f(x)=d(x)$ if $n$ is odd and $f(x)=0$ otherwise.
Explain why $f$ is integrable and calculate $\int_Xf\,d\lambda$.
:::
