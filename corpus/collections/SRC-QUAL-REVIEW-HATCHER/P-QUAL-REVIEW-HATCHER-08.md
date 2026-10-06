---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-08
kind: problem
title: Covering-space existence among spheres and the torus
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 8 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The deterministic extraction drops the arrows in parts (b) and (c); they are restored from the unambiguous domain/codomain wording.
---

::: {.problem}
Determine whether each statement is true or false, and give reasons.

(a) There exists a covering space $S^2\to T$, where $T$ is the torus.

(b) There exists a covering space $T\to S^2$.

(c) There exists a nontrivial covering space $S^3\to S^3$.
:::

::: {.solution}
## Part (a)

The statement is
\[
\boxed{\text{false}}.
\]

Suppose, toward a contradiction, that
\[
p:S^2\to T
\]
is a covering map.

<1>1. Since \(S^2\) is compact, the covering has finitely many sheets.

::: {.proof}
For any \(y\in T\), the fiber
\[
p^{-1}(y)
\]
is a discrete subset of the compact space \(S^2\), hence finite. Because \(T\) is connected, all fibers have the same finite cardinality \(d\).
:::

<1>2. For a finite \(d\)-sheeted covering of finite CW complexes,
\[
\boxed{
\chi(S^2)=d\,\chi(T)}.
\]

::: {.proof}
Lift a finite CW structure on \(T\) to \(S^2\). Every cell of \(T\) has exactly \(d\) lifts, so each cellular count is multiplied by \(d\), and therefore so is the alternating sum defining Euler characteristic.
:::

<1>3. But
\[
\chi(S^2)=2
\qquad\text{and}\qquad
\chi(T)=0.
\]

::: {.proof}
These are the standard Euler characteristics of the sphere and torus.
:::

<1>4. Thus step <1>2 would give
\[
2=d\cdot0=0,
\]
a contradiction.

::: {.proof}
Substitute step <1>3 into step <1>2.
:::

<1>5. Therefore no covering
\[
S^2\to T
\]
exists.

::: {.proof}
The assumed covering led to the contradiction in step <1>4.
:::

## Part (b)

The statement is
\[
\boxed{\text{false}}.
\]

Suppose
\[
p:T\to S^2
\]
is a covering map.

<1>6. Since \(S^2\) is simply connected, every connected covering of \(S^2\) is trivial.

::: {.proof}
Connected covering spaces of a path-connected, locally path-connected, semilocally simply connected space correspond to subgroups of its fundamental group. Since
\[
\pi_1(S^2)=0,
\]
there is only the trivial subgroup, hence only the one-sheeted connected cover.
:::

<1>7. Therefore \(p\) would have to be a homeomorphism.

::: {.proof}
A one-sheeted covering map is a homeomorphism.
:::

<1>8. But \(T\) is not homeomorphic to \(S^2\).

::: {.proof}
For example,
\[
\pi_1(T)\cong\mathbb Z^2
\]
while
\[
\pi_1(S^2)=0.
\]
:::

<1>9. Hence no covering
\[
T\to S^2
\]
exists.

::: {.proof}
Steps <1>7--<1>8 contradict the assumption.
:::

## Part (c)

The statement is
\[
\boxed{\text{false}}.
\]

Suppose
\[
p:S^3\to S^3
\]
is a covering map.

<1>10. Since the target \(S^3\) is simply connected, every connected covering of \(S^3\) is one-sheeted.

::: {.proof}
Apply the same covering-space classification as in step <1>6, using
\[
\pi_1(S^3)=0.
\]
:::

<1>11. Therefore every covering
\[
S^3\to S^3
\]
is a homeomorphism.

::: {.proof}
The domain \(S^3\) is connected, so the cover is connected. By step <1>10 it has one sheet, and a one-sheeted covering is a homeomorphism.
:::

<1>12. Hence there is no nontrivial covering
\[
S^3\to S^3.
\]

::: {.proof}
Every such covering is equivalent to the identity cover by step <1>11.
:::

<1>13. Thus the three answers are
\[
\boxed{
\text{(a) false,\qquad (b) false,\qquad (c) false}.}
\]

::: {.proof}
Use steps <1>5, <1>9, and <1>12.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 gives the complete disposition.
:::
:::
