---
schema: qual/card@1
id: P-MMAQ-K5GCBZ3LXD
kind: problem
title: "Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show that $2^{n-1} \\sin\\frac{\\pi}{n} \\sin\\frac{2\\pi}{n} \\cdots \\sin\\frac{(n-1)\\pi}{n} = n \\;$"
classification:
  areas:
  - complex-analysis
  topics:
  - trigonometry
  - polynomials
  - zeros
relations: []
review: draft
solved: true
---

::: problem
Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show
that
$$2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n}
= n
\; .$$

> Hint: $1 - \cos 2 \theta = 2 \sin^2 \theta,\; \sin 2 \theta = 2 \sin \theta \cos \theta$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Use the $n$-th roots of unity to prove that for any integer $n \geq 2$,
$$2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = n.$$

---

### Step 1: Factorization of the Cyclotomic Polynomial

<1>1. **Roots of unity factor the geometric sum.**
  <2>1. The polynomial $z^n - 1$ factors as $(z - 1) P(z)$, where $P(z) = \sum_{k=0}^{n-1} z^k = z^{n-1} + z^{n-2} + \dots + z + 1$.
    *Proof:* Algebraic identity for difference of $n$-th powers.
  <2>2. The $n$ distinct roots of $z^n - 1 = 0$ are $\omega_k = e^{i 2\pi k/n}$ for $k = 0, 1, \dots, n-1$.
    *Proof:* $(e^{i 2\pi k/n})^n = e^{i 2\pi k} = 1$.
  <2>3. Since $\omega_0 = 1$ is the single root of $z - 1 = 0$, the remaining $n-1$ roots $\omega_1, \dots, \omega_{n-1}$ are the zeros of the monic polynomial $P(z)$:
  $$P(z) = \prod_{k=1}^{n-1} (z - e^{i 2\pi k/n}).$$
    *Proof:* Fundamental Theorem of Algebra: a monic polynomial of degree $n-1$ is the product of its linear factors.
  <2>4. Evaluating $P(z)$ at $z = 1$:
  $$\prod_{k=1}^{n-1} (1 - e^{i 2\pi k/n}) = P(1) = 1 + 1 + \dots + 1 = n.$$
    *Proof:* Direct evaluation of $P(1) = \sum_{k=0}^{n-1} 1^k = n$.
  <2>5. Q.E.D.

---

### Step 2: Modulus of the Linear Factors

<1>2. **Evaluate $|1 - e^{i 2\pi k/n}|$ using half-angle trigonometric identities.**
  <2>1. For any real $\phi$, expand $|1 - e^{i\phi}|^2$:
  $$|1 - e^{i\phi}|^2 = (1 - \cos\phi)^2 + \sin^2\phi = 1 - 2\cos\phi + \cos^2\phi + \sin^2\phi = 2(1 - \cos\phi).$$
    *Proof:* Definition of complex modulus.
  <2>2. Using the hint identity $1 - \cos(2\theta) = 2\sin^2\theta$ with $\theta = \phi/2$:
  $$|1 - e^{i\phi}|^2 = 2 \cdot 2\sin^2(\phi/2) = 4\sin^2(\phi/2) \implies |1 - e^{i\phi}| = 2\left|\sin\left(\frac{\phi}{2}\right)\right|.$$
    *Proof:* Taking square roots of non-negative real numbers.
  <2>3. Set $\phi = \frac{2\pi k}{n}$ for $k \in \{1, 2, \dots, n-1\}$. Then $\frac{\phi}{2} = \frac{k\pi}{n} \in (0, \pi)$.
    *Proof:* $1 \leq k \leq n-1 \implies 0 < \frac{k\pi}{n} < \pi$.
  <2>4. Since the sine function is strictly positive on $(0, \pi)$, $\left|\sin\left(\frac{k\pi}{n}\right)\right| = \sin\left(\frac{k\pi}{n}\right)$.
    *Proof:* Positivity of $\sin$ on $(0, \pi)$.
  <2>5. Therefore, $|1 - e^{i 2\pi k/n}| = 2\sin\left(\frac{k\pi}{n}\right)$ for every $1 \leq k \leq n-1$.
    *Proof:* Follows from <2>2 and <2>4.
  <2>6. Q.E.D.

---

### Step 3: Conclusion

<1>3. **Take the modulus of the product formula.**
  <2>1. Taking the complex modulus of both sides of <1>1.<2>4:
  $$\left| \prod_{k=1}^{n-1} (1 - e^{i 2\pi k/n}) \right| = |n| = n.$$
    *Proof:* Modulus of positive integer is itself.
  <2>2. By multiplicativity of the complex modulus:
  $$\prod_{k=1}^{n-1} |1 - e^{i 2\pi k/n}| = n.$$
    *Proof:* $|z_1 \cdots z_m| = |z_1| \cdots |z_m|$.
  <2>3. Substituting the evaluation from <1>2.<2>5:
  $$\prod_{k=1}^{n-1} \left( 2\sin\left(\frac{k\pi}{n}\right) \right) = n \implies 2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = n.$$
    *Proof:* Factoring out $2^{n-1}$ from the $n-1$ terms.
  <2>4. Q.E.D.
:::
