---
schema: qual/card@1
id: E-SS6.EX-14
kind: exercise
title: "This exercise gives an asymptotic formula for log n!"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
solved: false
---

::: exercise
14. This exercise gives an asymptotic formula for log n!. A more refined asymptotic formula for $\Gamma ( s )$ as $s \to \infty$ (Stirling’s formula) is given in Appendix A.

(a) Show that

$$

{\frac {d}{d x}} \int_ {x} ^ {x + 1} \log \Gamma (t) d t = \log x, \qquad {\mathrm{for}} x > 0,

$$

and as a result

$$

\int_ {x} ^ {x + 1} \log \Gamma (t) d t = x \log x - x + c.

$$

(b) Show as a consequence that log $\Gamma ( n ) \sim n$ log n as $n \to \infty$ . In fact, prove that log $\Gamma ( n ) \sim n \log n + O ( n )$ as $n \to \infty$ . [Hint: Use the fact that $\Gamma ( x )$ is monotonically increasing for all large x.]
:::
