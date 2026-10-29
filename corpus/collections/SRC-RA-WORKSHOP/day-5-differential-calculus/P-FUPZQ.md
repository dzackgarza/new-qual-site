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
Evaluate $$\lim_{x\to a}\frac{a^nf(x)-x^nf(a)}{x-a},\quad n\in\NN.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$a^n f(x) - x^n f(a) = a^n(f(x) - f(a)) - f(a)(x^n - a^n)$.

::: pf-proof

Adding and subtracting $a^nf(a)$ gives $a^n f(x) - x^n f(a) = a^n f(x) - a^n f(a) + a^n f(a) - x^n f(a)$, which regroups as stated.

:::

:::

::: {.pf-step #s2}

$\dfrac{x^n - a^n}{x - a} = x^{n-1} + x^{n-2}a + \cdots + a^{n-1} \to n a^{n-1}$ as $x \to a$.

::: pf-proof

The identity is the factorization of $x^n - a^n$. Each of the $n$ terms of the sum is continuous in $x$ and tends to $a^{n-1}$.

:::

:::

::: pf-step

$$\lim_{x \to a}\frac{a^n f(x) - x^n f(a)}{x - a} = \boxed{a^n f'(a) - n a^{n-1} f(a)}.$$

::: pf-proof

For $x\neq a$, step [](#s1){.pf-ref} splits the quotient as
$$
a^n\frac{f(x) - f(a)}{x-a} - f(a)\frac{x^n - a^n}{x-a}.
$$
The first quotient tends to $f'(a)$ by the definition of the derivative, and the second tends to $na^{n-1}$ by step [](#s2){.pf-ref}.

:::

:::

:::

:::
