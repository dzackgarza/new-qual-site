---
schema: qual/card@1
id: P-MMAQ-CFGXL3QPK7
kind: problem
title: Let $f$ be a meromorphic function in the plane such that
classification:
  areas:
  - complex-analysis
  topics:
  - meromorphic-functions
relations: []
review: draft
---

::: problem
Let $f$ be a meromorphic function in the plane such that `\begin{align*} \lim_{|z|\to\infty} |f(z)| = \infty \end{align*}`{=tex}

1. Show that $f$ has only finitely many poles.

2. Show that $f$ is a rational function.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f$ be a meromorphic function on $\mathbb{C}$ such that $\lim_{|z|\to\infty} |f(z)| = \infty$. Prove that:
1. $f$ has only finitely many poles in $\mathbb{C}$.
2. $f$ is a rational function.

---

### Part 1: Finiteness of Poles

<1>1. **There exists $R > 0$ such that $f$ has no poles in $\{z \in \mathbb{C} : |z| \geq R\}$.**
  <2>1. By hypothesis, $\lim_{|z|\to\infty} |f(z)| = \infty$, which means for $M = 1$, there exists $R > 0$ such that for all $|z| \geq R$ where $f$ is defined, $|f(z)| \geq 1 > 0$.
    *Proof:* Definition of limit at infinity.
  <2>2. Near any pole $p$ of a meromorphic function, $f(z) \to \infty$. But if $p$ were a pole with $|p| \geq R$, by definition of a meromorphic function, $p$ is an isolated singularity.
    *Proof:* Poles of meromorphic functions are isolated.
  <2>3. In fact, on $|z| > R$, the function $g(z) = 1/f(z)$ is holomorphic and bounded: $|g(z)| \leq 1$.
    *Proof:* $f(z) \neq 0$ and $|f(z)| \geq 1$ implies $1/f(z)$ is analytic and bounded by 1 on $|z| > R$.
  <2>4. Therefore, $f(z)$ has no poles in the exterior region $\{z \in \mathbb{C} : |z| \geq R\}$.
    *Proof:* Any pole would have $1/f(p) = 0$, but $1/f$ is analytic and non-vanishing on $|z| > R$ since $|f(z)| \to \infty$.
  <2>5. Q.E.D.

<1>2. **$f$ has only finitely many poles in the entire plane $\mathbb{C}$.**
  <2>1. All poles of $f$ must lie in the bounded closed disk $\overline{D}(0, R) = \{z \in \mathbb{C} : |z| \leq R\}$.
    *Proof:* By <1>1, no poles exist in $\{|z| > R\}$.
  <2>2. The set of poles of a meromorphic function is a discrete (isolated) subset of $\mathbb{C}$.
    *Proof:* Definition of meromorphic functions.
  <2>3. A discrete subset of a compact set $\overline{D}(0, R)$ must be finite.
    *Proof:* Bolzano-Weierstrass theorem: an infinite subset of a compact metric space has an accumulation point, which would contradict discreteness of the pole set.
  <2>4. Thus, $f$ has only finitely many poles in $\mathbb{C}$, say $p_1, p_2, \dots, p_k$.
    *Proof:* Follows from <2>1 and <2>3.
  <2>5. Q.E.D.

---

### Part 2: $f$ is a Rational Function

<1>3. **Subtract the principal parts at all poles to obtain an entire function.**
  <2>1. At each pole $p_j$ ($j = 1, \dots, k$), let the principal part of the Laurent expansion of $f$ be $P_j\left(\frac{1}{z - p_j}\right) = \sum_{m=1}^{d_j} \frac{c_{j,m}}{(z - p_j)^m}$, where $d_j \geq 1$ is the order of the pole $p_j$.
    *Proof:* Laurent expansion at an isolated pole.
  <2>2. Define $h(z) = f(z) - \sum_{j=1}^k P_j\left(\frac{1}{z - p_j}\right)$.
    *Proof:* Algebraic definition.
  <2>3. At each $p_j$, the singularity of $h(z)$ is removable because the principal part has been subtracted: $\lim_{z\to p_j} (z - p_j) (h(z) - \text{regular part}) = 0$.
    *Proof:* Standard property of Laurent series subtraction.
  <2>4. Since $f$ has no other singularities in $\mathbb{C}$, $h(z)$ extends to an entire function on $\mathbb{C}$.
    *Proof:* Riemann's removable singularity theorem applied at each $p_j$.
  <2>5. Q.E.D.

<1>4. **Analyze the behavior of $h(z)$ at infinity.**
  <2>1. For each $j = 1, \dots, k$, $\lim_{|z|\to\infty} P_j\left(\frac{1}{z - p_j}\right) = 0$.
    *Proof:* $\frac{1}{|z - p_j|^m} \to 0$ as $|z| \to \infty$ for all $m \geq 1$.
  <2>2. Thus $\lim_{|z|\to\infty} \sum_{j=1}^k P_j\left(\frac{1}{z - p_j}\right) = 0$.
    *Proof:* Finite sum of limits.
  <2>3. Therefore, $\lim_{|z|\to\infty} |h(z)| = \lim_{|z|\to\infty} \left| f(z) - \sum_{j=1}^k P_j\left(\frac{1}{z - p_j}\right) \right| = \infty$.
    *Proof:* Since $|f(z)| \to \infty$ and the subtracted term tends to $0$.
  <2>4. Q.E.D.

<1>5. **An entire function $h$ satisfying $\lim_{|z|\to\infty} |h(z)| = \infty$ is a non-constant polynomial.**
  <2>1. Since $h$ is entire and $\lim_{|z|\to\infty} |h(z)| = \infty$, the isolated singularity of $h$ at $\infty$ is a pole.
    *Proof:* By definition, an isolated singularity $z_0$ of a holomorphic function is a pole iff $\lim_{z\to z_0} |h(z)| = \infty$ (it cannot be essential by Casorati-Weierstrass, nor removable since the limit is not finite).
  <2>2. An entire function with a pole at $\infty$ has a Laurent series centered at 0 with only finitely many non-zero positive powers: $h(z) = a_n z^n + \dots + a_1 z + a_0$ with $n \geq 1$ and $a_n \neq 0$.
    *Proof:* If the Taylor series had infinitely many non-zero terms, $\infty$ would be an essential singularity.
  <2>3. Thus, $h(z)$ is a polynomial.
    *Proof:* Follows from <2>2.
  <2>4. Q.E.D.

<1>6. **Conclusion: $f(z)$ is a rational function.**
  <2>1. From <1>3.<2>2, $f(z) = h(z) + \sum_{j=1}^k P_j\left(\frac{1}{z - p_j}\right)$.
    *Proof:* Rearrangement of definition of $h(z)$.
  <2>2. $h(z)$ is a polynomial, and each $P_j\left(\frac{1}{z - p_j}\right)$ is a rational function (a finite sum of terms $\frac{c}{(z - p_j)^m}$).
    *Proof:* By <1>5.<2>3 and <1>3.<2>1.
  <2>3. The sum of a polynomial and finitely many rational functions is a rational function.
    *Proof:* Closure of the field of rational functions $\mathbb{C}(z)$ under addition.
  <2>4. Q.E.D.
:::
