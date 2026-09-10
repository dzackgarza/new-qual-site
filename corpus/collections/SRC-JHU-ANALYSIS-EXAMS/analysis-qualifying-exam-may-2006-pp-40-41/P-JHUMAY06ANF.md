---
schema: qual/card@1
id: P-JHUMAY06ANF
kind: problem
title: Poles and residues of $e^{\pi z}/(z^2+1)^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2006 problem 6 on PDF page 40; removed the subsequent Real Analysis instructions from this problem."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified noncancellation at both double poles and computed both derivative-formula residues, including the exponential and imaginary signs at minus i."
---

6. Find all the poles of the function

$$
f ( z ) = \frac { e ^ { \pi z } } { ( z ^ { 2 } + 1 ) ^ { 2 } } .
$$

Determine the residue of f at each pole.

::: solution
The only poles are $i$ and $-i$, both of order two, with
$$
\boxed{\operatorname{Res}_{i}f=\frac{\pi+i}{4},\qquad
\operatorname{Res}_{-i}f=\frac{\pi-i}{4}.}
$$

<1>1. Factoring the denominator identifies all poles and their orders.
::: proof
The denominator is $(z-i)^2(z+i)^2$, and the numerator
$e^{\pi z}$ is entire and never zero. Thus the quotient
is holomorphic away from $\pm i$, and at either point
the denominator has order two while the numerator is
nonzero. Both are genuine double poles; there are no
other finite poles.
:::

<1>2. Differentiate the holomorphic factors to compute the residues.
::: proof
For a double pole at $a$, the residue of $H(z)/(z-a)^2$
is $H'(a)$, by the Taylor expansion of the holomorphic
factor $H$ [@SS03]. At $i$, this gives
$$
\begin{aligned}
\operatorname{Res}_{i}f
&=\left.\frac{d}{dz}\frac{e^{\pi z}}{(z+i)^2}\right|_{z=i}\\
&=e^{\pi i}\left(\frac{\pi}{(2i)^2}-\frac{2}{(2i)^3}\right)
=\frac{\pi+i}{4}.
\end{aligned}
$$
At $-i$, the same calculation with the other factor yields
$$
\begin{aligned}
\operatorname{Res}_{-i}f
&=\left.\frac{d}{dz}\frac{e^{\pi z}}{(z-i)^2}\right|_{z=-i}\\
&=e^{-\pi i}\left(\frac{\pi}{(-2i)^2}-\frac{2}{(-2i)^3}\right)
=\frac{\pi-i}{4}.
\end{aligned}
$$
Here $e^{\pi i}=e^{-\pi i}=-1$, $(2i)^3=-8i$ and
$(-2i)^3=8i$. These are the residues at all the poles.
:::
:::
