---
schema: qual/card@1
id: P-SQUAL1-06
kind: problem
title: The Möbius band does not retract onto its boundary circle
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $M$ be the Möbius band and $S=\partial M$ its boundary circle.
Show that there is no retraction
$$M\longrightarrow S.$$
:::

::: {.solution}
Use the standard quotient model
\[
M=
[0,1]\times[-1,1]/(0,t)\sim(1,-t).
\]

Let
\[
C=\{[s,0]:0\le s\le1\}
\]
be the core circle.

<1>1. The map
\[
H([s,t],u)
=
[s,(1-u)t]
\]
defines a deformation retraction of \(M\) onto \(C\).

::: {.proof}
The formula respects the identification
\[
(0,t)\sim(1,-t)
\]
because
\[
(0,(1-u)t)\sim(1,-(1-u)t).
\]
At \(u=0\), \(H\) is the identity; at \(u=1\), its image lies in \(C\); and points of \(C\) are fixed for all \(u\).
:::

<1>2. Hence
\[
\boxed{
\pi_1(M)\cong\pi_1(C)\cong\mathbb Z}.
\]

::: {.proof}
A deformation retraction is a homotopy equivalence, and the core \(C\) is a circle.
:::

Let
\[
i:S=\partial M\hookrightarrow M
\]
be the boundary inclusion.

<1>3. The boundary \(S\) is a single circle.

::: {.proof}
In the rectangle model, the top edge
\[
[0,1]\times\{1\}
\]
and bottom edge
\[
[0,1]\times\{-1\}
\]
are joined at their endpoints by the Möbius identification:
\[
(0,1)\sim(1,-1),
\qquad
(1,1)\sim(0,-1).
\]
Thus the two edges form one closed loop.
:::

<1>4. A generator of \(\pi_1(S)\) traverses the top edge once and then the bottom edge once.

::: {.proof}
The boundary circle is exactly the union of those two edge arcs joined end-to-end as described in step <1>3.
:::

<1>5. Under the deformation retraction \(M\to C\), the top edge traverses the core circle once.

::: {.proof}
The retraction sends
\[
[s,1]\longmapsto[s,0].
\]
As \(s\) runs from \(0\) to \(1\), this goes once around the core circle.
:::

<1>6. Under the same deformation retraction, the bottom edge also traverses the core circle once in the same direction.

::: {.proof}
To continue the oriented boundary loop after the top edge, the bottom edge is traversed from \((1,-1)\) to \((0,-1)\). Under the quotient identification,
\[
[1,-1]=[0,1],
\]
and the retraction sends this bottom traversal to a second traversal of the core consistent with the first. Equivalently, the boundary of a Möbius band is the connected double cover of its core circle.
:::

<1>7. Therefore the induced homomorphism
\[
i_*:\pi_1(S)\to\pi_1(M)
\]
is multiplication by \(2\):
\[
\boxed{
i_*(1)=2}.
\]

::: {.proof}
By steps <1>4--<1>6, one trip around the boundary becomes two trips around the core after applying the deformation retraction that identifies \(\pi_1(M)\) with \(\mathbb Z\).
:::

Suppose, toward a contradiction, that there exists a retraction
\[
r:M\to S.
\]

<1>8. Since \(r\) is a retraction,
\[
\boxed{
r\circ i=\operatorname{id}_S}.
\]

::: {.proof}
A retraction restricts to the identity on the subspace onto which it retracts.
:::

<1>9. Passing to fundamental groups,
\[
\boxed{
r_*\circ i_*=\operatorname{id}_{\pi_1(S)}}.
\]

::: {.proof}
Fundamental groups are functorial with respect to composition.
:::

<1>10. Write
\[
r_*(1)=m
\]
for some \(m\in\mathbb Z\).

::: {.proof}
Both fundamental groups are isomorphic to \(\mathbb Z\), and every homomorphism \(\mathbb Z\to\mathbb Z\) is determined by the image of \(1\).
:::

<1>11. Then
\[
(r_*\circ i_*)(1)=2m.
\]

::: {.proof}
By step <1>7,
\[
i_*(1)=2.
\]
Since \(r_*\) is a homomorphism,
\[
r_*(2)=2r_*(1)=2m.
\]
:::

<1>12. But step <1>9 requires
\[
(r_*\circ i_*)(1)=1.
\]

::: {.proof}
The identity homomorphism on \(\mathbb Z\) sends \(1\) to \(1\).
:::

<1>13. Hence
\[
2m=1,
\]
which has no integer solution.

::: {.proof}
The left-hand side is even and the right-hand side is odd.
:::

<1>14. Therefore no retraction
\[
\boxed{
M\to\partial M}
\]
exists.

::: {.proof}
The assumption of a retraction led to the contradiction in step <1>13.
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>14 is the required conclusion.
:::
:::
