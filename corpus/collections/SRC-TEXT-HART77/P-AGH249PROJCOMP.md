---
schema: qual/card@1
id: P-AGH249PROJCOMP
kind: problem
title: Compositions of projective morphisms are projective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Morphisms
  - Segre Embedding
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.9, the projective-morphism definition, and the Segre embedding from I.2.14.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: problem
Show that a composition of projective morphisms is projective.
Conclude that projective morphisms have the stability properties (a)--(f) of (Ex. 4.8) above.

*Hint:* use the Segre embedding defined in (I, Ex. 2.14), and show that it gives a closed immersion $\PP^r \times \PP^s \injects \PP^{r + s + rs}$.
:::

::: {.solution}
<1>1. Let
\[
X\xrightarrow{f}Y\xrightarrow{g}Z
\]
be projective morphisms.  Choose factorizations
\[
X\xhookrightarrow{i}\mathbb P^r_Y\longrightarrow Y
\]
and
\[
Y\xhookrightarrow{j}\mathbb P^s_Z\longrightarrow Z
\]
with $i$ and $j$ closed immersions.
::: {.proof}
This is exactly the definition of a projective morphism.
:::

<1>2. There is a canonical identification
\[
\mathbb P^r_Y
\cong
\mathbb P^r_Z\times_ZY.
\]
Under this identification, the morphism
\[
\mathbb P^r_Y
\longrightarrow
\mathbb P^r_Z\times_Z\mathbb P^s_Z
\]
induced by $j$ is a closed immersion.
::: {.proof}
Relative projective space commutes with base change:
\[
\mathbb P^r_Y
=
\mathbb P^r_Z\times_ZY.
\]

The displayed morphism is the base change of the closed immersion
\[
j:Y\hookrightarrow\mathbb P^s_Z
\]
along the projection
\[
\mathbb P^r_Z\times_Z\mathbb P^s_Z
\longrightarrow
\mathbb P^s_Z.
\]
Closed immersions are stable under base change, so it is a closed immersion.
:::

<1>3. The composite
\[
X
\xhookrightarrow{i}
\mathbb P^r_Y
\hookrightarrow
\mathbb P^r_Z\times_Z\mathbb P^s_Z
\]
is a closed immersion.
::: {.proof}
Both arrows are closed immersions, and closed immersions are stable under composition.
:::

<1>4. The relative Segre morphism
\[
\operatorname{Seg}:
\mathbb P^r_Z\times_Z\mathbb P^s_Z
\longrightarrow
\mathbb P^{r+s+rs}_Z
\]
is a closed immersion.
::: {.proof}
Over $\Spec\mathbb Z$, the ordinary Segre embedding
\[
\mathbb P^r_\mathbb Z\times\mathbb P^s_\mathbb Z
\hookrightarrow
\mathbb P^{(r+1)(s+1)-1}_\mathbb Z
\]
is cut out by the $2\times2$ minors of the matrix of homogeneous coordinates, hence is a closed immersion.

Since
\[
(r+1)(s+1)-1=r+s+rs,
\]
base changing this closed immersion along $Z\to\Spec\mathbb Z$ gives the displayed relative Segre closed immersion.
:::

<1>5. The composite
\[
X\longrightarrow\mathbb P^{r+s+rs}_Z
\]
is a closed immersion.
::: {.proof}
Compose the closed immersion of <1>3 with the Segre closed immersion of <1>4.  A composition of closed immersions is a closed immersion.
:::

<1>6. Therefore
\[
\boxed{g\circ f:X\longrightarrow Z\text{ is projective}.}
\]
::: {.proof}
Step <1>5 gives a factorization
\[
X\hookrightarrow\mathbb P^{r+s+rs}_Z\longrightarrow Z
\]
with first arrow a closed immersion.  This is precisely the definition of projectivity.
:::

<1>7. Every closed immersion is projective.
::: {.proof}
If
\[
i:X\hookrightarrow Y
\]
is a closed immersion, use
\[
\mathbb P^0_Y\cong Y.
\]
Then
\[
X\xhookrightarrow{i}\mathbb P^0_Y\longrightarrow Y
\]
is a projective factorization.
Thus projective morphisms satisfy property (a) of Hartshorne II.4.8.
:::

<1>8. Projective morphisms are stable under arbitrary base extension.
::: {.proof}
Let
\[
f:X\to Y
\]
be projective, with factorization
\[
X\hookrightarrow\mathbb P^n_Y\to Y,
\]
and let $Y'\to Y$ be any morphism.

After base change,
\[
X\times_YY'
\hookrightarrow
\mathbb P^n_Y\times_YY'
\cong
\mathbb P^n_{Y'}
\longrightarrow
Y'.
\]
The first arrow remains a closed immersion.  Hence the base-changed morphism is projective.
Thus property (c) of II.4.8 holds.
:::

<1>9. Projective morphisms satisfy properties (a)--(c) of Hartshorne II.4.8.
::: {.proof}
Property (a) is <1>7, property (b) is the composition result <1>6, and property (c) is <1>8.
:::

<1>10. Consequently projective morphisms satisfy all six stability properties (a)--(f) of Hartshorne II.4.8.
::: {.proof}
Hartshorne II.4.8 proves formally that any class of morphisms satisfying (a)--(c) also satisfies:

- products preserve the property;
- if $g\circ f$ has the property and $g$ is separated, then $f$ has the property;
- passage to reductions preserves the property.

Applying that exercise to projective morphisms using <1>9 proves (d)--(f) as well.
:::

<1>11. Q.E.D.
::: {.proof}
Step <1>6 proves closure under composition, and <1>10 gives the requested stability package.
:::
:::
