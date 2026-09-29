---
schema: qual/card@1
id: P-BKS83-3
kind: problem
title: Modulus of an annulus mapped between two circle boundaries
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-corrected
  by: chatgpt
  date: 2026-09-24
  note: Removed the incorrect tangent-circle characterization from the title; the retained source circles are disjoint nested circles.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the Möbius-invariant inversive distances of both boundary pairs and the admissible root of the resulting quadratic.
---

::: {.problem}
A fractional linear transformation maps the annulus
\[
r<|z|<1,
\qquad r>0,
\]
onto the domain bounded by the circles
\[
\left|z-\frac14\right|=\frac14
\qquad\text{and}\qquad
|z|=1.
\]
Find $r$.
:::

::: {.solution}
For two disjoint circles with center distance $d$ and radii $R_1,R_2$,
write
$$
\mathcal I
\coloneqq
\frac{\left|d^2-R_1^2-R_2^2\right|}{2R_1R_2}
$$
for their absolute inversive distance.

::: pf

::: {.pf-step #inversive-distance-invariant}
The quantity $\mathcal I$ is invariant under fractional linear
transformations.

::: pf-proof
This is the standard inversive-distance invariant of generalized circles:
Möbius transformations preserve the inversive distance of any two circles
or lines. In particular, if a fractional linear transformation carries one
pair of disjoint circles to another pair, their absolute inversive
distances are equal.
:::

:::

::: {.pf-step #source-inversive-distance}
The two boundary circles of the source annulus
$$
r<|z|<1
$$
have inversive distance
$$
\mathcal I_{\mathrm{src}}
=
\frac{1+r^2}{2r}.
$$

::: pf-proof
The circles are concentric, so their center distance is $d=0$, and their
radii are $1$ and $r$. Hence
$$
\mathcal I_{\mathrm{src}}
=
\frac{|0-1-r^2|}{2r}
=
\frac{1+r^2}{2r}.
$$
:::

:::

::: {.pf-step #target-inversive-distance}
The two boundary circles of the target domain have inversive
distance
$$
\mathcal I_{\mathrm{tgt}}=2.
$$

::: pf-proof
The circles
$$
|z|=1
\qquad\text{and}\qquad
\left|z-\frac14\right|=\frac14
$$
have center distance $d=1/4$ and radii $1$ and $1/4$. Therefore
$$
\begin{aligned}
\mathcal I_{\mathrm{tgt}}
&=
\frac{
\left|
\frac1{16}-1-\frac1{16}
\right|
}{
2\cdot1\cdot\frac14
}\\
&=
\frac1{1/2}
=2.
\end{aligned}
$$
:::

:::

::: {.pf-step #quadratic-for-r}
The radius $r$ satisfies
$$
r^2-4r+1=0.
$$

::: pf-proof
By hypothesis, a fractional linear transformation maps the two source
boundary circles to the two target boundary circles, possibly interchanging
them. Step [](#inversive-distance-invariant){.pf-ref} therefore gives
$$
\mathcal I_{\mathrm{src}}
=
\mathcal I_{\mathrm{tgt}}.
$$
Using steps [](#source-inversive-distance){.pf-ref} and [](#target-inversive-distance){.pf-ref},
$$
\frac{1+r^2}{2r}=2.
$$
Since $r>0$, multiplying by $2r$ gives
$$
r^2-4r+1=0.
$$
:::

:::

::: {.pf-step #r-value-boxed}
Hence
$$
\boxed{r=2-\sqrt3}.
$$

::: pf-proof
The roots of the quadratic in step [](#quadratic-for-r){.pf-ref} are
$$
r=2\pm\sqrt3.
$$
For the annulus $r<|z|<1$ to be nonempty one must have
$$
0<r<1.
$$
The root $2+\sqrt3$ is greater than $1$, whereas
$2-\sqrt3$ lies in $(0,1)$. Thus the only admissible value is
$$
r=2-\sqrt3.
$$
:::

:::

::: pf-qed
Step [](#r-value-boxed){.pf-ref} gives the required value of the inner radius.
:::

:::
:::
