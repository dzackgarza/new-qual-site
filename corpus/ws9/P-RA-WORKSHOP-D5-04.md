---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-04
kind: problem
title: 'Derive the product rule from the derivative definition'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 2005 #1a) Use the definition of the derivative to prove that if $f$ and $g$ are differentiable at $x$, then $fg$ is differentiable at $x$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Set up the difference quotient for $fg$.
Proof: for $h \ne 0$, \[\frac{(fg)(x+h) - (fg)(x)}{h} = \frac{f(x+h)g(x+h) - f(x)g(x)}{h} = \frac{f(x+h)g(x+h) - f(x)g(x+h) + f(x)g(x+h) - f(x)g(x)}{h}\] \[ = \frac{f(x+h) - f(x)}{h}\,g(x+h) + f(x)\,\frac{g(x+h) - g(x)}{h}.\] <1>2. Take the limit.
Proof: $f$ is differentiable at $x$, so $\frac{f(x+h)-f(x)}{h} \to f'(x)$; $g$ is differentiable at $x$, so $\frac{g(x+h)-g(x)}{h} \to g'(x)$; and differentiability of $g$ at $x$ implies continuity of $g$ at $x$, so $g(x+h) \to g(x)$.
Hence \[\lim_{h\to 0}\frac{(fg)(x+h)-(fg)(x)}{h} = f'(x)g(x) + f(x)g'(x),\] so $fg$ is differentiable at $x$ with $(fg)'(x) = f'(x)g(x) + f(x)g'(x)$.
<1>3. Q.E.D.
:::
