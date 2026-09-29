---
schema: qual/card@1
id: P-BKS12-3B
kind: problem
title: Contour integral of $z^4/(z^5-z-1)$ over $|z|=2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2012 solution PDF and independently reviewed the residue-at-infinity computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked by Rouche that all five denominator zeros lie inside |z|=2 and computed the residue at infinity from the Laurent expansion.
---

::: {.problem}
Compute

$$
\int _ { C } { \frac { z ^ { 4 } } { z ^ { 5 } - z - 1 } } d z ,
$$

where C is a circle of radius 2 around the origin.
:::

::: {.solution}
Set
$$
F(z)\coloneqq\frac{z^4}{z^5-z-1}.
$$
Take $C$ with the standard positive, counterclockwise orientation.

::: pf

::: {.pf-step #zeros-inside}
Every zero of
$$
z^5-z-1
$$
lies in the disk
$$
\abs{z}<2,
$$
counted with multiplicity.

::: pf-proof
On $\abs{z}=2$,
$$
\abs{z^5}=32,
$$
while
$$
\abs{z+1}
\leq
\abs{z}+1
=
3.
$$
Thus
$$
\abs{z+1}<\abs{z^5}
$$
on the contour. By Rouché's theorem, $z^5-z-1$ and $z^5$ have the same
number of zeros in $\abs{z}<2$, namely five counted with multiplicity.
Since the denominator has degree five, these are all its zeros.
:::

:::

::: {.pf-step #residue-at-infinity}
The residue of $F$ at infinity is
$$
\operatorname{Res}_{z=\infty}F(z)=-1.
$$

::: pf-proof
For large $z$,
$$
\begin{aligned}
F(z)
&=
\frac1z
\frac{1}{1-z^{-4}-z^{-5}}\\
&=
\frac1z
\left(
1+O(z^{-4})
\right)\\
&=
\frac1z+O(z^{-5}).
\end{aligned}
$$
The residue at infinity is the negative of the coefficient of $z^{-1}$ in
the Laurent expansion at infinity. Hence it is $-1$.
:::

:::

::: {.pf-step #finite-residue-sum}
The sum of all finite residues of $F$ is $1$.

::: pf-proof
For a rational function,
$$
\sum_{\text{finite }a}\operatorname{Res}_{z=a}F
+
\operatorname{Res}_{z=\infty}F
=
0.
$$
Step [](#residue-at-infinity){.pf-ref} therefore gives the finite-residue sum as $1$.
:::

:::

::: {.pf-step #contour-value}
The contour integral is
$$
\boxed{
\int_C\frac{z^4}{z^5-z-1}\,dz
=
2\pi i
}.
$$

::: pf-proof
By step [](#zeros-inside){.pf-ref}, $C$ encloses every finite pole of $F$. The residue theorem
and step [](#finite-residue-sum){.pf-ref} therefore give
$$
\int_CF(z)\,dz
=
2\pi i
\sum_{\text{finite }a}
\operatorname{Res}_{z=a}F
=
2\pi i.
$$
:::

:::

::: pf-qed
Step [](#contour-value){.pf-ref} is the required value.
:::

:::

:::
