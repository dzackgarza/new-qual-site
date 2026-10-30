---
schema: qual/card@1
id: P-UCLARA17S-10
kind: problem
title: Harmonic functions modulo real parts of analytic functions on a punctured plane
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $a_1,\dots,a_n$ be $n\ge1$ distinct points in $\CC$ and let
$$
\Omega=\CC\setminus\{a_1,\dots,a_n\}.
$$
Let $H(\Omega)$ be the vector space of real-valued harmonic functions on $\Omega$ and let $R(\Omega)\subset H(\Omega)$ be the space of real parts of analytic functions on $\Omega$. Prove that the quotient space
$$
H(\Omega)/R(\Omega)
$$
has dimension $n$, find a basis for this space, and prove it is a basis.
:::

::: {.solution}

For $u\in H(\Omega)$, define
$$
g_u(z)\coloneqq u_x(z)-i u_y(z).
$$

::: pf

::: pf-step

The function $g_u$ is holomorphic on $\Omega$.


::: pf-proof

Since $u$ is harmonic, $u_{xx}+u_{yy}=0$. Writing
$$
g_u=u_x-i u_y,
$$
the Cauchy--Riemann equations for $g_u$ are
$$
(u_x)_x=(-u_y)_y,
\qquad
(u_x)_y=-(-u_y)_x,
$$
which are respectively harmonicity of $u$ and equality of mixed partial derivatives. Thus $g_u$ is holomorphic.

:::

:::

::: {.pf-step #s1-2}

A harmonic function $u$ belongs to $R(\Omega)$ if and only if the holomorphic differential
$$
g_u(z)\,dz
$$
has zero integral around every closed curve in $\Omega$.


::: pf-proof

If $u=\operatorname{Re}F$ for an analytic function $F$, the Cauchy--Riemann equations give
$$
F'=u_x-i u_y=g_u,
$$
so $g_u$ has the primitive $F$ and all closed-curve integrals vanish.

Conversely, if all closed-curve integrals of $g_u$ vanish, then $g_u$ has a holomorphic primitive $F$ on $\Omega$. Since
$$
F'=g_u=u_x-i u_y,
$$
the gradients of $u$ and $\operatorname{Re}F$ agree. The domain $\Omega$ is connected, so their difference is constant. A real constant is itself the real part of a constant analytic function, hence $u\in R(\Omega)$.

:::

:::

::: {.pf-step #s1-3}

Let $\gamma_j$ be a positively oriented small circle about $a_j$ containing no other puncture, and define
$$
c_j(u)\coloneqq\frac1{2\pi i}\int_{\gamma_j}g_u(z)\,dz.
$$
Then $c_j(u)\in\RR$.


::: pf-proof

Along any closed piecewise smooth curve $z=x+iy$,
$$
\begin{aligned}
g_u(z)\,dz
&=(u_x-i u_y)(dx+i\,dy)\\
&=du+i(u_x\,dy-u_y\,dx).
\end{aligned}
$$
The integral of $du$ around a closed curve is $0$, so the integral of $g_u\,dz$ is purely imaginary. Therefore division by $2\pi i$ gives a real number.

:::

:::

::: {.pf-step #s1-4}

For each $j$, the function
$$
\ell_j(z)\coloneqq\log\abs{z-a_j}
$$
belongs to $H(\Omega)$ and satisfies
$$
g_{\ell_j}(z)=\frac1{z-a_j}.
$$


::: pf-proof

The function $\log\abs{z-a_j}$ is harmonic away from $a_j$. A direct differentiation gives
$$
(\ell_j)_x-i(\ell_j)_y
=\frac1{z-a_j}.
$$

:::

:::

::: {.pf-step #s1-5}

For every $u\in H(\Omega)$, the harmonic function
$$
v\coloneqq u-\sum_{j=1}^n c_j(u)\ell_j
$$
belongs to $R(\Omega)$.


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
g_v(z)
=g_u(z)-\sum_{j=1}^n\frac{c_j(u)}{z-a_j}.
$$
For each $k$,
$$
\int_{\gamma_k}g_v(z)\,dz
=2\pi i\,c_k(u)-2\pi i\,c_k(u)=0.
$$
Now let $\gamma$ be any closed curve in $\Omega$. The residue theorem gives
$$
\int_\gamma g_v(z)\,dz
=2\pi i\sum_{j=1}^n
\operatorname{Ind}(\gamma,a_j)
\operatorname{Res}_{a_j}(g_v).
$$
The vanishing integrals around the small circles imply that every residue $\operatorname{Res}_{a_j}(g_v)$ is $0$. Hence every closed-curve integral of $g_v$ vanishes. Step [](#s1-2){.pf-ref} therefore gives $v\in R(\Omega)$.

:::

:::

::: {.pf-step #s1-6}

The classes
$$
\boxed{[\ell_1],\ldots,[\ell_n]}
$$
span $H(\Omega)/R(\Omega)$.


::: pf-proof

Step [](#s1-5){.pf-ref} gives
$$
u-\sum_{j=1}^n c_j(u)\ell_j\in R(\Omega),
$$
so in the quotient
$$
[u]=\sum_{j=1}^n c_j(u)[\ell_j].
$$

:::

:::

::: {.pf-step #s1-7}

The classes $[\ell_1],\ldots,[\ell_n]$ are linearly independent.


::: pf-proof

Suppose
$$
\sum_{j=1}^n d_j\ell_j\in R(\Omega)
$$
for real scalars $d_j$. By step [](#s1-2){.pf-ref}, the corresponding holomorphic differential has zero period around every $\gamma_k$. By step [](#s1-4){.pf-ref},
$$
0
=\int_{\gamma_k}\sum_{j=1}^n\frac{d_j}{z-a_j}\,dz
=2\pi i\,d_k.
$$
Thus $d_k=0$ for every $k$.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{\dim_{\RR}H(\Omega)/R(\Omega)=n},
$$
with basis
$$
\boxed{[\log\abs{z-a_1}],\ldots,[\log\abs{z-a_n}]}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} proves spanning and step [](#s1-7){.pf-ref} proves linear independence.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required dimension and basis statement.

:::

:::

:::
