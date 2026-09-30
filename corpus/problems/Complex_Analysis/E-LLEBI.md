---
schema: qual/card@1
id: E-LLEBI
kind: problem
title: $\frac{|f(0)|-|z|}{1+|f(0)||z|}\le|f(z)|\le\frac{|f(0)|+|z|}{1-|f(0)||z|}$
  for holomorphic $f:\mathbb{D}\to\mathbb{D}$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.problem}
Let $f$ be a non-constant analytic function on $\mathbb D$ with $f(\mathbb D) \subseteq \mathbb D$.
Use $\psi_{a} (f(z))$ (where $a=f(0)$, $\displaystyle \psi_a(z) = \frac{a - z}{1 - \bar{a}z}$) to prove that $\displaystyle \frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq \frac{|f(0)| + |z|}{1 - |f(0)||z|}$.
:::

::: {.solution}
**Goal:** Let $f: \mathbb{D} \to \mathbb{D}$ be a holomorphic self-map of the unit disk with $a = f(0) \in \mathbb{D}$.
Using the Blaschke automorphism $\psi_a(w) = \frac{a - w}{1 - \bar{a}w}$, prove that for all $z \in \mathbb{D}$: $$\frac{|a| - |z|}{1 + |a||z|} \leq |f(z)| \leq \frac{|a| + |z|}{1 - |a||z|}.$$

* * *

### Step 1: Application of the Schwarz Lemma to the Composite Map

::: pf

::: pf-step
**Define $g(z) = \psi_a(f(z))$.
Then $g$ satisfies the hypotheses of the Schwarz Lemma.**

::: pf-proof

::: {.pf-step #psi-a-automorphism}
The Möbius transformation $\psi_a(w) = \frac{a - w}{1 - \bar{a}w}$ is an automorphism of $\mathbb{D}$ (i.e. $\psi_a \in \text{Aut}(\mathbb{D})$) with $\psi_a(a) = 0$ and $\psi_a^{-1} = \psi_a$.

::: pf-proof
For $|a| < 1$, the map $\psi_a$ is a Blaschke factor: it maps $\mathbb{D}$ to itself, maps the unit circle to itself, satisfies $\psi_a(a) = 0$, and is its own inverse since $\psi_a(\psi_a(w)) = w$.
:::

:::

::: pf-step
Since $f(\mathbb{D}) \subseteq \mathbb{D}$, the composite map $g(z) = \psi_a(f(z))$ is holomorphic from $\mathbb{D}$ to $\mathbb{D}$.

::: pf-proof
$g$ is the composition of the holomorphic map $f$ with the holomorphic automorphism $\psi_a$, and its image lies in $\mathbb{D}$ because both factors map into $\mathbb{D}$.
:::

:::

::: pf-step
$g(0) = \psi_a(f(0)) = \psi_a(a) = 0$.

::: pf-proof
By hypothesis $f(0) = a$, and $\psi_a(a) = 0$ by step [](#psi-a-automorphism){.pf-ref}.
:::

:::

::: {.pf-step #schwarz-bound-g}
By the Schwarz Lemma, $|g(z)| \leq |z|$ for all $z \in \mathbb{D}$.

::: pf-proof
$g \colon \mathbb{D} \to \mathbb{D}$ is holomorphic with $g(0) = 0$, so the Schwarz Lemma applies and gives $|g(z)| \le |z|$.
:::

:::

:::

:::

::: pf-step
**Express $f(z)$ in terms of $g(z)$.**

::: pf-proof

::: pf-step
Since $\psi_a$ is an involution, $g(z) = \psi_a(f(z)) \implies f(z) = \psi_a(g(z)) = \frac{a - g(z)}{1 - \bar{a} g(z)}$.

::: pf-proof
Applying $\psi_a$ to both sides of $g(z) = \psi_a(f(z))$ and using $\psi_a \circ \psi_a = \operatorname{id}$ gives $f(z) = \psi_a(g(z))$.
:::

:::

::: {.pf-step #w-bound}
Define $w = g(z)$, which satisfies $|w| \leq |z| < 1$.

::: pf-proof
By step [](#schwarz-bound-g){.pf-ref}, $|g(z)| \le |z|$, and $|z| < 1$ since $z \in \mathbb{D}$.
:::

:::

:::

:::

:::

* * *

### Step 2: Upper Bound for $|f(z)|$

::: pf

::: {.pf-step #upper-bound-step}
**Prove $|f(z)| \leq \frac{|a| + |z|}{1 - |a||z|}$.**

::: pf-proof

::: pf-step
Using the triangle inequality on the numerator of $f(z) = \frac{a - w}{1 - \bar{a}w}$: $$|a - w| \leq |a| + |w| \leq |a| + |z|.$$

::: pf-proof
The triangle inequality gives $|a - w| \le |a| + |w|$, and $|w| \le |z|$ by step [](#w-bound){.pf-ref}.
:::

:::

::: pf-step
Using the reverse triangle inequality on the denominator: $$|1 - \bar{a}w| \geq 1 - |\bar{a}w| = 1 - |a||w| \geq 1 - |a||z| > 0.$$

::: pf-proof
The reverse triangle inequality gives $|1 - \bar{a}w| \ge 1 - |\bar{a}w| = 1 - |a||w|$; since $|w| \le |z| < 1$ and $|a| < 1$, this is at least $1 - |a||z| > 0$.
:::

:::

::: {.pf-step #upper-bound-value}
Combining the bounds for numerator and denominator: $$|f(z)| = \frac{|a - w|}{|1 - \bar{a}w|} \leq \frac{|a| + |z|}{1 - |a||z|}.$$

::: pf-proof
The numerator is at most $|a| + |z|$ and the positive denominator is at least $1 - |a||z|$, so the quotient is at most $\frac{|a| + |z|}{1 - |a||z|}$.
:::

:::

:::

:::

:::

* * *

### Step 3: Lower Bound for $|f(z)|$

::: pf

::: {.pf-step #lower-bound-step}
**Prove $|f(z)| \geq \frac{|a| - |z|}{1 + |a||z|}$.**

::: pf-proof

::: pf-step
If $|z| \geq |a|$, then $\frac{|a| - |z|}{1 + |a||z|} \leq 0$, so the inequality $|f(z)| \geq 0 \geq \frac{|a|-|z|}{1+|a||z|}$ holds.

::: pf-proof
The modulus of any complex number is non-negative, and $\frac{|a| - |z|}{1 + |a||z|} \le 0$ when $|z| \ge |a|$, so $|f(z)| \ge 0$ dominates it.
:::

:::

::: pf-step
Now assume $|z| < |a|$.
By the reverse triangle inequality on the numerator: $$|a - w| \geq |a| - |w| \geq |a| - |z| > 0.$$

::: pf-proof
The reverse triangle inequality gives $|a - w| \ge |a| - |w|$; since $|w| \le |z| < |a|$, this is at least $|a| - |z| > 0$.
:::

:::

::: pf-step
By the triangle inequality on the denominator: $$|1 - \bar{a}w| \leq 1 + |\bar{a}w| = 1 + |a||w| \leq 1 + |a||z|.$$

::: pf-proof
The triangle inequality gives $|1 - \bar{a}w| \le 1 + |\bar{a}w| = 1 + |a||w|$, and $|w| \le |z|$.
:::

:::

::: {.pf-step #lower-bound-value}
Combining the bounds: $$|f(z)| = \frac{|a - w|}{|1 - \bar{a}w|} \geq \frac{|a| - |z|}{1 + |a||z|}.$$

::: pf-proof
The numerator is at least the positive quantity $|a| - |z|$ and the denominator is at most $1 + |a||z|$, so the quotient is at least $\frac{|a| - |z|}{1 + |a||z|}$.
:::

:::

:::

:::

:::

* * *

### Step 4: Conclusion

::: pf

::: pf-step
**The double inequality holds for all $z \in \mathbb{D}$.**

::: pf-proof

::: pf-step
By step [](#upper-bound-step){.pf-ref} and step [](#lower-bound-step){.pf-ref}, for all $z \in \mathbb{D}$: $$\frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq \frac{|f(0)| + |z|}{1 - |f(0)||z|}.$$

::: pf-proof
Combining the upper bound step [](#upper-bound-value){.pf-ref} and the lower bound step [](#lower-bound-value){.pf-ref}, and substituting $a = f(0)$, gives the double inequality.
:::

:::

:::

:::

:::

:::
