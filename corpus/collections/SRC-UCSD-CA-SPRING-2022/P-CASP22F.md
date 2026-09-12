---
schema: qual/card@1
id: P-CASP22F
kind: problem
title: "Bounded harmonic function on D with limsup <= 0 except at one boundary point"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Maximum Principle
  - Boundary Values
relations: []
review: draft
---

::: problem
Let $h$ be a bounded harmonic function on the unit disc $\mathbb{D} = \{z : |z| < 1\}$.
Assume that
$$
\limsup_{z \to a} h(z) \leq 0
$$
for all $a \in \partial \mathbb{D} \setminus \{1\}$.
Show that $h \leq 0$ in $\mathbb{D}$.
:::

::: solution
Let $|h|\le M$. Fix $z\in\mathbb D$ and $\varepsilon>0$. Choose a small open
arc $I\subset\partial\mathbb D$ centered at $1$. By compactness of
$\partial\mathbb D\setminus I$ and the boundary limsup hypothesis, there is
$r_0<1$ such that
\[
h(re^{it})\le\varepsilon
\]
whenever $r_0<r<1$ and $e^{it}\notin I$.

For $r>|z|$ sufficiently close to $1$, the Poisson formula in the disk
$|w|<r$ gives
\[
h(z)=\frac1{2\pi}\int_{-\pi}^{\pi}
P_{|z|/r}(\arg z-t)h(re^{it})\,dt.
\]
Split the integral over $I$ and its complement. Since the Poisson kernel is
positive and has total mass $2\pi$,
\[
h(z)\le \varepsilon
+M\frac1{2\pi}\int_I P_{|z|/r}(\arg z-t)\,dt.
\]
Let $r\uparrow1$. For fixed $z$, the Poisson kernel is bounded as a function
of $t$, so the second term can be made arbitrarily small by shrinking the arc
$I$. Hence $h(z)\le\varepsilon$. Finally let $\varepsilon\downarrow0$ to obtain
\[
h(z)\le0.
\]
Since $z$ was arbitrary, $h\le0$ throughout $\mathbb D$.
:::
