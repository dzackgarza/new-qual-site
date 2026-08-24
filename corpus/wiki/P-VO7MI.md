---
schema: qual/card@1
id: P-VO7MI
kind: problem
title: Use the definition of the derivative to prove that
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
relations: []
review: draft
---

::: problem
Use the definition of the derivative to prove that if $f$ and $g$ are differentiable at $x$, then $fg$ is differentiable at $x$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Write the difference quotient of $fg$.
Proof: for $h \neq 0$, \[ \frac{(fg)(x+h) - (fg)(x)}{h} = \frac{f(x+h)g(x+h) - f(x)g(x)}{h} = \frac{f(x+h) - f(x)}{h}\,g(x+h) + f(x)\,\frac{g(x+h) - g(x)}{h}. \] <1>2. $g$ is continuous at $x$.
Proof: $g$ is differentiable at $x$, hence continuous at $x$: $g(x+h) \to g(x)$ as $h \to 0$.
<1>3. Pass to the limit.
Proof: as $h \to 0$, $\frac{f(x+h)-f(x)}{h} \to f'(x)$, $g(x+h) \to g(x)$ (<1>2), and $\frac{g(x+h)-g(x)}{h} \to g'(x)$; substituting into <1>1, \[ \lim_{h\to 0}\frac{(fg)(x+h)-(fg)(x)}{h} = f'(x)g(x) + f(x)g'(x), \] so $fg$ is differentiable at $x$ with derivative $f'(x)g(x) + f(x)g'(x)$.
<1>4. Q.E.D.
:::
