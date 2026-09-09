---
schema: qual/card@1
id: P-RAF25B
kind: problem
title: "Level sets of the distance function have Lebesgue measure zero"
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Measure
  - Lebesgue Differentiation Theorem
  - Distance Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $K \subset \mathbb{R}^2$ be compact.
Given $\delta > 0$, consider the set
$$
K_\delta := \{x \in \mathbb{R}^2 : d(x, K) := \inf_{y \in K} |x - y| = \delta\},
$$
that is, the collection of points at distance $\delta$ from $K$.

(1) Prove that $K_\delta$ is closed and that the distance is always realized, that is, for every $x \in K_\delta$ there is $y_x \in K$ such that $|y_x - x| = \delta$.

(2) Given $x \in K_\delta$ and $\epsilon \in (0, \delta)$, show that
$$
L^2(B_\epsilon(x) \cap K_\delta^c) \geq \frac{\pi \epsilon^2}{4},
$$
where $L^2$ is the Lebesgue measure on $\mathbb{R}^2$, $B_\epsilon(x)$ is the ball of radius $\epsilon$ centered at $x$ and $K_\delta^c = \mathbb{R}^2 \setminus K_\delta$.

(3) Using the Lebesgue differentiation theorem show that $L^2(K_\delta) = 0$.
:::

::: solution
<1>1. The distance level set is closed and the distance is attained.
::: proof
The distance function
\[
d_K(x):=d(x,K)
\]
is $1$-Lipschitz, since for all $x,z\in\mathbb R^2$,
\[
|d_K(x)-d_K(z)|\le |x-z|.
\]
Hence $d_K$ is continuous and
\[
K_\delta=d_K^{-1}(\{\delta\})
\]
is closed.

Fix $x\in K_\delta$. The function
\[
y\longmapsto |x-y|
\]
is continuous on compact $K$, so it attains its minimum at some $y_x\in K$. Thus
\[
|x-y_x|=d(x,K)=\delta.
\]
:::

<1>2. Find a quarter-area ball inside the complement of $K_\delta$.
::: proof
Fix $x\in K_\delta$ and $0<\varepsilon<\delta$. Let
\[
u:=\frac{y_x-x}{|y_x-x|}
\]
and define
\[
c:=x+\frac\varepsilon2u.
\]
Consider the ball $B_{\varepsilon/2}(c)$.

If $z\in B_{\varepsilon/2}(c)$, then
\[
|z-x|
\le |z-c|+|c-x|
<\frac\varepsilon2+\frac\varepsilon2
=\varepsilon,
\]
so
\[
z\in B_\varepsilon(x).
\]
Also
\[
|c-y_x|=\delta-\frac\varepsilon2,
\]
and therefore
\[
|z-y_x|
\le |z-c|+|c-y_x|
<\frac\varepsilon2+\delta-\frac\varepsilon2
=\delta.
\]
Since $y_x\in K$,
\[
d(z,K)\le |z-y_x|<\delta,
\]
so $z\notin K_\delta$. Hence
\[
B_{\varepsilon/2}(c)
\subset B_\varepsilon(x)\cap K_\delta^c.
\]
Taking Lebesgue measure gives
\[
L^2(B_\varepsilon(x)\cap K_\delta^c)
\ge \pi\left(\frac\varepsilon2\right)^2
=\frac{\pi\varepsilon^2}{4}.
\]
:::

<1>3. Apply the Lebesgue differentiation theorem.
::: proof
Suppose $L^2(K_\delta)>0$. Since $K_\delta$ is measurable, the Lebesgue differentiation theorem applied to $\mathbf1_{K_\delta}$ implies that for almost every $x\in K_\delta$,
\[
\lim_{\varepsilon\downarrow0}
\frac{L^2(B_\varepsilon(x)\cap K_\delta)}{\pi\varepsilon^2}
=1.
\]

But Step 2 shows that for every $x\in K_\delta$ and every $0<\varepsilon<\delta$,
\[
L^2(B_\varepsilon(x)\cap K_\delta)
\le \pi\varepsilon^2-\frac{\pi\varepsilon^2}{4}
=\frac34\pi\varepsilon^2.
\]
Thus the density of $K_\delta$ at every one of its points is at most $3/4$ along all sufficiently small balls, contradicting the density theorem if $K_\delta$ had positive measure.

Therefore
\[
\boxed{L^2(K_\delta)=0.}
\]
:::
:::
