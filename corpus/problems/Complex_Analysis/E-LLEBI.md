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

::: problem
Let $f$ be a non-constant analytic function on $\mathbb D$ with $f(\mathbb D) \subseteq \mathbb D$.
Use $\psi_{a} (f(z))$ (where $a=f(0)$, $\displaystyle \psi_a(z) = \frac{a - z}{1 - \bar{a}z}$) to prove that $\displaystyle \frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq \frac{|f(0)| + |z|}{1 - |f(0)||z|}$.
:::

::: {.solution}
**Goal:** Let $f: \mathbb{D} \to \mathbb{D}$ be a holomorphic self-map of the unit disk with $a = f(0) \in \mathbb{D}$.
Using the Blaschke automorphism $\psi_a(w) = \frac{a - w}{1 - \bar{a}w}$, prove that for all $z \in \mathbb{D}$: $$\frac{|a| - |z|}{1 + |a||z|} \leq |f(z)| \leq \frac{|a| + |z|}{1 - |a||z|}.$$

* * *

### Step 1: Application of the Schwarz Lemma to the Composite Map

<1>1. **Define $g(z) = \psi_a(f(z))$.
Then $g$ satisfies the hypotheses of the Schwarz Lemma.** <2>1. The Möbius transformation $\psi_a(w) = \frac{a - w}{1 - \bar{a}w}$ is an automorphism of $\mathbb{D}$ (i.e. $\psi_a \in \text{Aut}(\mathbb{D})$) with $\psi_a(a) = 0$ and $\psi_a^{-1} = \psi_a$.
::: {.proof}
For $|a| < 1$, the map $\psi_a$ is a Blaschke factor: it maps $\mathbb{D}$ to itself, maps the unit circle to itself, satisfies $\psi_a(a) = 0$, and is its own inverse since $\psi_a(\psi_a(w)) = w$.
:::
<2>2. Since $f(\mathbb{D}) \subseteq \mathbb{D}$, the composite map $g(z) = \psi_a(f(z))$ is holomorphic from $\mathbb{D}$ to $\mathbb{D}$.
::: {.proof}
$g$ is the composition of the holomorphic map $f$ with the holomorphic automorphism $\psi_a$, and its image lies in $\mathbb{D}$ because both factors map into $\mathbb{D}$.
:::
<2>3. $g(0) = \psi_a(f(0)) = \psi_a(a) = 0$.
::: {.proof}
By hypothesis $f(0) = a$, and $\psi_a(a) = 0$ by <2>1.
:::
<2>4. By the Schwarz Lemma, $|g(z)| \leq |z|$ for all $z \in \mathbb{D}$.
::: {.proof}
$g \colon \mathbb{D} \to \mathbb{D}$ is holomorphic with $g(0) = 0$, so the Schwarz Lemma applies and gives $|g(z)| \le |z|$.
:::
<2>5. Q.E.D.

<1>2. **Express $f(z)$ in terms of $g(z)$.** <2>1. Since $\psi_a$ is an involution, $g(z) = \psi_a(f(z)) \implies f(z) = \psi_a(g(z)) = \frac{a - g(z)}{1 - \bar{a} g(z)}$.
::: {.proof}
Applying $\psi_a$ to both sides of $g(z) = \psi_a(f(z))$ and using $\psi_a \circ \psi_a = \operatorname{id}$ gives $f(z) = \psi_a(g(z))$.
:::
<2>2. Define $w = g(z)$, which satisfies $|w| \leq |z| < 1$.
::: {.proof}
By <1>1.<2>4>, $|g(z)| \le |z|$, and $|z| < 1$ since $z \in \mathbb{D}$.
:::
<2>3. Q.E.D.

* * *

### Step 2: Upper Bound for $|f(z)|$

<1>3. **Prove $|f(z)| \leq \frac{|a| + |z|}{1 - |a||z|}$.** <2>1. Using the triangle inequality on the numerator of $f(z) = \frac{a - w}{1 - \bar{a}w}$: $$|a - w| \leq |a| + |w| \leq |a| + |z|.$$
::: {.proof}
The triangle inequality gives $|a - w| \le |a| + |w|$, and $|w| \le |z|$ by <1>2.<2>2>.
:::
<2>2. Using the reverse triangle inequality on the denominator: $$|1 - \bar{a}w| \geq 1 - |\bar{a}w| = 1 - |a||w| \geq 1 - |a||z| > 0.$$
::: {.proof}
The reverse triangle inequality gives $|1 - \bar{a}w| \ge 1 - |\bar{a}w| = 1 - |a||w|$; since $|w| \le |z| < 1$ and $|a| < 1$, this is at least $1 - |a||z| > 0$.
:::
<2>3. Combining the bounds for numerator and denominator: $$|f(z)| = \frac{|a - w|}{|1 - \bar{a}w|} \leq \frac{|a| + |z|}{1 - |a||z|}.$$
::: {.proof}
The numerator is at most $|a| + |z|$ and the positive denominator is at least $1 - |a||z|$, so the quotient is at most $\frac{|a| + |z|}{1 - |a||z|}$.
:::
<2>4. Q.E.D.

* * *

### Step 3: Lower Bound for $|f(z)|$

<1>4. **Prove $|f(z)| \geq \frac{|a| - |z|}{1 + |a||z|}$.** <2>1. If $|z| \geq |a|$, then $\frac{|a| - |z|}{1 + |a||z|} \leq 0$, so the inequality $|f(z)| \geq 0 \geq \frac{|a|-|z|}{1+|a||z|}$ holds.
::: {.proof}
The modulus of any complex number is non-negative, and $\frac{|a| - |z|}{1 + |a||z|} \le 0$ when $|z| \ge |a|$, so $|f(z)| \ge 0$ dominates it.
:::
<2>2. Now assume $|z| < |a|$.
By the reverse triangle inequality on the numerator: $$|a - w| \geq |a| - |w| \geq |a| - |z| > 0.$$
::: {.proof}
The reverse triangle inequality gives $|a - w| \ge |a| - |w|$; since $|w| \le |z| < |a|$, this is at least $|a| - |z| > 0$.
:::
<2>3. By the triangle inequality on the denominator: $$|1 - \bar{a}w| \leq 1 + |\bar{a}w| = 1 + |a||w| \leq 1 + |a||z|.$$
::: {.proof}
The triangle inequality gives $|1 - \bar{a}w| \le 1 + |\bar{a}w| = 1 + |a||w|$, and $|w| \le |z|$.
:::
<2>4. Combining the bounds: $$|f(z)| = \frac{|a - w|}{|1 - \bar{a}w|} \geq \frac{|a| - |z|}{1 + |a||z|}.$$
::: {.proof}
The numerator is at least the positive quantity $|a| - |z|$ and the denominator is at most $1 + |a||z|$, so the quotient is at least $\frac{|a| - |z|}{1 + |a||z|}$.
:::
<2>5. Q.E.D.

* * *

### Step 4: Conclusion

<1>5. **The double inequality holds for all $z \in \mathbb{D}$.** <2>1. By <1>3 and <1>4, for all $z \in \mathbb{D}$: $$\frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq \frac{|f(0)| + |z|}{1 - |f(0)||z|}.$$
::: {.proof}
Combining the upper bound <1>3.<2>3> and the lower bound <1>4.<2>4>, and substituting $a = f(0)$, gives the double inequality.
:::
<2>2. Q.E.D.
:::
