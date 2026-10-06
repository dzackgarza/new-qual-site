---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-07
kind: problem
title: Classify a circular chain of tori with two links replaced by projective planes
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from practice problem 7 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md (Mistral OCR). The picture of X that it refers to was read from page 3 of the source PDF."
---

::: {.problem}
Let $X$ be the 2-manifold drawn as a circular chain of five tori, each torus joined to its two neighbours, and let the classification list be

$$S^2,\ T_1,\ T_2,\ \ldots,\ \RR P^2,\ \RR P^2\#\RR P^2,\ \RR P^2\#\RR P^2\#\RR P^2,\ \ldots$$

Determine which of these 2-manifolds is homeomorphic to the space $Y$ which is constructed similarly to $X$, but where two of the tori making up the "links" in the circular chain are replaced by $\RR P^2$'s.
:::

::: {.remark}
The source states this problem as "Repeat the above problem for the space $Y$ which is constructed similarly to $X$, but where two of the tori making up the 'links' in the circular chain are replaced by $\RR P^2$'s," referring to [[P-QUAL-REVIEW-HATCHER-06|practice problem 6]].
:::

::: {.solution}
Cut the circular chain along the five neck circles joining adjacent links.

<1>1. The three torus-links become orientable genus-\(1\) surfaces with two boundary components.

::: {.proof}
Each torus-link is a torus, and cutting its two attaching necks removes two open disks.
:::

<1>2. Each such torus piece has Euler characteristic
\[
\boxed{
2-2(1)-2=-2}.
\]

::: {.proof}
For an orientable genus-\(g\) surface with \(b\) boundary components,
\[
\chi=2-2g-b.
\]
Here \(g=1\) and \(b=2\).
:::

<1>3. Each projective-plane link becomes a nonorientable genus-\(1\) surface with two boundary components.

::: {.proof}
Replacing a torus-link by \(\mathbb{RP}^2\) and cutting its two attaching necks removes two open disks from \(\mathbb{RP}^2\).
:::

<1>4. Each such projective-plane piece has Euler characteristic
\[
\boxed{
2-1-2=-1}.
\]

::: {.proof}
For a nonorientable genus-\(k\) surface with \(b\) boundary components,
\[
\chi=2-k-b.
\]
Here \(k=1\) and \(b=2\).
:::

<1>5. Gluing along a boundary circle does not change the sum of Euler characteristics.

::: {.proof}
For a gluing along \(S^1\),
\[
\chi(A\cup_{S^1}B)
=
\chi(A)+\chi(B)-\chi(S^1),
\]
and
\[
\chi(S^1)=0.
\]
:::

<1>6. Therefore
\[
\boxed{
\chi(Y)
=
3(-2)+2(-1)
=
-8}.
\]

::: {.proof}
There are three torus pieces and two projective-plane pieces. Perform the five cyclic boundary-circle gluings and use step <1>5.
:::

<1>7. The surface \(Y\) is nonorientable.

::: {.proof}
Each projective-plane piece contains a one-sided simple closed curve disjoint from its boundary circles. After the boundary gluings, that curve remains embedded in \(Y\) with a Möbius-band neighborhood. Hence \(Y\) contains a one-sided loop and is nonorientable.
:::

<1>8. By the classification theorem, \(Y\) is homeomorphic to a connected sum of \(k\) copies of \(\mathbb{RP}^2\) for some \(k\ge1\).

::: {.proof}
The surface is closed, connected, and nonorientable by construction and step <1>7.
:::

<1>9. A closed nonorientable surface of genus \(k\) has
\[
\chi=2-k.
\]

::: {.proof}
This is the Euler-characteristic formula for
\[
\#^k\mathbb{RP}^2.
\]
:::

<1>10. Hence
\[
2-k=-8.
\]

::: {.proof}
Combine steps <1>6 and <1>9.
:::

<1>11. Therefore
\[
\boxed{k=10}.
\]

::: {.proof}
Solve
\[
2-k=-8.
\]
:::

<1>12. Thus
\[
\boxed{
Y
\cong
\#^{10}\mathbb{RP}^2}.
\]

::: {.proof}
Apply the classification theorem using steps <1>7 and <1>11.
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>12 identifies the required surface.
:::
:::
