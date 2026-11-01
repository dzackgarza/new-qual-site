---
schema: qual/card@1
id: E-SS7.EX-6
kind: problem
title: A vertical contour integral for the step function
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 6, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise; nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All three cases. $a=1$ is computed directly as $\arctan(N/c)/\pi$; $a>1$ closes the contour to
    the left around the simple pole at $0$ with residue $1$; $0\le a<1$ closes it to the right, where
    the integrand is holomorphic. The side contributions are estimated explicitly. Nothing is left in
    outline.
---

::: {.exercise}
Show that for every $c>0$,
$$
\lim_{N\to\infty}\frac{1}{2\pi i}\int_{c-iN}^{c+iN}\frac{a^s}{s}\,ds
=\begin{cases}
1,&a>1,\\
\frac12,&a=1,\\
0,&0\leq a<1.
\end{cases}
$$
The integral follows the vertical segment from $c-iN$ to $c+iN$.
:::

::: {.solution}

Fix $c>0$ and $N>0$, and put
$$
I_N(a)=\frac{1}{2\pi i}\int_{c-iN}^{c+iN}\frac{a^{s}}{s}\,ds,
$$
where $a^{s}=e^{s\log a}$ and the segment is traversed upwards.

::: pf

::: {.pf-step #s1}

For $a=1$, $I_N(1)=\dfrac{1}{\pi}\arctan\dfrac{N}{c}\to\dfrac12$.

::: pf-proof

Here $a^{s}=1$. Parametrizing $s=c+iy$ with $-N\le y\le N$, $ds=i\,dy$, so
$$
I_N(1)=\frac{1}{2\pi i}\int_{-N}^{N}\frac{i\,dy}{c+iy}=\frac{1}{2\pi}\Bigl[\log(c+iy)\Bigr]_{-N}^{N}=\frac{1}{2\pi}\cdot2i\arctan\frac{N}{c}\cdot\frac{1}{i}=\frac{1}{\pi}\arctan\frac{N}{c},
$$
using $\arg(c+iN)=-\arg(c-iN)=\arctan(N/c)$. Since $\arctan t\to\pi/2$ as $t\to+\infty$, the limit is $1/2$.

:::

:::

::: {.pf-step #s2}

For $a>1$, $I_N(a)\to1$.

::: pf-proof

Write $a^{s}=e^{bs}$ with $b=\log a>0$. The function $s\mapsto e^{bs}/s$ is holomorphic away from $s=0$, where it has a simple pole with residue $e^{0}=1$.

Fix $N$ and $R>0$, and let $\Gamma_R$ be the boundary of the rectangle $[-R,c]\times[-N,N]$ traversed counterclockwise; the pole $0$ lies inside it and the segment from $c-iN$ to $c+iN$ is its right side. The residue theorem gives
$$
1=\frac{1}{2\pi i}\oint_{\Gamma_R}\frac{e^{bs}}{s}\,ds=I_N(a)+T_{R,N}+B_{R,N}+L_{R,N},
$$
with $T_{R,N},B_{R,N}$ the horizontal sides and $L_{R,N}$ the left side $s=-R+iy$, $\abs{y}\le N$.

On the horizontal sides $s=x\pm iN$ with $-R\le x\le c$, so $\abs{s}\ge N$ and
$$
\abs{T_{R,N}},\ \abs{B_{R,N}}\le\frac{1}{2\pi N}\int_{-R}^{c}e^{bx}\,dx\le\frac{e^{bc}}{2\pi bN},
$$
an estimate independent of $R$. On the left side $\abs{e^{bs}}=e^{-bR}$ and $\abs{s}\ge R$, so
$$
\abs{L_{R,N}}\le\frac{2N}{2\pi R}e^{-bR}\longrightarrow0\qquad(R\to\infty).
$$
Letting $R\to\infty$ at fixed $N$ therefore leaves $\abs{I_N(a)-1}\le\frac{e^{bc}}{\pi bN}$, which tends to $0$ as $N\to\infty$. Hence $I_N(a)\to1$.

:::

:::

::: {.pf-step #s3}

For $0\le a<1$, $I_N(a)\to0$.

::: pf-proof

For $a=0$ the integrand vanishes identically, so $I_N(0)=0$. Let $0<a<1$ and write $b=\log a<0$.

The function $s\mapsto e^{bs}/s$ is holomorphic on the closed rectangle $[c,N]\times[-N,N]$ (its only singularity is $s=0$, and $\operatorname{Re}s\ge c>0$ there), so by Cauchy's theorem
$$
0=I_N(a)+T_N+B_N+E_N,
$$
with $T_N,B_N$ the horizontal sides and $E_N$ the right side $s=N+iy$, $\abs{y}\le N$.

On the right side $\abs{e^{bs}}=e^{bN}$ and $\abs{s}\ge N$, so
$$
\abs{E_N}\le\frac{2N\,e^{bN}}{2\pi N}=\frac{e^{bN}}{\pi}\longrightarrow0
$$
because $b<0$. On the top side $s=x+iN$ with $c\le x\le N$, so $\abs{s}\ge N$ and
$$
\abs{T_N}\le\frac{1}{2\pi N}\int_c^{N}e^{bx}\,dx=\frac{e^{bN}-e^{bc}}{2\pi N b}=\frac{e^{bc}-e^{bN}}{2\pi N\abs{b}}\le\frac{e^{bc}}{2\pi N\abs{b}}\longrightarrow0,
$$
and the same bound holds for $B_N$. Hence $I_N(a)\to0$.

:::

:::

:::

:::
