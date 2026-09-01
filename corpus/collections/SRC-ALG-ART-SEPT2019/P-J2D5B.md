---
schema: qual/card@1
id: P-J2D5B
kind: problem
title: Invariants of a dihedral action on $\mathbb{C}[x,y]$
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Integral Extensions
  - Algebras
relations: []
review: draft
---

::: {.problem}
The dihedral group $G = \langle a,b \mid a^3=b^2=1, bab=a^{-1}\rangle$ acts on the $\mathbb{C}$-algebra $S = \mathbb{C}[x,y]$ by algebra automorphisms so that $$a\cdot x = \omega x, \qquad a\cdot y = \omega^{-1}y, \qquad b\cdot x = y,$$ where $\omega = e^{2\pi i/3}$.
Let $R := S^G$ be the invariant subalgebra.

a. Show that $R = \mathbb{C}[x^3+y^3, xy]$.
b. Show that $R \subseteq S$ is an integral extension.
c. Find an explicit monic polynomial $f(t) \in R[t]$ such that $f(x) = 0$.
:::

::: {.solution}
**(a)** Consider $z = \sum c_{ij}x^iy^j \in S$.
Then $$a\cdot z = \sum c_{ij}\omega^{i-j}x^iy^j$$ So need $c_{ij}=0$ unless $i\equiv j \pmod 3$.
$$b\cdot z = \sum c_{ji}x^iy^j$$ So need $c_{ij}=c_{ji}$ for all $i,j$.

Shows $R$ is spanned by $x^3+y^3$ and $xy$ (you can get any $x^{3n}+y^{3n}$ as monomials in these!). Hence $R = \mathbb{C}[x^3+y^3,xy]$.

**(b)** This is a general fact about invariants of finite groups.
Given $z\in S$, consider $$f(t) = \prod_{g\in G}(t - g\cdot z)$$ It's monic in $R[t]$ with $z$ as a root $\Rightarrow$ integral.

**(c)** Use the recipe from (b)! $$f(t) = \prod_{g\in G}(t-g\cdot x) = (t-x)(t-\omega x)(t-\omega^2 x)(t-y)(t-\omega y)(t-\omega^2 y)$$ $$= (t^3-x^3)(t^3-y^3) = t^6 - (x^3+y^3)t^3 + x^3y^3$$
:::
