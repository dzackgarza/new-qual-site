---
schema: qual/card@1
id: P-ROEFL
kind: problem
title: Uniform compact convergence of $\sum f^{n}$ for analytic $f$ on $\DD$ with
  $f(0)=0$ not a rotation
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
solved: true
---

::: problem
Assume $f(z)$ is analytic in ${\mathbb D}$ and $f(0)=0$ and is not a rotation (i.e. $f(z) \neq e^{i \theta} z$). Show that $\displaystyle \sum_{n=1}^\infty f^{n}(z)$ converges uniformly to an analytic function on compact subsets of ${\mathbb D}$, where $f^{n+1}(z) = f(f^{n}(z))$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f: \mathbb{D} \to \mathbb{D}$ be a holomorphic self-map of the unit disk with $f(0) = 0$ that is not a rotation ($f(z) \neq e^{i\theta} z$). Prove that the series of iterates $\sum_{n=1}^\infty f^n(z)$ converges locally uniformly on $\mathbb{D}$ to a holomorphic function, where $f^1(z) = f(z)$ and $f^{n+1}(z) = f(f^n(z))$.

* * *

### Step 1: Strict Contraction Bound from the Schwarz Lemma

<1>1. **Apply the Schwarz Lemma to $f$.** <2>1. By the Schwarz Lemma, for any holomorphic $f: \mathbb{D} \to \mathbb{D}$ with $f(0) = 0$, $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$.
*Proof:* Schwarz Lemma.
<2>2. The auxiliary function $h(z) = \frac{f(z)}{z}$ for $z \neq 0$ and $h(0) = f'(0)$ is holomorphic on $\mathbb{D}$ and satisfies $|h(z)| \leq 1$ for all $z \in \mathbb{D}$.
*Proof:* Riemann removable singularity and Schwarz Lemma bound.
<2>3. If $|h(z_0)| = 1$ for some $z_0 \in \mathbb{D}$, the Maximum Modulus Principle implies $h(z) \equiv e^{i\theta}$ is constant, so $f(z) = e^{i\theta} z$.
*Proof:* Maximum Modulus Principle applied to $h$.
<2>4. Since $f$ is given to not be a rotation, $h(z)$ cannot attain the value $1$ anywhere in $\mathbb{D}$.
Therefore, $|h(z)| < 1$ for all $z \in \mathbb{D}$.
*Proof:* Strict inequality from the hypothesis that $f$ is not a rotation.
<2>5. Q.E.D.

<1>2. **Uniform geometric bound on compact subsets $K \subset \mathbb{D}$.** <2>1. Let $K \subset \mathbb{D}$ be an arbitrary compact subset.
*Proof:* Setting test compact set.
<2>2. Since $K$ is compact, $r_0 \coloneqq \sup_{z \in K} |z| < 1$.
*Proof:* Continuous function $|z|$ achieves its maximum on compact sets.
<2>3. Choose $R$ such that $r_0 \leq R < 1$.
The closed disk $\overline{D}(0, R) = \{|z| \leq R\}$ is compact and contains $K$.
*Proof:* $K \subseteq \overline{D}(0, R) \subset \mathbb{D}$.
<2>4. Since $|h(z)| < 1$ is continuous on the compact set $\overline{D}(0, R)$, it achieves its maximum: $$c \coloneqq \max_{|z| \leq R} |h(z)| = \max_{|z| \leq R} \left| \frac{f(z)}{z} \right| < 1.$$ *Proof:* Extreme Value Theorem on compact disks.
<2>5. Thus for all $z \in \overline{D}(0, R)$, $|f(z)| \leq c |z|$.
*Proof:* Multiplying $|h(z)| \leq c$ by $|z|$.
<2>6. Q.E.D.

* * *

### Step 2: Exponential Decay of Iterates $f^n(z)$

<1>3. **Induction bound on $|f^n(z)|$ on $K$.** <2>1. Base case $n = 1$: For all $z \in K \subseteq \overline{D}(0, R)$, $|f(z)| \leq c |z| \leq c R \leq R$ (since $c < 1$). *Proof:* By <1>2.<2>5. <2>2. In particular, $f(z) \in \overline{D}(0, R)$ whenever $z \in \overline{D}(0, R)$.
*Proof:* $|f(z)| \leq c |z| \leq |z| \leq R$.
<2>3. Inductive step: Assume $|f^k(z)| \leq c^k |z|$ for all $z \in K$.
*Proof:* Induction hypothesis.
<2>4. Then $f^k(z) \in \overline{D}(0, R)$, so by <1>2.<2>5: $$|f^{k+1}(z)| = |f(f^k(z))| \leq c |f^k(z)| \leq c \cdot (c^k |z|) = c^{k+1} |z| \leq c^{k+1} R.$$ *Proof:* Applying contraction property to the point $f^k(z) \in \overline{D}(0, R)$.
<2>5. Therefore, for all $n \geq 1$ and all $z \in K$: $$|f^n(z)| \leq R \cdot c^n.$$ *Proof:* Mathematical induction.
<2>6. Q.E.D.

* * *

### Step 3: Uniform Convergence via the Weierstrass M-Test

<1>4. **Apply the Weierstrass M-test to $\sum_{n=1}^\infty f^n(z)$.** <2>1. Each iterate $f^n(z)$ is a composition of holomorphic functions, hence holomorphic on $\mathbb{D}$.
*Proof:* Composition of holomorphic functions.
<2>2. On the compact set $K$, $|f^n(z)| \leq M_n \coloneqq R c^n$.
*Proof:* Established in <1>3.<2>5. <2>3. Since $0 \leq c < 1$, the geometric series $\sum_{n=1}^\infty M_n = R \sum_{n=1}^\infty c^n = \frac{R c}{1 - c} < \infty$ converges.
*Proof:* Convergence of geometric series with ratio $c < 1$.
<2>4. By the Weierstrass M-Test, the series $\sum_{n=1}^\infty f^n(z)$ converges uniformly and absolutely on $K$.
*Proof:* Weierstrass M-Test.
<2>5. Since $K \subset \mathbb{D}$ was arbitrary, the series converges locally uniformly on $\mathbb{D}$.
*Proof:* Definition of local uniform convergence.
<2>6. By Weierstrass's theorem on analytic series, the locally uniform limit of holomorphic functions is holomorphic.
*Proof:* Morera's Theorem / Weierstrass convergence theorem.
<2>7. Q.E.D.
:::
