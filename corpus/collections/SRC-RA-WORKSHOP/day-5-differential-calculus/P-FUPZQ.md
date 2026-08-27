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

::: problem
Assume that $f$ is differentiable at $a$.
Evaluate $$\lim_{x\to a}\frac{a^nf(x)-x^nf(a)}{x-a},\quad n\in\mathbb{N}.$$
:::
::: {.solution}
<1>1. Rewrite the numerator: $a^n f(x) - x^n f(a) = a^n(f(x) - f(a)) - f(a)(x^n - a^n)$.
Proof: $a^n f(x) - x^n f(a) = a^n f(x) - a^n f(a) + a^n f(a) - x^n f(a) = a^n(f(x) - f(a)) - f(a)(x^n - a^n)$.

<1>2. $f$ is differentiable at $a$, so $\frac{f(x) - f(a)}{x - a} \to f'(a)$ as $x \to a$.
Proof: definition of the derivative.

<1>3. $\frac{x^n - a^n}{x - a} = x^{n-1} + x^{n-2}a + \cdots + a^{n-1} \to n a^{n-1}$ as $x \to a$.
Proof: factorization of $x^n - a^n$; or the derivative of $x \mapsto x^n$ at $a$.

<1>4. Hence $$\lim_{x \to a}\frac{a^n f(x) - x^n f(a)}{x - a} = a^n f'(a) - f(a)\,(n a^{n-1}) = a^n f'(a) - n a^{n-1} f(a).$$ Proof: <1>1 splits the quotient as $a^n\frac{f(x) - f(a)}{x-a} - f(a)\frac{x^n - a^n}{x-a}$, and <1>2, <1>3 give the two limits.
:::
