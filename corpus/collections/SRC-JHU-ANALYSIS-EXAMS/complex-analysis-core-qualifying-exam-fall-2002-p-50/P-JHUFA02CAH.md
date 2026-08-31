---
schema: qual/card@1
id: P-JHUFA02CAH
kind: problem
title: "Entire functions bounded by the square of the modulus"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Determine all entire functions $f: \mathbb{C} \to \mathbb{C}$ for which $|f(z)| \le |z|^2$ for all $z \in \mathbb{C}$.
:::

::: solution
**Goal:** Determine all entire functions $f(z)$ satisfying $|f(z)| \le |z|^2$ for all $z \in \mathbb{C}$.

<1>1. Vanishing of coefficients $a_n$ for $n \ge 3$ via Cauchy estimates:
    *Proof:*
    <2>1. Since $f$ is entire, it has a global power series expansion centered at 0:
    $$f(z) = \sum_{n=0}^\infty a_n z^n, \qquad a_n = \frac{f^{(n)}(0)}{n!}.$$
    <2>2. By Cauchy's Estimate on the circle $C_R = \{z \in \mathbb{C} : |z| = R\}$ for any $R > 0$:
    $$|a_n| \le \frac{1}{R^n} \max_{|z|=R} |f(z)| \le \frac{R^2}{R^n} = R^{2-n}.$$
    <2>3. For any $n \ge 3$, the exponent $2 - n \le -1 < 0$.
    <2>4. Taking the limit as $R \to \infty$:
    $$|a_n| \le \lim_{R \to \infty} R^{2-n} = 0 \implies a_n = 0 \quad \text{for all } n \ge 3.$$
    <2>5. Therefore $f(z)$ is a polynomial of degree at most 2:
    $$f(z) = a_0 + a_1 z + a_2 z^2.$$

<1>2. Vanishing of $a_0$ and $a_1$:
    *Proof:*
    <2>1. Setting $z = 0$ in the hypothesis $|f(z)| \le |z|^2$:
    $$|f(0)| = |a_0| \le 0^2 = 0 \implies a_0 = 0.$$
    <2>2. Thus $f(z) = a_1 z + a_2 z^2 = z(a_1 + a_2 z)$.
    <2>3. For all $z \neq 0$, dividing by $|z|$ gives:
    $$|a_1 + a_2 z| = \frac{|f(z)|}{|z|} \le \frac{|z|^2}{|z|} = |z|.$$
    <2>4. Taking the limit as $z \to 0$:
    $$|a_1| = \lim_{z \to 0} |a_1 + a_2 z| \le \lim_{z \to 0} |z| = 0 \implies a_1 = 0.$$

<1>3. Constraint on the leading coefficient $a_2$:
    *Proof:*
    <2>1. From <1>1 and <1>2, $f(z) = a_2 z^2$.
    <2>2. The bound $|f(z)| \le |z|^2$ becomes $|a_2 z^2| = |a_2| |z|^2 \le |z|^2$ for all $z \in \mathbb{C}$.
    <2>3. Evaluating at $z = 1$ yields $|a_2| \le 1$.
    <2>4. Conversely, for any complex constant $c \in \mathbb{C}$ with $|c| \le 1$, the function $f(z) = c z^2$ is entire and satisfies $|f(z)| = |c| |z|^2 \le |z|^2$ for all $z \in \mathbb{C}$.

<1>4. Conclusion:
    *Proof:*
    The entire functions satisfying $|f(z)| \le |z|^2$ for all $z \in \mathbb{C}$ are precisely
    $$f(z) = c z^2 \quad \text{for any } c \in \mathbb{C} \text{ with } |c| \le 1.$$
:::
