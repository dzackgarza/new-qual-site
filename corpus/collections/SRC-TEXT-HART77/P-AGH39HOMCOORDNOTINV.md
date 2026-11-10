---
schema: qual/card@1
id: P-AGH39HOMCOORDNOTINV
kind: problem
title: The homogeneous coordinate ring is not an isomorphism invariant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coordinate Rings
  - Veronese Embedding
  - Isomorphism
relations:
- kind: uses
  target: P-AGH34DUPLEISO
- kind: uses
  target: P-AGH212DUPLE
- kind: uses
  target: P-AGH28HYPERSURFACE
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with Hartshorne I.3.9. The proof identifies the conic coordinate ring of the quadratic Veronese image and distinguishes it from k[s,t] by unique factorization, an invariant of the underlying ring rather than only of its grading.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the coordinate-ring calculation and the non-UFD factorization against independent published solutions. The irreducibility argument for the degree-one classes works in every characteristic.'
---

::: {.problem}
The homogeneous coordinate ring of a projective variety is not invariant under isomorphism.
Let $X = \PP^1$ and let $Y$ be the $2$-uple embedding of $\PP^1$ in $\PP^2$.
Then $X \cong Y$, but show that $S(X) \not\cong S(Y)$.
:::

::: {.solution}
Choose homogeneous coordinates $[s:t]$ on $X=\PP^1$ and $[u:v:w]$ on $\PP^2$ so that the quadratic Veronese map is
$$
[s:t]\longmapsto[s^2:st:t^2].
$$

::: pf

::: pf-step

The homogeneous coordinate rings are
$$
S(X)=k[s,t],
\qquad
S(Y)=k[u,v,w]/(uw-v^2).
$$

::: pf-proof

The projective line has zero homogeneous ideal, so $S(X)=k[s,t]$.
The displayed parametrization satisfies $uw-v^2=0$.
By [[P-AGH212DUPLE]], its image is a projective variety isomorphic to $\PP^1$ and is exactly the quadratic Veronese conic.
The polynomial $uw-v^2$ is irreducible: viewing it as a degree-one polynomial in $u$ over $k[v,w]$, any nonconstant factor independent of $u$ would have to divide both $w$ and $v^2$, whose greatest common divisor is $1$.
Thus $Z(uw-v^2)$ is an irreducible hypersurface in $\PP^2$, and its homogeneous ideal is $(uw-v^2)$ by [[P-AGH28HYPERSURFACE]].
Hence the second displayed description follows.

:::

:::

::: {.pf-step #s2}

The ring $S(X)$ is a unique factorization domain.

::: pf-proof

It is the polynomial ring in two variables over the field $k$, hence is a unique factorization domain.

:::

:::

::: {.pf-step #s3}

The ring
$$
R=k[u,v,w]/(uw-v^2)
$$
is not a unique factorization domain.

::: pf-proof

The polynomial $uw-v^2$ is irreducible in the UFD $k[u,v,w]$, hence prime, so $R$ is a domain.
Give $R$ its standard grading, and write $\bar u,\bar v,\bar w$ for the degree-one residue classes.

First, every nonzero homogeneous element of degree one in $R$ is irreducible.
Indeed, suppose such an element $h$ factors as $h=ab$.
Write $a$ and $b$ as sums of homogeneous components, and let $r,s$ be their highest occurring degrees and $p,q$ their lowest occurring degrees.
Since $R$ is a domain, the highest and lowest nonzero homogeneous components of $ab$ occur in degrees $r+s$ and $p+q$, respectively.
Because $h$ is homogeneous of degree one,
$$
r+s=p+q=1.
$$
The inequalities $p\le r$ and $q\le s$ then force $p=r$ and $q=s$.
Thus both factors are homogeneous, and one has degree zero.
Since $R_0=k$, that factor is a unit.

Consequently $\bar u,\bar v,\bar w$ are irreducible.
They are pairwise nonassociate: all units are nonzero constants by the same highest-degree argument, and the degree-one component of $R$ has basis $\bar u,\bar v,\bar w$ because the defining relation has degree two.
But in $R$,
$$
\bar u\,\bar w=\bar v^2.
$$
This gives two factorizations into irreducibles which cannot be matched by reordering and multiplication by units.
Therefore $R$ is not a unique factorization domain.

:::

:::

::: pf-qed

By [[P-AGH34DUPLEISO]], the quadratic Veronese map gives $X\cong Y$.
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that $S(X)$ is a UFD while $S(Y)$ is not.
Since being a UFD is preserved by ring isomorphism,
$$
S(X)\not\cong S(Y).
$$

:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 3.9, PDF p. 4: $S(X)=k[X_0,X_1]$, while $S(Y)$ is the subring $k[X_0^2,X_0X_1,X_1^2]$ of $k[X_0,X_1,X_2]$, "which is not a graded polynomial ring in $2$ variables (as the space of elements of the smallest nonzero degree is $3$ dimensional)".
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 3.9, PDF p. 12: $S(X)\cong S^1$ and $S(Y)\cong S^2/(x_0x_1-x_2^2)$, and the first is a UFD while the second is not, since $x_2^2=x_0x_1$.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.9, PDF p. 33: $S(X)=k[x,y]$ and $S(Y)=k[x,y,z]/(xy-z^2)$, whose maximal ideal $\mathfrak m=(x,y,z)$ at the vertex has $\dim_k\mathfrak m/\mathfrak m^2=3$, which no $k[s,t]$ has.
Borcherds' conclusion is about graded polynomial rings, and a ring isomorphism $S(X)\cong S(Y)$ need not preserve the grading, so his sentence as printed does not close; the two invariants that do are the ones in the other sets, unique factorization (Troiani, and the proof above) and the embedding dimension $\dim_k\mathfrak m/\mathfrak m^2$ (Egbert).
Agree with Troiani and Egbert.
:::
