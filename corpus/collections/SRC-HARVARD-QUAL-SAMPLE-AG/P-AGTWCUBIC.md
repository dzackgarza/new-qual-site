---
schema: qual/card@1
id: P-AGTWCUBIC
kind: problem
title: The twisted cubic as an intersection of two surfaces, set- and scheme-theoretically
classification:
  areas:
  - algebraic-geometry
  topics:
  - Twisted Cubic
  - Complete Intersections
  - Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks the twisted-cubic set- and scheme-theoretic questions and explicitly records the final general affine-curve question as withdrawn.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be the twisted cubic in $\AA^3$.
Is $X$ the set-theoretic intersection of two surfaces in $\PP^3$?

Is it the scheme-theoretic intersection of two surfaces?

More generally, for a curve $Y \subseteq \AA^3$ with $Y \cong \AA^1$: is it a set-theoretic or scheme-theoretic intersection of two surfaces?
:::

::: {.remark}
The examiner withdrew the final question, about curves $Y \cong \AA^1$ in $\AA^3$, after posing it.
:::

::: {.solution}
Let $C\subseteq\mathbb P^3$ be the projective closure of the affine twisted cubic.  In homogeneous coordinates $[x:y:z:w]$ it is parametrized by
\[
\nu_3:\mathbb P^1\longrightarrow\mathbb P^3,
\qquad
[s:t]\longmapsto[s^3:s^2t:st^2:t^3].
\]

<1>1. The three quadrics
\[
q_1=xz-y^2,
\qquad
q_2=xw-yz,
\qquad
q_3=yw-z^2.
\]
cut out $C$ set-theoretically.
::: {.proof}
Each $q_i$ vanishes on the parametrization, so
\[
C\subseteq V(q_1,q_2,q_3).
\]

Conversely, suppose
\[
[x:y:z:w]\in V(q_1,q_2,q_3).
\]
If $x=0$, then $q_1=0$ gives $y=0$, and $q_3=0$ gives $z=0$.  Thus the point is
\[
[0:0:0:1]=\nu_3([0:1]).
\]

If $x\ne0$, scale to $x=1$ and put $r=y$.  Then $q_1=0$ gives
\[
z=r^2,
\]
and $q_2=0$ gives
\[
w=rz=r^3.
\]
Thus the point is
\[
[1:r:r^2:r^3]=\nu_3([1:r]).
\]
Hence
\[
V(q_1,q_2,q_3)=C
\]
set-theoretically.
:::

<1>2. Define a quadric and a cubic by
\[
F=y^2-xz
\]
and
\[
G=z^3+xw^2-2yzw.
\]
Then
\[
\boxed{C=V(F,G)}
\]
set-theoretically.
::: {.proof}
Since
\[
F=-q_1
\]
and
\[
G=wq_2-zq_3,
\]
both $F$ and $G$ vanish on $C$.

Conversely, let $P=[x:y:z:w]$ satisfy $F(P)=G(P)=0$.  Put
\[
A=q_2=xw-yz,
\qquad
B=q_3=yw-z^2.
\]
The identity
\[
yA-xB
=z(xz-y^2)
=zq_1
\]
shows that, on $F=0$,
\[
yA=xB.
\]

If $x\ne0$, then
\[
B=\frac yx A.
\]
Using $G=wA-zB=0$ gives
\[
0=A\left(w-\frac{yz}{x}\right)
=\frac{A(xw-yz)}x
=\frac{A^2}{x}.
\]
Hence $A=0$, and then $B=0$.  Thus
\[
q_1=q_2=q_3=0,
\]
so <1>1 gives $P\in C$.

If $x=0$, then $F=0$ gives $y=0$, and $G=0$ becomes
\[
z^3=0.
\]
Hence $z=0$, so
\[
P=[0:0:0:1]\in C.
\]
Therefore $V(F,G)=C$ as sets.
:::

<1>3. The twisted cubic is not the scheme-theoretic intersection of two surfaces in $\mathbb P^3$.
::: {.proof}
Suppose instead that
\[
C=V(H_1,H_2)
\]
scheme-theoretically, with $H_i$ homogeneous of positive degrees
\[
d_i=\deg H_i.
\]
Since the scheme-theoretic intersection has pure codimension $2$, the two surfaces have no common surface component, so $C$ is a complete intersection of type $(d_1,d_2)$.  Bézout then gives
\[
\deg C=d_1d_2.
\]
The twisted cubic has degree $3$, hence
\[
d_1d_2=3.
\]
Thus, after interchanging the equations,
\[
d_1=1,
\qquad
d_2=3.
\]
But $d_1=1$ means $H_1=0$ is a plane, so $C$ would lie in a plane.

The twisted cubic is nondegenerate: a linear form
\[
a_0x+a_1y+a_2z+a_3w
\]
vanishing on $C$ would give the polynomial identity
\[
a_0s^3+a_1s^2t+a_2st^2+a_3t^3=0
\]
for all $[s:t]$, forcing
\[
a_0=a_1=a_2=a_3=0.
\]
Thus no plane contains $C$, a contradiction.
:::

<1>4. Equivalently, the pair $(F,G)$ from <1>2 cuts out a nonreduced scheme supported on $C$, rather than the twisted cubic scheme itself.
::: {.proof}
Step <1>2 proves that the reduced closed subscheme underlying $V(F,G)$ is $C$.  If $V(F,G)$ itself were the twisted cubic scheme, then $C$ would be the scheme-theoretic complete intersection of a quadric and a cubic, contradicting <1>3.  Thus the two equations have the correct support but a thicker scheme structure along that support.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>2 proves the set-theoretic intersection statement, and step <1>3 proves the failure of scheme-theoretic complete intersection.
:::
:::
