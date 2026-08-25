---
schema: qual/card@1
id: E-SS6.PR-1
kind: exercise
title: "This problem provides further estimates for  and  near"
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta
relations: []
review: draft
---

::: exercise
1. This problem provides further estimates for $\zeta$ and $\zeta ^ { \prime }$ near $\operatorname { R e } ( s ) = 1$

(a) Use Proposition 2.5 and its corollary to prove

$$

\zeta (s) = \sum_ {1 \leq n <   N} n ^ {- s} - \frac {N ^ {s - 1}}{s - 1} + \sum_ {n \geq N} \delta_ {n} (s)

$$

for every integer $N \geq 2$ , whenever $\operatorname { R e } ( s ) > 0$

(b) Show that $| \zeta ( 1 + i t ) | = O ( \log | t | )$ , as $| t |  \infty$ by using the previous result with N =greatest integer in $| t | .$

(c) The second conclusion of Proposition 2.7 can be similarly refined.

(d) Show that if $t \neq 0$ and t is fixed, then the partial sums of the series $\textstyle \sum _ { n = 1 } ^ { \infty } 1 / n ^ { 1 + i t }$ are bounded, but the series does not converge.

2.∗ Prove that for $\operatorname { R e } ( s ) > 0$

$$

\zeta (s) = \frac {s}{s - 1} - s \int_ {1} ^ {\infty} \frac {\{x \}}{x ^ {s + 1}} d x

$$

where $\{ x \}$ is the fractional part of $x .$

3.∗ If $Q ( x ) = \{ x \} - 1 / 2$ , then we can write the expression in the previous problem as

$$

\zeta (s) = \frac {s}{s - 1} - \frac {1}{2} - s \int_ {1} ^ {\infty} \frac {Q (x)}{x ^ {s + 1}} d x.

$$

Let us construct $Q _ { k } ( x )$ recursively so that

$$

\int_ {0} ^ {1} Q _ {k} (x) d x = 0, \quad \frac {d Q _ {k + 1}}{d x} = Q _ {k} (x), \quad Q _ {0} (x) = Q (x) \quad \text { and } \quad Q _ {k} (x + 1) = Q _ {k} (x).

$$

Then we can write

$$

\zeta (s) = \frac {s}{s - 1} - \frac {1}{2} - s \int_ {1} ^ {\infty} \left(\frac {d ^ {k}}{d x ^ {k}} Q _ {k} (x)\right) x ^ {- s - 1} d x,
:::
