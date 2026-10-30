---
schema: qual/card@1
id: P-TRIV-DE47
kind: problem
title: Heat equation on a rod with fixed end temperatures
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 47, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider a metal rod of length $L$. One end is kept at temperature $0$, and the other at temperature $T_0$. Find the temperature $T(x, t)$, knowing that $T(x, 0) = 0$.
:::

::: {.solution}

Let the rod occupy $0<x<L$, take
$$
T(0,t)=0,
\qquad
T(L,t)=T_0,
$$
and write the heat equation as $T_t=\kappa T_{xx}$.

::: pf

::: {.pf-step #s1-1}

The stationary temperature profile is
$$
S(x)=\frac{T_0x}{L}.
$$


::: pf-proof

A stationary profile satisfies $S''=0$, hence $S=A+Bx$. The endpoint values $S(0)=0$ and $S(L)=T_0$ give $A=0$ and $B=T_0/L$.

:::

:::

::: pf-step

Set
$$
v(x,t)=T(x,t)-S(x).
$$
Then
$$
v_t=\kappa v_{xx},
\qquad
v(0,t)=v(L,t)=0,
\qquad
v(x,0)=-\frac{T_0x}{L}.
$$


::: pf-proof

Since $S''=0$, subtracting $S$ preserves the heat equation. The boundary values become homogeneous, and the initial condition follows from $T(x,0)=0$ for $0<x<L$.

:::

:::

::: {.pf-step #s1-3}

The separated Dirichlet expansion is
$$
v(x,t)=\sum_{n=1}^{\infty}b_n
\sin\frac{n\pi x}{L}
\exp\left(-\kappa\frac{n^2\pi^2}{L^2}t\right).
$$


::: pf-proof

The Dirichlet eigenfunctions of $-d^2/dx^2$ on $(0,L)$ are $\sin(n\pi x/L)$ with eigenvalues $(n\pi/L)^2$. Separation of variables gives the displayed decay factors.

:::

:::

::: {.pf-step #s1-4}

The Fourier coefficients are
$$
b_n=\frac{2T_0(-1)^n}{n\pi}.
$$


::: pf-proof

By sine-series orthogonality,
$$
b_n=\frac2L\int_0^L
\left(-\frac{T_0x}{L}\right)
\sin\frac{n\pi x}{L}\,dx.
$$
Integration by parts gives
$$
\int_0^Lx\sin\frac{n\pi x}{L}\,dx
=-\frac{L^2(-1)^n}{n\pi},
$$
which yields the stated coefficient.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
T(x,t)=\frac{T_0x}{L}
+\frac{2T_0}{\pi}
\sum_{n=1}^{\infty}\frac{(-1)^n}{n}
\sin\frac{n\pi x}{L}
\exp\left(-\kappa\frac{n^2\pi^2}{L^2}t\right).}
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}. For $t>0$ the series satisfies the heat equation and both endpoint temperatures. As $t\to0^+$, its sine series equals $-T_0x/L$ for $0<x<L$, so the interior initial temperature is zero. The incompatibility at the corner $(L,0)$ is forced by the source data: the boundary prescribes $T(L,t)=T_0$ while the initial condition prescribes zero at $t=0$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the temperature evolution for the stated fixed endpoint temperatures and zero interior initial temperature.

:::

:::

:::
