---
schema: qual/card@1
id: E-UU8CC
kind: problem
title: The degree of a map of the circle
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

We define the degree of a continuous map $h: S^1 \to S^1$ as follows.

Let $b_0$ be the point $(1, 0)$ of $S^1$; choose a generator $\gamma$ for the infinite cyclic group $\pi_1(S^1, b_0)$.
If $x_0$ is any point of $S^1$, choose a path $\alpha$ in $S^1$ from $b_0$ to $x_0$, and define $\gamma(x_0) = \hat{\alpha}(\gamma)$.
Then $\gamma(x_0)$ generates $\pi_1(S^1, x_0)$.
The element $\gamma(x_0)$ is independent of the choice of the path $\alpha$, since the fundamental group of $S^1$ is abelian.

Now given $h: S^1 \to S^1$, choose $x_0 \in S^1$ and let $h(x_0) = x_1$.
Consider the homomorphism

$$
h_*: \pi_1(S^1, x_0) \to \pi_1(S^1, x_1).
$$

Since both groups are infinite cyclic, we have

$$
h_*(\gamma(x_0)) = d \cdot \gamma(x_1)
$$

for some integer $d$, if the group is written additively.
The integer $d$ is called the degree of $h$ and is denoted by $\deg h$.

The degree of $h$ is independent of the choice of the generator $\gamma$; choosing the other generator would merely change the sign of both sides.

(a) Show that $d$ is independent of the choice of $x_0$.

(b) Show that if $h, k: S^1 \to S^1$ are homotopic, they have the same degree.

(c) Show that $\deg(h \circ k) = (\deg h) \cdot (\deg k)$.

(d) Compute the degrees of the constant map, the identity map, the reflection map $\rho(x_1, x_2) = (x_1, -x_2)$, and the map $h(z) = z^n$, where $z$ is a complex number.

(e) Show that if $h, k: S^1 \to S^1$ have the same degree, they are homotopic.
:::

::: {.solution}
Let \(\gamma(x)\) denote the preferred generator described in the exercise.

(a) Let \(x_0,x_0'\in S^1\), and choose a path \(\alpha:x_0\to x_0'\). Put \(x_1=h(x_0)\), \(x_1'=h(x_0')\), and \(\beta=h\circ\alpha\). Naturality of change of basepoint gives
\[
\widehat\beta\circ h_{*,x_0}=h_{*,x_0'}\circ\widehat\alpha.
\]
By the definition of the preferred generators,
\[
\widehat\alpha(\gamma(x_0))=\gamma(x_0'),\qquad
\widehat\beta(\gamma(x_1))=\gamma(x_1').
\]
If \(h_{*,x_0}(\gamma(x_0))=d\gamma(x_1)\), applying the displayed naturality equation gives
\[
h_{*,x_0'}(\gamma(x_0'))=d\gamma(x_1').
\]
Thus \(d\) is independent of \(x_0\).

(b) If \(h\simeq k\), choose a path \(\eta(t)=H(x_0,t)\) traced by the basepoint under a homotopy \(H\). The standard homotopy/basepoint-change theorem gives
\[
\widehat\eta\circ h_*=k_*.
\]
Since \(\widehat\eta\) carries the preferred generator at \(h(x_0)\) to that at \(k(x_0)\), the integer multiplying the generator is unchanged. Hence \(\deg h=\deg k\).

(c) If \(k(x_0)=x_1\) and \(h(x_1)=x_2\), then
\[
k_*(\gamma(x_0))=(\deg k)\gamma(x_1),
\]
so
\[
(h\circ k)_*(\gamma(x_0))
=h_*k_*(\gamma(x_0))
=(\deg k)(\deg h)\gamma(x_2).
\]
Thus
\[
\deg(h\circ k)=(\deg h)(\deg k).
\]

(d) A constant map induces the zero homomorphism, so its degree is \(0\). The identity induces the identity homomorphism, so its degree is \(1\). The reflection \(\rho(e^{2\pi it})=e^{-2\pi it}\) reverses the standard generator, so \(\deg\rho=-1\). Finally, \(z\mapsto z^n\) lifts under \(t\mapsto e^{2\pi it}\) to \(t\mapsto nt\), so it carries the generator to \(n\) times itself and has degree \(n\).

(e) Suppose \(\deg h=\deg k=d\). Choose lifts of \(h\) and \(k\) to the universal covering \(q:\mathbb R\to S^1\):
\[
h(e^{2\pi it})=e^{2\pi iH(t)},\qquad
k(e^{2\pi it})=e^{2\pi iK(t)}.
\]
The degree condition is exactly
\[
H(t+1)=H(t)+d,\qquad K(t+1)=K(t)+d.
\]
Hence for \(0\le s\le1\),
\[
L_s(t)=(1-s)H(t)+sK(t)
\]
also satisfies \(L_s(t+1)=L_s(t)+d\). Therefore
\[
F(e^{2\pi it},s)=e^{2\pi iL_s(t)}
\]
is well defined and continuous on \(S^1\times I\), with \(F(-,0)=h\) and \(F(-,1)=k\). Thus \(h\simeq k\).
:::
