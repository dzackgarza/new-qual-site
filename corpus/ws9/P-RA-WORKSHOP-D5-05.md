---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-05
kind: problem
title: 'A difference quotient involving powers of the variable'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - limits
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2006 #2b) Assume that $f$ is differentiable at $a$.
Evaluate $$\lim_{x\to a}\frac{a^n f(x)-x^n f(a)}{x-a},\qquad n\in\mathbb N.$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Add and subtract $a^n f(a)$ in the numerator.
Proof: \[\frac{a^n f(x) - x^n f(a)}{x - a} = \frac{a^n f(x) - a^n f(a) + a^n f(a) - x^n f(a)}{x-a} = a^n\frac{f(x) - f(a)}{x-a} + f(a)\frac{a^n - x^n}{x-a}.\] <1>2. Evaluate the two limits.
Proof: $\frac{f(x)-f(a)}{x-a} \to f'(a)$ by differentiability.
And $\frac{a^n - x^n}{x-a} = -\frac{x^n - a^n}{x-a} \to -(x^n)'_{x=a} = -n a^{n-1}$ (derivative of the monomial).
<1>3. Conclude.
Proof: the limit is $a^n f'(a) - n a^{n-1} f(a)$, i.e. \[\lim_{x\to a}\frac{a^n f(x) - x^n f(a)}{x-a} = a^n f'(a) - n a^{n-1} f(a).\] <1>4. Q.E.D.
:::
