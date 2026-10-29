---
schema: qual/card@1
id: P-SQUAL1-08
kind: problem
title: Universal cover and homology of $\RP^2\vee S^2$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $X$ be the space obtained by identifying one point of $\RP^2$ with one point of $S^2$.
Find the universal covering space $\widetilde X$ of $X$ and compute its homology groups.
:::

::: {.solution}

Let
\[
X=\RP^2\vee S^2
\]
with wedgepoint \(x_0\).

Let
\[
q:S^2\to\RP^2
\]
be the antipodal double cover, and choose
\[
q^{-1}(x_0)=\{u,-u\}.
\]

Construct \(\widetilde X\) by taking one copy \(S^2_0\) of the covering sphere \(S^2\), together with two additional copies \(S^2_+\) and \(S^2_-\), and identifying the chosen basepoint of \(S^2_+\) with \(u\in S^2_0\) and the chosen basepoint of \(S^2_-\) with \(-u\in S^2_0\).

::: pf

::: pf-step

There is a continuous map
\[
p:\widetilde X\to X
\]
defined by:
- \(p|_{S^2_0}=q\) onto \(\RP^2\);
- \(p|_{S^2_+}\) is the identity homeomorphism onto the wedged \(S^2\)-summand of \(X\);
- \(p|_{S^2_-}\) is another identity homeomorphism onto the same \(S^2\)-summand.


::: pf-proof

The three maps agree at the attachment points because
\[
q(u)=q(-u)=x_0,
\]
and the basepoints of \(S^2_+\) and \(S^2_-\) both map to the wedgepoint of the \(S^2\)-summand. Hence they paste to a continuous map.

:::

:::

::: {.pf-step #s1-2}

Away from the wedgepoint \(x_0\), the map \(p\) is locally a two-sheeted covering.


::: pf-proof

On the \(\RP^2\)-part away from \(x_0\), this is the usual antipodal covering
\[
S^2_0\to\RP^2.
\]
On the \(S^2\)-summand away from its basepoint, there are exactly two disjoint copies, one in \(S^2_+\) and one in \(S^2_-\), each mapping homeomorphically to the same neighborhood.

:::

:::

::: {.pf-step #s1-3}

The map \(p\) is also evenly covered near the wedgepoint.


::: pf-proof

Choose an open neighborhood
\[
U_R\subset\RP^2
\]
of \(x_0\) that is evenly covered by two disjoint open sets
\[
\widetilde U_+,\widetilde U_-\subset S^2_0
\]
containing \(u\) and \(-u\), respectively.

Choose a small open disk neighborhood
\[
U_S
\]
of the wedgepoint in the \(S^2\)-summand. Then
\[
U=U_R\vee U_S
\]
is a neighborhood of the wedgepoint in \(X\).

Its preimage is the disjoint union of
\[
\widetilde U_+\cup U_S^+
\]
and
\[
\widetilde U_-\cup U_S^-,
\]
where \(U_S^\pm\) are the corresponding disk neighborhoods in \(S^2_\pm\). Each component maps homeomorphically to \(U\).

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{
p:\widetilde X\to X
}
\]
is a connected two-sheeted covering.


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} establish the covering property. The space \(\widetilde X\) is connected because all three spheres are attached to the connected sphere \(S^2_0\).

:::

:::

::: {.pf-step #s1-5}

The space \(\widetilde X\) is simply connected.


::: pf-proof

Each of the three spheres is simply connected. Attach \(S^2_+\) to \(S^2_0\) at the single point \(u\). By Seifert--van Kampen, the fundamental group remains trivial. Then attach \(S^2_-\) at the single point \(-u\); van Kampen again gives trivial fundamental group.

:::

:::

::: {.pf-step #s1-6}

Hence \(p\) is the universal covering map.


::: pf-proof

A connected covering space is universal exactly when its total space is simply connected. Apply steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-step

Choose an embedded arc
\[
\gamma\subset S^2_0
\]
joining \(u\) to \(-u\).


::: pf-proof

Any two points on the sphere can be joined by an embedded arc.

:::

:::

::: pf-step

Collapsing \(\gamma\) to a point gives a homotopy equivalence
\[
\widetilde X
\simeq
S^2\vee S^2\vee S^2.
\]


::: pf-proof

The arc \(\gamma\) is contractible and is a cofibration in the CW structure obtained by triangulating the spheres with \(\gamma\) as a subcomplex. Collapsing such a contractible subcomplex is a homotopy equivalence.

After the collapse, the two attachment points \(u\) and \(-u\) become one point. The quotient of \(S^2_0\) by the arc \(\gamma\) is again homotopy equivalent to \(S^2\), while the two attached spheres \(S^2_+\) and \(S^2_-\) now meet it at the same point. Thus the quotient has the homotopy type of a wedge of three \(2\)-spheres.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\widetilde H_k(\widetilde X;\ZZ)
\cong
\widetilde H_k(S^2\vee S^2\vee S^2;\ZZ)}.
\]


::: pf-proof

Reduced homology is invariant under homotopy equivalence.

:::

:::

::: {.pf-step #s1-10}

For the wedge of three \(2\)-spheres,
\[
\boxed{
\widetilde H_2
\cong
\ZZ^3}.
\]


::: pf-proof

Reduced homology of a wedge of pointed CW complexes is the direct sum of the reduced homology groups:
\[
\widetilde H_2(S^2\vee S^2\vee S^2)
\cong
\ZZ\oplus\ZZ\oplus\ZZ.
\]

:::

:::

::: {.pf-step #s1-11}

For \(k\ne2\),
\[
\boxed{
\widetilde H_k(\widetilde X;\ZZ)=0}.
\]


::: pf-proof

Each \(S^2\) has reduced homology only in degree \(2\), and reduced homology of a wedge is the direct sum.

:::

:::

::: {.pf-step #s1-12}

Since \(\widetilde X\) is connected,
\[
\boxed{
H_0(\widetilde X;\ZZ)\cong\ZZ}.
\]


::: pf-proof

Every nonempty connected space has zeroth homology \(\ZZ\).

:::

:::

::: {.pf-step #s1-13}

Thus
\[
\boxed{
H_k(\widetilde X;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ^3,&k=2,\\
0,&\text{otherwise}.
\end{cases}}
\]


::: pf-proof

Combine steps [](#s1-10){.pf-ref} through [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} identifies the universal cover, and step [](#s1-13){.pf-ref} computes all of its homology groups.

:::

:::

:::
