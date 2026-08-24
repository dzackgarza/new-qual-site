---
schema: qual/card@1
id: P-PJY52
kind: problem
title: If the series $\sum_{n=0}^\infty a_n$ converges
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Series of Numbers
relations: []
review: draft
---

::: problem
If the series $\sum_{n=0}^\infty a_n$ converges conditionally, show that the radius of convergence of the power series $\sum_{n=0}^\infty a_nx^n$ is 1.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $a_n \to 0$.
Proof: $\sum_{n\ge 0} a_n$ converges, so its terms tend to $0$.
Hence $(a_n)$ is bounded: $|a_n| \le C$ for all $n$.
<1>2. $R \ge 1$.
Proof: for $|x| < 1$, $|a_n x^n| \le C|x|^n$, and $\sum_n C|x|^n$ is a convergent geometric series; so $\sum_n a_n x^n$ converges absolutely for every $|x| < 1$.
<1>3. $R \le 1$.
Proof: if $R > 1$, the power series converges absolutely for every $|x| < R$, in particular at $x = 1$, so $\sum_n |a_n| < \infty$, contradicting conditional convergence.
<1>4. $R = 1$.
Proof: <1>2 and <1>3. <1>5. Q.E.D.
:::
