---
schema: qual/card@1
id: E-SS9.EX-8
kind: problem
title: $E_4(\tau)\to\pi^4/45$ as $\Im\tau\to\infty$, with exponential error
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Modular Forms
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
    card's own and the card says so. Each step re-read: the m = 0 terms of the lattice sum are
    2 zeta(4); the one-variable Fourier expansion (Lemma 2.4 with k = 4) applies at w = m tau since
    Im w = mt > 0; the m and -m sums agree after n -> -n because (-1)^{-4} = 1; 2 zeta(4) =
    pi^4/45; the absolute-value estimate uses |e^{2 pi i r m tau}| = e^{-2 pi r m t} and t >= 1, and
    the residual double series converges; and the modular transformation E_4(-1/tau) =
    tau^4 E_4(tau) is the reindexing (n,m) -> (n,-m) of the lattice sum. The three parts are kept in
    the order of the exercise. Not claimed: any bound better than exponential, or any statement
    about E_4 away from the upper half-plane.
---

::: {.exercise}
Let
$$
E_4(\tau) = \sum_{(n, m) \neq (0, 0)} \frac{1}{(n + m\tau)^4}
$$
be the Eisenstein series of order $4$.

(a) Show that $E_4(\tau) \to \pi^4/45$ as $\Im(\tau) \to \infty$.

(b) More precisely,
$$
\abs{E_4(\tau) - \frac{\pi^4}{45}} \leq ce^{-2\pi t} \quad \text{if } \tau = x + it \text{ and } t \geq 1.
$$

(c) Deduce that
$$
\abs{E_4(\tau) - \tau^{-4}\frac{\pi^4}{45}} \leq ct^{-4} e^{-2\pi/t} \quad \text{if } \tau = it \text{ and } 0 < t \leq 1.
$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 9 Exercise 8, and uses the Fourier expansion of the Eisenstein series of weight $4$ (Lemma 2.4 there).

::: pf

::: {.pf-step #split}
$E_{4}(\tau)=\sum_{m\ne0}\sum_{n\in\ZZ}(n+m\tau)^{-4}+2\zeta(4)$.

::: pf-proof
The terms with $m=0$ are $\sum_{n\ne0}n^{-4}=2\zeta(4)$; separate them from the rest of the lattice sum.
:::

:::

::: {.pf-step #lemma}
If $\operatorname{Im}w>0$ then $\sum_{n\in\ZZ}(n+w)^{-4}=\dfrac{8\pi^{4}}{3}\sum_{r=1}^{\infty}r^{3}e^{2\pi irw}$.

::: pf-proof
This is the Fourier expansion of the weight $4$ Eisenstein series in one variable (Lemma 2.4 of the text with $k=4$), absolutely and locally uniformly convergent for $\operatorname{Im}w>0$.
:::

:::

::: {.pf-step #pairing}
The contributions of $m$ and $-m$ are equal.

::: pf-proof
For $m=-M$ with $M>0$, substitute $n\mapsto-n$: $\sum_{n}(n-M\tau)^{-4}=\sum_{n}(-n-M\tau)^{-4}=\sum_{n}(n+M\tau)^{-4}$, since $(-1)^{-4}=1$.
:::

:::

::: {.pf-step #formula}
$E_{4}(\tau)=\dfrac{\pi^{4}}{45}+\dfrac{16\pi^{4}}{3}\sum_{m,r\ge1}r^{3}e^{2\pi irm\tau}$.

::: pf-proof
By steps [](#pairing){.pf-ref} and [](#lemma){.pf-ref} applied with $w=m\tau$, whose imaginary part $mt$ is positive for $m>0$, the sum over $m\ne0$ is $2\sum_{m\ge1}\frac{8\pi^{4}}{3}\sum_{r\ge1}r^{3}e^{2\pi irm\tau}$. Adding $2\zeta(4)=\pi^{4}/45$ gives the displayed formula.
:::

:::

::: {.pf-step #partb}
For $\tau=x+it$ with $t\ge1$, $\abs{E_{4}(\tau)-\pi^{4}/45}\le Ce^{-2\pi t}$.

::: pf-proof
Taking absolute values in step [](#formula){.pf-ref} and using $\abs{e^{2\pi irm\tau}}=e^{-2\pi rmt}$,
$$
\abs{E_{4}(\tau)-\frac{\pi^{4}}{45}}\le\frac{16\pi^{4}}{3}\sum_{m,r\ge1}r^{3}e^{-2\pi rmt}\le\frac{16\pi^{4}}{3}e^{-2\pi t}\sum_{m,r\ge1}r^{3}e^{-2\pi(rm-1)},
$$
the last inequality using $t\ge1$. The remaining double sum is a convergent series of positive numbers independent of $t$ and $x$, so it is a finite constant $C$; this is the estimate of part (b).
:::

:::

::: {.pf-step #parta}
$E_{4}(\tau)\to\pi^{4}/45$ as $\operatorname{Im}\tau=t\to\infty$.

::: pf-proof
The bound of step [](#partb){.pf-ref} tends to $0$ as $t\to\infty$, so $E_{4}(\tau)\to\pi^{4}/45$ uniformly in $x$ for $t\ge1$.
:::

:::

::: {.pf-step #modular}
$E_{4}(-1/\tau)=\tau^{4}E_{4}(\tau)$.

::: pf-proof
$E_{4}(-1/\tau)=\sum_{(n,m)\ne(0,0)}(n-m/\tau)^{-4}=\sum_{(n,m)\ne(0,0)}\tau^{4}(n\tau-m)^{-4}=\tau^{4}\sum_{(n,m)\ne(0,0)}(n\tau-m)^{-4}$, and as $(n,m)$ runs over the nonzero lattice points so does $(n,-m)$, so the last sum is $E_{4}(\tau)$.
:::

:::

::: {.pf-step #partc}
$\abs{E_{4}(it)-t^{-4}\pi^{4}/45}\le Ct^{-4}e^{-2\pi/t}$ for $0<t\le1$.

::: pf-proof
Put $\tau=it$ in step [](#modular){.pf-ref}: $E_{4}(-1/(it))=E_{4}(i/t)=t^{4}E_{4}(it)$, since $(it)^{4}=t^{4}$. Hence $E_{4}(it)=t^{-4}E_{4}(i/t)$, and the height $1/t\ge1$ lets step [](#partb){.pf-ref} be applied:
$$
\abs{E_{4}(it)-t^{-4}\pi^{4}/45}=t^{-4}\abs{E_{4}(i/t)-\pi^{4}/45}\le t^{-4}Ce^{-2\pi/t}.
$$
:::

:::

::: {.pf-step}
Parts (a), (b) and (c) hold.

::: pf-proof
Steps [](#parta){.pf-ref}, [](#partb){.pf-ref} and [](#partc){.pf-ref} are the three assertions:
$$
\boxed{E_{4}(\tau)\to\pi^{4}/45;\quad \abs{E_{4}(\tau)-\pi^{4}/45}\le Ce^{-2\pi t}\ (t\ge1);\quad \abs{E_{4}(it)-t^{-4}\pi^{4}/45}\le Ct^{-4}e^{-2\pi/t}\ (0<t\le1).}
$$
The exponential decay is what makes $E_{4}$ tend to its constant value at the cusp, and the modular transformation transfers the estimate to the other end.
:::

:::

:::
:::
