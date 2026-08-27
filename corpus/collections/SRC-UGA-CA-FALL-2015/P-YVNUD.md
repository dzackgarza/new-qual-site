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

::: problem
1.
Let $f(z) \in H({\mathbb D})$, $\text{Re}(f(z)) >0$ and $f(0)= a>0$.
Show that
$$
\abs{ \frac{f(z)-a}{f(z)+a}} \leq |z|, \; \; \; |f'(0)| \leq 2a
.$$

2.
Show that the above is still true if $\text{Re}(f(z)) >0$ is replaced with $\text{Re}(f(z)) \geq 0$.
:::

::: {.solution}
**Goal:** (1) For $f \in H(\DD)$ with $\Re f > 0$ and $f(0) = a > 0$, prove $\abs{\frac{f(z) - a}{f(z) + a}} \leq \abs z$ and $\abs{f'(0)} \leq 2a$; (2) same conclusion when $\Re f \geq 0$.

<1>1. The Cayley transform $T(w) := \frac{w - a}{w + a}$ maps the right half-plane $\theset{\Re w > 0}$ conformally onto $\DD$, with $T(a) = 0$.
Proof: $T$ is a M\"obius map; $w = a$ (the point in the right half-plane with $\abs{T(w)} = 0$) maps to $0$, the boundary $\Re w = 0$ maps to the unit circle, and the interior $\Re w > 0$ maps to the interior $\abs{T(w)} < 1$ (check at $w = \infty$-type points or a test point like $w = 1$: $T(1) = \frac{1-a}{1+a} \in (-1,1)$).

<1>2. Define $g(z) := T(f(z)) = \frac{f(z) - a}{f(z) + a}$; then $g: \DD \to \DD$ is analytic and $g(0) = 0$.
<2>1. $g$ is analytic on $\DD$.
Proof: $f$ is holomorphic and $f(z) + a \neq 0$ because $\Re(f(z) + a) = \Re f(z) + a > 0$ (using $\Re f > 0$, $a > 0$). <2>2. $\abs{g(z)} < 1$ on $\DD$.
Proof: $T$ maps the right half-plane into $\DD$ (<1>1) and $\Re f > 0$.
<2>3. $g(0) = T(a) = 0$.
Proof: $f(0) = a$ and <1>1.

<1>3. By Schwarz's lemma, $\abs{g(z)} \leq \abs z$ for all $z \in \DD$.
Proof: Schwarz lemma applied to $g$ (<1>2).

<1>4. This proves the first inequality: $\abs{\frac{f(z) - a}{f(z) + a}} \leq \abs z$.
Proof: $g(z) = \frac{f(z) - a}{f(z) + a}$ by definition.

<1>5. $\abs{f'(0)} \leq 2a$.
<2>1. $g'(0) = T'(f(0)) \cdot f'(0) = T'(a) f'(0)$.
Proof: Chain rule.
<2>2. $T'(a) = \frac{2a}{(2a)^2} = \frac{1}{2a}$.
Proof: $T'(w) = \frac{(w+a) - (w-a)}{(w+a)^2} = \frac{2a}{(w+a)^2}$; evaluate at $w = a$.
<2>3. Schwarz's lemma also gives $\abs{g'(0)} \leq 1$.
Proof: Schwarz lemma, derivative form.
<2>4. $\abs{f'(0)} = 2a \abs{g'(0)} \leq 2a$.
Proof: <2>1--<2>3.

<1>6. Part (2): the same conclusions hold when $\Re f \geq 0$.
<2>1. $g = T \circ f$ still maps $\DD$ into $\overline{\DD}$ and is analytic with $g(0) = 0$.
Proof: $T$ maps the closed right half-plane $\Re w \geq 0$ into the closed unit disk; $f(z) + a \neq 0$ still holds since $\Re(f(z)+a) \geq a > 0$.
<2>2. Schwarz's lemma applies to $g: \DD \to \overline{\DD}$ with $g(0) = 0$.
Proof: Schwarz's lemma requires only $\abs g \leq 1$, not strict.
<2>3. Hence $\abs{g(z)} \leq \abs z$ and $\abs{g'(0)} \leq 1$, giving the same two inequalities.
Proof: Same argument as <1>3--<1>5.

<1>7. Q.E.D. Proof: <1>4 and <1>5 prove (1); <1>6 proves (2).
:::
