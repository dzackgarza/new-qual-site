---
schema: qual/card@1
id: P-YVNUD
kind: problem
title: 'Schwarz lemma for holomorphic maps of the disk into the right half-plane:
  $\bigl|\frac{f(z)-a}{f(z)+a}\bigr|\le|z|$ and $|f''(0)|\le 2a$, also when $\operatorname{Re}f\ge
  0$'
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f(z) \in H({\mathbb D})$, $\text{Re}(f(z)) >0$ and $f(0)= a>0$.
Show that
$$
\abs{ \frac{f(z)-a}{f(z)+a}} \leq |z|, \; \; \; |f'(0)| \leq 2a
.$$

Show that the above is still true if $\text{Re}(f(z)) >0$ is replaced with $\text{Re}(f(z)) \geq 0$.
:::

::: {.solution}
**Goal:** (1) For $f \in H(\DD)$ with $\Re f > 0$ and $f(0) = a > 0$, prove $\abs{\frac{f(z) - a}{f(z) + a}} \leq \abs z$ and $\abs{f'(0)} \leq 2a$; (2) same conclusion when $\Re f \geq 0$.

::: pf

::: {.pf-step #s1}
The Cayley transform $T(w) := \frac{w - a}{w + a}$ maps the right half-plane $\theset{\Re w > 0}$ conformally onto $\DD$, with $T(a) = 0$.

::: pf-proof
$T$ is a M\"obius map; $w = a$ (the point in the right half-plane with $\abs{T(w)} = 0$) maps to $0$, the boundary $\Re w = 0$ maps to the unit circle, and the interior $\Re w > 0$ maps to the interior $\abs{T(w)} < 1$ (check at $w = \infty$-type points or a test point like $w = 1$: $T(1) = \frac{1-a}{1+a} \in (-1,1)$).
:::

:::

::: {.pf-step #s2}
Define $g(z) := T(f(z)) = \frac{f(z) - a}{f(z) + a}$; then $g: \DD \to \DD$ is analytic and $g(0) = 0$.

::: pf-proof

::: pf-step
$g$ is analytic on $\DD$.

::: pf-proof
$f$ is holomorphic and $f(z) + a \neq 0$ because $\Re(f(z) + a) = \Re f(z) + a > 0$ (using $\Re f > 0$, $a > 0$).
:::

:::

::: pf-step
$\abs{g(z)} < 1$ on $\DD$.

::: pf-proof
$T$ maps the right half-plane into $\DD$ (step [](#s1){.pf-ref}) and $\Re f > 0$.
:::

:::

::: pf-step
$g(0) = T(a) = 0$.

::: pf-proof
$f(0) = a$ and step [](#s1){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
By Schwarz's lemma, $\abs{g(z)} \leq \abs z$ for all $z \in \DD$.

::: pf-proof
Schwarz lemma applied to $g$ (step [](#s2){.pf-ref}).
:::

:::

::: {.pf-step #s4}
This proves the first inequality: $\abs{\frac{f(z) - a}{f(z) + a}} \leq \abs z$.

::: pf-proof
$g(z) = \frac{f(z) - a}{f(z) + a}$ by definition.
:::

:::

::: {.pf-step #s5}
$\abs{f'(0)} \leq 2a$.

::: pf-proof

::: {.pf-step #s5-1}
$g'(0) = T'(f(0)) \cdot f'(0) = T'(a) f'(0)$.

::: pf-proof
Chain rule.
:::

:::

::: {.pf-step #s5-2}
$T'(a) = \frac{2a}{(2a)^2} = \frac{1}{2a}$.

::: pf-proof
$T'(w) = \frac{(w+a) - (w-a)}{(w+a)^2} = \frac{2a}{(w+a)^2}$; evaluate at $w = a$.
:::

:::

::: {.pf-step #s5-3}
Schwarz's lemma also gives $\abs{g'(0)} \leq 1$.

::: pf-proof
Schwarz lemma, derivative form.
:::

:::

::: pf-step
$\abs{f'(0)} = 2a \abs{g'(0)} \leq 2a$.

::: pf-proof
Steps [](#s5-1){.pf-ref}, [](#s5-2){.pf-ref} and [](#s5-3){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s6}
Part (2): the same conclusions hold when $\Re f \geq 0$.

::: pf-proof

::: pf-step
$g = T \circ f$ still maps $\DD$ into $\overline{\DD}$ and is analytic with $g(0) = 0$.

::: pf-proof
$T$ maps the closed right half-plane $\Re w \geq 0$ into the closed unit disk; $f(z) + a \neq 0$ still holds since $\Re(f(z)+a) \geq a > 0$.
:::

:::

::: pf-step
Schwarz's lemma applies to $g: \DD \to \overline{\DD}$ with $g(0) = 0$.

::: pf-proof
Schwarz's lemma requires only $\abs g \leq 1$, not strict.
:::

:::

::: pf-step
Hence $\abs{g(z)} \leq \abs z$ and $\abs{g'(0)} \leq 1$, giving the same two inequalities.

::: pf-proof
Same argument as steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (1); step [](#s6){.pf-ref} proves (2).
:::

:::
:::
