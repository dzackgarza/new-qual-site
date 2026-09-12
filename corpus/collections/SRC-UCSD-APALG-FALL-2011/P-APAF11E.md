---
schema: qual/card@1
id: P-APAF11E
kind: problem
title: Irreducible representations of a direct product $G\times H$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $G$ and $H$ be finite groups and let $A:G\to\mathrm{GL}_n(\mathbb{C})$ and $B:H\to\mathrm{GL}_m(\mathbb{C})$ be representations of $G$ and $H$ respectively.

(a) Show that $A\times B:G\times H\to\mathrm{GL}_{nm}(\mathbb{C})$ is a representation where for $(\sigma,\tau)\in G\times H$,
\[
(A\times B)((\sigma,\tau))=A(\sigma)\otimes B(\tau)
\]
and for matrices $M$ and $N$, $M\otimes N$ is the Kronecker product of $M$ and $N$.

(b) Show that if $A$ is an irreducible representation of $G$ and $B$ is an irreducible representation of $H$, then $A\times B$ is an irreducible representation of $G\times H$.

(c) Show that every irreducible representation of $G\times H$ is of the form $A\times B$ where $A$ is an irreducible representation of $G$ and $B$ is an irreducible representation of $H$.
:::


::: {.solution}
<1>1. The map
\[
A\times B:G\times H\to \mathrm{GL}_{nm}(\mathbb C),\qquad
(A\times B)(g,h)=A(g)\otimes B(h),
\]
is a representation.
::: {.proof}
For compatible matrices,
\[
(M_1\otimes N_1)(M_2\otimes N_2)=(M_1M_2)\otimes(N_1N_2).
\]
Hence multiplication in $G\times H$ is respected, and $(A\times B)(e_G,e_H)=I_{nm}$.
:::

<1>2. Its character is
\[
\chi_{A\times B}(g,h)=\chi_A(g)\chi_B(h).
\]
::: {.proof}
This follows from $\operatorname{tr}(M\otimes N)=\operatorname{tr}(M)\operatorname{tr}(N)$.
:::

<1>3. If $A$ and $B$ are irreducible, then $A\times B$ is irreducible.
::: {.proof}
Using <1>2,
\[
\langle\chi_{A\times B},\chi_{A\times B}\rangle_{G\times H}
=\langle\chi_A,\chi_A\rangle_G\,\langle\chi_B,\chi_B\rangle_H=1.
\]
Thus the character has norm $1$, hence is irreducible.
:::

<1>4. More generally, for irreducibles $A_i,A_j$ of $G$ and $B_r,B_s$ of $H$,
\[
\langle\chi_{A_i\times B_r},\chi_{A_j\times B_s}\rangle_{G\times H}
=\langle\chi_{A_i},\chi_{A_j}\rangle_G\,\langle\chi_{B_r},\chi_{B_s}\rangle_H.
\]
::: {.proof}
Expand the inner product as a double sum over $G\times H$ and separate the $g$- and $h$-sums.
:::

<1>5. If $G$ has $r$ irreducible characters and $H$ has $s$, then the $rs$ characters $\chi_{A_i\times B_j}$ are pairwise orthonormal irreducible characters of $G\times H$.
::: {.proof}
Irreducibility is <1>3, and pairwise orthogonality is <1>4 together with orthogonality of irreducible characters on each factor.
:::

<1>6. The group $G\times H$ has exactly $rs$ conjugacy classes.
::: {.proof}
Two pairs $(g,h)$ and $(g',h')$ are conjugate in $G\times H$ exactly when $g,g'$ are conjugate in $G$ and $h,h'$ are conjugate in $H$. Hence conjugacy classes are precisely products $C\times D$ of conjugacy classes from the two factors. Since a finite group has as many irreducible complex characters as conjugacy classes, $G$ and $H$ have $r$ and $s$ classes respectively, so $G\times H$ has $rs$.
:::

<1>7. Every irreducible representation of $G\times H$ is of the form $A_i\times B_j$.
::: {.proof}
By <1>5 there are already $rs$ pairwise nonisomorphic irreducible representations of this form, while <1>6 shows that $G\times H$ has exactly $rs$ irreducible representations up to isomorphism. Therefore the list is complete.
:::
:::
