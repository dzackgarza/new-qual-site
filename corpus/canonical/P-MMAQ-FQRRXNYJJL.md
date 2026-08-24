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
---

::: problem
Let $f$ be an entire function and suppose that $|f(z)| \leq A|z|^2$ for all $z$ and some constant $A$.
Show that $f$ is a polynomial of degree $\leq 2$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f: \mathbb{C} \to \mathbb{C}$ be an entire function such that $|f(z)| \leq A |z|^2$ for all $z \in \mathbb{C}$ and some constant $A \geq 0$.
Prove that $f(z) = c_2 z^2$ for some constant $c_2 \in \mathbb{C}$ (in particular, a polynomial of degree $\leq 2$ with $f(0) = f'(0) = 0$).

* * *

### Step 1: Taylor Series and Cauchy's Estimates

<1>1. **$f$ is represented by its Taylor series centered at the origin for all $z \in \mathbb{C}$.** <2>1. Since $f$ is entire, $f(z) = \sum_{n=0}^\infty c_n z^n$ converges everywhere on $\mathbb{C}$, with coefficients given by $c_n = \frac{f^{(n)}(0)}{n!}$.
*Proof:* Fundamental property of entire functions.
<2>2. For any $R > 0$ and any $n \geq 0$, Cauchy's coefficient formula gives: $$c_n = \frac{1}{2\pi i} \oint_{|z|=R} \frac{f(z)}{z^{n+1}} \, dz.$$ *Proof:* Cauchy integral formula for derivatives.
<2>3. Q.E.D.

<1>2. **Apply Cauchy's Estimates for each coefficient $c_n$.** <2>1. By the $ML$-inequality on the circle $|z| = R$: $$|c_n| \leq \frac{1}{2\pi} \cdot \left( \sup_{|z|=R} \frac{|f(z)|}{|z|^{n+1}} \right) \cdot (2\pi R) = \frac{\sup_{|z|=R} |f(z)|}{R^n}.$$ *Proof:* Standard derivation of Cauchy's estimates.
<2>2. By the growth hypothesis, on $|z| = R$, $|f(z)| \leq A R^2$.
*Proof:* Given assumption $|f(z)| \leq A|z|^2$.
<2>3. Substituting <2>2 into <2>1 yields the bound: $$|c_n| \leq \frac{A R^2}{R^n} = A R^{2-n} \quad \text{for all } R > 0.$$ *Proof:* Algebra.
<2>4. Q.E.D.

* * *

### Step 2: Vanishing of Higher-Order Coefficients

<1>3. **$c_n = 0$ for all $n \geq 3$.** <2>1. For $n \geq 3$, the exponent $2 - n \leq -1 < 0$.
*Proof:* $n \geq 3 \implies 2 - n \leq -1$.
<2>2. Since the bound $|c_n| \leq A R^{2-n}$ holds for all $R > 0$, taking the limit as $R \to \infty$: $$|c_n| \leq \lim_{R \to \infty} A R^{2-n} = 0.$$ *Proof:* $\lim_{R\to\infty} R^{-k} = 0$ for $k \geq 1$.
<2>3. Therefore, $|c_n| = 0 \implies c_n = 0$ for all $n \geq 3$.
*Proof:* Absolute value is non-negative.
<2>4. Q.E.D.

* * *

### Step 3: Behavior at the Origin and Lower-Order Coefficients

<1>4. **$c_0 = 0$ and $c_1 = 0$.** <2>1. Evaluating the growth condition at $z = 0$: $|f(0)| \leq A |0|^2 = 0 \implies f(0) = 0$, so $c_0 = 0$.
*Proof:* Evaluation at $z=0$.
<2>2. For $c_1$, apply the bound from <1>2.<2>3 with $n = 1$: $|c_1| \leq A R^{2-1} = A R$ for all $R > 0$.
*Proof:* Setting $n=1$ in <1>2.<2>3. <2>3. Taking the limit as $R \to 0^+$: $$|c_1| \leq \lim_{R \to 0^+} A R = 0 \implies c_1 = 0.$$ *Proof:* $R$ can be taken arbitrarily small.
<2>4. Q.E.D.

* * *

### Step 4: Conclusion

<1>5. **$f(z)$ is a polynomial of degree at most 2 (in fact $f(z) = c_2 z^2$).** <2>1. From <1>3 and <1>4, $c_n = 0$ for all $n \neq 2$.
*Proof:* Combining $c_0 = c_1 = 0$ and $c_n = 0$ for $n \geq 3$.
<2>2. Thus $f(z) = c_2 z^2$, which is a polynomial of degree $\leq 2$ (with $|c_2| \leq A$). *Proof:* Direct substitution into Taylor series.
<2>3. Q.E.D.
:::
