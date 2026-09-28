---
schema: qual/card@1
id: P-BERK86S-11
kind: problem
title: An orthonormal rational family on the real line
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Simplified f_m conjugate(f_n) to the Cauchy weight times a power of the
    Cayley factor (x-i)/(x+i). The substitution x=cot(theta/2) turns the
    integral into ordinary Fourier orthogonality on [0,2pi].
---

::: {.problem}
For $n\in\mathbb Z$, define
\[
f_n(x)=\frac{(x-i)^n}{\sqrt\pi\,(x+i)^{n+1}},
\qquad x\in\mathbb R.
\]
Prove that the functions $f_n$ are orthonormal:
\[
\int_{-\infty}^{\infty}f_m(x)\overline{f_n(x)}\,dx
=
\begin{cases}
1,&m=n,\\
0,&m\ne n.
\end{cases}
\]
:::

::: {.solution}
<1>1. For real $x$ and every $n\in\ZZ$,
$$
\overline{f_n(x)}
=
\frac{(x+i)^n}{\sqrt\pi\,(x-i)^{n+1}}.
$$

::: {.proof}
For real $x$,
$$
\overline{x-i}=x+i,
\qquad
\overline{x+i}=x-i.
$$
Complex conjugation commutes with every integer power because
$x\pm i\neq0$. Applying conjugation to the definition of $f_n$ gives the
formula.
:::

<1>2. For all $m,n\in\ZZ$,
$$
f_m(x)\overline{f_n(x)}
=
\frac{1}{\pi(1+x^2)}
\left(\frac{x-i}{x+i}\right)^{m-n}.
$$

::: {.proof}
Using step <1>1,
$$
\begin{aligned}
f_m(x)\overline{f_n(x)}
&=
\frac1\pi
\frac{(x-i)^m(x+i)^n}
{(x+i)^{m+1}(x-i)^{n+1}}\\
&=
\frac1\pi
\left(\frac{x-i}{x+i}\right)^{m-n}
\frac1{(x-i)(x+i)}\\
&=
\frac{1}{\pi(1+x^2)}
\left(\frac{x-i}{x+i}\right)^{m-n}.
\end{aligned}
$$
:::

<1>3. Under the substitution
$$
x=\cot\frac{\theta}{2},
\qquad
0<\theta<2\pi,
$$
one has
$$
\frac{x-i}{x+i}=e^{-i\theta}
$$
and
$$
\frac{dx}{1+x^2}=-\frac12\,d\theta.
$$

::: {.proof}
Writing $t=\theta/2$,
$$
\frac{\cot t-i}{\cot t+i}
=
\frac{\cos t-i\sin t}{\cos t+i\sin t}
=
\frac{e^{-it}}{e^{it}}
=
e^{-2it}
=
e^{-i\theta}.
$$
Also,
$$
dx
=
-\frac12\csc^2\frac{\theta}{2}\,d\theta,
$$
while
$$
1+x^2
=
1+\cot^2\frac{\theta}{2}
=
\csc^2\frac{\theta}{2}.
$$
Dividing gives the second formula.
:::

<1>4. For every $m,n\in\ZZ$,
$$
\int_{-\infty}^{\infty}
f_m(x)\overline{f_n(x)}\,dx
=
\frac1{2\pi}
\int_0^{2\pi}e^{-i(m-n)\theta}\,d\theta.
$$

::: {.proof}
By step <1>2, the absolute value of the integrand is
$$
\frac1{\pi(1+x^2)},
$$
because
$$
\abs{\frac{x-i}{x+i}}=1
$$
for real $x$. Thus the integral is absolutely convergent.

As $\theta$ increases from $0$ to $2\pi$,
$$
\cot\frac{\theta}{2}
$$
decreases from $+\infty$ to $-\infty$. Applying step <1>3 and reversing
the limits gives
$$
\begin{aligned}
\int_{-\infty}^{\infty}
f_m(x)\overline{f_n(x)}\,dx
&=
\frac1\pi
\int_{2\pi}^{0}
e^{-i(m-n)\theta}
\left(-\frac12\right)d\theta\\
&=
\frac1{2\pi}
\int_0^{2\pi}e^{-i(m-n)\theta}\,d\theta.
\end{aligned}
$$
:::

<1>5. The integral in step <1>4 equals
$$
\boxed{
\begin{cases}
1,&m=n,\\
0,&m\neq n.
\end{cases}
}
$$

::: {.proof}
If $m=n$, the integrand in step <1>4 is $1$, so the normalized integral
equals $1$.

If $m\neq n$, set $r=m-n\in\ZZ\setminus\{0\}$. Then
$$
\int_0^{2\pi}e^{-ir\theta}\,d\theta
=
\left[
\frac{e^{-ir\theta}}{-ir}
\right]_0^{2\pi}
=
0
$$
because $e^{-2\pi ir}=1$.
:::

<1>6. Therefore the family $(f_n)_{n\in\ZZ}$ is orthonormal.

::: {.proof}
Step <1>5 is exactly the stated orthonormality relation.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves the claim.
:::
:::
