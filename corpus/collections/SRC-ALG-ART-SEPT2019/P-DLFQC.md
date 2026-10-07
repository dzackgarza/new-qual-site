---
schema: qual/card@1
id: P-DLFQC
kind: problem
title: Density in affine varieties via the Nullstellensatz
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Commutative Algebra
  - Maximal Ideals
relations: []
review: draft
---

::: {.problem}
Work over an algebraically closed field $F$ of characteristic zero.

a. Let $X$ be an affine variety with coordinate algebra $F[X]$. State the *Nullstellensatz*. Then use it to show that a subset $S \subseteq X$ is dense (in the Zariski topology) if and only if the following property holds for all $f \in F[X]$:
$$(f(s)=0 \text{ for all } s\in S) \Rightarrow f=0.$$
b. Given affine varieties $X$ and $Y$ and dense subsets $S \subseteq X$ and $T \subseteq Y$, prove that $S\times T$ is dense in $X\times Y$.
c. Show that the integer lattice $\mathbb{Z}^n$ is dense in $F^n$.
:::

::: {.solution}
<1>1. For an ideal $J\subseteq F[X]$, the Nullstellensatz gives
$$
\boxed{I(V(J))=\sqrt J}.
$$
Equivalently, radical ideals of $F[X]$ correspond inclusion-reversingly to Zariski-closed subsets of $X$.
::: {.proof}
This is the strong Nullstellensatz applied to the finitely generated reduced $F$-algebra $F[X]$, with $F$ algebraically closed.
:::

<1>2. For every subset $S\subseteq X$,
$$
\boxed{\overline S=V(I(S))}.
$$
::: {.proof}
By definition, every function in $I(S)$ vanishes on $S$, so
$$
S\subseteq V(I(S)).
$$
The right-hand side is closed, hence
$$
\overline S\subseteq V(I(S)).
$$

Conversely, let $Z=V(J)$ be any closed subset containing $S$. Then every $f\in J$ vanishes on $S$, so
$$
J\subseteq I(S).
$$
Applying $V$ reverses inclusion:
$$
V(I(S))\subseteq V(J)=Z.
$$
Thus $V(I(S))$ is contained in every closed subset containing $S$, hence in their intersection $\overline S$.
:::

<1>3. A subset $S\subseteq X$ is dense if and only if
$$
\boxed{
f|_S=0\Longrightarrow f=0
\quad\text{for every }f\in F[X].
}
$$
::: {.proof}
The displayed property is exactly
$$
I(S)=0.
$$
By step <1>2,
$$
\overline S=X
\iff
V(I(S))=X.
$$
Since $I(S)$ is radical, step <1>1 gives
$$
V(I(S))=X
\iff
I(S)=I(X)=0.
$$
Thus density is equivalent to the stated vanishing criterion.
:::

<1>4. If $S\subseteq X$ and $T\subseteq Y$ are dense, then
$$
\boxed{S\times T\text{ is dense in }X\times Y}.
$$
::: {.proof}
The coordinate ring of the product is
$$
F[X\times Y]\cong F[X]\tensor_F F[Y].
$$
Let
$$
\theta\in F[X]\tensor_FF[Y]
$$
vanish on $S\times T$. Write
$$
\theta=\sum_{i=1}^r f_i\tensor g_i
$$
with $f_1,\ldots,f_r$ linearly independent over $F$.

Fix $t\in T$. The function on $X$
$$
x\longmapsto \theta(x,t)
=\sum_i g_i(t)f_i(x)
$$
vanishes on $S$. By step <1>3 and density of $S$, it is the zero function in $F[X]$. Linear independence of the $f_i$ yields
$$
g_i(t)=0
$$
for every $i$ and every $t\in T$. Since $T$ is dense in $Y$, step <1>3 gives
$$
g_i=0
$$
for all $i$. Hence $\theta=0$.

By step <1>3 applied to $X\times Y$, this proves that $S\times T$ is dense.
:::

<1>5. The subset $\ZZ\subseteq F$ is dense in $\AA^1_F$.
::: {.proof}
Because $\operatorname{char}F=0$, the prime subfield of $F$ contains an embedded copy of $\ZZ$, so $\ZZ$ is infinite in $F$. A nonzero polynomial in one variable over a field has only finitely many roots. Therefore if
$$
f\in F[x]
$$
vanishes on every integer, then $f=0$. By step <1>3, $\ZZ$ is dense in $F$.
:::

<1>6. For every $n\ge1$,
$$
\boxed{\ZZ^n\text{ is dense in }F^n}.
$$
::: {.proof}
The case $n=1$ is step <1>5. If $\ZZ^n$ is dense in $F^n$, then step <1>4 applied to
$$
S=\ZZ^n\subseteq F^n,
\qquad
T=\ZZ\subseteq F
$$
shows that
$$
\ZZ^{n+1}=\ZZ^n\times\ZZ
$$
is dense in $F^{n+1}$. Induction proves the claim.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>3 proves part (a), step <1>4 proves part (b), and step <1>6 proves part (c).
:::
:::
