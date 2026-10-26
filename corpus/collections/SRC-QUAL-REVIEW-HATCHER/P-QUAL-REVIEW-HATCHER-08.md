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

::: pf

::: pf-step

Since \(S^2\) is compact, the covering has finitely many sheets.


::: pf-proof

For any \(y\in T\), the fiber
\[
p^{-1}(y)
\]
is a discrete subset of the compact space \(S^2\), hence finite. Because \(T\) is connected, all fibers have the same finite cardinality \(d\).

:::

:::

::: pf-step

For a finite \(d\)-sheeted covering of finite CW complexes,
\[
\boxed{
\chi(S^2)=d\,\chi(T)}.
\]


::: pf-proof

Lift a finite CW structure on \(T\) to \(S^2\). Every cell of \(T\) has exactly \(d\) lifts, so each cellular count is multiplied by \(d\), and therefore so is the alternating sum defining Euler characteristic.

:::

:::

::: pf-step

But
\[
\chi(S^2)=2
\qquad\text{and}\qquad
\chi(T)=0.
\]


::: pf-proof

These are the standard Euler characteristics of the sphere and torus.

:::

:::

::: pf-step

Thus step <1>2 would give
\[
2=d\cdot0=0,
\]
a contradiction.


::: pf-proof

Substitute step <1>3 into step <1>2.

:::

:::

::: pf-step

Therefore no covering
\[
S^2\to T
\]
exists.


::: pf-proof

The assumed covering led to the contradiction in step <1>4.

:::

:::

::: pf-step

Since \(S^2\) is simply connected, every connected covering of \(S^2\) is trivial.


::: pf-proof

Connected covering spaces of a path-connected, locally path-connected, semilocally simply connected space correspond to subgroups of its fundamental group. Since
\[
\pi_1(S^2)=0,
\]
there is only the trivial subgroup, hence only the one-sheeted connected cover.

:::

:::

::: pf-step

Therefore \(p\) would have to be a homeomorphism.


::: pf-proof

A one-sheeted covering map is a homeomorphism.

:::

:::

::: pf-step

But \(T\) is not homeomorphic to \(S^2\).


::: pf-proof

For example,
\[
\pi_1(T)\cong\mathbb Z^2
\]
while
\[
\pi_1(S^2)=0.
\]

:::

:::

::: pf-step

Hence no covering
\[
T\to S^2
\]
exists.


::: pf-proof

Steps <1>7--<1>8 contradict the assumption.

:::

:::

::: pf-step

Since the target \(S^3\) is simply connected, every connected covering of \(S^3\) is one-sheeted.


::: pf-proof

Apply the same covering-space classification as in step <1>6, using
\[
\pi_1(S^3)=0.
\]

:::

:::

::: pf-step

Therefore every covering
\[
S^3\to S^3
\]
is a homeomorphism.


::: pf-proof

The domain \(S^3\) is connected, so the cover is connected. By step <1>10 it has one sheet, and a one-sheeted covering is a homeomorphism.

:::

:::

::: pf-step

Hence there is no nontrivial covering
\[
S^3\to S^3.
\]


::: pf-proof

Every such covering is equivalent to the identity cover by step <1>11.

:::

:::

::: pf-step

Thus the three answers are
\[
\boxed{
\text{(a) false,\qquad (b) false,\qquad (c) false}.}
\]


::: pf-proof

Use steps <1>5, <1>9, and <1>12.

:::

:::

::: pf-qed

Step <1>13 gives the complete disposition.

:::

:::
