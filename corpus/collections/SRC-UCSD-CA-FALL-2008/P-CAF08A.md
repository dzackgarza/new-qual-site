---
schema: qual/card@1
id: P-CAF08A
kind: problem
title: "Harnack inequality bound for a nonnegative harmonic function"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: problem
Let $u$ be a nonnegative real-valued harmonic function defined in $B(1; 2)$ with $u(1) = 1/3$.
Prove that $$u(i) \leq 1 + \frac{2}{3}\sqrt{2}.$$
:::

::: solution
Apply Harnack's inequality in the disk $B(1,2)$. If $|z-1|=r<2$, then
\[
u(z)\le \frac{2+r}{2-r}\,u(1).
\]
For $z=i$,
\[
r=|i-1|=\sqrt2.
\]
Hence
\[
u(i)
\le \frac{2+\sqrt2}{2-\sqrt2}\cdot\frac13.
\]
Since
\[
\frac{2+\sqrt2}{2-\sqrt2}=3+2\sqrt2,
\]
we obtain
\[
u(i)\le \frac{3+2\sqrt2}{3}
=1+\frac23\sqrt2,
\]
as required.
:::
