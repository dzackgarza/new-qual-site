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

::: {.problem}
Let $f(z)$ be analytic in $\DD$ and assume $\abs{f(z)} \leq 1$ for all $z \in \DD$.

(a) Suppose that $f(z)$ has a zero of order $m$ at $z = 0$.
Show that $\abs{f(z)} \leq \abs{z}^m$.

(b) Suppose that $f(0) = \alpha$ and $f'(0) = 0$.
Show that, for $\abs{z} \leq \sqrt{\abs{\alpha}}$, $$\abs{f(z)} \geq \frac{\abs{\alpha} - \abs{z}^2}{1 + \abs{\alpha}\abs{z}^2}.$$
:::

::: {.solution}
For part (a), write
$$
f(z)=z^m g(z),
$$
where $g$ is holomorphic in $\DD$. Fix $0<r<1$. On $\abs{z}=r$,
$$
\abs{g(z)}=\frac{\abs{f(z)}}{r^m}\le \frac1{r^m}.
$$
By the maximum modulus principle, the same bound holds for $\abs{z}\le r$.
For a fixed $z\in\DD$, let $r\uparrow1$ to obtain $\abs{g(z)}\le1$.
Therefore
$$
\abs{f(z)}\le \abs{z}^m.
$$

For part (b), let
$$
\phi_\alpha(w)=\frac{w-\alpha}{1-\overline\alpha w}
$$
when $\abs{\alpha}<1$; the boundary case $\abs{\alpha}=1$ forces $f$ to be constant by
the maximum modulus principle and is immediate. Set
$$
h(z)=\phi_\alpha(f(z)).
$$
Then $h:\DD\to\DD$, $h(0)=0$, and $h'(0)=0$. Thus $h$ has a zero
of order at least $2$, so part (a) gives
$$
\abs{\frac{f(z)-\alpha}{1-\overline\alpha f(z)}}
\le \abs{z}^2.
$$
Put $\rho=\abs{z}^2$. By the triangle inequality,
$$
\abs{\alpha}-\abs{f(z)}
\le \abs{f(z)-\alpha}
\le \rho\,\abs{1-\overline\alpha f(z)}
\le \rho\bigl(1+\abs{\alpha}\,\abs{f(z)}\bigr).
$$
Hence
$$
\abs{f(z)}\bigl(1+\abs{\alpha}\rho\bigr)
\ge \abs{\alpha}-\rho.
$$
If $\abs{z}\le\sqrt{\abs{\alpha}}$, then $\rho\le\abs{\alpha}$, so the right-hand side is
nonnegative and
$$
\abs{f(z)}\ge
\frac{\abs{\alpha}-\abs{z}^2}{1+\abs{\alpha}\abs{z}^2}.
$$
:::
