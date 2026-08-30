---
schema: qual/card@1
id: P-CASP23E
kind: problem
title: "Rational approximation of cos(z)/(z(z-5)) on the annulus 3<=|z|<=4"
classification:
  areas:
  - complex-analysis
  topics:
  - Rational Approximation
  - Runge Theorem
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $f(z) = \frac{\cos z}{z(z-5)}$.

(a) Prove that there is a sequence of rational functions $R_n(z)$ whose poles can only occur at $2$ and $6$ such that
$$
\lim_{n \to \infty} \sup_{3 \leq |z| \leq 4} |f(z) - R_n(z)| = 0.
$$

(b) Does there exist a sequence of rational functions $R_n(z)$ whose poles can only occur at $6$ such that the above limit holds?
Justify your answer.
:::

::: {.solution}
<1>1. Part (a): Rational approximation via Runge's Theorem:
<2>1. Let $K = \{z \in \mathbb{C} \mid 3 \le |z| \le 4\}$ be the closed annulus. $K$ is a compact subset of $\mathbb{C}$.
Proof: closed and bounded subset of $\mathbb{C}$.
<2>2. The complement $\mathbb{C} \setminus K$ consists of exactly two connected components:
- The bounded component $U_1 = \{z \in \mathbb{C} \mid |z| < 3\}$, which contains the point $2 \in U_1$.
- The unbounded component $U_2 = \{z \in \mathbb{C} \mid |z| > 4\}$, which contains the point $6 \in U_2$.
Proof: topology of the annulus.
<2>3. The set $S = \{2, 6\}$ contains exactly one point in each connected component of $\mathbb{C} \setminus K$.
Proof: $2 \in U_1$ and $6 \in U_2$.
<2>4. The function $f(z) = \frac{\cos z}{z(z-5)}$ is meromorphic on $\mathbb{C}$ with poles only at $z = 0 \in U_1$ and $z = 5 \in U_2$.
In particular, $f$ has no poles on $K$, so $f$ is holomorphic on an open neighborhood of $K$.
Proof: poles $0, 5 \notin K$.
<2>5. By **Runge’s Theorem** (with prescribed poles), every function holomorphic in a neighborhood of a compact set $K$ can be uniformly approximated on $K$ by rational functions whose poles lie in $S$.
Thus there exists a sequence of rational functions $R_n(z)$ with poles only in $\{2, 6\}$ such that:
\[
\lim_{n \to \infty} \sup_{z \in K} |f(z) - R_n(z)| = 0.
\]
Proof: Runge's Rational Approximation Theorem.

<1>2. Part (b): Non-existence of approximations with poles only at $6$:
<2>1. The answer is **no**: no such sequence of rational functions exists.
Proof: statement of claim.
<2>2. Suppose for contradiction that there exists a sequence of rational functions $R_n(z)$ with poles only at $6$ such that $R_n \to f$ uniformly on $K$.
Proof: assumption for contradiction.
<2>3. Let $\gamma(t) = 3.5 e^{it}$ for $t \in [0, 2\pi]$ be the circle of radius $3.5$ centered at $0$, oriented counterclockwise.
Note that $\gamma \subset K$.
Proof: $3 \le 3.5 \le 4$.
<2>4. For each $n$, the only pole of $R_n(z)$ is at $z = 6$.
Since $|6| = 6 > 3.5$, the closed disk $\overline{D}(0, 3.5)$ contains no poles of $R_n(z)$.
Thus $R_n$ is holomorphic on a simply connected neighborhood of $\overline{D}(0, 3.5)$, so by Cauchy’s Integral Theorem:
\[
\int_\gamma R_n(z) \, dz = 0 \quad \text{for all } n \ge 1.
\]
Proof: Cauchy's Integral Theorem.
<2>5. Since $R_n \to f$ uniformly on $K$ and $\gamma \subset K$, we can pass the limit under the integral sign:
\[
\int_\gamma f(z) \, dz = \lim_{n \to \infty} \int_\gamma R_n(z) \, dz = \lim_{n \to \infty} 0 = 0.
\]
Proof: uniform convergence on compact contours preserves integrals.
<2>6. On the other hand, compute $\int_\gamma f(z) \, dz$ directly using the Residue Theorem:
Inside $\gamma$, the function $f(z) = \frac{\cos z}{z(z-5)}$ has a single singularity at $z = 0$ (a simple pole), since $|0| < 3.5 < 5 = |5|$.
Compute the residue:
\[
\operatorname{Res}(f, 0) = \lim_{z \to 0} z f(z) = \lim_{z \to 0} \frac{\cos z}{z - 5} = \frac{\cos 0}{-5} = -\frac{1}{5}.
\]
Proof: residue at a simple pole.
<2>7. By Cauchy’s Residue Theorem:
\[
\int_\gamma f(z) \, dz = 2\pi i \operatorname{Res}(f, 0) = 2\pi i \left(-\frac{1}{5}\right) = -\frac{2\pi i}{5} \neq 0.
\]
This contradicts <2>5 ($\int_\gamma f(z) \, dz = 0$).
Proof: $-2\pi i / 5 \neq 0$.

<1>3. Conclusion:
(a) The sequence $R_n(z)$ with poles in $\{2, 6\}$ exists by Runge's Theorem.
(b) No sequence with poles only at $6$ can exist. Q.E.D.
Proof: <1>1 and <1>2.
:::
