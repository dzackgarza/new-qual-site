---
schema: qual/card@1
id: E-SS2.EX-9
kind: exercise
title: "A holomorphic self-map with a fixed point of derivative one"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
9. Let Ω be a bounded open subset of $\mathbb { C } ,$ and $\varphi : \Omega \to \Omega$ a holomorphic function.
   Prove that if there exists a point $z _ { 0 } \in \Omega$ such that

$$
\varphi (z _ {0}) = z _ {0} \quad \mathrm{and} \quad \varphi^ {\prime} (z _ {0}) = 1
$$

then $\varphi$ is linear.

[Hint: Why can one assume that $z _ { 0 } = 0 ?$ Write $\varphi ( z ) = z + a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ near 0, and prove that if $\varphi _ { k } = \varphi \circ \cdots \circ \varphi$ (where $\varphi$ appears k times), then $\varphi _ { k } ( z ) =$ $z + k a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ . Apply the Cauchy inequalities and let $k \to \infty$ to conclude the proof. Here we use the standard O notation, where $f ( z ) = O ( g ( z ) )$ as $z  0$ means that $| f ( z ) | \leq C | g ( z ) |$ for some constant C as $| z | \xrightarrow { } 0 . ]$
:::

::: {.solution}
<1>1. Translation to the origin and setup:
<2>1. By translating $\Omega$ via $w \mapsto w - z_0$, we may assume without loss of generality that $0 \in \Omega$, $\varphi(0) = 0$, and $\varphi'(0) = 1$.
Proof: translation is an automorphism of $\mathbb{C}$.
<2>2. Since $\Omega$ is bounded, there exists a constant $M > 0$ such that $|\varphi(z)| \le M$ for all $z \in \Omega$.
Since $0 \in \Omega$ is open, there exists $r > 0$ such that the closed disk $\overline{D}_r(0) \subset \Omega$.
Proof: definition of bounded open subset of $\mathbb{C}$.

<1>2. Taylor expansion of iterates $\varphi_k$:
<2>1. Suppose for contradiction that $\varphi$ is not the identity map.
Let $n \ge 2$ be the smallest integer such that the $n$-th Taylor coefficient of $\varphi$ at $0$ is non-zero, so:
\[
\varphi(z) = z + a_n z^n + O(z^{n+1}) \quad \text{with } a_n \neq 0.
\]
Proof: Taylor expansion of holomorphic functions.
<2>2. For $k \ge 1$, let $\varphi_k = \underbrace{\varphi \circ \cdots \circ \varphi}_{k \text{ times}}$ be the $k$-th iterate.
We claim by induction that:
\[
\varphi_k(z) = z + k a_n z^n + O(z^{n+1}).
\]
For $k = 1$, the base case holds. Assuming the claim for $k$:
\[
\begin{aligned}
\varphi_{k+1}(z) &= \varphi(\varphi_k(z)) \\
&= (z + k a_n z^n + O(z^{n+1})) + a_n (z + k a_n z^n + O(z^{n+1}))^n + O(z^{n+1}) \\
&= z + k a_n z^n + a_n z^n + O(z^{n+1}) \\
&= z + (k+1) a_n z^n + O(z^{n+1}).
\end{aligned}
\]
Thus the claim holds for all $k \ge 1$.
Proof: mathematical induction on $k$.

<1>3. Application of Cauchy’s Inequalities:
<2>1. Because $\varphi(\Omega) \subseteq \Omega$, every iterate satisfies $\varphi_k(\Omega) \subseteq \Omega$, so $|\varphi_k(z)| \le M$ for all $z \in \overline{D}_r(0)$ and all $k \ge 1$.
Proof: invariance of the bounded domain $\Omega$ under iteration.
<2>2. The $n$-th derivative of $\varphi_k$ at $0$ is $\frac{\varphi_k^{(n)}(0)}{n!} = k a_n$.
By Cauchy’s Inequalities for derivatives:
\[
|k a_n| \le \frac{\sup_{|z|=r} |\varphi_k(z)|}{r^n} \le \frac{M}{r^n}.
\]
Proof: Cauchy’s Inequalities for holomorphic functions on disks.
<2>3. Dividing by $k$:
\[
|a_n| \le \frac{M}{k r^n} \quad \text{for every } k \ge 1.
\]
Taking $k \to \infty$ yields $|a_n| = 0$, so $a_n = 0$, contradicting the assumption that $a_n \neq 0$.
Proof: squeeze theorem as $k \to \infty$.

<1>4. Conclusion:
All non-linear Taylor coefficients vanish, so $\varphi(z) = z_0 + (z - z_0) = z$ on $\Omega$, proving $\varphi$ is linear (the identity). Q.E.D.
Proof: <1>1 through <1>3.
:::
