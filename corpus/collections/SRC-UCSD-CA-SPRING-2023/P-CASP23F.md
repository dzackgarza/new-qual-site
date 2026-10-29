---
schema: qual/card@1
id: P-CASP23F
kind: problem
title: "Green's function on D\\{a} and failure of the Dirichlet problem"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Dirichlet Problem
  - Green's Function
  - Boundary Values
relations: []
review: draft
---

::: {.problem}
Let $a \in \DD$ and $G = \DD \setminus \{a\}$.

(a) Construct a harmonic function $v$ on $G$ such that the following two conditions are satisfied: $\lim_{z \to z^*} v(z) = 0$ for all $z^* \in \circlegroup$ and $\lim_{z \to a} v(z) = +\infty$.
Write down an explicit formula for the function $v$ you constructed.

(b) Let $f \in C(\partial G)$ be defined as $f(z) = 0$ for $z \in \circlegroup$ and $f(a) = 2$.
Prove that the Dirichlet problem on $G$ with boundary data $f$ has no solution: there is no harmonic function $u$ on $G$ such that $\lim_{z \to z_0} u(z) = f(z_0)$ for all $z_0 \in \partial G$.
:::

::: {.solution}
(a) The Green function of the unit disk with pole at $a$ gives the required
example:
\[
v(z)=\log\left|
\frac{1-\overline a z}{z-a}
\right|.
\]
It is harmonic on $\DD\setminus\{a\}$. If $|z|=1$, then
\[
|1-\overline a z|=|z-a|,
\]
so $v(z)\to0$ as $z$ tends to any point of $\circlegroup$. As $z\to a$, the
numerator tends to $1-|a|^2>0$ while the denominator tends to $0$, hence
$v(z)\to+\infty$.

(b) Suppose such a harmonic function $u$ existed. Since
\[
\lim_{z\to a}u(z)=2,
\]
$u$ is bounded near the isolated point $a$. By the removable singularity
theorem for harmonic functions, $u$ extends harmonically across $a$, with
$u(a)=2$. The extension is harmonic on all of $\DD$ and continuous on
$\overline{\DD}$, with boundary value $0$ on $\circlegroup$. The maximum
and minimum principles therefore force $u\equiv0$, contradicting $u(a)=2$.
Thus the Dirichlet problem has no solution.
:::
