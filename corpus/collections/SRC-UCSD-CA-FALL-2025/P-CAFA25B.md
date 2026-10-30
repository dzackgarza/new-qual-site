---
schema: qual/card@1
id: P-CAFA25B
kind: problem
title: 'A holomorphic function on a punctured disc with $\abs{f}\leq A\abs{z}^{-3/2}$ has at most a simple pole'
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Poles
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $f : \{z : 0 < \abs{z} < 1\} \to \CC$ be holomorphic and assume that $\abs{f(z)} \leq A\abs{z}^{-3/2}$ for some constant $A$.
Prove that there is a complex constant $\alpha$ such that $g(z) := f(z) - \alpha z^{-1}$ can be extended to a holomorphic function on $\{z : \abs{z} < 1\}$.
:::

::: {.solution}
**Goal.** Show $f$ has at worst a simple pole at $0$, i.e. $f(z) - \alpha z^{-1}$ extends holomorphically across $0$.

::: pf

::: pf-step

$f$ has a Laurent expansion $f(z) = \sum_{n=-\infty}^{\infty} a_n z^n$ on $0 < \abs{z} < 1$.

::: pf-proof

$f$ is holomorphic on the punctured disk.

:::

:::

::: {.pf-step #s2}

$a_n = 0$ for all $n \le -2$.

::: pf-proof

::: pf-step

For $n \le -2$, $a_n = \frac{1}{2\pi i} \oint_{\abs{z} = r} f(z) z^{-n-1}\, dz$ for any $0 < r < 1$.

::: pf-proof

Laurent coefficient formula.

:::

:::

::: {.pf-step #s2-2}

$\abs{a_n} \le \frac{1}{2\pi} \cdot 2\pi r \cdot \sup_{\abs{z}=r} \abs{f(z)} \cdot r^{-n-1} \le A r^{-3/2} \cdot r^{-n-1} = A r^{-n - 5/2}$.

::: pf-proof

bound the integral by length times sup; use $\abs{f(z)} \le A \abs{z}^{-3/2} = A r^{-3/2}$.

:::

:::

::: {.pf-step #s2-3}

For $n \le -2$, $-n - 5/2 \ge -1/2 > 0$, so $A r^{-n-5/2} \to 0$ as $r \to 0^+$.

::: pf-proof

the exponent is positive.

:::

:::

::: pf-step

Hence $a_n = 0$ for $n \le -2$.

::: pf-proof

Steps [](#s2-2){.pf-ref} and [](#s2-3){.pf-ref} force $\abs{a_n} = 0$.

:::

:::

:::

:::

::: {.pf-step #s3}

Therefore $f(z) = a_{-1} z^{-1} + h(z)$ where $h$ is holomorphic on $\abs{z} < 1$.

::: pf-proof

Step [](#s2){.pf-ref} removes all terms of order $\le -2$; the remaining nonnegative powers form a holomorphic function $h$ on the full disk.

:::

:::

::: {.pf-step #s4}

Set $\alpha = a_{-1}$ and $g(z) = f(z) - \alpha z^{-1} = h(z)$.

::: pf-proof

definition.

:::

:::

::: {.pf-step #s5}

$g$ extends holomorphically to $\abs{z} < 1$.

::: pf-proof

$g = h$ is holomorphic on the full disk by step [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::
