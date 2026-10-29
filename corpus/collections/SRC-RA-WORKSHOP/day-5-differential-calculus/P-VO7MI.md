---
schema: qual/card@1
id: P-VO7MI
kind: problem
title: "Product rule from the definition of the derivative"
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Use the definition of the derivative to prove that if $f$ and $g$ are differentiable at $x$, then $fg$ is differentiable at $x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $h \neq 0$,
$$
\frac{(fg)(x+h) - (fg)(x)}{h} = \frac{f(x+h) - f(x)}{h}\,g(x+h) + f(x)\,\frac{g(x+h) - g(x)}{h}.
$$

::: pf-proof

The numerator $f(x+h)g(x+h) - f(x)g(x)$ equals $(f(x+h)-f(x))g(x+h) + f(x)(g(x+h)-g(x))$, as adding and subtracting $f(x)g(x+h)$ shows.

:::

:::

::: {.pf-step #s2}

$g$ is continuous at $x$.

::: pf-proof

For $h\neq0$, $g(x+h)-g(x) = h\cdot\frac{g(x+h)-g(x)}{h}\to 0\cdot g'(x)=0$ as $h\to0$.

:::

:::

::: pf-step

$fg$ is differentiable at $x$ with $(fg)'(x)=f'(x)g(x) + f(x)g'(x)$.

::: pf-proof

As $h \to 0$, $\frac{f(x+h)-f(x)}{h} \to f'(x)$, $g(x+h) \to g(x)$ by step [](#s2){.pf-ref}, and $\frac{g(x+h)-g(x)}{h} \to g'(x)$. Substituting into the identity of step [](#s1){.pf-ref} gives
$$
\lim_{h\to 0}\frac{(fg)(x+h)-(fg)(x)}{h} = f'(x)g(x) + f(x)g'(x).
$$

:::

:::

:::

:::
