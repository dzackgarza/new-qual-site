---
schema: qual/card@1
id: P-BKF91-6
kind: problem
title: An $L^1$ bound on radial values of $f'$ controls $f$ on a radius
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Integrated Cauchy's formula for f' along the real radius and bounded the
    resulting logarithmic kernel uniformly in the circle angle.
---

::: {.problem}
Let $f$ be analytic in the unit disk $|z|<1$. Assume that there is a constant $M>0$ such that
\[
\int_0^{2\pi}|f'(re^{i\theta})|\,d\theta\le M
\qquad(0\le r<1).
\]
Prove that
\[
\int_0^1|f(x)|\,dx<\infty.
\]
:::

::: {.solution}
Fix $R$ with $0<R<1$ and put $g=f'$.

::: pf

::: {.pf-step #s1}

For $0\le x<R$,
$$
f(x)-f(0)
=
-\frac{R}{2\pi}
\int_0^{2\pi}
g(Re^{i\theta})e^{i\theta}
\log\left(1-\frac{x}{R}e^{-i\theta}\right)
\,d\theta.
$$

::: pf-proof

For $0\le t<R$, Cauchy's formula on the circle $\abs z=R$ gives
$$
g(t)
=
\frac1{2\pi}
\int_0^{2\pi}
g(Re^{i\theta})
\frac{Re^{i\theta}}{Re^{i\theta}-t}
\,d\theta.
$$
Integrate this identity in $t$ from $0$ to $x$. Since $x<R$, the integrand is continuous on the compact product of integration domains, so the order of integration may be exchanged. With $s=t/R$,
$$
\int_0^x\frac{Re^{i\theta}}{Re^{i\theta}-t}\,dt
=
R\int_0^{x/R}\frac{ds}{1-se^{-i\theta}}
=
-Re^{i\theta}\log\left(1-\frac{x}{R}e^{-i\theta}\right).
$$
For $0\le s<1$, the number $1-se^{-i\theta}$ has positive real part, so the logarithm can be taken on the principal branch throughout the integration path.

:::

:::

::: {.pf-step #s2}

There is an absolute constant $C$ such that, for every real $\theta$,
$$
\int_0^1\abs{\log(1-se^{-i\theta})}\,ds\le C.
$$

::: pf-proof

For $0\le s<1$,
$$
1-s\le\abs{1-se^{-i\theta}}\le1+s\le2,
$$
and the real part of $1-se^{-i\theta}$ is positive, so its principal argument has absolute value at most $\pi/2$. Hence
$$
\abs{\log(1-se^{-i\theta})}
\le
-\log(1-s)+\log2+\frac\pi2.
$$
The right-hand side is integrable on $[0,1)$; for example one may take
$$
C=1+\log2+\frac\pi2.
$$

:::

:::

::: {.pf-step #s3}

For every $0<R<1$,
$$
\int_0^R\abs{f(x)-f(0)}\,dx
\le
\frac{CM}{2\pi}.
$$

::: pf-proof

Taking absolute values in step [](#s1){.pf-ref}, integrating in $x$, and using Tonelli's theorem gives
$$
\begin{aligned}
\int_0^R\abs{f(x)-f(0)}\,dx
&\le
\frac{R}{2\pi}
\int_0^{2\pi}\abs{g(Re^{i\theta})}
\int_0^R
\abs{\log\left(1-\frac{x}{R}e^{-i\theta}\right)}
\,dx\,d\theta\\
&=\frac{R^2}{2\pi}
\int_0^{2\pi}\abs{g(Re^{i\theta})}
\int_0^1\abs{\log(1-se^{-i\theta})}\,ds\,d\theta\\
&\le
\frac{CR^2}{2\pi}
\int_0^{2\pi}\abs{f'(Re^{i\theta})}\,d\theta\\
&\le\frac{CM}{2\pi},
\end{aligned}
$$
using step [](#s2){.pf-ref} and the hypothesis.

:::

:::

::: {.pf-step #s4}

For every $0<R<1$,
$$
\int_0^R\abs{f(x)}\,dx
\le
\abs{f(0)}+\frac{CM}{2\pi}.
$$

::: pf-proof

The triangle inequality and step [](#s3){.pf-ref} give
$$
\int_0^R\abs{f(x)}\,dx
\le
R\abs{f(0)}
+\int_0^R\abs{f(x)-f(0)}\,dx
\le
\abs{f(0)}+\frac{CM}{2\pi}.
$$

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{\int_0^1\abs{f(x)}\,dx<\infty}.
$$

::: pf-proof

The integrals
$$
\int_0^R\abs{f(x)}\,dx
$$
increase as $R\uparrow1$ and are uniformly bounded by step [](#s4){.pf-ref}. Taking the limit $R\uparrow1$ proves the claim.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
