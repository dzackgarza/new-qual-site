---
schema: qual/card@1
id: P-CAF07B
kind: problem
title: "Schwarz lemma applications: modulus bound and lower bound near a zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Zeros of Holomorphic Functions
relations: []
review: draft
---

::: problem
Let $f(z)$ be analytic in $\mathbb{D}$ and assume $|f(z)| \leq 1$ for all $z \in \mathbb{D}$.

(a) Suppose that $f(z)$ has a zero of order $m$ at $z = 0$.
Show that $|f(z)| \leq |z|^m$.

(b) Suppose that $f(0) = \alpha$ and $f'(0) = 0$.
Show that, for $|z| \leq \sqrt{|\alpha|}$, $$|f(z)| \geq \frac{|\alpha| - |z|^2}{1 + |\alpha||z|^2}.$$
:::

::: solution
For part (a), write
\[
f(z)=z^m g(z),
\]
where $g$ is holomorphic in $\mathbb D$. Fix $0<r<1$. On $|z|=r$,
\[
|g(z)|=\frac{|f(z)|}{r^m}\le \frac1{r^m}.
\]
By the maximum modulus principle, the same bound holds for $|z|\le r$.
For a fixed $z\in\mathbb D$, let $r\uparrow1$ to obtain $|g(z)|\le1$.
Therefore
\[
|f(z)|\le |z|^m.
\]

For part (b), let
\[
\phi_\alpha(w)=\frac{w-\alpha}{1-\overline\alpha w}
\]
when $|\alpha|<1$; the boundary case $|\alpha|=1$ forces $f$ to be constant by
the maximum modulus principle and is immediate. Set
\[
h(z)=\phi_\alpha(f(z)).
\]
Then $h:\mathbb D\to\mathbb D$, $h(0)=0$, and $h'(0)=0$. Thus $h$ has a zero
of order at least $2$, so part (a) gives
\[
\left|\frac{f(z)-\alpha}{1-\overline\alpha f(z)}\right|
\le |z|^2.
\]
Put $\rho=|z|^2$. By the triangle inequality,
\[
|\alpha|-|f(z)|
\le |f(z)-\alpha|
\le \rho\,|1-\overline\alpha f(z)|
\le \rho\bigl(1+|\alpha|\,|f(z)|\bigr).
\]
Hence
\[
|f(z)|\bigl(1+|\alpha|\rho\bigr)
\ge |\alpha|-\rho.
\]
If $|z|\le\sqrt{|\alpha|}$, then $\rho\le|\alpha|$, so the right-hand side is
nonnegative and
\[
|f(z)|\ge
\frac{|\alpha|-|z|^2}{1+|\alpha||z|^2}.
\]
:::
