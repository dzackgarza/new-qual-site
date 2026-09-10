---
schema: qual/card@1
id: P-CAFA20B
kind: problem
title: "Unique real solution of a + z - e^{2z} = 0 in the left half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $a \in \mathbb{R}$ and $a > 2$.
Consider the equation $$(1)\quad a + z - e^{2z} = 0.$$

(a) Prove that if $z_0 \in \{\operatorname{Re}(z) < 0\}$ is a solution of (1), then $|z_0 + a| < 1$.

(b) Prove the equation (1) has exactly one solution on the left half plane $\{\operatorname{Re}(z) < 0\}$.
Furthermore, prove that this solution must be a real number.
:::

::: solution
If $z_0$ is a solution with $\operatorname{Re}z_0<0$, then
\[
z_0+a=e^{2z_0},
\]
so
\[
|z_0+a|=e^{2\operatorname{Re}z_0}<1.
\]
This proves (a).

For (b), on the circle $|z+a|=1$ we have
\[
|e^{2z}|=e^{2\operatorname{Re}z}
\le e^{2(1-a)}<1=|z+a|,
\]
because $a>2$. By Rouché's theorem, $z+a-e^{2z}$ and $z+a$ have the same
number of zeros in $|z+a|<1$, namely one. Part (a) shows that every zero in
the left half-plane lies in this disk. Conversely the disk lies in the left
half-plane because $\operatorname{Re}z<-a+1<0$. Hence there is exactly one
left-half-plane zero.

The coefficients are real in the sense that
\[
\overline{a+z-e^{2z}}=a+\bar z-e^{2\bar z}.
\]
Thus the conjugate of any zero is again a zero. The unique left-half-plane
zero must therefore equal its conjugate, so it is real.
:::
