---
schema: qual/card@1
id: P-JWOJ5
kind: problem
title: "The integral of the log of the chord length over the circle"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Mean Value Property
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: problem
a. 
Show (without using 3.8.9 in the S&S) that
\[
\int_0^{2\pi} \log\abs{1 - e^{i\theta}}~d\theta = 0
\]

b. 
Show that this identity is equivalent to S&S 3.8.9:
\[
\int_0^1 \log(\sin(\pi x)) ~dx = -\log 2
.\]
:::

::: solution
For $0<r<1$, the function
\[
z\longmapsto \log(1-rz)
\]
is holomorphic on the unit disk, using the branch determined by its power series at $0$. Its real part is
\[
\log|1-rz|.
\]
By the mean-value property for harmonic functions,
\[
\frac1{2\pi}\int_0^{2\pi}
\log|1-re^{i\theta}|\,d\theta
=\log|1|=0.
\]
Hence
\[
\int_0^{2\pi}
\log|1-re^{i\theta}|\,d\theta=0
\]
for every $0<r<1$.

Now let $r\uparrow1$. Pointwise for $0<\theta<2\pi$,
\[
\log|1-re^{i\theta}|
\longrightarrow
\log|1-e^{i\theta}|.
\]
To justify passing to the limit, restrict to $r\ge1/2$. Since
\[
|1-re^{i\theta}|^2
=(1-r)^2+4r\sin^2(\theta/2),
\]
the negative part near the endpoints is bounded by a constant multiple of
\[
1+|\log\theta|+|\log(2\pi-\theta)|,
\]
which is integrable, while the positive part is uniformly bounded because
\[
|1-re^{i\theta}|\le2.
\]
Dominated convergence therefore gives
\[
\boxed{
\int_0^{2\pi}
\log|1-e^{i\theta}|\,d\theta=0.}
\]

For part (b), use
\[
|1-e^{i\theta}|
=2\sin(\theta/2),
\qquad 0<\theta<2\pi.
\]
Thus part (a) is equivalent to
\[
0
=\int_0^{2\pi}
\left(\log2+\log\sin(\theta/2)\right)d\theta.
\]
With the substitution
\[
x=\frac{\theta}{2\pi},
\]
this becomes
\[
0
=2\pi\log2
+2\pi\int_0^1\log(\sin\pi x)\,dx.
\]
Hence
\[
\boxed{
\int_0^1\log(\sin\pi x)\,dx=-\log2.}
\]
Every step is reversible, so the two identities are equivalent.
:::
