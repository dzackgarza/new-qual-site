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
\RP^n\setminus\{x,y\},
\]
where $x$ and $y$ are distinct points of $\RP^n$.
:::

::: {.solution}

Assume first
\[
n\ge2.
\]
Let
\[
X=\RP^n\setminus\{x,y\}.
\]

## Homotopy type

::: pf

::: {.pf-step #s1-1}

There exists a projective hyperplane
\[
H\cong\RP^{n-1}
\]
that contains neither \(x\) nor \(y\).


::: pf-proof

Choose homogeneous representatives \(v_x,v_y\in\RR^{n+1}\) for the two projective points. Since the two projective points are distinct, choose a nonzero linear functional
\[
\lambda:\RR^{n+1}\to\RR
\]
with
\[
\lambda(v_x)\ne0
\qquad\text{and}\qquad
\lambda(v_y)\ne0.
\]
Then the projectivization of \(\ker\lambda\) is a projective hyperplane avoiding both points.

:::

:::

::: {.pf-step #s1-2}

The complement
\[
\RP^n-H
\]
is an affine \(n\)-space, hence homeomorphic to \(\RR^n\), and contains both punctures.


::: pf-proof

The complement of a projective hyperplane is the standard affine chart.

:::

:::

::: {.pf-step #s1-3}

With respect to the standard CW decomposition
\[
\RP^n
=
\RP^{n-1}\cup e^n,
\]
we may therefore regard both \(x\) and \(y\) as points of the open \(n\)-cell.


::: pf-proof

Take \(H\) from step [](#s1-1){.pf-ref} as the \((n-1)\)-skeleton. Its complement is the top cell by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Let
\[
D^n
\]
be the characteristic disk of the top cell, whose boundary is attached to
\[
\RP^{n-1}
\]
by the antipodal quotient map
\[
q:S^{n-1}\to\RP^{n-1}.
\]
Choose two interior points \(u,v\in D^n\) mapping to \(x,y\).


::: pf-proof

This is the standard characteristic-map description of the top cell of \(\RP^n\).

:::

:::

::: {.pf-step #s1-5}

The punctured disk
\[
D^n\setminus\{u,v\}
\]
deformation retracts, relative to its boundary, onto a subspace homotopy equivalent to
\[
S^{n-1}\vee S^{n-1},
\]
with one sphere equal to the original boundary sphere.


::: pf-proof

Choose a small closed ball around one puncture, disjoint from the second puncture and from the boundary. Join the boundary of that small ball to the outer boundary by an embedded arc avoiding the other puncture. Collapse a regular neighborhood of the complement of the outer boundary, inner boundary, and connecting arc. This gives a deformation retraction onto the union of the outer boundary sphere and one additional \((n-1)\)-sphere attached at a point.

Equivalently, \(D^n\setminus\{u,v\}\) is obtained from \(D^n\setminus\{u\}\), which retracts onto \(\partial D^n\), by puncturing once more, thereby adding one additional \((n-1)\)-sphere.

:::

:::

::: {.pf-step #s1-6}

After gluing the outer boundary sphere to \(\RP^{n-1}\) by \(q\), the boundary-sphere part of the deformation retract becomes a mapping cylinder of \(q\), which deformation retracts onto \(\RP^{n-1}\).


::: pf-proof

Keeping a collar of \(\partial D^n\) produces the mapping cylinder
\[
M_q
=
S^{n-1}\times[0,1]\cup_q\RP^{n-1}.
\]
Every mapping cylinder deformation retracts onto its target.

:::

:::

::: {.pf-step #s1-7}

The additional \((n-1)\)-sphere from step [](#s1-5){.pf-ref} is attached at one point.


::: pf-proof

In the relative deformation retract from step [](#s1-5){.pf-ref}, the extra sphere meets the outer-boundary part only at the endpoint of the chosen connecting arc. After the outer-boundary part retracts to \(\RP^{n-1}\), that intersection remains one point.

:::

:::

::: {.pf-step #s1-8}

Hence
\[
\boxed{
X\simeq
\RP^{n-1}\vee S^{n-1}}.
\]


::: pf-proof

Combine steps [](#s1-3){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The integral homology of \(\RP^{m}\) is
\[
H_k(\RP^{m};\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ/2,&0<k<m\text{ and }k\text{ odd},\\
0,&0<k<m\text{ and }k\text{ even},\\
\ZZ,&k=m\text{ and }m\text{ odd},\\
0,&k=m\text{ and }m\text{ even}.
\end{cases}
\]


::: pf-proof

This is the standard cellular-homology computation for real projective space: the cellular boundary maps alternate between multiplication by \(2\) and \(0\).

:::

:::

::: {.pf-step #s1-10}

Reduced homology of a wedge of pointed CW complexes is the direct sum of the reduced homologies.


::: pf-proof

The wedge is a one-point union, and reduced cellular chains split as the direct sum of the reduced cellular chains of the summands.

:::

:::

::: {.pf-step #s1-11}

Therefore, for
\[
0<k<n-1,
\]
\[
\boxed{
H_k(X;\ZZ)
\cong
\begin{cases}
\ZZ/2,&k\text{ odd},\\
0,&k\text{ even}.
\end{cases}}
\]


::: pf-proof

In these degrees, only the \(\RP^{n-1}\)-summand contributes. Apply steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

If \(n\) is even, then \(n-1\) is odd, so
\[
\boxed{
H_{n-1}(X;\ZZ)
\cong
\ZZ\oplus\ZZ}.
\]


::: pf-proof

The top homology of \(\RP^{n-1}\) is \(\ZZ\) when \(n-1\) is odd, and the \(S^{n-1}\)-summand contributes another \(\ZZ\).

:::

:::

::: {.pf-step #s1-13}

If \(n\) is odd, then \(n-1\) is even, so
\[
\boxed{
H_{n-1}(X;\ZZ)
\cong
\ZZ}.
\]


::: pf-proof

The top integral homology of the even-dimensional nonorientable manifold \(\RP^{n-1}\) is \(0\), while the sphere summand contributes \(\ZZ\).

:::

:::

::: {.pf-step #s1-14}

Since \(X\) is connected for \(n\ge2\),
\[
\boxed{
H_0(X;\ZZ)\cong\ZZ}.
\]


::: pf-proof

Removing finitely many points from an \(n\)-manifold with \(n\ge2\) does not disconnect this space; equivalently, the wedge model in step [](#s1-8){.pf-ref} is connected.

:::

:::

::: {.pf-step #s1-15}

For \(k\ge n\),
\[
\boxed{
H_k(X;\ZZ)=0}.
\]


::: pf-proof

The wedge model in step [](#s1-8){.pf-ref} has CW dimension \(n-1\).

:::

:::

::: {.pf-step #s1-16}

By the universal coefficient theorem,
\[
0\to
\operatorname{Ext}(H_{k-1}(X),\ZZ)
\to
H^k(X;\ZZ)
\to
\operatorname{Hom}(H_k(X),\ZZ)
\to0.
\]


::: pf-proof

This is the universal coefficient theorem for cohomology over \(\ZZ\).

:::

:::

::: {.pf-step #s1-17}

For
\[
0<k<n-1,
\]
\[
\boxed{
H^k(X;\ZZ)
\cong
\begin{cases}
\ZZ/2,&k\text{ even},\\
0,&k\text{ odd}.
\end{cases}}
\]


::: pf-proof

In these degrees:
- if \(k\) is even, then \(H_k=0\) and \(H_{k-1}\cong\ZZ/2\), so
  \[
  H^k\cong\operatorname{Ext}(\ZZ/2,\ZZ)\cong\ZZ/2;
  \]
- if \(k\) is odd, then \(H_k\cong\ZZ/2\), so
  \[
  \operatorname{Hom}(H_k,\ZZ)=0,
  \]
  while \(H_{k-1}=0\).

:::

:::

::: {.pf-step #s1-18}

If \(n\) is even, then
\[
\boxed{
H^{n-1}(X;\ZZ)
\cong
\ZZ^2}.
\]


::: pf-proof

Here \(n-1\) is odd. By step [](#s1-12){.pf-ref},
\[
H_{n-1}\cong\ZZ^2,
\]
and
\[
H_{n-2}=0
\]
because \(n-2\) is even. Apply step [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-19}

If \(n\) is odd, then
\[
\boxed{
H^{n-1}(X;\ZZ)
\cong
\ZZ\oplus\ZZ/2}.
\]


::: pf-proof

Here \(n-1\) is even. By step [](#s1-13){.pf-ref},
\[
H_{n-1}\cong\ZZ,
\]
while
\[
H_{n-2}\cong\ZZ/2
\]
because \(n-2\) is odd. Thus step [](#s1-16){.pf-ref} gives
\[
H^{n-1}
\cong
\operatorname{Hom}(\ZZ,\ZZ)
\oplus
\operatorname{Ext}(\ZZ/2,\ZZ)
\cong
\ZZ\oplus\ZZ/2.
\]

:::

:::

::: {.pf-step #s1-20}

Also,
\[
\boxed{
H^0(X;\ZZ)\cong\ZZ}
\]
and
\[
\boxed{
H^k(X;\ZZ)=0
\qquad(k\ge n)}.
\]


::: pf-proof

The degree-zero statement follows from connectedness. For \(k\ge n\), both \(H_k\) and \(H_{k-1}\) vanish by step [](#s1-15){.pf-ref} except possibly \(H_{n-1}\) when \(k=n\); but \(H_{n-1}\) is free in both parity cases, so its \(\operatorname{Ext}\) group vanishes. Hence all \(H^k\) with \(k\ge n\) are zero.

:::

:::

::: {.pf-step #s1-21}

Since
\[
\RP^1\cong S^1,
\]
removing two distinct points gives two open intervals.


::: pf-proof

A circle minus two points has exactly two connected components, each homeomorphic to an open interval.

:::

:::

::: {.pf-step #s1-22}

Therefore, when \(n=1\),
\[
\boxed{
H_0(X;\ZZ)\cong\ZZ^2}
\]
and
\[
\boxed{
H_k(X;\ZZ)=0
\quad(k>0)}.
\]


::: pf-proof

Each component is contractible.

:::

:::

::: {.pf-step #s1-23}

Likewise, when \(n=1\),
\[
\boxed{
H^0(X;\ZZ)\cong\ZZ^2}
\]
and
\[
\boxed{
H^k(X;\ZZ)=0
\quad(k>0)}.
\]


::: pf-proof

Cohomology of a disjoint union of two contractible components has rank \(2\) in degree \(0\) and vanishes above degree \(0\).

:::

:::

::: pf-qed

Steps [](#s1-8){.pf-ref} and [](#s1-11){.pf-ref} through [](#s1-20){.pf-ref} compute the homotopy type, homology, and cohomology for \(n\ge2\), while steps [](#s1-21){.pf-ref} through [](#s1-23){.pf-ref} handle \(n=1\).

:::

:::

:::
