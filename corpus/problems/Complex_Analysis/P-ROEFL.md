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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: problem
Assume $f(z)$ is analytic in ${\mathbb D}$ and $f(0)=0$ and is not a rotation (i.e. $f(z) \neq e^{i \theta} z$). Show that $\displaystyle \sum_{n=1}^\infty f^{n}(z)$ converges uniformly to an analytic function on compact subsets of ${\mathbb D}$, where $f^{n+1}(z) = f(f^{n}(z))$.
:::

::: {.solution}
**Goal:** Let $f: \mathbb{D} \to \mathbb{D}$ be a holomorphic self-map of the unit disk with $f(0) = 0$ that is not a rotation ($f(z) \neq e^{i\theta} z$). Prove that the series of iterates $\sum_{n=1}^\infty f^n(z)$ converges locally uniformly on $\mathbb{D}$ to a holomorphic function, where $f^1(z) = f(z)$ and $f^{n+1}(z) = f(f^n(z))$.

* * *

### Step 1: Strict Contraction Bound from the Schwarz Lemma

<1>1. **Apply the Schwarz Lemma to $f$.** <2>1. By the Schwarz Lemma, for any holomorphic $f: \mathbb{D} \to \mathbb{D}$ with $f(0) = 0$, $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$.
::: {.proof}
The Schwarz Lemma states that a holomorphic self-map $f \colon \mathbb{D} \to \mathbb{D}$ with $f(0) = 0$ satisfies $|f(z)| \le |z|$ for all $z \in \mathbb{D}$ and $|f'(0)| \le 1$.
:::
<2>2. The auxiliary function $h(z) = \frac{f(z)}{z}$ for $z \neq 0$ and $h(0) = f'(0)$ is holomorphic on $\mathbb{D}$ and satisfies $|h(z)| \leq 1$ for all $z \in \mathbb{D}$.
::: {.proof}
Since $f(0) = 0$, the quotient $\frac{f(z)}{z}$ has a removable singularity at $0$ with value $f'(0)$, so $h$ is holomorphic on $\mathbb{D}$; the Schwarz Lemma bound $|f(z)| \le |z|$ gives $|h(z)| = \frac{|f(z)|}{|z|} \le 1$ for $z \neq 0$, and $|h(0)| = |f'(0)| \le 1$.
:::
<2>3. If $|h(z_0)| = 1$ for some $z_0 \in \mathbb{D}$, the Maximum Modulus Principle implies $h(z) \equiv e^{i\theta}$ is constant, so $f(z) = e^{i\theta} z$.
::: {.proof}
A holomorphic function attaining its maximum modulus at an interior point is constant; since $|h| \le 1$ and $|h(z_0)| = 1$, $h$ is constant of modulus $1$, so $h \equiv e^{i\theta}$ and $f(z) = z h(z) = e^{i\theta} z$.
:::
<2>4. Since $f$ is given to not be a rotation, $h(z)$ cannot attain the value $1$ anywhere in $\mathbb{D}$.
Therefore, $|h(z)| < 1$ for all $z \in \mathbb{D}$.
::: {.proof}
If $|h(z_0)| = 1$ for some $z_0$, then by <2>3 $f$ would be a rotation $z \mapsto e^{i\theta} z$, contradicting the hypothesis; hence $|h(z)| < 1$ everywhere.
:::
<2>5. Q.E.D.

<1>2. **Uniform geometric bound on compact subsets $K \subset \mathbb{D}$.** <2>1. Let $K \subset \mathbb{D}$ be an arbitrary compact subset.
::: {.proof}
We fix an arbitrary compact subset $K$ of $\mathbb{D}$ on which to establish the uniform bound.
:::
<2>2. Since $K$ is compact, $r_0 \coloneqq \sup_{z \in K} |z| < 1$.
::: {.proof}
The function $z \mapsto |z|$ is continuous, so it attains its maximum on the compact set $K$; since $K \subset \mathbb{D}$, this maximum $r_0$ is strictly less than $1$.
:::
<2>3. Choose $R$ such that $r_0 \leq R < 1$.
The closed disk $\overline{D}(0, R) = \{|z| \leq R\}$ is compact and contains $K$.
::: {.proof}
Any $R$ with $r_0 \le R < 1$ works; then $|z| \le r_0 \le R$ for every $z \in K$, so $K \subseteq \overline{D}(0, R) \subset \mathbb{D}$.
:::
<2>4. Since $|h(z)| < 1$ is continuous on the compact set $\overline{D}(0, R)$, it achieves its maximum: $$c \coloneqq \max_{|z| \leq R} |h(z)| = \max_{|z| \leq R} \left| \frac{f(z)}{z} \right| < 1.$$
::: {.proof}
The continuous function $|h|$ attains its maximum $c$ on the compact disk $\overline{D}(0, R)$ by the Extreme Value Theorem; since $|h(z)| < 1$ for every $z \in \mathbb{D}$ by <1>1.<2>4>, this maximum satisfies $c < 1$.
:::
<2>5. Thus for all $z \in \overline{D}(0, R)$, $|f(z)| \leq c |z|$.
::: {.proof}
For $z \neq 0$, $|f(z)| = |z| \cdot |h(z)| \le c |z|$; at $z = 0$ both sides vanish, so the inequality holds for all $z \in \overline{D}(0, R)$.
:::
<2>6. Q.E.D.

* * *

### Step 2: Exponential Decay of Iterates $f^n(z)$

<1>3. **Induction bound on $|f^n(z)|$ on $K$.** <2>1. Base case $n = 1$: For all $z \in K \subseteq \overline{D}(0, R)$, $|f(z)| \leq c |z| \leq c R \leq R$ (since $c < 1$).
::: {.proof}
By <1>2.<2>5>, $|f(z)| \le c|z|$; since $|z| \le R$ and $c < 1$, this gives $|f(z)| \le cR \le R$.
:::
<2>2. In particular, $f(z) \in \overline{D}(0, R)$ whenever $z \in \overline{D}(0, R)$.
::: {.proof}
The bound $|f(z)| \le c|z| \le |z| \le R$ shows $f$ maps $\overline{D}(0, R)$ into itself.
:::
<2>3. Inductive step: Assume $|f^k(z)| \leq c^k |z|$ for all $z \in K$.
::: {.proof}
This is the induction hypothesis.
:::
<2>4. Then $f^k(z) \in \overline{D}(0, R)$, so by <1>2.<2>5>: $$|f^{k+1}(z)| = |f(f^k(z))| \leq c |f^k(z)| \leq c \cdot (c^k |z|) = c^{k+1} |z| \leq c^{k+1} R.$$
::: {.proof}
Since $|f^k(z)| \le c^k |z| \le c^k R \le R$, the point $f^k(z)$ lies in $\overline{D}(0, R)$; applying the contraction bound <1>2.<2>5> to this point gives $|f(f^k(z))| \le c |f^k(z)|$, and the induction hypothesis gives $|f^k(z)| \le c^k |z|$.
:::
<2>5. Therefore, for all $n \geq 1$ and all $z \in K$: $$|f^n(z)| \leq R \cdot c^n.$$
::: {.proof}
Induction on $n$ using the base case <2>1 and the step <2>4 yields $|f^n(z)| \le c^n |z| \le c^n R$.
:::
<2>6. Q.E.D.

* * *

### Step 3: Uniform Convergence via the Weierstrass M-Test

<1>4. **Apply the Weierstrass M-test to $\sum_{n=1}^\infty f^n(z)$.** <2>1. Each iterate $f^n(z)$ is a composition of holomorphic functions, hence holomorphic on $\mathbb{D}$.
::: {.proof}
$f^n$ is the $n$-fold composition of the holomorphic map $f$ with itself, and a composition of holomorphic functions is holomorphic.
:::
<2>2. On the compact set $K$, $|f^n(z)| \leq M_n \coloneqq R c^n$.
::: {.proof}
This is exactly the bound established in <1>3.<2>5>.
:::
<2>3. Since $0 \leq c < 1$, the geometric series $\sum_{n=1}^\infty M_n = R \sum_{n=1}^\infty c^n = \frac{R c}{1 - c} < \infty$ converges.
::: {.proof}
The geometric series $\sum_{n=1}^\infty c^n$ converges to $\frac{c}{1-c}$ because its ratio $c$ satisfies $|c| < 1$.
:::
<2>4. By the Weierstrass M-Test, the series $\sum_{n=1}^\infty f^n(z)$ converges uniformly and absolutely on $K$.
::: {.proof}
The Weierstrass M-test states that if $|f^n(z)| \le M_n$ on $K$ and $\sum M_n$ converges, then $\sum f^n(z)$ converges uniformly and absolutely on $K$; <2>2 and <2>3 supply exactly these hypotheses.
:::
<2>5. Since $K \subset \mathbb{D}$ was arbitrary, the series converges locally uniformly on $\mathbb{D}$.
::: {.proof}
Local uniform convergence means uniform convergence on every compact subset; since $K$ was arbitrary, the series converges uniformly on every compact subset of $\mathbb{D}$.
:::
<2>6. By Weierstrass's theorem on analytic series, the locally uniform limit of holomorphic functions is holomorphic.
::: {.proof}
A locally uniform limit of holomorphic functions is holomorphic: uniform convergence on compact sets permits interchanging the limit with contour integrals, so Morera's theorem applies.
:::
<2>7. Q.E.D.
:::
