---
schema: qual/card@1
id: P-ZRVTI
kind: problem
title: "Entire univalent functions are affine/linear"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="Entire univalent functions are affine/linear"}
Let $f: \mathbb{C} \rightarrow \mathbb{C}$ be an injective analytic (also called univalent) function. Show that there exist complex numbers $a \neq 0$ and $b$ such that $f(z)=a z+b$.

> Hint: Apply the Casorati-Weierstrass theorem to $f(1/z)$.
:::

:::{.solution}
Note that $f$ is non-constant, since a constant function is extremely non-injective.
Consider the singularity at $\infty$:

- If it is removable, then $f$ is bounded outside of a large disc, and bounded inside of it as a continuous function on a compact set, making $f$ entire and bounded and thus constant by Liouville.

- If it is essential, then by Casorati-Weierstrass there is a large disc of radius $R$ such that $f(\bar{\DD_R}^c) \subseteq \CC$ is dense.
  By the open mapping theorem, $f(\DD_R) \subseteq \CC$ is open, so by density it intersects $f(\bar{\DD_R}^c)$, but $\DD_R \intersect \bar{\DD_R}^c$ is empty so this contradicts injectivity.

So we can conclude $\infty$ is a pole of some order $N$, so $f\qty{1\over z} = \sum_{0\leq k\leq N} c_k z^{-k}$ and thus $f(z) = \sum_{0\leq k\leq N} c_k z^k$ is a polynomial of degree $N$.
However, a polynomial of degree $N$ is generically $N$-to-one locally, so injectivity forces $N=1$ and $f(z) = c_0 + c_1 z$, where $c_1\neq 0$ since $f$ is nonconstant.
:::

:::{.solution title="older"}
Write $g(z) \da f(1/z)$, which has a singularity at $z=0$.
The claim is that this is a pole.

If $z=0$ is a removable singularity, $g$ is bounded on some closed disc $\abs{z} \leq \eps$, so $f$ is bounded on $\abs{z} > \eps$.
Moreover $f$ is continuous and $\abs{z}\leq \eps$, $f$ is bounded on this disc.
This makes $f$ an entire bounded function and thus constant by Liouville, contradicting injectivity.

If $z=0$ is essential, then by Casorati-Weierstrass pick a punctured disc $D = \ts{\abs{z} \leq \eps}$ where $g(D)$ is dense in $\CC$.
Writing $D^c \da \ts{\abs{z} > \eps}$, this means that $f(D^c)$ is dense. 
But $U\da \ts{\abs{z} < \eps}$ is open and by the open mapping theorem $f(U)$ is open, so by density there is a point $w\in f(D^c) \intersect f(U)$ while $U \intersect D^c = \emptyset$, again contradicting injectivity.

So $z=0$ is a pole of $g$, and $g$ admits a Laurent expansion
\[
g(z) = \sum_{k\geq -N} c_k z^k
.\]
Since $f$ is entire, it equals its Laurent expansion at $z=0$, so equating the two series yields
\[
f(z) = \sum_{k\geq 0} d_k z^k 
&\implies g(z) = \sum_{k\geq 0} {d_k \over z^k} = \sum_{1\leq k\leq N} {c_k\over z^k} + \sum_{k\geq 0} c_k z^k \\
&\implies \sum_{k\geq 0} c_k z^k = 0 \\
&\implies f(z) = \sum_{0\leq k \leq N} c_k z^k
,\]
making $f$ a polynomial of degree at most $N$.

Now $f$ can not be degree zero, since constant maps are not injective.
Moreover $f$ can not be degree $N\geq 2$, since any polynomial of degree $N$ has $N$ roots in $\CC$ by the fundamental theorem of algebra, and any two distinct roots will be points where injectivity fails.
Finally, ruling out the case of roots with multiplicity, if $f(z) = c(z-a)^N$, then $f$ has exactly $N$ preimages in a neighborhood of $a$.
Letting $p$ be any such point, we can find $N$ complex points mapping to it:
\[
p = c(z-a)^N &\implies {p\over c} = (z-a)^N \\
&\implies \qty{p\over c}^{1\over N}\zeta_N^k = z-a \quad k=0,1,\cdots, n-1 \\
&\implies z_k\da \qty{p\over c}^{1\over N}\zeta_N^k + a \mapsvia{f} p
.\]

So $f$ must be degree exactly 1, i.e. $f(z) = az+b$.
:::
