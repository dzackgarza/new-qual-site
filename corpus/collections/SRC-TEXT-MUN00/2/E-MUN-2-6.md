---
schema: qual/card@1
id: E-MUN-2-6
kind: exercise
title: Restricting domain and range to obtain a bijection
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Let $f: \mathbb{R} \to \mathbb{R}$ be the function $f(x) = x^3 - x$ . By restricting the domain and range of $f$ appropriately, obtain from $f$ a bijective function $g$ . Draw the graphs of $g$ and $g^{-1}$ . (There are several possible choices for $g$ .)
:::

::: {.solution}
<1>1. $f(x) = x^3 - x = x(x-1)(x+1)$, with critical points at $x = \pm 1/\sqrt{3}$.
::: {.proof}
$f'(x) = 3x^2 - 1 = 0$ at $x = \pm 1/\sqrt{3}$.
:::

<1>2. $f$ is strictly increasing on $[1/\sqrt{3}, \infty)$.
::: {.proof}
$f'(x) > 0$ for $x > 1/\sqrt{3}$.
:::

<1>3. Restrict the domain to $[1/\sqrt{3}, \infty)$ and the range to $f([1/\sqrt{3}, \infty)) = [f(1/\sqrt{3}), \infty)$.
::: {.proof}
<1>2 (a strictly increasing function is injective, and restricting the codomain to the image makes it surjective).
:::

<1>4. Then $g = f|_{[1/\sqrt{3}, \infty)} : [1/\sqrt{3}, \infty) \to [f(1/\sqrt{3}), \infty)$ is bijective.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. $f(1/\sqrt{3}) = (1/\sqrt{3})^3 - 1/\sqrt{3} = \frac{1}{3\sqrt{3}} - \frac{1}{\sqrt{3}} = -\frac{2}{3\sqrt{3}}$.
::: {.proof}
compute the minimum value.
:::

<1>6. Hence $g : [1/\sqrt{3}, \infty) \to [-2/(3\sqrt{3}), \infty)$, $g(x) = x^3 - x$, is a bijection.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
