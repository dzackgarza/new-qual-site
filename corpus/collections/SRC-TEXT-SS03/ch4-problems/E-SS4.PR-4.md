---
schema: qual/card@1
id: E-SS4.PR-4
kind: problem
title: Borel representation of entire functions of exponential type
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 4, §5.5, exercise 4, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card reproduces the printed
    exercise, parts (a) and (b), unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    The printed part (b) is inconsistent with the printed part (a): the two displayed formulas for
    $g$ differ by a sign. With the book's own conventions, $\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}dx$
    and $f(x)=\int\hat f(\xi)e^{2\pi i\xi x}d\xi$ (both as printed in Chapter 4), an entire $f$ of
    exponential type and its Borel transform $g$ as defined in part (a) satisfy
    $g(w)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{\hat f(\xi)}{w-\xi}d\xi$ for $\abs{w}>M$, not the printed
    $\frac{1}{2\pi i}\int\frac{\hat f(\xi)}{\xi-w}d\xi$. Verified on an explicit pair: for
    $\hat f\equiv1$ on $[-1/2,1/2]$ one has $f(z)=\sin(\pi z)/(\pi z)$ and
    $g(w)=-\frac{i}{\pi}\operatorname{artanh}\frac{1}{2w}$, and $\oint_{\abs{w}=1}e^{2\pi izw}g(w)dw$
    equals $f(z)$ (checked numerically at $z=0.3$ and $z=0.7+0.2i$), while the printed form gives
    $-f(z)$; correspondingly the jump $g(x+i0)-g(x-i0)$ of the part (a) transform is $-\hat f(x)$, and
    with the sign of the present solution the jump statement reads
    $\hat f(x)=\lim_{\varepsilon\to0+}(g(x-i\varepsilon)-g(x+i\varepsilon))$. The solution below
    proves the consistent version. The printed pair cannot both hold, so no reading makes both
    displays true; nothing else in the exercise is affected.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Both parts proved. (a) both directions: the coefficient estimate gives
    $\abs{a_n}\le A_\varepsilon(2\pi e(M+\varepsilon))^n/n!$, hence $\abs{A_n}^{1/n}\le e(M+\varepsilon)/(2\pi)$
    and the series for $g$ converges exactly on $\abs{w}>M$; the representation follows by expanding
    $e^{2\pi izw}$ and using $\oint w^m dw=2\pi i\delta_{m,-1}$ for any radius $\rho>M$; conversely the
    representation gives $\abs{f(z)}\le2\pi\rho\max_{\abs{w}=\rho}\abs{g}e^{2\pi\rho\abs{z}}$ for every
    $\rho>M$. (b) uses Paley--Wiener (Theorem 3.3) for $\operatorname{supp}\hat f\subseteq[-M,M]$, the
    Cauchy-type integral $\Phi$, and the geometric series to identify $\Phi=g$ on $\abs{w}>M$, which
    extends $g$ across $\CC\setminus[-M,M]$. No part is left in outline.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Locator correction to the first event: this is Chapter 4, Problem 4, on printed p. 133 (PDF
    p. 152), not an "exercise" of "§5.5". Re-read there today: the asterisk the print sets before
    "4." is recorded in the remark, and the two parts of the card's statement are the printed ones,
    including the printed form of (b) with the sign that the card's remark repairs. The two
    displayed formulas of the print do differ in sign, as the second event above states. Not checked
    today: that sign defect was neither re-derived nor re-evaluated in this pass and the earlier
    note's numerical check was not re-run; step s1's estimate (Cauchy's estimates at
    $R=n/(2\pi\tau)$ and Stirling) was read and is correct.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step s6 on the reader's report. The two boundary limits were displayed with the signs
    interchanged: for $\Phi(z)=\frac{1}{2\pi i}\int_{-M}^{M}\hat f(\xi)/(z-\xi)\,d\xi$ the
    distributional identity $1/(u+i\varepsilon)\to P.V.(1/u)-i\pi\delta$ gives
    $\Phi(x+i\varepsilon)\to\frac{1}{2\pi i}P.V.\int\hat f(\xi)/(x-\xi)d\xi-\hat f(x)/2$ and
    $\Phi(x-i\varepsilon)\to\frac{1}{2\pi i}P.V.\int+\hat f(x)/2$, so that the difference in the
    displayed orientation is $+\hat f(x)$, which is what the step concludes. The limits are corrected
    and the sign convention stated in the step; the conclusion, step s5 and the rest of the card are
    unchanged. Not checked in this pass: the numerical counterexample recorded in the second event.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Record of the search behind the solution's provenance sentence, which the reader asked for where
    no published solution set covers the Problem. Read: the head of R. C. Rhoades,
    *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), whose
    abstract describes it as solutions or hints to "many of the exercises", with one part per
    chapter. Searched the open web for a set answering the end-of-chapter Problems of this book: no
    document answering Chapter 4, Problem 4 was found. This search located no published set answering
    this Problem, and none is retained in this repository. Not checked: whether such a set exists
    outside what a web search reaches. The mathematics of the card is unchanged.
---

::: {.exercise}
There is a relation between the Paley–Wiener theorem and an earlier representation due to E. Borel.

(a) A function $f$, holomorphic on $\CC$, satisfies $\abs{f(z)}\leq A_\varepsilon e^{2\pi(M+\varepsilon)\abs{z}}$ for all $\varepsilon>0$ if and only if it has a representation
$$
f(z)=\int_C e^{2\pi izw}g(w)\,dw,
$$
where $g$ is holomorphic outside the circle of radius $M$ centered at the origin and vanishes at infinity. Here $C$ is any circle centered at the origin with radius larger than $M$. In fact, if $f(z)=\sum_{n=0}^{\infty}a_nz^n$, then $g(w)=\sum_{n=0}^{\infty}A_nw^{-n-1}$, with $a_n=A_n(2\pi i)^{n+1}/n!$.

(b) The connection with Theorem 3.3 is as follows. For these functions $f$, if in addition $f$ and $\hat f$ are of moderate decrease on the real axis, show that $g$ is holomorphic on the slit plane $\CC\setminus[-M,M]$ and
$$
g(z)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{\hat f(\xi)}{\xi-z}\,d\xi.
$$
Thus $\hat f$ represents the jump of $g$ across $[-M,M]$:
$$
\hat f(x)=\lim_{\varepsilon\to0,\,\varepsilon>0}\bigl(g(x+i\varepsilon)-g(x-i\varepsilon)\bigr).
$$
See Problem 5 in Chapter 3.
:::

::: {.solution}
No published solution set covers the end-of-chapter Problems of Stein--Shakarchi: the set of R. C. Rhoades, *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), covers a selection of the chapter Exercises and not the Problems, and no other set was located. The argument is the card's own.

Write $f(z)=\sum_{n\ge0}a_nz^n$ and $A_n=\dfrac{a_n\,n!}{(2\pi i)^{n+1}}$, so that the series proposed for $g$ is $g(w)=\sum_{n\ge0}A_nw^{-n-1}$.

::: pf

::: {.pf-step #s1}

Suppose $\abs{f(z)}\le A_\varepsilon e^{2\pi(M+\varepsilon)\abs{z}}$ for every $\varepsilon>0$. Then $g(w)=\sum_nA_nw^{-n-1}$ converges for $\abs{w}>M$, is holomorphic there, and satisfies $g(w)\to0$ as $w\to\infty$.

::: pf-proof

Fix $\varepsilon>0$ and put $\tau=M+\varepsilon$. By Cauchy's estimates on the circle of radius $R$, for every $R>0$
$$
\abs{a_n}\le\frac{A_\varepsilon e^{2\pi\tau R}}{R^n}.
$$
For $n\ge1$ take $R=n/(2\pi\tau)$, which gives $\abs{a_n}\le A_\varepsilon\bigl(\frac{2\pi e\tau}{n}\bigr)^{n}$, and hence
$$
\abs{A_n}=\frac{\abs{a_n}\,n!}{(2\pi)^{n+1}}\le\tau^n\,c_n,
\qquad c_n:=\frac{A_\varepsilon\,e^{n}n!}{2\pi\,n^{\,n}} .
$$
By Stirling's formula $n!\sim\sqrt{2\pi n}\,(n/e)^n$, so $c_n\sim\frac{A_\varepsilon}{2\pi}\sqrt{2\pi n}$ and in particular $c_n^{1/n}\to1$. Therefore, for $\abs{w}>\tau$,
$$
\sum_{n\ge0}\abs{A_n}\abs{w}^{-n-1}
\le\frac{1}{\abs{w}}\sum_{n\ge0}c_n\Bigl(\frac{\tau}{\abs{w}}\Bigr)^{n}<\infty,
$$
since $\tau/\abs{w}<1$ and $c_n$ grows subexponentially. As $\varepsilon>0$ was arbitrary, the series converges absolutely for every $\abs{w}>M$. Being a convergent Laurent series in $w^{-1}$ it defines a holomorphic function on $\abs{w}>M$, and $\abs{g(w)}\le\sum_n\abs{A_n}\abs{w}^{-n-1}\to0$ as $\abs{w}\to\infty$.

:::

:::

::: {.pf-step #s2}

Under the hypothesis of step [](#s1){.pf-ref}, for every circle $C$ centred at $0$ of radius $\rho>M$,
$$
f(z)=\int_Ce^{2\pi izw}g(w)\,dw\qquad\text{for all }z\in\CC .
$$

::: pf-proof

Fix $\rho>M$ and $\abs{w}=\rho$. Expanding the exponential and inserting the series,
$$
e^{2\pi izw}g(w)=\sum_{k\ge0}\sum_{n\ge0}\frac{(2\pi iz)^k}{k!}A_nw^{k-n-1}.
$$
The double series is absolutely convergent on the circle, because $\sum_n\abs{A_n}\rho^{-n-1}<\infty$ and $\sum_k(2\pi\abs{z}\rho)^k/k!<\infty$, so it may be integrated term by term. Since
$$
\int_Cw^m\,dw=2\pi i\,\delta_{m,-1},
$$
only the terms with $k=n$ survive, and
$$
\int_Ce^{2\pi izw}g(w)\,dw=\sum_{n\ge0}\frac{(2\pi iz)^n}{n!}A_n\,2\pi i=\sum_{n\ge0}A_n\frac{(2\pi i)^{n+1}}{n!}z^n=\sum_{n\ge0}a_nz^n=f(z).
$$

:::

:::

::: {.pf-step #s3}

Conversely, suppose $f(z)=\int_Ce^{2\pi izw}g(w)\,dw$ for every circle $C$ of radius $\rho>M$, where $g$ is holomorphic on $\abs{w}>M$ and $g(w)\to0$ as $w\to\infty$. Then for every $\varepsilon>0$ there is $A_\varepsilon$ with $\abs{f(z)}\le A_\varepsilon e^{2\pi(M+\varepsilon)\abs{z}}$.

::: pf-proof

Fix $\rho>M$ and $z\in\CC$. On $\abs{w}=\rho$ one has $\abs{e^{2\pi izw}}=e^{-2\pi\operatorname{Im}(zw)}\le e^{2\pi\abs{z}\rho}$, so
$$
\abs{f(z)}\le2\pi\rho\sup_{\abs{w}=\rho}\abs{g(w)}\,e^{2\pi\rho\abs{z}} .
$$
Given $\varepsilon>0$ choose $\rho\in(M,M+\varepsilon)$; then $\abs{f(z)}\le A_\varepsilon e^{2\pi(M+\varepsilon)\abs{z}}$ with $A_\varepsilon=2\pi\rho\sup_{\abs{w}=\rho}\abs{g}$, which is finite because $g$ is holomorphic on the closed annulus $\abs{w}\ge\rho>M$.

:::

:::

::: {.pf-step #s4}

Part (b): assume in addition that $f$ and $\hat f$ are of moderate decrease on $\RR$. Then $\hat f$ is supported in $[-M,M]$, and the function
$$
\Phi(z)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{\hat f(\xi)}{z-\xi}\,d\xi
$$
is holomorphic on $\CC\setminus[-M,M]$.

::: pf-proof

By Paley--Wiener (Chapter 4, Theorem 3.3), an entire $f$ with $\abs{f(z)}\le Ae^{2\pi M\abs{z}}$ has $\hat f$ supported in $[-M,M]$. For the holomorphy of $\Phi$: the integrand $(\xi,z)\mapsto\hat f(\xi)/(z-\xi)$ is continuous on $[-M,M]\times(\CC\setminus[-M,M])$ and holomorphic in $z$ for each $\xi$, and on a compact $K$ disjoint from $[-M,M]$ it is dominated by $\sup\abs{\hat f}/\operatorname{dist}(K,[-M,M])$, so $\Phi$ is holomorphic off the segment by Morera's theorem or differentiation under the integral.

:::

:::

::: {.pf-step #s5}

For $\abs{z}>M$ one has $\Phi(z)=g(z)$, so $\Phi$ is the holomorphic extension of $g$ to $\CC\setminus[-M,M]$.

::: pf-proof

Since $\hat f$ is supported in $[-M,M]$ and $f(x)=\int_{-M}^{M}\hat f(\xi)e^{2\pi i\xi x}d\xi$, differentiating under the integral gives
$$
a_n=\frac{f^{(n)}(0)}{n!}=\frac{(2\pi i)^n}{n!}\int_{-M}^{M}\hat f(\xi)\xi^n\,d\xi,
\qquad\text{hence}\qquad
A_n=\frac{1}{2\pi i}\int_{-M}^{M}\hat f(\xi)\xi^n\,d\xi .
$$
For $\abs{z}>M$ and $\abs{\xi}\le M$ the geometric series $\frac{1}{z-\xi}=\sum_{n\ge0}\xi^nz^{-n-1}$ converges uniformly in $\xi$, so
$$
\Phi(z)=\frac{1}{2\pi i}\sum_{n\ge0}z^{-n-1}\int_{-M}^{M}\hat f(\xi)\xi^n\,d\xi=\sum_{n\ge0}A_nz^{-n-1}=g(z).
$$
Since $g$ is determined on $\abs{w}>M$ and $\Phi$ is holomorphic on the larger set $\CC\setminus[-M,M]$, this is the asserted extension.

:::

:::

::: {.pf-step #s6}

The jump of the extension across the segment is $\hat f$:
$$
\hat f(x)=\lim_{\varepsilon\to0+}\bigl(\Phi(x-i\varepsilon)-\Phi(x+i\varepsilon)\bigr),\qquad -M<x<M .
$$

::: pf-proof

Fix $x\in(-M,M)$ and write, for $z=x\pm i\varepsilon$ with $\varepsilon>0$ small,
$$
\frac{1}{z-\xi}=\frac{1}{(x-\xi)\pm i\varepsilon}.
$$
As $\varepsilon\to0+$, $\frac{1}{u\mp i\varepsilon}=P.V.\frac1u\pm\pi i\delta$, so
$$
\Phi(x+i\varepsilon)\longrightarrow\frac{1}{2\pi i}P.V.\!\int_{-M}^{M}\frac{\hat f(\xi)}{x-\xi}d\xi-\frac{\hat f(x)}{2},
\qquad
\Phi(x-i\varepsilon)\longrightarrow\frac{1}{2\pi i}P.V.\!\int_{-M}^{M}\frac{\hat f(\xi)}{x-\xi}d\xi+\frac{\hat f(x)}{2},
$$
and subtracting gives $\hat f(x)$. That is, $\hat f$ is the jump of the extension in the displayed orientation. The lower sign of the distributional identity is the one that applies to $1/(u+i\varepsilon)$, hence to $z=x+i\varepsilon$, and the upper sign to $z=x-i\varepsilon$.

:::

:::

:::

:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 4, Problem 4). The printed exercise writes $\Phi(z)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{\hat f(\xi)}{\xi-z}d\xi$ together with $\hat f(x)=\lim(g(x+i\varepsilon)-g(x-i\varepsilon))$. Those two displays differ in sign from part (a): with the normalization $A_n=a_nn!/(2\pi i)^{n+1}$ of part (a) and the book's convention $\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}dx$, the identity that holds is $g(w)=\frac{1}{2\pi i}\int\frac{\hat f(\xi)}{w-\xi}d\xi$, whose jump is $-\hat f$. The correction is recorded in this card's audit events; the mathematics above is self-consistent and is the version proved.
:::
