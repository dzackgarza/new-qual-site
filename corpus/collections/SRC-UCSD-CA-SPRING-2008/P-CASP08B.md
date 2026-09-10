---
schema: qual/card@1
id: P-CASP08B
kind: problem
title: "True or False: Cauchy estimates, entire extensions, zero products, essential singularities, and bounded below harmonic functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
For each part, determine if it is always true or sometimes false.
If true give a brief proof.
If false give a counterexample.

(a) If $f \in H(\mathbb{D})$ with $|f(z)| \leq 3$ for all $z$ satisfying $|z| = 1/2$, then $|f''(0)| \leq 24$.

(b) Suppose $f \in H(\mathbb{D})$ and there exists $C > 0$ such that $|f^{(n)}(0)| \leq Cn!$ for all $n \in \mathbb{N}$.
Then $f$ extends to an entire function.

(c) Let $f, g \in H(G)$, where $G$ is open and connected in $\mathbb{C}$.
If $f(z)g(z) \equiv 0$, then either $f$ or $g$ is identically zero in $G$.

(d) Suppose $f \in H(\mathbb{D} \setminus \{0\})$ such that for any positive integer $m$ and any constant $R > 0$, there exists $z \in B(0; 1/2) \setminus \{0\}$ with $|z^m f(z)| > R$.
Then for any $c \in \mathbb{C}$ and any $\epsilon > 0$ there exists $z \in \mathbb{D} \setminus \{0\}$ with $|f(z) - c| < \epsilon$.

(e) If $u(z)$ is a (real-valued) harmonic function defined in all of $\mathbb{C}$ and satisfying $u(z) \geq -1$ for all $z \in \mathbb{C}$, then $u$ is constant.
:::

::: solution
(a) **True.** Cauchy's estimate on the circle $|z|=1/2$ gives
\[
|f''(0)|\le \frac{2!\,3}{(1/2)^2}=24.
\]

(b) **False.** The function
\[
f(z)=\frac1{1-z}
\]
is holomorphic on $\mathbb D$ and satisfies $f^{(n)}(0)=n!$, but it has a pole at
$z=1$ and therefore does not extend to an entire function.

(c) **True.** If neither function were identically zero, choose a point where
$f\ne0$. On a neighborhood of that point, $g=0$; the identity theorem then
gives $g\equiv0$ on the connected region $G$.

(d) **True.** The hypothesis rules out both a removable singularity and a pole
at $0$: if $f$ had a pole of order $N$, then $z^mf(z)$ would be bounded near
$0$ for every $m\ge N$. Hence $0$ is an essential singularity. By the
Casorati--Weierstrass theorem, the image of every punctured neighborhood of
$0$ is dense in $\mathbb C$, which is precisely the asserted approximation of
every $c\in\mathbb C$.

(e) **True.** Since $\mathbb C$ is simply connected, $u$ has a global harmonic
conjugate $v$, and $F=u+iv$ is entire. Then
\[
|e^{-F(z)}|=e^{-u(z)}\le e.
\]
Liouville's theorem makes $e^{-F}$ constant. Differentiating shows $F'=0$, so
$u$ is constant.
:::
