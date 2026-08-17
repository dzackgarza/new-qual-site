---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-09
kind: problem
title: 'A conditionally convergent series has power-series radius one'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-functions
  - series-of-numbers
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 2005 #3b) If the series $\sum_{n=0}^{\infty}a_n$ converges conditionally, show that the radius of convergence of the power series $\sum_{n=0}^{\infty}a_nx^n$ is $1$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $R \ge 1$.
Proof: conditional convergence implies $a_n \to 0$ (nth-term test), so the sequence $(a_n)$ is bounded; say $|a_n| \le M$ for all $n$.
For $|x| < 1$, $|a_n x^n| \le M|x|^n$ and $\sum M|x|^n$ converges, so $\sum a_n x^n$ converges absolutely.
Hence the radius of convergence satisfies $R \ge 1$.
<1>2. $R \le 1$.
Proof: suppose $R > 1$.
Then $\sum a_n x^n$ converges absolutely at some $x_0 > 1$ (e.g. any $x_0 \in (1, R)$), i.e. $\sum |a_n|x_0^n < \infty$.
Since $x_0^n \ge 1$ for $x_0 > 1$, we get $\sum |a_n| < \infty$, i.e. $\sum a_n$ converges absolutely — contradicting that it converges only conditionally.
<1>3. Q.E.D. Proof: $R \ge 1$ and $R \le 1$, so $R = 1$.
:::
