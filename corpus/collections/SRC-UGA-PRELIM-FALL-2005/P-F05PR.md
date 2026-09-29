---
schema: qual/card@1
id: P-F05PR
kind: problem
title: Differentiability implies continuity, and the product rule
classification:
  areas:
  - prelim
  topics:
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.problem}
i) Let $f$ be a function from $\mathbb{R}$ to $\mathbb{R}$ and let $a \in \mathbb{R}$.
From the definition of the derivative, prove that if $f$ is differentiable at $a$ then $f$ is continuous at $a$.

ii) Prove the product rule, $(fg)' = f'g + g'f$.
:::

::: {.solution}
**Goal:** Prove that differentiability implies continuity at a point, and deduce the product rule for derivatives using limit laws.

::: pf

::: {.pf-step #s1}

Part (i): Differentiability at $a$ implies continuity at $a$.
    *Proof:*

::: pf-proof

::: pf-step

By definition of differentiability, the limit
        $$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$
        exists as a real number.

:::

::: pf-step

For all $x \neq a$, we have the algebraic identity:
        $$f(x) - f(a) = \frac{f(x) - f(a)}{x - a} \cdot (x - a).$$

:::

::: pf-step

Applying the product law for limits:
        $$\lim_{x \to a} (f(x) - f(a)) = \left(\lim_{x \to a} \frac{f(x) - f(a)}{x - a}\right) \cdot \left(\lim_{x \to a} (x - a)\right) = f'(a) \cdot 0 = 0.$$

:::

::: pf-step

Therefore $\lim_{x \to a} f(x) = f(a)$, which proves that $f$ is continuous at $a$.

:::

:::

:::

::: pf-step

Part (ii): Product rule $(fg)'(a) = f'(a)g(a) + f(a)g'(a)$.
    *Proof:*

::: pf-proof

::: pf-step

Suppose $f$ and $g$ are differentiable at $a$. The difference quotient for the product $fg$ is:
        $$\frac{(fg)(x) - (fg)(a)}{x - a} = \frac{f(x)g(x) - f(a)g(a)}{x - a}.$$

:::

::: pf-step

Add and subtract the cross-term $f(a)g(x)$ in the numerator:
        $$\frac{f(x)g(x) - f(a)g(a)}{x - a} = \frac{[f(x)g(x) - f(a)g(x)] + [f(a)g(x) - f(a)g(a)]}{x - a} = \frac{f(x) - f(a)}{x - a} g(x) + f(a) \frac{g(x) - g(a)}{x - a}.$$

:::

::: pf-step

Since $g$ is differentiable at $a$, by step [](#s1){.pf-ref} $g$ is continuous at $a$, so $\lim_{x \to a} g(x) = g(a)$.

:::

::: pf-step

Applying limit laws for sums and products as $x \to a$:
        $$\begin{aligned}
        (fg)'(a) &= \lim_{x \to a} \left[ \frac{f(x) - f(a)}{x - a} g(x) + f(a) \frac{g(x) - g(a)}{x - a} \right] \\
        &= \left(\lim_{x \to a} \frac{f(x) - f(a)}{x - a}\right) \cdot \left(\lim_{x \to a} g(x)\right) + f(a) \cdot \left(\lim_{x \to a} \frac{g(x) - g(a)}{x - a}\right) \\
        &= f'(a) g(a) + f(a) g'(a).
        \end{aligned}$$

:::

::: pf-step

Thus $(fg)' = f'g + fg'$. Q.E.D.

:::

:::

:::

:::

:::
