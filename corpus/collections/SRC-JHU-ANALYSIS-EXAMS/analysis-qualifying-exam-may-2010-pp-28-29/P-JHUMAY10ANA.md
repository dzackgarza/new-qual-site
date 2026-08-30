---
schema: qual/card@1
id: P-JHUMAY10ANA
kind: problem
title: "f has a removable singularity at 0."
classification:
  areas:
  - complex-analysis
  topics:
  - Isolated Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f$ be a holomorphic function on the punctured disk $U = \{z \in \mathbb{C} : 0 < |z| < 1\}$.
Suppose that $|f(z)| \le |z|^{-1/2}$ for all $z \in U$.
Prove that $f$ has a removable singularity at $0$.
:::

::: {.solution}
<1>1. Expand $f(z)$ in its Laurent series on $U = \{z \in \mathbb{C} : 0 < |z| < 1\}$:
\[
f(z) = \sum_{n=-\infty}^\infty c_n z^n, \quad \text{where } c_n = \frac{1}{2\pi i} \oint_{|z| = r} \frac{f(z)}{z^{n+1}}\,dz \quad (0 < r < 1).
\]
Proof: Laurent Expansion Theorem for holomorphic functions on an annulus / punctured disk.

<1>2. Bound the negative Laurent coefficients $c_{-k}$ for $k \ge 1$: <2>1. For $n = -k$ with $k \ge 1$, the integral representation is:
\[
c_{-k} = \frac{1}{2\pi i} \oint_{|z| = r} f(z) z^{k-1}\,dz.
\]
Proof: substitution $n = -k$ in <1>1. <2>2. On the circle $|z| = r$, $|f(z)| \le r^{-1/2}$ by hypothesis.
Proof: hypothesis $|f(z)| \le |z|^{-1/2}$.
<2>3. Applying the $ML$-inequality along the circular path of length $2\pi r$:
\[
|c_{-k}| \le \frac{1}{2\pi} \left(\sup_{|z|=r} |f(z)|\right) r^{k-1} (2\pi r) \le r^{-1/2} \cdot r^k = r^{k - 1/2}.
\]
Proof: $ML$-inequality on circle of radius $r$.
<2>4. Since $k \ge 1$, the exponent satisfies $k - 1/2 \ge 1/2 > 0$.
Proof: $k \ge 1 \implies k - 1/2 \ge 1/2$.

<1>3. Show that $c_{-k} = 0$ for all $k \ge 1$: <2>1. The value of $c_{-k}$ is independent of the choice of $r \in (0, 1)$ by Cauchy’s Integral Theorem.
Proof: deformation of contour.
<2>2. Taking the limit as $r \to 0^+$ in <2>3:
\[
|c_{-k}| \le \lim_{r \to 0^+} r^{k - 1/2} = 0.
\]
Proof: <2>3 and <2>4. <2>3. Thus $c_{-k} = 0$ for every $k \ge 1$.
Proof: $|c_{-k}| = 0$.

<1>4. Conclusion: The principal part of the Laurent series vanishes identically:
\[
f(z) = \sum_{n=0}^\infty c_n z^n \quad \text{for } 0 < |z| < 1.
\]
Setting $f(0) = c_0$ extends $f$ to a holomorphic function on the entire unit disk $|z| < 1$, so $f$ has a removable singularity at $0$.
Q.E.D. Proof: Riemann's Removable Singularity Theorem and <1>3.
:::
