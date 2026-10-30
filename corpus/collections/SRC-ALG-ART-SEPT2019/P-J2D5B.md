---
schema: qual/card@1
id: P-J2D5B
kind: problem
title: Invariants of a dihedral action on $\CC[x,y]$
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
The dihedral group $G = \langle a,b \mid a^3=b^2=1, bab=a^{-1}\rangle$ acts on the $\CC$-algebra $S = \CC[x,y]$ by algebra automorphisms so that $$a\cdot x = \omega x, \qquad a\cdot y = \omega^{-1}y, \qquad b\cdot x = y,$$ where $\omega = e^{2\pi i/3}$.
Let $R := S^G$ be the invariant subalgebra.

(a) Show that $R = \CC[x^3+y^3, xy]$.

(b) Show that $R \subseteq S$ is an integral extension.

(c) Find an explicit monic polynomial $f(t) \in R[t]$ such that $f(x) = 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
(a) $R = \CC[x^3+y^3,xy]$.

::: pf-proof
Let $z = \sum c_{ij}x^iy^j \in S$. Then $a\cdot z = \sum c_{ij}\omega^{i-j}x^iy^j$, so $a\cdot z=z$ if and only if $c_{ij}=0$ unless $i\equiv j \pmod 3$. Also $b\cdot z = \sum c_{ji}x^iy^j$, so $b\cdot z=z$ if and only if $c_{ij}=c_{ji}$ for all $i,j$. Hence $R$ is spanned by the polynomials $x^iy^j+x^jy^i$ with $i\ge j$ and $i\equiv j\pmod 3$. Writing $i-j=3n$,
$$
x^iy^j+x^jy^i=(xy)^j\bigl(x^{3n}+y^{3n}\bigr),
$$
and $x^{3n}+y^{3n}$ is a polynomial in $x^3+y^3$ and $x^3y^3=(xy)^3$ by Newton's identities. Conversely $x^3+y^3$ and $xy$ are invariant.
:::

:::

::: {.pf-step #s2}
(b) $R \subseteq S$ is integral.

::: pf-proof
Given $z\in S$, the polynomial
$$
f_z(t) = \prod_{g\in G}(t - g\cdot z)
$$
is monic, its coefficients are invariant under $G$ and so lie in $R$, and $f_z(z)=0$.
:::

:::

::: {.pf-step #s3}
(c) One may take $f(t) = t^6 - (x^3+y^3)t^3 + (xy)^3$.

::: pf-proof
The polynomial of step [](#s2){.pf-ref} for $z=x$ is
$$
\prod_{g\in G}(t-g\cdot x) = (t-x)(t-\omega x)(t-\omega^2 x)(t-y)(t-\omega y)(t-\omega^2 y)
= (t^3-x^3)(t^3-y^3),
$$
which expands to the displayed polynomial.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} answer (a), (b) and (c).
:::

:::

:::
