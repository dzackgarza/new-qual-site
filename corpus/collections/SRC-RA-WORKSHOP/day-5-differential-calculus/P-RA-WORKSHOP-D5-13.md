---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-13
kind: problem
title: Prove Theorem 4.1
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
relations:
- kind: uses
  target: T-RA-WORKSHOP-D5-4-1
review: draft
---

::: {.problem}
Prove Theorem 4.1.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Suppose $f$ has a local maximum at $c \in (a,b)$ and $f'(c)$ exists.
Proof: by definition of local maximum, there is $\delta > 0$ with $f(x) \le f(c)$ for all $x \in (c-\delta, c+\delta) \subseteq (a,b)$.
<1>2. The left-hand derivative is $\ge 0$.
Proof: for $h < 0$ with $|h| < \delta$, $\frac{f(c+h) - f(c)}{h} \ge 0$ (numerator $\le 0$, denominator $< 0$). Hence $f'(c) = \lim_{h\to 0^-}\frac{f(c+h)-f(c)}{h} \ge 0$.
<1>3. The right-hand derivative is $\le 0$.
Proof: for $h > 0$ with $h < \delta$, $\frac{f(c+h) - f(c)}{h} \le 0$ (numerator $\le 0$, denominator $> 0$). Hence $f'(c) = \lim_{h\to 0^+}\frac{f(c+h)-f(c)}{h} \le 0$.
<1>4. Conclude.
Proof: $f'(c) \ge 0$ and $f'(c) \le 0$, so $f'(c) = 0$.
(For a local minimum, apply the argument to $-f$.)
<1>5. Q.E.D.
:::
