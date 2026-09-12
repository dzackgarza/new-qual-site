---
schema: qual/card@1
id: P-UCTOP-SU12-8
kind: problem
title: Conjugacy classes and intersection on genus-2 surface
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

Let $\Sigma$ be a closed orientable surface of genus 2, whose fundamental group $\pi$ (with respect to some basepoint $x_0$) can be described by the presentation

$$\pi = \langle a, b, c, d : aba^{-1}b^{-1}cdc^{-1}d^{-1} = 1 \rangle.$$

Explain how to associate, to any oriented loop on the surface (not necessarily passing through the basepoint) a conjugacy class in $\pi$.
Consider two oriented loops $\alpha$ and $\beta$ on the surface, whose conjugacy classes are represented by the elements $ab^2cda^{-1}b^{-1}c^{-1}d^{-1}$ and $a^2bcda^{-1}b^{-1}c^{-1}d^{-1}$ respectively.
Explain why it is impossible to use homotopies of the loops to make $\alpha$ and $\beta$ disjoint.

::: {.solution}
<1>1. An oriented loop $\gamma:S^1\to\Sigma$ determines a conjugacy class in $\pi_1(\Sigma,x_0)$.
::: {.proof}
Choose a point $y=\gamma(1)$ on the loop and a path $\eta$ from $x_0$ to $y$. The based loop
$$
\eta\cdot\gamma\cdot\eta^{-1}
$$
represents an element of $\pi_1(\Sigma,x_0)$. Replacing $\eta$ by another path conjugates this element, so the resulting conjugacy class is independent of the chosen basepath. Free homotopies of oriented loops correspond exactly to conjugacy classes.
:::

<1>2. In the abelianization
$$
H_1(\Sigma;\mathbb Z)\cong\mathbb Z\langle a,b,c,d\rangle,
$$
the class of $\alpha$ is $b$ and the class of $\beta$ is $a$.
::: {.proof}
Abelianizing the first word gives exponent sums
$$
a:1-1=0,\quad b:2-1=1,\quad c:1-1=0,\quad d:1-1=0,
$$
so $[\alpha]=b$. For the second word the exponent sums are
$$
a:2-1=1,\quad b:1-1=0,\quad c:1-1=0,\quad d:1-1=0,
$$
so $[\beta]=a$.
:::

<1>3. Their algebraic intersection number is nonzero:
$$
[\alpha]\cdot[\beta]=b\cdot a=\pm1.
$$
::: {.proof}
For the standard symplectic basis on a genus-$2$ surface, $a\cdot b=1$ and $c\cdot d=1$, with all other basic intersections zero. Skew-symmetry gives $b\cdot a=-1$; the sign depends only on the orientation convention, and in particular is nonzero.
:::

<1>4. Homotopies cannot make $\alpha$ and $\beta$ disjoint.
::: {.proof}
The algebraic intersection number depends only on the homology classes and is invariant under homotopy. Two disjoint oriented loops have geometric, hence algebraic, intersection number zero. This contradicts <1>3.
:::
:::
