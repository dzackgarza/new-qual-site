---
schema: qual/card@1
id: P-MMAQ-FQRRXNYJJL
kind: problem
title: An entire function with $|f(z)|\leq A|z|^2$ is a polynomial of degree at most
  $2$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (4) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMCA4, whose solution repeats this Cauchy-estimate argument."
---

::: {.problem}
Let $f$ be an entire function and suppose that $|f(z)| \leq A|z|^2$ for all $z$ and some constant $A$.
Show that $f$ is a polynomial of degree $\leq 2$.
:::

::: {.solution}
We prove the stronger statement $f(z)=c_2z^2$ for a constant $c_2\in\mathbb C$.

### Step 1: Taylor Series and Cauchy's Estimates

::: pf

::: pf-step

**$f$ is represented by its Taylor series centered at the origin for all $z \in \mathbb{C}$.**

::: pf-proof

::: pf-step

Since $f$ is entire, $f(z) = \sum_{n=0}^\infty c_n z^n$ converges everywhere on $\mathbb{C}$, with coefficients given by $c_n = \frac{f^{(n)}(0)}{n!}$.

::: pf-proof

The Taylor series of a holomorphic function at $0$ converges to it on every open disk centered at $0$ contained in its domain, here $\mathbb C$.

:::

:::

::: {.pf-step #s1-2}

For any $R > 0$ and any $n \geq 0$, Cauchy's coefficient formula gives: $$c_n = \frac{1}{2\pi i} \oint_{|z|=R} \frac{f(z)}{z^{n+1}} \, dz.$$

::: pf-proof

Cauchy integral formula for derivatives.

:::

:::

:::

:::

::: pf-step

**Apply Cauchy's Estimates for each coefficient $c_n$.**

::: pf-proof

::: {.pf-step #s2-1}

By the $ML$-inequality on the circle $|z| = R$: $$|c_n| \leq \frac{1}{2\pi} \cdot \left( \sup_{|z|=R} \frac{|f(z)|}{|z|^{n+1}} \right) \cdot (2\pi R) = \frac{\sup_{|z|=R} |f(z)|}{R^n}.$$

::: pf-proof

On $|z|=R$ the integrand of step [](#s1-2){.pf-ref} has modulus at most $\sup_{|z|=R}|f(z)|/R^{n+1}$, and the circle has length $2\pi R$.

:::

:::

::: {.pf-step #s2-2}

By the growth hypothesis, on $|z| = R$, $|f(z)| \leq A R^2$.

::: pf-proof

Given assumption $|f(z)| \leq A|z|^2$.

:::

:::

::: {.pf-step #s2-3}

Substituting step [](#s2-2){.pf-ref} into step [](#s2-1){.pf-ref} yields the bound: $$|c_n| \leq \frac{A R^2}{R^n} = A R^{2-n} \quad \text{for all } R > 0.$$

::: pf-proof

Algebra.

:::

:::

:::

:::

:::

* * *

### Step 2: Vanishing of Higher-Order Coefficients

::: pf

::: {.pf-step #s3}

**$c_n = 0$ for all $n \geq 3$.**

::: pf-proof

::: pf-step

For $n \geq 3$, the exponent $2 - n \leq -1 < 0$.

::: pf-proof

$n \geq 3 \implies 2 - n \leq -1$.

:::

:::

::: pf-step

Since the bound $|c_n| \leq A R^{2-n}$ holds for all $R > 0$, taking the limit as $R \to \infty$: $$|c_n| \leq \lim_{R \to \infty} A R^{2-n} = 0.$$

::: pf-proof

$\lim_{R\to\infty} R^{-k} = 0$ for $k \geq 1$.

:::

:::

::: pf-step

Therefore, $|c_n| = 0 \implies c_n = 0$ for all $n \geq 3$.

::: pf-proof

Absolute value is non-negative.

:::

:::

:::

:::

:::

* * *

### Step 3: Behavior at the Origin and Lower-Order Coefficients

::: pf

::: {.pf-step #s4}

**$c_0 = 0$ and $c_1 = 0$.**

::: pf-proof

::: pf-step

Evaluating the growth condition at $z = 0$: $|f(0)| \leq A |0|^2 = 0 \implies f(0) = 0$, so $c_0 = 0$.

::: pf-proof

Evaluation at $z=0$.

:::

:::

::: pf-step

For $c_1$, apply the bound from step [](#s2-3){.pf-ref} with $n = 1$: $|c_1| \leq A R^{2-1} = A R$ for all $R > 0$.

::: pf-proof

Setting $n=1$ in step [](#s2-3){.pf-ref}.

:::

:::

::: pf-step

Taking the limit as $R \to 0^+$: $$|c_1| \leq \lim_{R \to 0^+} A R = 0 \implies c_1 = 0.$$

::: pf-proof

$R$ can be taken arbitrarily small.

:::

:::

:::

:::

:::

* * *

### Step 4: Conclusion

::: pf

::: pf-step

**$f(z)$ is a polynomial of degree at most 2 (in fact $f(z) = c_2 z^2$).**

::: pf-proof

::: pf-step

From steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $c_n = 0$ for all $n \neq 2$.

::: pf-proof

Combining $c_0 = c_1 = 0$ and $c_n = 0$ for $n \geq 3$.

:::

:::

::: pf-step

Thus $f(z) = c_2 z^2$, which is a polynomial of degree $\leq 2$ (with $|c_2| \leq A$).

::: pf-proof

Direct substitution into Taylor series.

:::

:::

:::

:::

:::

:::
