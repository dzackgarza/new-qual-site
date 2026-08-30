---
schema: qual/card@1
id: P-CASP26B
kind: problem
title: "Bound on an even holomorphic function on D with f(0)=0 and |f|<2000"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $f : \mathbb{D} \to \mathbb{C}$ be holomorphic such that (i) $f(0) = 0$, (ii) $|f(z)| < 2000$ for all $z \in \mathbb{D}$, (iii) $f(z) = f(-z)$ for all $z \in \mathbb{D}$.

Show that $|f(z)| \leq 2000|z|^2$ for all $z \in \mathbb{D}$, and determine when equality holds.
:::

::: {.solution}
<1>1. Power series expansion and order of zero at the origin:
<2>1. Since $f: \mathbb{D} \to \mathbb{C}$ is holomorphic, it admits a power series expansion around 0:
\[
f(z) = \sum_{n=0}^\infty a_n z^n.
\]
Proof: Taylor expansion for holomorphic functions on the unit disk.
<2>2. Condition (i) gives $a_0 = f(0) = 0$.
Condition (iii) $f(z) = f(-z)$ means $f$ is an even function, so $a_n = 0$ for all odd $n$.
In particular, $a_1 = 0$.
Proof: uniqueness of power series coefficients for even functions.
<2>3. Therefore $f(z) = z^2 g(z)$, where $g(z) = \sum_{k=0}^\infty a_{2k+2} z^{2k}$ is holomorphic on $\mathbb{D}$.
Proof: dividing by $z^2$.

<1>2. Proof of the bound $|f(z)| \le 2000 |z|^2$:
<2>1. For any $0 < r < 1$ and any $z$ with $|z| = r$:
\[
|g(z)| = \frac{|f(z)|}{|z|^2} = \frac{|f(z)|}{r^2} < \frac{2000}{r^2}.
\]
Proof: condition (ii) $|f(z)| < 2000$.
<2>2. By the Maximum Modulus Principle applied to $g$ on the closed disk $\overline{D}(0, r)$, for all $z \in D(0, r)$:
\[
|g(z)| \le \max_{|w| = r} |g(w)| \le \frac{2000}{r^2}.
\]
Proof: Maximum Modulus Principle.
<2>3. Taking the limit as $r \to 1^-$ yields:
\[
|g(z)| \le 2000 \quad \text{for all } z \in \mathbb{D}.
\]
Proof: limit of upper bounds as $r \to 1^-$.
<2>4. Multiplying by $|z|^2$:
\[
|f(z)| = |z^2 g(z)| = |z|^2 |g(z)| \le 2000 |z|^2 \quad \text{for all } z \in \mathbb{D}.
\]
Proof: <2>3.

<1>3. Characterization of equality:
<2>1. Suppose equality $|f(z_0)| = 2000 |z_0|^2$ holds for some non-zero $z_0 \in \mathbb{D} \setminus \{0\}$.
Then $|g(z_0)| = 2000$.
Proof: $|f(z_0)| = |z_0|^2 |g(z_0)|$.
<2>2. Since $|g(z)| \le 2000$ throughout $\mathbb{D}$, the modulus $|g|$ attains its global maximum at the interior point $z_0 \in \mathbb{D}$.
By the Maximum Modulus Principle, $g(z)$ must be constant:
\[
g(z) = 2000 e^{i\theta} \quad \text{for some constant } \theta \in \mathbb{R}.
\]
Proof: Maximum Modulus Principle forces constant functions.
<2>3. Consequently, $f(z) = 2000 e^{i\theta} z^2$.
Notice that for this function, $|f(z)| = 2000 |z|^2 < 2000$ holds strictly for all $z \in \mathbb{D}$, and $f(z) = f(-z)$ and $f(0) = 0$ are satisfied.
Proof: $|z| < 1 \implies 2000|z|^2 < 2000$.

<1>4. Conclusion:
$|f(z)| \le 2000 |z|^2$ for all $z \in \mathbb{D}$, with equality at any non-zero point if and only if $f(z) = 2000 e^{i\theta} z^2$ for some $\theta \in [0, 2\pi)$. Q.E.D.
Proof: <1>2 and <1>3.
:::
