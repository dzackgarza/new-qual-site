---
schema: qual/card@1
id: E-OBU6T
kind: problem
title: A bijective analytic map on $\mathbb{C}\setminus\{z_0\}$, bounded off a neighborhood
  of $z_0$, is a Möbius transformation $\frac{az+b}{cz+d}$ with $c\neq 0$
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Biholomorphisms
  - Removable Singularities
  - Poles
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be an analytic function on ${\mathbb C} \backslash \{ z_0 \}$, where $z_0$ is a fixed point.
Assume that $f(z)$ is bijective from ${\mathbb C} \backslash \{ z_0 \}$ onto its image, and that $f(z)$ is bounded outside $D_r(z_0)$, where $r$ is some fixed positive number.
Show that there exist $a, b, c, d \in \mathbb C$ with $ad-bc \neq 0$, $c \neq 0$ such that $\displaystyle f(z) = \frac{az + b}{cz + d}$.
:::

::: {.solution}
Since $f$ is bounded for large $|z|$, the singularity of $f$ at $\infty$ is
removable. Hence
\[
L:=\lim_{z\to\infty}f(z)
\]
exists and is finite.

The isolated singularity at $z_0$ cannot be removable. If it were, $f$ would
extend to an entire function on $\mathbb C$ with a finite limit at infinity,
and therefore would be bounded and constant by Liouville's theorem, contrary
to injectivity. It also cannot be essential: by the Great Picard theorem, in
every punctured neighborhood of $z_0$ the function would assume all but at
most one complex value infinitely often, again contradicting injectivity.
Thus $z_0$ is a pole.

Therefore $f$ extends to a meromorphic function on the Riemann sphere with its
only finite pole at $z_0$, so $f$ is rational. Because $f$ is injective on
$\mathbb C\setminus\{z_0\}$, its degree is one: a rational map of degree
$d\ge2$ is generically $d$-to-one on the sphere. Hence
\[
f(z)=\frac{az+b}{cz+d},\qquad ad-bc\ne0.
\]
Since $f$ has the finite pole $z_0$, the denominator is nonconstant, so
$c\ne0$. This is the required form.
:::
