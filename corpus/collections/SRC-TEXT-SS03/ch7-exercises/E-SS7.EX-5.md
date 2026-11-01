---
schema: qual/card@1
id: E-SS7.EX-5
kind: problem
title: Alternating zeta series and real zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 5, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a)--(c); nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved as stated. (a) by summation by parts with the bounded partial sums of $(-1)^{n+1}$; (b) by
    separating the even terms; the identity is then extended from $s>1$ to $\Re s>0$ by the identity
    theorem, both sides being holomorphic there including $s=1$, where $1-2^{1-s}$ cancels the pole;
    (c) from the alternating series for $0<\sigma<1$ and from the functional equation
    $\zeta(s)=\pi^{s-1/2}\Gamma((1-s)/2)\zeta(1-s)/\Gamma(s/2)$ at $\sigma=0$, where the two poles
    cancel to give $\zeta(0)=-1/2$. Nothing is left in outline.
---

::: {.exercise}
Consider
$$
\widetilde\zeta(s)=1-\frac1{2^s}+\frac1{3^s}-\cdots
=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^s}.
$$

(a) Prove that this series converges for $\Re s>0$ and defines a holomorphic function there.

(b) Show that, for real $s>1$, $\widetilde\zeta(s)=(1-2^{1-s})\zeta(s)$.

(c) Use the alternating series to conclude that $\zeta$ has no zeros on the real segment $0<\sigma<1$. Extend this to $\sigma=0$ using the functional equation.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a): $\widetilde\zeta(s)=\sum_{n\ge1}(-1)^{n+1}n^{-s}$ converges for $\Re s>0$ and defines a holomorphic function there.

::: pf-proof

Put $\sigma_n=\sum_{k=1}^{n}(-1)^{k+1}$, so that $\sigma_n\in\{0,1\}$ and $(-1)^{n+1}=\sigma_n-\sigma_{n-1}$ with $\sigma_0=0$. Summation by parts gives, for $N\ge1$,
$$
\sum_{n=1}^{N}\frac{(-1)^{n+1}}{n^{s}}=\frac{\sigma_N}{N^{s}}+\sum_{n=1}^{N-1}\sigma_n\Bigl(\frac{1}{n^{s}}-\frac{1}{(n+1)^{s}}\Bigr).
$$
Since $\Re s>0$, the first term tends to $0$. For the sum, $\sigma_n\in\{0,1\}$ and
$$
\Bigl|\frac{1}{n^{s}}-\frac{1}{(n+1)^{s}}\Bigr|=\Bigl|s\int_n^{n+1}t^{-s-1}\,dt\Bigr|\le\abs{s}\,n^{-\Re s-1},
$$
which is summable over $n$; so the series converges. On the half-plane $\Re s\ge\delta>0$ the bound is $\abs{s}n^{-\delta-1}$, uniform in $s$, so the series converges uniformly there and is holomorphic by Weierstrass's theorem. As $\delta>0$ is arbitrary, $\widetilde\zeta$ is holomorphic on $\Re s>0$.

:::

:::

::: {.pf-step #s2}

Part (b): for real $s>1$, $\widetilde\zeta(s)=(1-2^{1-s})\zeta(s)$.

::: pf-proof

Absolute convergence allows the split
$$
\widetilde\zeta(s)=\sum_{n\ge1}\frac{1}{n^{s}}-2\sum_{m\ge1}\frac{1}{(2m)^{s}}=\zeta(s)-2^{1-s}\zeta(s)=(1-2^{1-s})\zeta(s).
$$

:::

:::

::: {.pf-step #s3}

The identity $\widetilde\zeta(s)=(1-2^{1-s})\zeta(s)$ holds on the whole half-plane $\Re s>0$, where both sides are holomorphic.

::: pf-proof

$\widetilde\zeta$ is holomorphic on $\Re s>0$ by step [](#s1){.pf-ref}. The function $s\mapsto(1-2^{1-s})\zeta(s)$ is holomorphic on $\Re s>0$ away from $s=1$, where $\zeta$ has a simple pole with residue $1$ while $1-2^{1-s}$ has a simple zero with derivative $\log2\cdot2^{1-s}\big|_{s=1}=\log2\ne0$; hence the product extends holomorphically across $s=1$ as well. The half-plane $\Re s>0$ is connected, and by step [](#s2){.pf-ref} the two holomorphic functions agree on the open set $(1,\infty)$; by the identity theorem they agree on $\Re s>0$.

:::

:::

::: {.pf-step #s4}

Part (c), first half: $\zeta$ has no zeros with $0<\sigma<1$ real.

::: pf-proof

Let $0<\sigma<1$. The numbers $n^{-\sigma}$ decrease strictly to $0$, so the alternating series $\widetilde\zeta(\sigma)=\sum_{n\ge1}(-1)^{n+1}n^{-\sigma}$ converges and its sum lies strictly between any two consecutive partial sums; in particular between $s_2=1-2^{-\sigma}$ and $s_1=1$, both of which are positive because $\sigma>0$. Hence $\widetilde\zeta(\sigma)>0$.

By step [](#s3){.pf-ref} at the real point $\sigma$,
$$
\widetilde\zeta(\sigma)=(1-2^{1-\sigma})\zeta(\sigma).
$$
Finally $1-2^{1-\sigma}\ne0$ because $2^{1-\sigma}=1$ only for $\sigma=1$. Therefore $\zeta(\sigma)=\widetilde\zeta(\sigma)/(1-2^{1-\sigma})$ is finite and non-zero.

:::

:::

::: {.pf-step #s5}

Part (c), second half: $\zeta(0)\ne0$, by the functional equation.

::: pf-proof

Chapter 7 gives the functional equation in the form
$$
\zeta(s)=\pi^{s-1/2}\,\frac{\Gamma\bigl(\frac{1-s}{2}\bigr)}{\Gamma\bigl(\frac{s}{2}\bigr)}\,\zeta(1-s).
$$
As $s\to0$ one has $\Gamma(s/2)\sim2/s$, so $1/\Gamma(s/2)\sim s/2$; $\Gamma\bigl(\frac{1-s}{2}\bigr)\to\Gamma\bigl(\frac12\bigr)=\sqrt\pi$; and $\zeta(1-s)\sim-1/s$ because $\zeta$ has residue $1$ at $1$. Hence
$$
\zeta(s)\sim\pi^{-1/2}\cdot\sqrt\pi\cdot\frac{s}{2}\cdot\Bigl(-\frac1s\Bigr)=-\frac12,
$$
so $\zeta(0)=-1/2\ne0$. Together with step [](#s4){.pf-ref}, $\zeta$ has no zeros on the real segment $0\le\sigma<1$.

:::

:::

:::

:::
