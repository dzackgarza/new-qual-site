---
schema: qual/card@1
id: E-W3QMS
kind: problem
title: Holomorphic functions with vanishing derivative are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Contour Integration
relations: []
review: draft
---

::: {.exercise}
- Do any example from [here](http://home.iitk.ac.in/~psraj/mth102/lecture_notes/comp8.pdf)

- Prove that no sequence of polynomials converges uniformly to $1/z$ on
  $S^1$.

- Anything from the [homeworks](https://www.notion.so/Complex-Analysis-3ca8032a73fc4366836a9f5085f5e601)

- Show that $f'=0 \implies f$ is constant using integrals and *primitives* (i.e. antiderivatives).

> See S&S Corollary 3.4.

- Suppose $f$ is continuously complex differentiable on $\Omega$, and $T$ is
  a triangle whose interior is contained in $\Omega$. Use Green's theorem to
  prove $\int_{\partial T}f(z)\,dz=0$.

- Show that for $0<a<1$,
  \[
  \int_{-\infty}^{\infty}{e^{ax}\over1+e^x}\,dx
  ={\pi\over\sin\pi a}.
  \]
:::

::: {.solution}
The bullets “Do any example from here” and “Anything from the homeworks” are
open-ended study prompts rather than propositions with unique answers. The
remaining finite tasks are as follows.

If $f'=0$ on a region $\Omega$, then for any $a,b\in\Omega$ choose a
piecewise $C^1$ path $\gamma$ from $a$ to $b$. Since $f$ is a primitive of
the zero function,
\[
f(b)-f(a)=\int_\gamma f'(z)\,dz=0.
\]
Thus $f$ is constant.

Suppose polynomials $p_n$ converged uniformly to $1/z$ on $S^1$. Then
$q_n(z)=zp_n(z)-1$ converges uniformly to $0$ on $S^1$. By the maximum
modulus principle,
\[
\sup_{|z|\le1}|q_n(z)|\le\sup_{|z|=1}|q_n(z)|\longrightarrow0.
\]
But $q_n(0)=-1$ for every $n$, a contradiction.

For the Green-theorem exercise, write $f=u+iv$. Then
\[
\int_{\partial T}f(z)\,dz
=\int_{\partial T}(u\,dx-v\,dy)
+i\int_{\partial T}(v\,dx+u\,dy).
\]
Green's theorem turns the real and imaginary parts into
\[
\iint_T(-v_x-u_y)\,dxdy,
\qquad
\iint_T(u_x-v_y)\,dxdy,
\]
respectively. Both vanish by the Cauchy--Riemann equations, proving the
contour integral is zero.

Finally, with $t=e^x$,
\[
\int_{-\infty}^{\infty}{e^{ax}\over1+e^x}\,dx
=\int_0^\infty {t^{a-1}\over1+t}\,dt.
\]
For $0<a<1$, Euler's beta integral gives
\[
\int_0^\infty {t^{a-1}\over1+t}\,dt
=B(a,1-a)=\Gamma(a)\Gamma(1-a)
={\pi\over\sin\pi a},
\]
by Euler's reflection formula.
:::
