---
schema: qual/card@1
id: P-H2WTL
kind: problem
title: Integrals of $z^n$ and $1/((z-a)(z-b))$ on circles, without Cauchy's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Winding Number
  - Integrals
relations: []
review: draft
---

::: {.problem}
The question provides some insight into Cauchy's theorem.
Solve the problem without using the Cauchy theorem.

1. Evaluate the integral $\displaystyle{\int_{\gamma} z^n dz}$ for all integers $n$.
   Here $\gamma$ is any circle centered at the origin with the positive (counterclockwise) orientation.

2. Same question as (a), but with $\gamma$ any circle not containing the origin.

3. Show that if $|a|<r<|b|$, then $\displaystyle{\int_{\gamma}\frac{dz}{(z-a)(z-b)} dz=\frac{2\pi i}{a-b}}$.
   Here $\gamma$ denotes the circle centered at the origin, of radius $r$, with the positive orientation.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate the given contour integrals purely by direct parametrization and power series expansions, without using Cauchy's theorem.

* * *

### Part 1: Integral of $z^n$ on a Circle Centered at 0

<1>1. **Parametrize $\gamma(t) = R e^{it}$ for $t \in [0, 2\pi]$ ($R > 0$).** <2>1. $dz = i R e^{it} dt$, and $z^n = R^n e^{int}$.
*Proof:* Derivative of parametrization.
<2>2. The integral becomes: $$\int_\gamma z^n \, dz = \int_0^{2\pi} R^n e^{int} \cdot i R e^{it} \, dt = i R^{n+1} \int_0^{2\pi} e^{i(n+1)t} \, dt.$$ *Proof:* Substitution into definition of line integral.
<2>3. Case $n = -1$: $n+1 = 0 \implies \int_0^{2\pi} e^0 \, dt = 2\pi$.
Thus $\int_\gamma z^{-1} \, dz = i R^0 (2\pi) = 2\pi i$.
*Proof:* Evaluating the integral of constant 1. <2>4. Case $n \neq -1$: $n+1 \neq 0$, so: $$\int_0^{2\pi} e^{i(n+1)t} \, dt = \left[ \frac{e^{i(n+1)t}}{i(n+1)} \right]_0^{2\pi} = \frac{e^{i(n+1)2\pi} - 1}{i(n+1)} = \frac{1 - 1}{i(n+1)} = 0.$$ *Proof:* $e^{i 2\pi k} = 1$ for all integers $k = n+1 \neq 0$.
<2>5. Therefore: $$\int_\gamma z^n \, dz = \begin{cases} 2\pi i & \text{if } n = -1, \\ 0 & \text{if } n \in \mathbb{Z} \setminus \{-1\}. \end{cases}$$ *Proof:* Combining <2>3 and <2>4. <2>6. Q.E.D.

* * *

### Part 2: Integral of $z^n$ on a Circle Not Containing 0

<1>2. **Let $\gamma$ be a circle whose closed interior does not contain the origin $0$.
Then $\int_\gamma z^n \, dz = 0$ for all $n \in \mathbb{Z}$.** <2>1. Case $n \neq -1$: For every $n \neq -1$, $z^n$ has a global single-valued primitive on $\mathbb{C} \setminus \{0\}$, namely $F(z) = \frac{z^{n+1}}{n+1}$.
*Proof:* $\frac{d}{dz}\left(\frac{z^{n+1}}{n+1}\right) = z^n$.
<2>2. The integral of a function with a continuous primitive along any closed loop is zero: $\int_\gamma z^n \, dz = F(\gamma(2\pi)) - F(\gamma(0)) = 0$.
*Proof:* Fundamental Theorem of Calculus for line integrals.
<2>3. Case $n = -1$: Since the circle $\gamma$ does not enclose the origin, the winding number of $\gamma$ around $0$ is $\text{Ind}_\gamma(0) = 0$.
*Proof:* The origin lies in the unbounded connected component of $\mathbb{C} \setminus \gamma$.
<2>4. Equivalently, there exists a ray from the origin (e.g. through the opposite side of $\gamma$) on which a continuous single-valued branch of $\log z$ is defined that contains the entire circle $\gamma$.
Thus $\frac{1}{z} = \frac{d}{dz}\log z$ has a primitive on an open neighborhood of $\gamma$.
*Proof:* A slit plane $\mathbb{C} \setminus L$ containing the circle admits a holomorphic logarithm branch.
<2>5. By the FTC for line integrals, $\int_\gamma \frac{1}{z} \, dz = 0$.
*Proof:* Integral of a derivative along a closed curve in the branch domain.
<2>6. Therefore, $\int_\gamma z^n \, dz = 0$ for all $n \in \mathbb{Z}$.
*Proof:* Combines <2>2 and <2>5. <2>7. Q.E.D.

* * *

### Part 3: Evaluation of $\int_\gamma \frac{dz}{(z-a)(z-b)}$ for $|a| < r < |b|$

<1>3. **Partial fraction decomposition of the integrand.** <2>1. Algebraic partial fractions: $$\frac{1}{(z-a)(z-b)} = \frac{1}{a-b} \left( \frac{1}{z-a} - \frac{1}{z-b} \right).$$ *Proof:* $\frac{1}{a-b}\left(\frac{(z-b)-(z-a)}{(z-a)(z-b)}\right) = \frac{1}{a-b}\left(\frac{a-b}{(z-a)(z-b)}\right) = \frac{1}{(z-a)(z-b)}$.
<2>2. Thus: $$\int_\gamma \frac{dz}{(z-a)(z-b)} = \frac{1}{a-b} \left( \int_\gamma \frac{dz}{z-a} - \int_\gamma \frac{dz}{z-b} \right).$$ *Proof:* Linearity of the integral.
<2>3. Q.E.D.

<1>4. **Evaluate $\int_\gamma \frac{dz}{z-a}$ using geometric series since $|a| < r = |z|$.** <2>1. On $\gamma$, $|z| = r > |a|$, so $|a/z| = |a|/r < 1$.
*Proof:* Given $|a| < r$.
<2>2. Expand $\frac{1}{z-a} = \frac{1}{z} \frac{1}{1 - a/z} = \frac{1}{z} \sum_{k=0}^\infty \left(\frac{a}{z}\right)^k = \sum_{k=0}^\infty a^k z^{-(k+1)} = \frac{1}{z} + \sum_{k=1}^\infty a^k z^{-(k+1)}$.
*Proof:* Geometric series expansion for $|a/z| < 1$, which converges uniformly on $|z| = r$.
<2>3. Integrating term-by-term on $\gamma$ using Part 1 (<1>1.<2>5): $$\int_\gamma \frac{dz}{z-a} = \int_\gamma \frac{dz}{z} + \sum_{k=1}^\infty a^k \int_\gamma z^{-(k+1)} \, dz = 2\pi i + \sum_{k=1}^\infty a^k \cdot 0 = 2\pi i.$$ *Proof:* By Part 1, $\int_\gamma z^{-1}\,dz = 2\pi i$ and $\int_\gamma z^{-m}\,dz = 0$ for all $m \geq 2$.
<2>4. Q.E.D.

<1>5. **Evaluate $\int_\gamma \frac{dz}{z-b}$ using geometric series since $|b| > r = |z|$.** <2>1. On $\gamma$, $|z| = r < |b|$, so $|z/b| = r/|b| < 1$.
*Proof:* Given $r < |b|$.
<2>2. Expand $\frac{1}{z-b} = -\frac{1}{b} \frac{1}{1 - z/b} = -\sum_{k=0}^\infty \frac{z^k}{b^{k+1}}$, which converges uniformly on $|z| = r$.
*Proof:* Geometric series expansion for $|z/b| < 1$.
<2>3. Integrating term-by-term on $\gamma$ using Part 1 (<1>1.<2>5): $$\int_\gamma \frac{dz}{z-b} = -\sum_{k=0}^\infty \frac{1}{b^{k+1}} \int_\gamma z^k \, dz = -\sum_{k=0}^\infty \frac{1}{b^{k+1}} \cdot 0 = 0.$$ *Proof:* By Part 1, $\int_\gamma z^k\,dz = 0$ for all $k \geq 0$.
<2>4. Q.E.D.

<1>6. **Combine the results.** <2>1. Substituting <1>4.<2>3 and <1>5.<2>3 into <1>3.<2>2: $$\int_\gamma \frac{dz}{(z-a)(z-b)} = \frac{1}{a-b} (2\pi i - 0) = \frac{2\pi i}{a-b}.$$ *Proof:* Direct substitution.
<2>2. Q.E.D.
:::
