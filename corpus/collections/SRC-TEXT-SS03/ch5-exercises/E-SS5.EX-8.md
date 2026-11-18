---
schema: qual/card@1
id: E-SS5.EX-8
kind: problem
title: $\prod_{k\ge1}\cos(z/2^k)=\sin z/z$
classification:
  areas:
  - complex-analysis
  topics:
  - Infinite Products
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so; the printed hint is followed exactly. Each step re-read: the
    double-angle identity iterates to give sin z = 2^N sin(z/2^N) times the N-th partial product;
    dividing by 2^N sin(z/2^N), written as z times sin(w)/w with w = z/2^N, gives the closed form of
    the partial products; the factor sin(w)/w tends to 1; and z = 0 is handled separately since
    every factor is then 1. The card states convergence of the product as convergence of the
    partial products, which is the definition used. Not claimed: any statement about products of
    the same shape with other scale factors.
---

::: {.exercise}
Prove that for every $z$ the product below converges, and
$$
\cos(z/2)\cos(z/4)\cos(z/8)\cdots = \prod_{k=1}^{\infty}\cos(z/2^{k}) = \frac{\sin z}{z}.
$$

[Hint: Use the fact that $\sin 2z = 2\sin z\cos z$.]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 5 Exercise 8, and follows the printed hint to use $\sin 2z=2\sin z\cos z$.

::: pf

::: {.pf-step #iterate}
For every positive integer $N$ and every $z$, $\sin z=2^{N}\sin(z/2^{N})\prod_{k=1}^{N}\cos(z/2^{k})$.

::: pf-proof
Induction on $N$. For $N=1$ it is the double-angle identity $\sin z=2\sin(z/2)\cos(z/2)$. For the step, replace $z$ by $z/2^{N}$ in the double-angle identity: $\sin(z/2^{N})=2\sin(z/2^{N+1})\cos(z/2^{N+1})$, and substitute into the formula at $N$.
:::

:::

::: {.pf-step #partial}
For $z\ne0$ and $N\ge1$,
$$
\prod_{k=1}^{N}\cos\bigl(z/2^{k}\bigr)=\frac{\sin z/z}{\sin(z/2^{N})/(z/2^{N})}.
$$

::: pf-proof
By step [](#iterate){.pf-ref} and $2^{N}\sin(z/2^{N})=z\cdot\dfrac{\sin(z/2^{N})}{z/2^{N}}$, we get $\sin z=\dfrac{\sin z}{z}\cdot z\cdot\dfrac{\sin(z/2^{N})}{z/2^{N}}\cdot\prod_{k=1}^{N}\cos(z/2^{k})$; dividing by the nonzero quantity $z\cdot\dfrac{\sin(z/2^{N})}{z/2^{N}}$ (nonzero because $z\ne0$ and $\sin w\ne0$ for $0<\abs{w}<\pi$, which holds eventually) gives the displayed identity.
:::

:::

::: {.pf-step #limit}
$\dfrac{\sin(z/2^{N})}{z/2^{N}}\to1$ as $N\to\infty$, for each fixed $z$.

::: pf-proof
$z/2^{N}\to0$ and $\sin w/w\to1$ as $w\to0$, the function $\sin w/w$ extending continuously to $1$ at $0$; composition of limits gives the claim for the fixed sequence $w_{N}=z/2^{N}$.
:::

:::

::: {.pf-step #nonzero}
For $z\ne0$ the infinite product converges and equals $\sin z/z$.

::: pf-proof
The partial products are given by step [](#partial){.pf-ref}, and their denominator tends to $1$ by step [](#limit){.pf-ref} while the numerator $\sin z/z$ is fixed, so the partial products converge to $\sin z/z$. Convergence of the infinite product is exactly convergence of this sequence of partial products.
:::

:::

::: {.pf-step #zero}
At $z=0$ every factor equals $1$ and the value is the removable value of $\sin z/z$ at $0$, namely $1$.

::: pf-proof
$\cos 0=1$, so each partial product is $1$ and the product is $1$; and $\lim_{z\to0}\sin z/z=1$.
:::

:::

::: {.pf-step}
$\prod_{k\ge1}\cos(z/2^{k})=\sin z/z$ for every $z$.

::: pf-proof
Steps [](#nonzero){.pf-ref} and [](#zero){.pf-ref} cover $z\ne0$ and $z=0$:
$$
\boxed{\prod_{k=1}^{\infty}\cos\bigl(z/2^{k}\bigr)=\frac{\sin z}{z}\quad(z\in\CC),}
$$
the right side being read as $1$ at $z=0$. The product converges for every $z$ because its partial products are given in closed form by step [](#partial){.pf-ref}.
:::

:::

:::
:::
