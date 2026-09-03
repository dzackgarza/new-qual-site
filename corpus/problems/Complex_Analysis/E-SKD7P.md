---
schema: qual/card@1
id: E-SKD7P
kind: problem
title: Power series converge uniformly on their radius of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Uniform Convergence
  - Convergence Tests
relations: []
review: draft
---

:::{.exercise}
Show that any power series converges uniformly within its radius of convergence.

:::

:::{.solution}
Write $S_N(z) \da \sum_{0\leq k\leq N} c_k (z-z_0)^k$ and $S \da \lim_{N\to\infty} S_N$.
Suppose $R\da \qty{\limsup_k \abs{c_k}^{1\over k} }\inv$ is the radius of convergence and let $r\leq R$, we'll show $S_N\to S$ uniformly on any disc $\abs{z-z_0}< r$.

Use the $M\dash$test: $\sum f_k$ converges if $\norm{f_k}_\infty\leq M_k$ where $\ts{M_k}\in \ell^1(\NN)$.
Define $f_k \da c_k (z-z_0)^k$, then 
\[
\norm{f_k}_\infty =\sup_{\abs{z-z_0}\leq r} \abs{c_k(z-z_0)^k} \leq \abs{c_k} r^k \da M_k
.\]
Then
\[
\sum_{k\geq 0} M_k = \sum_{k\geq 0} \abs{c_k} r^k
,\]
and the claim is that this converges.

Note that since $r\leq R$, we have convergence of 
\[
\sum_{k\geq 0} c_k r^k
.\]
Recall that root test:
\[
\sum_k a_k \text{ converges absolutely if } \limsup_k \abs{a_k}^{1\over k} < 1
.\]
Here we take $a_k \da c_k r^k$, then
\[
\limsup_k \abs{a_k}^{1\over k} 
&\da \limsup_k \abs{c_k r^k}^{1\over k} \\
&= \limsup_k \abs{c_k}^{1\over k} r \\
&< \limsup_k \abs{c_k}^{1\over k} R\\
&\da \limsup_k \abs{c_k}^{1\over k} \qty{\limsup_{k} \abs{c_k}^{1\over k} }\inv \\
&= 1
,\]
so $\sum_k \abs{c_k r^k} < \infty$.
Thus $\ts{M_k}\in \ell^1(\NN)$, and so $\sum_k f_k$ converges uniformly and absolutely on $\abs{z-z_0} = r < R$.
:::

