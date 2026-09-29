---
schema: qual/card@1
id: P-BKF80-7
kind: problem
title: Fourier-series solution of $f''+kf=g$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $g$ be $2\pi$-periodic and continuous on $[-\pi,\pi]$, with Fourier series
$$
\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nx+b_n\sin nx).
$$
Let $f$ be $2\pi$-periodic and satisfy
$$
f''(x)+k f(x)=g(x),
$$
where $k\ne n^2$ for $n=1,2,3,\ldots$. Find the Fourier series of $f$ and prove that it converges everywhere.
:::

::: {.solution}
Write the Fourier coefficients of $f$ as
$$
\frac{A_0}{2}+\sum_{n=1}^\infty(A_n\cos nx+B_n\sin nx).
$$

::: pf

::: {.pf-step #coefficient-relations}
The Fourier coefficients satisfy
$$
kA_0=a_0,
\qquad
(k-n^2)A_n=a_n,
\qquad
(k-n^2)B_n=b_n
$$
for every $n\geq1$.

::: pf-proof
Since $f''=g-kf$ is continuous and $f$ is periodic, $f$ is $C^2$ and $f'$ is also $2\pi$-periodic. Integrating the differential equation over $[-\pi,\pi]$ gives
$$
\int_{-\pi}^{\pi}f''(x)\,dx=0,
$$
so comparison of the constant Fourier coefficients gives $kA_0=a_0$.

For $n\geq1$, two integrations by parts, using periodicity of $f$ and $f'$, give
$$
\frac1\pi\int_{-\pi}^{\pi}f''(x)\cos(nx)\,dx=-n^2A_n
$$
and
$$
\frac1\pi\int_{-\pi}^{\pi}f''(x)\sin(nx)\,dx=-n^2B_n.
$$
Taking the cosine and sine Fourier coefficients of $f''+kf=g$ therefore yields
$$
(k-n^2)A_n=a_n,
\qquad
(k-n^2)B_n=b_n.
$$
:::

:::

::: {.pf-step #fourier-series-formula}
If $k\neq0$, the Fourier series of $f$ is
$$
\boxed{
\frac{a_0}{2k}
+\sum_{n=1}^\infty
\frac{a_n\cos(nx)+b_n\sin(nx)}{k-n^2}
}.
$$
If $k=0$, necessarily $a_0=0$, and the Fourier series is
$$
\boxed{
c-\sum_{n=1}^\infty
\frac{a_n\cos(nx)+b_n\sin(nx)}{n^2}
},
\qquad
c\coloneqq\frac1{2\pi}\int_{-\pi}^{\pi}f(x)\,dx.
$$

::: pf-proof
The hypothesis $k\neq n^2$ for $n\geq1$ makes every nonconstant denominator in step [](#coefficient-relations){.pf-ref} nonzero. Thus
$$
A_n=\frac{a_n}{k-n^2},
\qquad
B_n=\frac{b_n}{k-n^2}.
$$
If $k\neq0$, step [](#coefficient-relations){.pf-ref} also gives $A_0=a_0/k$, which yields the first displayed series.

If $k=0$, the constant relation in step [](#coefficient-relations){.pf-ref} gives $a_0=0$, while $A_0$ is not determined by the differential equation. Since the constant term in the Fourier series is the mean of $f$, one has $A_0/2=c$, giving the second displayed series.
:::

:::

::: {.pf-step #uniform-convergence-series}
In either case, the displayed Fourier series converges absolutely and uniformly on $\RR$.

::: pf-proof
Let $M=\max_{[-\pi,\pi]}\abs g$. The Fourier coefficients of $g$ satisfy
$$
\abs{a_n}\leq2M,
\qquad
\abs{b_n}\leq2M.
$$
For all sufficiently large $n$,
$$
\abs{k-n^2}\geq\frac{n^2}{2}.
$$
Hence, when $k\neq0$,
$$
\frac{\abs{a_n}+\abs{b_n}}{\abs{k-n^2}}
\leq\frac{8M}{n^2}
$$
for all sufficiently large $n$. When $k=0$, the corresponding bound is
$$
\frac{\abs{a_n}+\abs{b_n}}{n^2}\leq\frac{4M}{n^2}.
$$
Since $\sum n^{-2}$ converges and $\abs{\sin(nx)},\abs{\cos(nx)}\leq1$, the Weierstrass $M$-test gives absolute and uniform convergence.
:::

:::

::: {.pf-step #converges-to-f}
The Fourier series converges everywhere to $f$.

::: pf-proof
Let $F$ denote the uniform sum from step [](#uniform-convergence-series){.pf-ref}. Uniform convergence permits termwise integration against $1$, $\cos(nx)$, and $\sin(nx)$, so $F$ has the Fourier coefficients displayed in step [](#fourier-series-formula){.pf-ref}. These are exactly the Fourier coefficients $A_n,B_n$ of $f$ from step [](#coefficient-relations){.pf-ref}. Thus the continuous periodic function $h=f-F$ has every Fourier coefficient equal to zero.

By Fejér's theorem, the Cesàro means of the Fourier series of a continuous periodic function converge uniformly to that function. Every Cesàro mean of the Fourier series of $h$ is identically zero, so $h=0$. Hence $F=f$ everywhere.
:::

:::

::: pf-qed
Step [](#fourier-series-formula){.pf-ref} gives the Fourier series, and steps [](#uniform-convergence-series){.pf-ref} and [](#converges-to-f){.pf-ref} prove its everywhere convergence to $f$.
:::

:::
:::
