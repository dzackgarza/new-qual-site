---
schema: qual/card@1
id: P-TZCW3
kind: problem
title: Fundamental theorem of algebra via Rouché's theorem and the maximum modulus
  principle
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Maximum Modulus Principle
  - Polynomials
  - Zeros
relations: []
review: draft
solved: true
---

::: problem
Prove the fundamental theorem of Algebra using

a.  
Rouche's Theorem.

b. 
The maximum modulus principle.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $P(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$ be a non-constant polynomial with complex coefficients, where $n \geq 1$ and $a_n \neq 0$.

**(a) Proof using Rouché's Theorem:**
Let $f(z) = a_n z^n$ and $g(z) = a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$, so that $P(z) = f(z) + g(z)$.

On the circle $C_R = \{z \in \CC : |z| = R\}$ for $R > 0$:
$$
|f(z)| = |a_n| R^n,
$$
$$
|g(z)| \leq |a_{n-1}| R^{n-1} + \cdots + |a_1| R + |a_0|.
$$
Dividing by $|f(z)|$:
$$
\frac{|g(z)|}{|f(z)|} \leq \frac{|a_{n-1}|}{|a_n| R} + \cdots + \frac{|a_0|}{|a_n| R^n}.
$$
As $R \to \infty$, the right-hand side approaches $0$.
Therefore, there exists a sufficiently large $R > 0$ such that for all $z \in C_R$:
$$
|g(z)| < |f(z)|.
$$
By **Rouché's Theorem**, $P(z) = f(z) + g(z)$ and $f(z) = a_n z^n$ have the same number of zeros (counted with multiplicity) in the open disk $D(0, R) = \{z \in \CC : |z| < R\}$.
Since $f(z) = a_n z^n$ has exactly $n \geq 1$ zeros in $D(0, R)$ (a zero of multiplicity $n$ at the origin), $P(z)$ has exactly $n \geq 1$ zeros in $D(0, R) \subset \CC$.
In particular, $P(z)$ has at least one complex root.

**(b) Proof using the Maximum Modulus Principle:**
Suppose towards a contradiction that $P(z)$ has no zeros in $\CC$.
Then the function:
$$
h(z) = \frac{1}{P(z)}
$$
is entire (holomorphic on all of $\CC$).

For $|z| = R > 0$:
$$
|P(z)| = |a_n| R^n \left| 1 + \frac{a_{n-1}}{a_n z} + \cdots + \frac{a_0}{a_n z^n} \right| \geq |a_n| R^n \left( 1 - \frac{1}{2} \right) = \frac{|a_n|}{2} R^n \to \infty \quad \text{as } R \to \infty.
$$
Therefore:
$$
\lim_{|z| \to \infty} |h(z)| = \lim_{|z| \to \infty} \frac{1}{|P(z)|} = 0.
$$
This implies that $|h(z)|$ attains a global maximum on $\CC$:
Since $h(0) = 1/a_0 \neq 0$ (if $a_0 = 0$, $P(0) = 0$ is already a root), there exists $R > 0$ such that $|h(z)| < |h(0)|$ for all $|z| \geq R$.
On the compact closed disk $\overline{D(0, R)}$, the continuous function $|h(z)|$ attains its maximum at some point $z_0 \in D(0, R)$, which is therefore a global maximum of $|h|$ on the entire complex plane $\CC$.

By the **Maximum Modulus Principle**, since $h$ is holomorphic on $\CC$ and $|h|$ attains an interior local maximum at $z_0$, $h$ must be constant.
If $h(z)$ is constant, then $P(z) = 1/h(z)$ is constant, contradicting that $\deg(P) = n \geq 1$.
Thus $P(z)$ must have at least one root in $\CC$.
:::
