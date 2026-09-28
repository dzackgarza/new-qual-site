---
schema: qual/card@1
id: P-RILUB
kind: problem
title: $D_4$-invariant polynomials in two real variables
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Symmetric Functions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: claude-opus-5
  date: 2026-09-16
  note: "Merge adjudication: the consolidation merge kept one branch's rewritten statement and appended both authored solutions. Restored the imported statement and kept one solution: both proofs are correct and argue identically; the retained one justifies the converse inclusion by identifying the symmetry group with the signed permutation matrices."
---

::: {.problem}
What are the polynomials in two real variables that are invariant under the action of $D_4$, the symmetry group of a square, by rotations and reflections on the plane that the two variables form?
:::

::: {.solution}
Let $D_4$ act on $\RR[x,y]$ through the symmetries of the square with vertices $(\pm1,\pm1)$ in the $(x,y)$-plane.
Then
\[
\RR[x,y]^{D_4}=\RR[x^2+y^2,\,x^2y^2].
\]

<1>1. Every $D_4$-invariant polynomial lies in $\RR[x^2,y^2]$.
::: {.proof}
$D_4$ contains the reflections $(x,y)\mapsto(-x,y)$ and $(x,y)\mapsto(x,-y)$.
If $f=\sum_{i,j}a_{ij}x^iy^j$ is fixed by the first, then $a_{ij}=0$ for every odd $i$; invariance under the second similarly gives $a_{ij}=0$ for every odd $j$.
Hence $f(x,y)=F(x^2,y^2)$ for some $F\in\RR[u,v]$.
:::

<1>2. A polynomial $F(x^2,y^2)$ is $D_4$-invariant if and only if $F(u,v)=F(v,u)$.
::: {.proof}
$D_4$ contains the reflection $(x,y)\mapsto(y,x)$ in a diagonal, so invariance gives $F(x^2,y^2)=F(y^2,x^2)$.
The substitution $u\mapsto x^2$, $v\mapsto y^2$ is an injective homomorphism $\RR[u,v]\to\RR[x,y]$, so this is equivalent to $F(u,v)=F(v,u)$.
Conversely, the two sign changes and the interchange of coordinates generate the group of $2\times2$ signed permutation matrices, which has order $8$ and consists of symmetries of the square, so it is all of $D_4$.
A polynomial $F(x^2,y^2)$ with $F$ symmetric is fixed by each of these generators, hence by $D_4$.
:::

<1>3. $\RR[u,v]^{S_2}=\RR[u+v,\,uv]$.
::: {.proof}
This is the fundamental theorem of symmetric polynomials in two variables.
:::

<1>4. $\RR[x,y]^{D_4}=\RR[x^2+y^2,\,x^2y^2]$.
::: {.proof}
By <1>1 and <1>2, an invariant is $F(x^2,y^2)$ with $F$ symmetric; by <1>3, $F$ is a polynomial in $u+v$ and $uv$, and substituting $u=x^2$, $v=y^2$ expresses the invariant as a polynomial in $x^2+y^2$ and $x^2y^2$.
Conversely, $x^2+y^2$ and $x^2y^2$ are invariant by <1>2, so every polynomial in them is invariant.
:::

<1>5. The pair $x^2+y^2$, $x^4+y^4$ generates the same ring.
::: {.proof}
\[
x^4+y^4=(x^2+y^2)^2-2x^2y^2,
\qquad
x^2y^2=\frac{(x^2+y^2)^2-(x^4+y^4)}{2},
\]
and $2$ is invertible in $\RR$.
:::
:::
