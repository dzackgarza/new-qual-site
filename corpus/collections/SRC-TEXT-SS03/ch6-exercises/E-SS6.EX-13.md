---
schema: qual/card@1
id: E-SS6.EX-13
kind: problem
title: "SS 6.13: Second derivative of log Gamma as a summed series"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
13. Prove that

$$
\frac {d ^ {2} \log \Gamma (s)}{d s ^ {2}} = \sum_ {n = 0} ^ {\infty} \frac {1}{(s + n) ^ {2}}
$$

whenever s is a positive number.
Show that if the left-hand side is interpreted as $( \Gamma ^ { \prime } / \Gamma ) ^ { \prime }$ , then the above formula also holds for all complex numbers s with $s \neq 0 , - 1 , - 2 , . . .$
:::

::: {.solution}
Start from the Weierstrass product
\[
\frac1{\Gamma(s)}=s e^{\gamma s}\prod_{n=1}^{\infty}\left(1+\frac{s}{n}\right)e^{-s/n}.
\]
On compact subsets avoiding $0,-1,-2,\ldots$, logarithmic differentiation is justified by locally uniform convergence and gives
\[
-\frac{\Gamma'(s)}{\Gamma(s)}
=\frac1s+\gamma+\sum_{n=1}^{\infty}\left(\frac1{s+n}-\frac1n\right).
\]
Differentiating once more, again locally uniformly,
\[
-\left(\frac{\Gamma'}{\Gamma}\right)'(s)
=-\frac1{s^2}-\sum_{n=1}^{\infty}\frac1{(s+n)^2}.
\]
Hence
\[
\left(\frac{\Gamma'}{\Gamma}\right)'(s)
=\sum_{n=0}^{\infty}\frac1{(s+n)^2}.
\]
For positive real $s$, $(\Gamma'/\Gamma)'=d^2(\log\Gamma)/ds^2$, proving the stated formula. The same derivation holds for every complex $s\notin\{0,-1,-2,\ldots\}$, and the series is locally uniformly convergent there.
:::
