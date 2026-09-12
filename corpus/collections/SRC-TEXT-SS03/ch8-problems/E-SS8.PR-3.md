---
schema: qual/card@1
id: E-SS8.PR-3
kind: problem
title: Hyperbolic metric on the disc and the Schwarz-Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
3.* The Schwarz-Pick lemma (see Exercise 13) is the infinitesimal version of an important observation in complex analysis and geometry.

For complex numbers $w \in \mathbb{C}$ and $z \in \mathbb{D}$ we define the hyperbolic length of $w$ at $z$ by

$$
\| w \| _ {z} = \frac{| w |}{1 - | z | ^ {2}},
$$

where $|w|$ and $|z|$ denote the usual absolute values.
This length is sometimes referred to as the Poincaré metric, and as a Riemann metric it is written as

$$
d s ^ {2} = \frac{| d z | ^ {2}}{(1 - | z | ^ {2}) ^ {2}}.
$$

The idea is to think of $w$ as a vector lying in the tangent space at $z$.
Observe that for a fixed $w$, its hyperbolic length grows to infinity as $z$ approaches the boundary of the disc.
We pass from the infinitesimal hyperbolic length of tangent vectors to the global hyperbolic distance between two points by integration.

(a) Given two complex numbers $z_1$ and $z_2$ in the disc, we define the hyperbolic distance between them by

$$
d (z_1, z_2) = \inf_ {\gamma} \int_ {0} ^ {1} \| \gamma' (t) \| _ {\gamma (t)} d t,
$$

where the infimum is taken over all smooth curves $\gamma : [0, 1] \to \mathbb{D}$ joining $z_1$ and $z_2$.
Use the Schwarz-Pick lemma to prove that if $f : \mathbb{D} \to \mathbb{D}$ is holomorphic, then

$$
d (f (z_1), f (z_2)) \leq d (z_1, z_2) \quad \text{for any } z_1, z_2 \in \mathbb{D}.
$$

In other words, holomorphic functions are distance-decreasing in the hyperbolic metric.

(b) Prove that automorphisms of the unit disc preserve the hyperbolic distance, namely

$$
d (\varphi (z_1), \varphi (z_2)) = d (z_1, z_2), \quad \text{for any } z_1, z_2 \in \mathbb{D}
$$

and any automorphism $\varphi$.
Conversely, if $\varphi : \mathbb{D} \to \mathbb{D}$ preserves the hyperbolic distance, then either $\varphi$ or $\overline{\varphi}$ is an automorphism of $\mathbb{D}$.

(c) Given two points $z_1, z_2 \in \mathbb{D}$, show that there exists an automorphism $\varphi$ such that $\varphi(z_1) = 0$ and $\varphi(z_2) = s$ for some $s$ on the segment $[0, 1)$ on the real line.

(d) Prove that the hyperbolic distance between $0$ and $s \in [0, 1)$ is

$$
d (0, s) = \frac{1}{2} \log \frac{1 + s}{1 - s}.
$$

(e) Find a formula for the hyperbolic distance between any two points in the unit disc.
:::

::: solution
The Schwarz--Pick lemma says
\[
\frac{|f'(z)|}{1-|f(z)|^2}\le \frac1{1-|z|^2}.
\tag{1}
\]
Hence for every smooth curve $\gamma$ in $\mathbb D$,
\[
\frac{|(f\circ\gamma)'(t)|}{1-|f(\gamma(t))|^2}
\le
\frac{|\gamma'(t)|}{1-|\gamma(t)|^2}.
\]
Integrating and taking the infimum over all curves joining $z_1$ to $z_2$ gives
\[
d(f(z_1),f(z_2))\le d(z_1,z_2).
\]
This proves (a).

If $\varphi$ is an automorphism, apply (a) to $\varphi$ and then to $\varphi^{-1}$ to obtain both inequalities, hence
\[
d(\varphi(z_1),\varphi(z_2))=d(z_1,z_2).
\tag{2}
\]

For (c), first use
\[
\phi_{z_1}(z)=\frac{z-z_1}{1-\overline{z_1}z},
\]
which sends $z_1$ to $0$. If $\phi_{z_1}(z_2)=re^{i\theta}$, compose with the rotation $e^{-i\theta}z$. The resulting automorphism sends $z_1$ to $0$ and $z_2$ to $r\in[0,1)$.

For (d), let $\gamma(t)=r(t)e^{i\theta(t)}$ join $0$ to $s$. Then
\[
|\gamma'(t)|\ge |r'(t)|,
\]
so
\[
\int_0^1\frac{|\gamma'(t)|}{1-|\gamma(t)|^2}\,dt
\ge
\int_0^1\frac{|r'(t)|}{1-r(t)^2}\,dt
\ge
\left|\int_0^1\frac{r'(t)}{1-r(t)^2}\,dt\right|.
\]
Since $r(0)=0$ and $r(1)=s$, the last term is
\[
\int_0^s\frac{dr}{1-r^2}
=\frac12\log\frac{1+s}{1-s}.
\]
Equality is attained by the radial segment $\gamma(t)=ts$. Hence
\[
d(0,s)=\frac12\log\frac{1+s}{1-s}.
\tag{3}
\]

For arbitrary $z,w$, by (2) and (c),
\[
d(z,w)=d\left(0,\left|\frac{z-w}{1-\overline w z}\right|\right).
\]
Therefore, writing
\[
\delta(z,w)=\left|\frac{z-w}{1-\overline w z}\right|,
\]
we obtain
\[
\boxed{d(z,w)=\frac12\log\frac{1+\delta(z,w)}{1-\delta(z,w)}}.
\tag{4}
\]
This proves (e).

It remains to prove the converse in (b). Let $T:\mathbb D\to\mathbb D$ preserve hyperbolic distance. Formula (4) shows that it also preserves $\delta$. Choose a disk automorphism $A$ with $A(T(0))=0$ and set $S=A\circ T$. Then $S$ preserves $\delta$ and fixes $0$. Since
\[
\delta(0,z)=|z|,
\]
we have $|S(z)|=|z|$.

For $z,w$ with $|z|=r$, $|w|=s$, write $c=\cos(\arg z-\arg w)$. Then
\[
\delta(z,w)^2=\frac{r^2+s^2-2rsc}{1+r^2s^2-2rsc}.
\tag{5}
\]
For fixed $r,s<1$, the right side determines $c$ uniquely. Because $S$ preserves $r,s$ and $\delta$, it preserves $c$, hence preserves the Euclidean inner product and therefore Euclidean distance. Thus $S$ is a Euclidean isometry of the disk fixing $0$. Such a map is the restriction of an orthogonal linear map of $\mathbb R^2$, hence has one of the forms
\[
S(z)=e^{i\theta}z
\qquad\text{or}\qquad
S(z)=e^{i\theta}\overline z.
\]
Consequently $T=A^{-1}\circ S$ is either a disk automorphism or the conjugate of one. Equivalently, either $T$ or $\overline T$ is an automorphism of $\mathbb D$.
:::
