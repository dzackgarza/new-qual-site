---
schema: qual/card@1
id: P-TA3FG
kind: problem
title: 'Power series of radius $1$: convergence on $S^1$ versus analyticity at every
  point of $S^1$'
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Singularities
relations: []
review: draft
---

::: problem
Suppose $f(z) = \sum_{n=0}^\infty a_n z^n$ is a power series with radius of convergence exactly 1.

(a) Give an example of such a series that converges at every point of the unit circle $S^1 = \{|z| = 1\}$.

(b) Give an example of such a function $f$ that is analytic at $z = 1$, but whose series $\sum_{n=0}^\infty a_n$ diverges.

(c) Prove that $f$ cannot be analytically continued to be analytic at *every* point of $S^1$.
:::

::: solution
**Goal:** Provide examples illustrating boundary convergence/divergence vs analyticity, and prove that every power series with radius of convergence 1 has at least one singularity on its circle of convergence.

<1>1. Part (a): Example converging everywhere on $S^1$.
    *Proof:*
    <2>1. Define the power series
    $$f(z) = \sum_{n=1}^\infty \frac{z^n}{n^2}.$$
    <2>2. Radius of convergence:
    $$R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right| = \lim_{n \to \infty} \frac{(n+1)^2}{n^2} = 1.$$
    <2>3. Convergence on $S^1$:
        - For any $z \in S^1$, $|z| = 1$, so $\left| \frac{z^n}{n^2} \right| = \frac{1}{n^2}$.
        - The series $\sum_{n=1}^\infty \frac{1}{n^2} < \infty$ converges ($p$-series with $p = 2 > 1$).
        - By the Weierstrass $M$-test, the series converges absolutely (and uniformly) on the entire closed disk $\overline{\mathbb{D}} = \{|z| \le 1\}$.
    <2>4. Thus $f(z)$ converges at every point of $S^1$.

<1>2. Part (b): Example analytic at $z = 1$ with divergent series $\sum a_n$.
    *Proof:*
    <2>1. Define the function
    $$f(z) = \frac{1}{1 + z} = \sum_{n=0}^\infty (-1)^n z^n \quad \text{for } |z| < 1.$$
    <2>2. Radius of convergence: $R = 1$ because the sequence of coefficients is $a_n = (-1)^n$, so $\limsup_{n \to \infty} |a_n|^{1/n} = 1$.
    <2>3. Analyticity at $z = 1$:
        - $f(z) = \frac{1}{1 + z}$ is holomorphic on the open set $\mathbb{C} \setminus \{-1\}$.
        - In particular, $f(z)$ is holomorphic in the open disk $D(1, 1)$, so $f$ is analytic at $z = 1$.
    <2>4. Divergence of the series at $z = 1$:
        - At $z = 1$, $\sum_{n=0}^\infty a_n 1^n = \sum_{n=0}^\infty (-1)^n = 1 - 1 + 1 - 1 + \cdots$.
        - The sequence of terms does not converge to 0 ($\lim_{n \to \infty} (-1)^n \ne 0$), so the series diverges by the Divergence Test.

<1>3. Part (c): $f$ cannot be analytic at every point of $S^1$.
    *Proof:*
    <2>1. Suppose for contradiction that $f$ can be analytically continued across every point of $S^1$.
    <2>2. Local extensions: For each point $w \in S^1$, there exists an open disk $D(w, r_w)$ and a holomorphic function $f_w: D(w, r_w) \to \mathbb{C}$ such that $f_w(z) = f(z)$ on $D(w, r_w) \cap \mathbb{D}$.
    <2>3. Open cover of compact $S^1$:
        - The collection $\{D(w, r_w) \mid w \in S^1\}$ is an open cover of the compact set $S^1$.
        - By compactness, there exists a finite subcover $\{D(w_1, r_1), \dots, D(w_m, r_m)\}$ of $S^1$.
    <2>4. Global extension:
        - Define the open domain $U = \mathbb{D} \cup \bigcup_{j=1}^m D(w_j, r_j)$.
        - The functions $f$ and $f_{w_j}$ agree on all pairwise intersections by the Identity Theorem for connected domains.
        - Thus they define a single holomorphic function $F: U \to \mathbb{C}$ that extends $f$.
    <2>5. Enlarged disk:
        - The domain $U$ is an open set containing the compact set $\overline{\mathbb{D}} = \{|z| \le 1\}$.
        - By the Lebesgue Covering Lemma (or distance from a compact set to the complement), there exists $\varepsilon > 0$ such that the disk $D(0, 1 + \varepsilon) \subseteq U$.
    <2>6. Radius of convergence contradiction:
        - Since $F$ is holomorphic on the open disk $D(0, 1 + \varepsilon)$, its Taylor series centered at 0 converges on all of $D(0, 1 + \varepsilon)$.
        - The Taylor coefficients of $F$ at 0 are given by $\frac{F^{(n)}(0)}{n!} = \frac{f^{(n)}(0)}{n!} = a_n$.
        - This implies that the radius of convergence of $\sum_{n=0}^\infty a_n z^n$ is at least $1 + \varepsilon > 1$.
        - This contradicts the hypothesis that the radius of convergence is exactly 1.
    <2>7. Therefore, $f$ must have at least one singular point on $S^1$.

<1>4. Conclusion:
    *Proof:*
    $\sum z^n/n^2$ converges on $S^1$, $\frac{1}{1+z}$ is analytic at 1 with divergent series, and every power series has a singularity on its circle of convergence by compactness and Taylor's theorem.
:::

