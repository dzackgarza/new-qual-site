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
    source states the invariance of arithmetic genus under a blowup of a
    smooth centre. The proof uses vanishing of higher direct images of the
    structure sheaf and the definition p_a=(-1)^dim(chi(O)-1).
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    V.3.4 concerns Hilbert-Samuel multiplicity, not blowup cohomology.
    Replaced the false cross-reference with the projective birational
    vanishing theorem of Chatzistamatiou and Rulling, Theorem 1.1.
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
The blowup of a nonsingular variety along a nonsingular centre is
nonsingular, and the blowup morphism $\pi$ is projective and birational.
Both varieties are excellent because they are of finite type over $k$.
[Chatzistamatiou--Rülling, Theorem 1.1](https://arxiv.org/abs/1404.1827)
therefore gives
$$
R^j\pi_*\OO_{\widetilde X}=0\qquad(j>0).
$$
Since $X$ is normal and $\pi$ is proper and birational,
$$
\pi_*\OO_{\widetilde X}=\OO_X.
$$
The Leray spectral sequence now gives the displayed isomorphisms.
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
