---
schema: qual/card@1
id: P-HJPF5
kind: problem
title: Linear actions of $\ZZ/5\ZZ$, $S_3$, and dihedral groups on complex vector
  spaces
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Cyclic Groups
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
If you have a $\ZZ/5\ZZ$ action on a complex vector space, what does this action look like?
What about an $S_3$ action?
A dihedral group of any order?
:::


::: {.solution}
All representations below are finite-dimensional over $\CC$. Since the groups are finite, Maschke's theorem gives complete reducibility.

<1>1. A representation of $C_5=\langle g\rangle$ is a direct sum of one-dimensional characters.
::: {.proof}
The operator $\rho(g)$ satisfies
\[
\rho(g)^5=I,
\]
so its minimal polynomial divides $x^5-1$, which has distinct roots over $\CC$. Hence $\rho(g)$ is diagonalizable, with eigenvalues among the fifth roots of unity. Each eigenspace is $C_5$-stable. Thus
\[
V=\bigoplus_{k=0}^4 V_k,
\]
where $g$ acts on $V_k$ by multiplication by $\zeta_5^k$.
:::

<1>2. Every representation of $S_3$ is a direct sum of copies of the three irreducibles: the trivial representation, the sign representation, and the standard two-dimensional representation.
::: {.proof}
The group $S_3$ has three conjugacy classes, hence three irreducible complex representations. Their dimensions must satisfy
\[
\sum d_i^2=|S_3|=6.
\]
The two one-dimensional characters are trivial and sign, leaving one irreducible of dimension $2$, the standard representation on
\[
\{(x_1,x_2,x_3)\in\CC^3:x_1+x_2+x_3=0\}.
\]
Maschke's theorem decomposes every representation into these.
:::

<1>3. For the dihedral group
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\]
all irreducible complex representations have dimension $1$ or $2$.
::: {.proof}
Since $r^n=1$, the operator $\rho(r)$ is diagonalizable with eigenvalues among the $n$th roots of unity. If $v$ is a $\zeta^k$-eigenvector for $r$, then
\[
r(sv)=s(r^{-1}v)=\zeta^{-k}sv,
\]
so $s$ pairs the $\zeta^k$- and $\zeta^{-k}$-eigenspaces.

When $k\not\equiv -k\pmod n$, the span of $v$ and $sv$ gives a two-dimensional irreducible model
\[
r\mapsto
\begin{pmatrix}
\zeta^k&0\\
0&\zeta^{-k}
\end{pmatrix},
\qquad
s\mapsto
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
The self-inverse eigenvalues $1$ (and also $-1$ when $n$ is even) yield one-dimensional characters. Maschke's theorem then decomposes every representation into these irreducibles.
:::
:::
