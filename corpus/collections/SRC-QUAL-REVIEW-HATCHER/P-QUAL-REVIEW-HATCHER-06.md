---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-06
kind: problem
title: Classify a closed surface drawn as a circular chain of tori
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from practice problem 6 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md (Mistral OCR). The extraction emits the picture only as an image placeholder; the picture was read from page 3 of the source PDF and is described in the statement."
---

::: {.problem}
The following picture depicts a 2-manifold $X$: a closed surface in $\RR^3$ drawn as a circular chain of five tori, each torus joined to its two neighbours, so that the surface shows five small holes, one in each link, arranged around one large central hole.

We know that every 2-manifold is homeomorphic to one of

$$S^2,\ T_1,\ T_2,\ \ldots,\ \RR P^2,\ \RR P^2\#\RR P^2,\ \RR P^2\#\RR P^2\#\RR P^2,\ \ldots$$

Determine which of these 2-manifolds is homeomorphic to $X$.
:::

::: {.remark}
The source gives $X$ only by the picture; the description in the statement is a reading of that picture.
:::

::: {.solution}
The surface \(X\) is orientable because it is embedded as the boundary of a thickened compact region in \(\mathbb R^3\). Thus \(X\) must be one of the orientable closed surfaces
\[
S^2,\ T_1,\ T_2,\dots.
\]

<1>1. Cut \(X\) along five disjoint circles, one in each neck joining adjacent torus-links in the circular chain.

::: {.proof}
The picture consists of five torus-shaped links connected cyclically by five narrow tubes. Cutting each connecting tube along a cross-sectional circle separates the surface into five pieces.
:::

<1>2. Each resulting piece is a torus with two open disks removed.

::: {.proof}
Each link is topologically a torus. The two cuts occur where that link was attached to its two neighbors, so each cut removes one disk from the torus-shaped piece. Hence each piece is an orientable genus-\(1\) surface with two boundary components.
:::

<1>3. The Euler characteristic of one such piece is
\[
\boxed{
2-2(1)-2=-2}.
\]

::: {.proof}
For a compact connected orientable surface of genus \(g\) with \(b\) boundary components,
\[
\chi=2-2g-b.
\]
Here \(g=1\) and \(b=2\).
:::

<1>4. Gluing two surfaces along a boundary circle does not change the sum of their Euler characteristics.

::: {.proof}
If \(A\) and \(B\) are glued along a circle \(S^1\), then
\[
\chi(A\cup_{S^1}B)
=
\chi(A)+\chi(B)-\chi(S^1).
\]
Since
\[
\chi(S^1)=0,
\]
the Euler characteristics simply add.
:::

<1>5. Therefore the cyclic gluing of the five pieces has
\[
\boxed{
\chi(X)=5(-2)=-10}.
\]

::: {.proof}
Start with the disjoint union of the five pieces, whose total Euler characteristic is \(-10\). Perform the five boundary-circle gluings. By step <1>4, each gluing leaves the total Euler characteristic unchanged.
:::

<1>6. If \(X\cong T_g\), then
\[
\chi(X)=2-2g.
\]

::: {.proof}
This is the Euler characteristic of a closed connected orientable surface of genus \(g\).
:::

<1>7. Hence
\[
2-2g=-10.
\]

::: {.proof}
Combine steps <1>5--<1>6.
:::

<1>8. Solving,
\[
\boxed{g=6}.
\]

::: {.proof}
\[
2-2g=-10
\iff
-2g=-12
\iff
g=6.
\]
:::

<1>9. Therefore
\[
\boxed{
X\cong T_6}.
\]

::: {.proof}
By the classification theorem for closed connected orientable surfaces, the genus is determined by the Euler characteristic. Step <1>8 gives genus \(6\).
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 identifies the surface in the classification list.
:::
:::
