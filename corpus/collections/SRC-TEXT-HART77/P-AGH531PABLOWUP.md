---
schema: qual/card@1
id: P-AGH531PABLOWUP
kind: problem
title: Invariance of the arithmetic genus under blowing up a nonsingular subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.1 and the retained Egbert companion calculation. The
    source explicitly reduces the exercise to Hartshorne V.3.4, which gives
    H^i(\tilde X,O_{\tilde X}) isomorphic to H^i(X,O_X) for the blowup of a
    nonsingular variety along a nonsingular centre. The repository blowup
    summary records the same invariance of chi(O). The proof below then uses
    the intrinsic definition p_a=(-1)^dim(chi(O)-1).
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $X$ be a nonsingular projective variety of any dimension, let $Y$ be a nonsingular subvariety, and let $\pi: \tilde{X} \rightarrow X$ be obtained by blowing up $Y$.
Show that $p_a(\tilde{X})=p_a(X)$.
:::

::: {.solution}
Put
$$
n=\dim X.
$$
Since a blowup is birational,
$$
\dim\widetilde X=n.
$$

::: pf

::: {.pf-step #cohomology-invariance}
For every $i\ge0$,
$$
\boxed{
H^i(\widetilde X,\OO_{\widetilde X})
\cong
H^i(X,\OO_X).}
$$

::: pf-proof
This is Hartshorne V.3.4, applied to the blowup
$$
\pi:\widetilde X=\operatorname{Bl}_Y X\longrightarrow X
$$
of the nonsingular projective variety $X$ along the nonsingular centre $Y$.
It is exactly the blowup-cohomology statement cited by the source solution to
V.3.1.  In the surface case the same fact is recorded in [[FE-SRFBLOW]] as
the invariance of $\chi(\OO)$, $p_g$, and $q$.
:::

:::

::: {.pf-step #euler-char-invariance}
The structure-sheaf Euler characteristic is unchanged:
$$
\boxed{
\chi(\widetilde X,\OO_{\widetilde X})
=
\chi(X,\OO_X).}
$$

::: pf-proof
By definition,
$$
\chi(Z,\OO_Z)
=
\sum_{i\ge0}(-1)^i
\dim_k H^i(Z,\OO_Z)
$$
for a projective variety $Z$.  Step [](#cohomology-invariance){.pf-ref} identifies every summand for
$Z=\widetilde X$ with the corresponding summand for $Z=X$, so the two
alternating sums agree.
:::

:::

::: {.pf-step #arithmetic-genus-equal}
The arithmetic genera agree:
$$
\boxed{p_a(\widetilde X)=p_a(X).}
$$

::: pf-proof
For a nonempty projective scheme of dimension $n$, the arithmetic genus is
[[D-COHEULER]]
$$
p_a(Z)=(-1)^n\bigl(\chi(Z,\OO_Z)-1\bigr).
$$
The varieties $X$ and $\widetilde X$ have the same dimension $n$, and step
[](#euler-char-invariance){.pf-ref} gives equality of their structure-sheaf Euler characteristics.
Substitution into the displayed definition gives
$$
p_a(\widetilde X)
=
(-1)^n\bigl(\chi(\widetilde X,\OO_{\widetilde X})-1\bigr)
=
(-1)^n\bigl(\chi(X,\OO_X)-1\bigr)
=
p_a(X).
$$
:::

:::

::: pf-qed
Steps [](#cohomology-invariance){.pf-ref}, [](#euler-char-invariance){.pf-ref} and [](#arithmetic-genus-equal){.pf-ref} prove the asserted invariance of the arithmetic genus under
blowing up a nonsingular centre.
:::

:::
:::
