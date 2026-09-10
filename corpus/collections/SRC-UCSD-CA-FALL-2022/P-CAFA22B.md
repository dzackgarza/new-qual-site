---
schema: qual/card@1
id: P-CAFA22B
kind: problem
title: "Zero of e^{tz} + z + 1 in the left half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $0 \leq t < 1$.
Show that $f(z) = e^{tz} + z + 1$ has exactly one zero (counting multiplicities) in the left half-plane $\{z : \operatorname{Re} z < 0\}$.

Hint: Consider first $|z| < \varepsilon$ for $\varepsilon > 0$.
:::

::: remark
The official Fall 2022 source states only $t<1$. That is false for negative
$t$: for $t\ne0$, the equation is equivalent to
\[
-t(z+1)=W_k(te^{-t}),
\]
and for negative $t$ infinitely many branches give zeros in the left
half-plane. The hypothesis above records the intended nonnegative range.
:::

::: solution
Fix $\varepsilon>0$ small enough that
\[
e^{t\varepsilon}<1+\varepsilon.
\]
Such an $\varepsilon$ exists because $t<1$ and both sides equal $1$ at
$\varepsilon=0$, while their derivatives there are $t$ and $1$.

Consider the half-plane $\operatorname{Re}z<\varepsilon$. On its boundary
$z=\varepsilon+iy$,
\[
|e^{tz}|=e^{t\varepsilon}<1+\varepsilon\le|z+1|.
\]
Since $t\ge0$, the exponential is bounded by $e^{t\varepsilon}$ throughout
that half-plane. On a sufficiently large left semicircle closing the boundary,
$|z+1|$ is therefore larger than $|e^{tz}|$ as well. Rouché's theorem on the
resulting half-disk shows that
\[
e^{tz}+z+1
\]
and $z+1$ have the same number of zeros in
$\operatorname{Re}z<\varepsilon$, namely one, counting multiplicity.

It remains to show that this zero is actually in the left half-plane. If
$z=iy$ lies on the imaginary axis and is a zero, then
\[
|1+iy|=|e^{ity}|=1,
\]
which forces $y=0$; but $f(0)=2$. Hence there are no zeros on the imaginary
axis. Since the unique zero in $\operatorname{Re}z<\varepsilon$ cannot lie in
$0\le\operatorname{Re}z<\varepsilon$ for all sufficiently small
$\varepsilon$, it lies in $\operatorname{Re}z<0$. Thus there is exactly one
left-half-plane zero, counted with multiplicity.
:::
