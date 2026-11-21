---
schema: qual/card@1
id: P-APAS19F
kind: problem
title: Character table of $D_4$ and decomposition of $V\otimes V$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the computation into numbered steps and supplied the counts the prose asserted: the
    five conjugacy classes listed element by element, the four linear characters obtained from the
    independent choices of sign on r and s (the relation srs = r inverse being automatic when r maps
    to a sign), the completeness of the table from five classes and the sum of squares of degrees
    1+1+1+1+4 = 8, and the values of the defining character read off as traces of the rotation and
    reflection matrices. Also recorded the orthogonality check that verifies the multiplicity
    computation. Every macro used is one the preamble defines. Nothing was checked against a printed
    page.
---

::: {.problem}
Let $D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle$ be the dihedral group of symmetries of the square.

(a) Write down the character table of $D_4$.

(b) Let $V$ be the $2$-dimensional ``defining'' $D_4$-module obtained by centering the square at the origin in the plane and extending symmetries of the square to linear transformations of the plane.
Give the tensor product $V\otimes V$ the structure of a $D_4$-module by setting
$$
g.(v\otimes v'):=(g.v)\otimes(g.v')
$$
for all $g\in D_4$ and $v,v'\in V$.
Calculate the decomposition of $V\otimes V$ into irreducible $D_4$-modules.
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it.

Let $D_{4}=\langle r,s\mid r^{4}=s^{2}=1,\ srs=r^{-1}\rangle$, acting on $\RR^{2}$ with $r$ the rotation by $\pi/2$ and $s$ a reflection, and let $V=\RR^{2}\otimes\CC$ be the defining two-dimensional module.

::: pf

::: {.pf-step #classes}
The conjugacy classes of $D_{4}$ are $\{1\}$, $\{r^{2}\}$, $\{r,r^{3}\}$, $\{s,r^{2}s\}$, $\{rs,r^{3}s\}$.

::: pf-proof
The eight elements are $1,r,r^{2},r^{3},s,rs,r^{2}s,r^{3}s$. The centre is $\{1,r^{2}\}$, since $r^{2}$ commutes with $r$ and with $s$ ($sr^{2}=r^{-2}s=r^{2}s$). Conjugation by $r$ sends $r^{k}\mapsto r^{k}$ and $r^{k}s\mapsto r^{2k}s$, so the reflections split into $\{s,r^{2}s\}$ and $\{rs,r^{3}s\}$, and conjugation by $s$ inverts $r$, so $r$ and $r^{3}$ are conjugate. Hence the five displayed classes, and there are no others since they partition the eight elements.
:::

:::

::: {.pf-step #linear}
There are four one-dimensional characters, given on generators by $\chi(r)=\pm1$ and $\chi(s)=\pm1$.

::: pf-proof
A one-dimensional character is a homomorphism to $\CC^{\times}$, so it sends $r$, of order $4$, to a fourth root of unity and $s$ to $\pm1$; the relation $srs=r^{-1}$ requires $\chi(s)\chi(r)\chi(s)=\chi(r)^{-1}$, which for a scalar $\chi(s)$ reads $\chi(r)=\chi(r)^{-1}$, so $\chi(r)=\pm1$. Conversely any choice of signs defines a homomorphism because the relation is then automatically satisfied. So there are $2\cdot2=4$ such characters, $\chi_{++},\chi_{+-},\chi_{-+},\chi_{--}$ in the order (sign on $r$, sign on $s$).
:::

:::

::: {.pf-step #defining}
The defining character has values $\chi_{V}(1)=2$, $\chi_{V}(r^{2})=-2$, $\chi_{V}(r)=\chi_{V}(r^{3})=0$, $\chi_{V}(s)=\chi_{V}(rs)=0$.

::: pf-proof
A character depends only on the conjugacy class, so it suffices to evaluate on $1,r^{2},r,s,rs$. The identity has trace $2$. $r^{2}$ acts by rotation through $\pi$, whose matrix is $-I$, trace $-2$. $r$ acts by rotation through $\pi/2$ with eigenvalues $e^{\pm i\pi/2}$, trace $2\cos(\pi/2)=0$. A reflection has eigenvalues $1,-1$, trace $0$, and both $s$ and $rs$ are reflections.
:::

:::

::: {.pf-step #complete}
The five irreducible characters are the four linear ones and $\chi_{V}$, so the displayed table is the whole character table.

::: pf-proof
The number of irreducible characters equals the number of conjugacy classes, which is $5$ by step [](#classes){.pf-ref}. The four linear characters are distinct and irreducible, being one-dimensional. The sum of squares of degrees of these five characters is $1+1+1+1+4=8=\abs{D_{4}}$, so they exhaust the irreducible characters; equivalently a fifth irreducible distinct from the four linear ones would push the sum above $8$.
:::

:::

::: {.pf-step #tensor}
$\chi_{V\otimes V}=\chi_{V}^{2}=(4,4,0,0,0)$.

::: pf-proof
On classes, $g$ acts on $v\otimes v'$ by $gv\otimes gv'$, so in bases the matrix is the Kronecker product $g\otimes g$ and its trace is $\operatorname{tr}(g)^{2}=\chi_{V}(g)^{2}$. Squaring the values of step [](#defining){.pf-ref} gives $(4,4,0,0,0)$ in the class order.
:::

:::

::: {.pf-step #sum-of-linear}
$\chi_{++}+\chi_{+-}+\chi_{-+}+\chi_{--}=(4,4,0,0,0)$.

::: pf-proof
At $1$ and $r^{2}$ all four characters take the value $1$, giving $4$. At $r$ the signs on $r$ split the four into two of each, giving $1+1-1-1=0$; at $s$ the signs on $s$ split likewise, giving $1-1+1-1=0$; at $rs$ the product of the two signs is what matters, again two of each, giving $0$.
:::

:::

::: {.pf-step #decomposition}
$V\otimes V\cong\chi_{++}\oplus\chi_{+-}\oplus\chi_{-+}\oplus\chi_{--}$.

::: pf-proof
Two representations with equal characters are isomorphic, and a direct sum has the sum of the characters. By steps [](#tensor){.pf-ref} and [](#sum-of-linear){.pf-ref} the character of $V\otimes V$ equals that of the direct sum of the four linear characters, so the two are isomorphic; equivalently the multiplicities are $\langle\chi_{V}^{2},\chi_{\pm\pm}\rangle=1$ for each of the four linear characters and $0$ for $\chi_{V}$, by orthogonality of the five characters. Dimensions agree: $4=1+1+1+1$.
:::

:::

:::

:::

