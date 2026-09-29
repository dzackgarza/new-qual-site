---
schema: qual/card@1
id: P-MMAQ-RML5AHHINX
kind: problem
title: Darboux's theorem for $f'$ attaining $2$, and $f'(0)=\lim_{x\to 0}f'(x)$ when
  $f$ is continuous and the limit exists
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Sequences of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(a) Let $f : \mathbb{R} \to \mathbb{R}$ be a differentiable function.
    If $f'(-1) < 2$ and $f'(1) > 2$, show that there exists $x_0 \in (i1, 1)$ such that $f'(x_0) = 2$.

    > Hint: consider the function $f(x) - 2x$ and recall the proof of Rolle's theorem.)

(b) Let $f : (-1, 1) \to \mathbb{R}$ be a differentiable function on $(-1, 0) \union (0, 1)$ such that $\lim_{x\to 0} f'(x) = L$.
    If $f$ is continuous on $(-1, 1)$, show that $f$ is indeed differentiable at $0$ and $f'(0) = L$.
:::

::: {.solution}
In part (a) the interval is $(-1, 1)$.

::: pf

::: pf-step
Proof of (a).

::: pf-proof

::: pf-step
Define $g(x) \definedas f(x) - 2x$; then $g'(-1) = f'(-1) - 2 < 0$ and $g'(1) = f'(1) - 2 > 0$.

::: pf-proof
Differentiate $g$; the inequalities are the hypotheses.
:::

:::

::: {.pf-step #darboux-intermediate-value-property}
Derivatives have the intermediate value property (Darboux's theorem): $g'$ takes every value between $g'(-1)$ and $g'(1)$ on $(-1, 1)$.

::: pf-proof
Let $g'(a) < c < g'(b)$ and put $h(x) = g(x) - cx$, so $h'(a) < 0 < h'(b)$. The continuous function $h$ attains a minimum on $[a,b]$. Since $h'(a) < 0$, $h(x) < h(a)$ for $x$ slightly larger than $a$; since $h'(b) > 0$, $h(x) < h(b)$ for $x$ slightly smaller than $b$. So the minimum is attained at an interior point, where $h' = 0$, that is, $g' = c$.
:::

:::

::: pf-step
Since $0$ lies strictly between $g'(-1) < 0$ and $g'(1) > 0$, there is $x_0 \in (-1, 1)$ with $g'(x_0) = 0$.

::: pf-proof
By step [](#darboux-intermediate-value-property){.pf-ref} with $c = 0$.
:::

:::

::: pf-step
Hence $f'(x_0) = 2$.

::: pf-proof
$g'(x_0) = f'(x_0) - 2 = 0$.
:::

:::

:::

::: pf-qed
This proves (a).
:::

:::

::: pf-step
Proof of (b).

::: pf-proof

::: {.pf-step #mvt-positive-side}
Fix $x > 0$ (with $x$ small, $x \in (0, 1)$); the mean value theorem applies to $f$ on $[0, x]$: $f(x) - f(0) = f'(c_x) x$ for some $c_x \in (0, x)$.

::: pf-proof
$f$ is continuous on $[0, x]$ (hypothesis) and differentiable on $(0, x)$ (since $(0, x) \subseteq (0, 1)$); MVT applies.
:::

:::

::: {.pf-step #mvt-negative-side}
Similarly for $x < 0$: $f(x) - f(0) = f'(c_x) x$ for some $c_x \in (x, 0)$.

::: pf-proof
MVT on $[x, 0]$, differentiable on $(x, 0)$.
:::

:::

::: {.pf-step #cx-limit-L}
As $x \to 0$ (either side), the point $c_x$ (which lies between $0$ and $x$) tends to $0$, so $f'(c_x) \to L$.

::: pf-proof
$c_x \to 0$ by the squeeze theorem, and $\lim_{t \to 0} f'(t) = L$ by hypothesis.
:::

:::

::: pf-step
Hence $\frac{f(x) - f(0)}{x} = f'(c_x) \to L$ as $x \to 0$.

::: pf-proof
Divide steps [](#mvt-positive-side){.pf-ref} and [](#mvt-negative-side){.pf-ref} by $x$ and use step [](#cx-limit-L){.pf-ref}; the same limit $L$ is obtained from both sides.
:::

:::

:::

::: pf-qed
The two-sided limit $\lim_{x \to 0} (f(x) - f(0))/x$ exists and equals $L$, so $f$ is differentiable at $0$ with $f'(0) = L$.
:::

:::

:::
