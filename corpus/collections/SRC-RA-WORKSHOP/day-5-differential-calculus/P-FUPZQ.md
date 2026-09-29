---
schema: qual/card@1
id: P-FUPZQ
kind: problem
title: $\lim_{x\to a}\frac{a^n f(x)-x^n f(a)}{x-a}=a^n f'(a)-na^{n-1}f(a)$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Assume that $f$ is differentiable at $a$.
Evaluate $$\lim_{x\to a}\frac{a^nf(x)-x^nf(a)}{x-a},\quad n\in\mathbb{N}.$$
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

Rewrite the numerator: $a^n f(x) - x^n f(a) = a^n(f(x) - f(a)) - f(a)(x^n - a^n)$.

::: pf-proof

$a^n f(x) - x^n f(a) = a^n f(x) - a^n f(a) + a^n f(a) - x^n f(a) = a^n(f(x) - f(a)) - f(a)(x^n - a^n)$.

:::

:::

::: {.pf-step #s2}

$f$ is differentiable at $a$, so $\frac{f(x) - f(a)}{x - a} \to f'(a)$ as $x \to a$.

::: pf-proof

definition of the derivative.

:::

:::

::: {.pf-step #s3}

$\frac{x^n - a^n}{x - a} = x^{n-1} + x^{n-2}a + \cdots + a^{n-1} \to n a^{n-1}$ as $x \to a$.

::: pf-proof

factorization of $x^n - a^n$; or the derivative of $x \mapsto x^n$ at $a$.

:::

:::

::: pf-step

Hence $$\lim_{x \to a}\frac{a^n f(x) - x^n f(a)}{x - a} = a^n f'(a) - f(a)\,(n a^{n-1}) = a^n f'(a) - n a^{n-1} f(a).$$ Proof: step [](#s1){.pf-ref} splits the quotient as $a^n\frac{f(x) - f(a)}{x-a} - f(a)\frac{x^n - a^n}{x-a}$, and steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give the two limits.

:::

:::

:::
