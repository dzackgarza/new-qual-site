---
schema: qual/card@1
id: P-5YZPH
kind: problem
title: A $p$-subgroup acting on the cosets of a Sylow $p$-subgroup has a length-one
  orbit iff it lies in a conjugate
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---

::: problem
Let $G$ be a finite group, $H$ a $p\dash$subgroup, and $P$ a sylow $p\dash$subgroup for $p$ a prime.
Let $H$ act on the left cosets of $P$ in $G$ by left translation.

Prove that this is an orbit under this action of length 1.

Prove that $xP$ is an orbit of length 1 $\iff H$ is contained in $xPx\inv$.
:::

::: solution
Let $X=G/P$ be the set of left cosets of $P$. Since $P$ is a Sylow
$p$-subgroup,
\[
|X|=[G:P]
\]
is not divisible by $p$.

The $p$-group $H$ acts on $X$ by left multiplication. Every $H$-orbit has
cardinality
\[
[H:H_{xP}],
\]
hence is a power of $p$. Therefore every orbit of size greater than $1$ has
size divisible by $p$. If there were no orbit of size $1$, then $|X|$ would be
a sum of integers divisible by $p$, contradicting $p\nmid|X|$. Thus there is
at least one orbit of length $1$.

Now fix a coset $xP$. Its orbit has length $1$ exactly when every $h\in H$
fixes $xP$, i.e.
\[
hxP=xP
\qquad\text{for every }h\in H.
\]
For a given $h$ this is equivalent to
\[
x^{-1}hx\in P.
\]
Hence $xP$ is fixed by all of $H$ exactly when
\[
x^{-1}Hx\subseteq P,
\]
or equivalently
\[
\boxed{H\subseteq xPx^{-1}}.
\]
:::
