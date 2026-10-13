---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-05
kind: problem
title: Homology and cohomology of twice-punctured real projective space
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 5 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Compute the homology and cohomology groups of
\[
\mathbb{RP}^n\setminus\{x,y\},
\]
where $x$ and $y$ are distinct points of $\mathbb{RP}^n$.
:::

::: {.solution}
Assume first
\[
n\ge2.
\]
Let
\[
X=\mathbb{RP}^n\setminus\{x,y\}.
\]

## Homotopy type

<1>1. There exists a projective hyperplane
\[
H\cong\mathbb{RP}^{n-1}
\]
that contains neither \(x\) nor \(y\).

::: {.proof}
Choose homogeneous representatives \(v_x,v_y\in\mathbb R^{n+1}\) for the two projective points. Since the two projective points are distinct, choose a nonzero linear functional
\[
\lambda:\mathbb R^{n+1}\to\mathbb R
\]
with
\[
\lambda(v_x)\ne0
\qquad\text{and}\qquad
\lambda(v_y)\ne0.
\]
Then the projectivization of \(\ker\lambda\) is a projective hyperplane avoiding both points.
:::

<1>2. The complement
\[
\mathbb{RP}^n-H
\]
is an affine \(n\)-space, hence homeomorphic to \(\mathbb R^n\), and contains both punctures.

::: {.proof}
The complement of a projective hyperplane is the standard affine chart.
:::

<1>3. With respect to the standard CW decomposition
\[
\mathbb{RP}^n
=
\mathbb{RP}^{n-1}\cup e^n,
\]
we may therefore regard both \(x\) and \(y\) as points of the open \(n\)-cell.

::: {.proof}
Take \(H\) from step <1>1 as the \((n-1)\)-skeleton. Its complement is the top cell by step <1>2.
:::

<1>4. Let
\[
D^n
\]
be the characteristic disk of the top cell, whose boundary is attached to
\[
\mathbb{RP}^{n-1}
\]
by the antipodal quotient map
\[
q:S^{n-1}\to\mathbb{RP}^{n-1}.
\]
Choose two interior points \(u,v\in D^n\) mapping to \(x,y\).

::: {.proof}
This is the standard characteristic-map description of the top cell of \(\mathbb{RP}^n\).
:::

<1>5. The punctured disk
\[
D^n\setminus\{u,v\}
\]
deformation retracts, relative to its boundary, onto a subspace homotopy equivalent to
\[
S^{n-1}\vee S^{n-1},
\]
with one sphere equal to the original boundary sphere.

::: {.proof}
Choose a small closed ball around one puncture, disjoint from the second puncture and from the boundary. Join the boundary of that small ball to the outer boundary by an embedded arc avoiding the other puncture. Collapse a regular neighborhood of the complement of the outer boundary, inner boundary, and connecting arc. This gives a deformation retraction onto the union of the outer boundary sphere and one additional \((n-1)\)-sphere attached at a point.

Equivalently, \(D^n\setminus\{u,v\}\) is obtained from \(D^n\setminus\{u\}\), which retracts onto \(\partial D^n\), by puncturing once more, thereby adding one additional \((n-1)\)-sphere.
:::

<1>6. After gluing the outer boundary sphere to \(\mathbb{RP}^{n-1}\) by \(q\), the boundary-sphere part of the deformation retract becomes a mapping cylinder of \(q\), which deformation retracts onto \(\mathbb{RP}^{n-1}\).

::: {.proof}
Keeping a collar of \(\partial D^n\) produces the mapping cylinder
\[
M_q
=
S^{n-1}\times[0,1]\cup_q\mathbb{RP}^{n-1}.
\]
Every mapping cylinder deformation retracts onto its target.
:::

<1>7. The additional \((n-1)\)-sphere from step <1>5 is attached at one point.

::: {.proof}
In the relative deformation retract from step <1>5, the extra sphere meets the outer-boundary part only at the endpoint of the chosen connecting arc. After the outer-boundary part retracts to \(\mathbb{RP}^{n-1}\), that intersection remains one point.
:::

<1>8. Hence
\[
\boxed{
X\simeq
\mathbb{RP}^{n-1}\vee S^{n-1}}.
\]

::: {.proof}
Combine steps <1>3--<1>7.
:::

## Integral homology

Let
\[
m=n-1.
\]

<1>9. The integral homology of \(\mathbb{RP}^{m}\) is
\[
H_k(\mathbb{RP}^{m};\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/2,&0<k<m\text{ and }k\text{ odd},\\
0,&0<k<m\text{ and }k\text{ even},\\
\mathbb Z,&k=m\text{ and }m\text{ odd},\\
0,&k=m\text{ and }m\text{ even}.
\end{cases}
\]

::: {.proof}
This is the standard cellular-homology computation for real projective space: the cellular boundary maps alternate between multiplication by \(2\) and \(0\).
:::

<1>10. Reduced homology of a wedge of pointed CW complexes is the direct sum of the reduced homologies.

::: {.proof}
The wedge is a one-point union, and reduced cellular chains split as the direct sum of the reduced cellular chains of the summands.
:::

<1>11. Therefore, for
\[
0<k<n-1,
\]
\[
\boxed{
H_k(X;\mathbb Z)
\cong
\begin{cases}
\mathbb Z/2,&k\text{ odd},\\
0,&k\text{ even}.
\end{cases}}
\]

::: {.proof}
In these degrees, only the \(\mathbb{RP}^{n-1}\)-summand contributes. Apply steps <1>8--<1>10.
:::

<1>12. If \(n\) is even, then \(n-1\) is odd, so
\[
\boxed{
H_{n-1}(X;\mathbb Z)
\cong
\mathbb Z\oplus\mathbb Z}.
\]

::: {.proof}
The top homology of \(\mathbb{RP}^{n-1}\) is \(\mathbb Z\) when \(n-1\) is odd, and the \(S^{n-1}\)-summand contributes another \(\mathbb Z\).
:::

<1>13. If \(n\) is odd, then \(n-1\) is even, so
\[
\boxed{
H_{n-1}(X;\mathbb Z)
\cong
\mathbb Z}.
\]

::: {.proof}
The top integral homology of the even-dimensional nonorientable manifold \(\mathbb{RP}^{n-1}\) is \(0\), while the sphere summand contributes \(\mathbb Z\).
:::

<1>14. Since \(X\) is connected for \(n\ge2\),
\[
\boxed{
H_0(X;\mathbb Z)\cong\mathbb Z}.
\]

::: {.proof}
Removing finitely many points from an \(n\)-manifold with \(n\ge2\) does not disconnect this space; equivalently, the wedge model in step <1>8 is connected.
:::

<1>15. For \(k\ge n\),
\[
\boxed{
H_k(X;\mathbb Z)=0}.
\]

::: {.proof}
The wedge model in step <1>8 has CW dimension \(n-1\).
:::

Thus, for \(n\ge2\),
\[
\boxed{
H_k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/2,&0<k<n-1,\ k\text{ odd},\\
0,&0<k<n-1,\ k\text{ even},\\
\mathbb Z^2,&k=n-1,\ n\text{ even},\\
\mathbb Z,&k=n-1,\ n\text{ odd},\\
0,&k\ge n.
\end{cases}}
\]

## Integral cohomology

<1>16. By the universal coefficient theorem,
\[
0\to
\operatorname{Ext}(H_{k-1}(X),\mathbb Z)
\to
H^k(X;\mathbb Z)
\to
\operatorname{Hom}(H_k(X),\mathbb Z)
\to0.
\]

::: {.proof}
This is the universal coefficient theorem for cohomology over \(\mathbb Z\).
:::

<1>17. For
\[
0<k<n-1,
\]
\[
\boxed{
H^k(X;\mathbb Z)
\cong
\begin{cases}
\mathbb Z/2,&k\text{ even},\\
0,&k\text{ odd}.
\end{cases}}
\]

::: {.proof}
In these degrees:
- if \(k\) is even, then \(H_k=0\) and \(H_{k-1}\cong\mathbb Z/2\), so
  \[
  H^k\cong\operatorname{Ext}(\mathbb Z/2,\mathbb Z)\cong\mathbb Z/2;
  \]
- if \(k\) is odd, then \(H_k\cong\mathbb Z/2\), so
  \[
  \operatorname{Hom}(H_k,\mathbb Z)=0,
  \]
  while \(H_{k-1}=0\).
:::

<1>18. If \(n\) is even, then
\[
\boxed{
H^{n-1}(X;\mathbb Z)
\cong
\mathbb Z^2}.
\]

::: {.proof}
Here \(n-1\) is odd. By step <1>12,
\[
H_{n-1}\cong\mathbb Z^2,
\]
and
\[
H_{n-2}=0
\]
because \(n-2\) is even. Apply step <1>16.
:::

<1>19. If \(n\) is odd, then
\[
\boxed{
H^{n-1}(X;\mathbb Z)
\cong
\mathbb Z\oplus\mathbb Z/2}.
\]

::: {.proof}
Here \(n-1\) is even. By step <1>13,
\[
H_{n-1}\cong\mathbb Z,
\]
while
\[
H_{n-2}\cong\mathbb Z/2
\]
because \(n-2\) is odd. Thus step <1>16 gives
\[
H^{n-1}
\cong
\operatorname{Hom}(\mathbb Z,\mathbb Z)
\oplus
\operatorname{Ext}(\mathbb Z/2,\mathbb Z)
\cong
\mathbb Z\oplus\mathbb Z/2.
\]
:::

<1>20. Also,
\[
\boxed{
H^0(X;\mathbb Z)\cong\mathbb Z}
\]
and
\[
\boxed{
H^k(X;\mathbb Z)=0
\qquad(k\ge n)}.
\]

::: {.proof}
The degree-zero statement follows from connectedness. For \(k\ge n\), both \(H_k\) and \(H_{k-1}\) vanish by step <1>15 except possibly \(H_{n-1}\) when \(k=n\); but \(H_{n-1}\) is free in both parity cases, so its \(\operatorname{Ext}\) group vanishes. Hence all \(H^k\) with \(k\ge n\) are zero.
:::

Thus, for \(n\ge2\),
\[
\boxed{
H^k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/2,&0<k<n-1,\ k\text{ even},\\
0,&0<k<n-1,\ k\text{ odd},\\
\mathbb Z^2,&k=n-1,\ n\text{ even},\\
\mathbb Z\oplus\mathbb Z/2,&k=n-1,\ n\text{ odd},\\
0,&k\ge n.
\end{cases}}
\]

## The case \(n=1\)

<1>21. Since
\[
\mathbb{RP}^1\cong S^1,
\]
removing two distinct points gives two open intervals.

::: {.proof}
A circle minus two points has exactly two connected components, each homeomorphic to an open interval.
:::

<1>22. Therefore, when \(n=1\),
\[
\boxed{
H_0(X;\mathbb Z)\cong\mathbb Z^2}
\]
and
\[
\boxed{
H_k(X;\mathbb Z)=0
\quad(k>0)}.
\]

::: {.proof}
Each component is contractible.
:::

<1>23. Likewise, when \(n=1\),
\[
\boxed{
H^0(X;\mathbb Z)\cong\mathbb Z^2}
\]
and
\[
\boxed{
H^k(X;\mathbb Z)=0
\quad(k>0)}.
\]

::: {.proof}
Cohomology of a disjoint union of two contractible components has rank \(2\) in degree \(0\) and vanishes above degree \(0\).
:::

<1>24. Q.E.D.

::: {.proof}
Steps <1>8 and <1>11--<1>20 compute the homotopy type, homology, and cohomology for \(n\ge2\), while steps <1>21--<1>23 handle \(n=1\).
:::
:::
