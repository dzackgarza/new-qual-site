---
schema: qual/card@1
id: P-EER5M
kind: problem
title: An injective entire function is affine, $f(z)=az+b$
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - biholomorphisms
  - singularities
  - conformal-maps
relations: []
review: draft
solved: true
---

::: problem
Let $f: {\mathbb C} \rightarrow {\mathbb C}$ be an injective analytic (also called *univalent*) function.
Show that there exist complex numbers $a \neq 0$ and $b$ such that $f(z) = az + b$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that every injective entire function $f$ is affine: $f(z) = az + b$ with $a \neq 0$.

<1>1. $f$ is not constant.
Proof: An injective map of $\CC$ into itself cannot be constant (a constant map is not injective unless the domain has one point).

<1>2. $f$ has at most one zero.
Proof: Injectivity: if $f(z_1) = f(z_2) = 0$ then $z_1 = z_2$.

<1>3. $\infty$ is not an essential singularity of $f$.
Proof: Suppose $\infty$ were an essential singularity.
By Casorati–Weierstrass, $f(\CC \setminus \overline{D_R})$ is dense in $\CC$ for every $R$.
The image $f(D_R)$ is open (open mapping theorem, $f$ nonconstant by <1>1) and nonempty, so $f(\CC\setminus\overline{D_R}) \cap f(D_R) \neq \emptyset$ by density; then $f(z_1) = f(z_2)$ for some $z_1 \in D_R$ and $z_2 \notin \overline{D_R}$ with $z_1 \neq z_2$, contradicting injectivity.
Hence $\infty$ is not essential.

<1>4. $\infty$ is a pole of $f$, so $f$ is a polynomial.
Proof: $f$ is entire; the singularity at $\infty$ is either removable, a pole, or essential.
Not removable by <1>1 (if removable then $f$ bounded near $\infty$, hence bounded and constant by Liouville, contradicting <1>1); not essential by <1>3. Hence a pole, and a function with a pole at $\infty$ is a (nonconstant) polynomial.

<1>5. $\deg f = 1$.
Proof: Let $d = \deg f$.
If $d = 0$, $f$ is constant, contradicting <1>1. If $d \geq 2$, then $f'$ is a polynomial of degree $d - 1 \geq 1$ with a root $z_0$; near $z_0$, $f(z) = f(z_0) + (z - z_0)^m g(z)$ with $m \geq 2$ and $g(z_0) \neq 0$, so $f$ is $m$-to-one near $z_0$ (the equation $f(z) = w$ has $m$ distinct nearby solutions for $w$ near $f(z_0)$, $w \neq f(z_0)$), contradicting injectivity.
Hence $d = 1$.

<1>6. Q.E.D. Proof: <1>4 and <1>5 show $f(z) = az + b$ with $a \neq 0$.
:::
