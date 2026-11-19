---
schema: qual/card@1
id: E-SS9.PR-1
kind: problem
title: 'Circular and iterated sums of $(z+n+m\tau)^{-2}$ differ from $\wp$ by constants'
classification:
  areas:
    - complex-analysis
  topics:
    - Elliptic Functions
    - Weierstrass P
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Restructured into a structured proof under #2, the three summation conventions as the last three
      top-level steps and (c) as the QED step. Re-checked the analytic content: the corrected series
      has summand $O_z(abs omega^{-3})$ because $abs{z+omega} >= abs omega/2$ for large $omega$, and the
      lattice point count $O(r)$ gives convergence; the linear form $x+y x tau$ is bounded below by
      $c sqrt(x^2+y^2)$ since its imaginary part is $y Im tau$; the mean-value error on a unit square is
      $O((n^2+m^2)^{-3/2})$ and sums; the annular integral is $log R$ times an angular integral that
      vanishes because $sin theta/(cos theta + tau sin theta)$ differentiates to the integrand (checked
      by expanding the quotient rule, the $tau$ terms cancelling); and the inner sums are
      $pi^2 csc^2(pi m tau)$, respectively $tau^{-2} pi^2 csc^2(pi n/tau)$, which decay exponentially.
      Added: the derivative computation in full, the constancy identity behind (a), and the bounds
      justifying each interchange. Repaired: a raw $abs{.}$ pair written with big delimiters, which
      STYLE-04 requires as the semantic macro. No defect found in the statement; no retained solution
      set covers it.
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` at its printed folio (the scan runs nineteen pages ahead of the
      printed page): the statement is Problem 1 at the head of the Chapter 9 Problems, printed
      p. 281, and its printed words are the card's. The chapter, the problem number and the page
      are now named in the solution's opening sentence. Not checked in this pass: the argument, which
      the edit does not touch.
---

::: {.exercise}
This is Problem 1 of Chapter 9 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, printed p. 281; the statement below is its wording.

Besides the approach in Section 1.2, there are several alternate ways of dealing with the sum $\sum 1/(z+\omega)^2$, where $\omega = n + m\tau$. For example, one may sum either (a) circularly, (b) first in $n$ then in $m$, (c) or first in $m$ then in $n$.

(a) Prove that if $z \notin \Lambda$, then

$$
\lim_{R \to \infty} \sum_{n^2 + m^2 \leq R^2} \frac{1}{(z + n + m\tau)^2} = S_1(z)
$$

exists and $S_1(z) = \wp(z) + c_1$.

(b) Similarly,

$$
\sum_m \qty(\sum_n \frac{1}{(z + n + m\tau)^2}) = S_2(z)
$$

exists and $S_2(z) = \wp(z) + c_2$, where $c_2 = F(\tau)$, and $F$ is the forbidden Eisenstein series.

(c) Also

$$
\sum_n \qty(\sum_m \frac{1}{(z + n + m\tau)^2}) = S_3(z)
$$

exists with $S_3(z) = \wp(z) + c_3$, and $c_3 = \tilde{F}(\tau)$, the reverse of $F$.

[Hint: To prove (a), it suffices to show that $\displaystyle\lim_{R\to\infty}\sum_{1 \leq n^2 + m^2 \leq R^2} 1/(n + m\tau)^2 = c_1$ exists. This is proved by a comparison with $\displaystyle\int_{1 \leq x^2 + y^2 \leq R^2} \frac{dx\,dy}{(x + y\tau)^2} = I(R)$. It can be shown that $I(R) = 0$, which follows because $(x + y\tau)^{-2} = -(\partial/\partial x)(x + y\tau)^{-1}$.]
:::

::: {.solution}
No retained solution set covers this problem, so the argument is the card's own; it is the printed hint, with the comparison sums carried out. Write $\Lambda=\{n+m\tau:n,m\in\ZZ\}$ with $\Im\tau\ne0$, and recall
$$
\wp(z)=\frac1{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\Bigl(\frac1{(z+\omega)^2}-\frac1{\omega^2}\Bigr).
$$

::: pf

::: {.pf-step #corrected}
The corrected series converges absolutely and locally uniformly away from $\Lambda$, its summand being $O_z(\abs\omega^{-3})$.

::: pf-proof
For $\abs\omega\ge2\abs z$,
$$
\abs{\frac1{(z+\omega)^2}-\frac1{\omega^2}}=\frac{\abs{2z\omega+z^2}}{\abs{\omega}^2\abs{z+\omega}^2}\le\frac{C_z}{\abs\omega^3},
$$
since $\abs{z+\omega}\ge\abs\omega-\abs z\ge\abs\omega/2$. The number of lattice points with $\abs\omega$ between $r$ and $r+1$ is $O(r)$, because $\Lambda$ is a lattice in $\RR^2$ under $(n,m)\mapsto n+m\tau$; so the sum of $\abs\omega^{-3}$ over lattice points converges, which gives absolute and locally uniform convergence.
:::

:::

::: {.pf-step #convention}
For any summation convention that adds the terms of $\sum_{\omega\ne0}1/(z+\omega)^2$ in some order, the result is $\wp(z)$ plus the same convention applied to $\sum_{\omega\ne0}\omega^{-2}$.

::: pf-proof
Subtracting the absolutely convergent series of step [](#corrected){.pf-ref} termwise from the raw series leaves the constant series $\sum_{\omega\ne0}\omega^{-2}$, whose terms do not depend on $z$; so a convention that sums a finite set of $\omega$ and passes to a limit gives the corresponding partial sum of $\wp$'s correction plus that same finite sum of $\omega^{-2}$.
:::

:::

::: {.pf-step #circular}
(a) $\lim_{R\to\infty}\sum_{1\le n^2+m^2\le R^2}(z+n+m\tau)^{-2}$ exists and equals $\wp(z)+c_1$.

::: pf-proof
By step [](#convention){.pf-ref} it is enough to treat the case $z=0$, and the correction $\wp(z)-z^{-2}$ is a convergent sum of constants, so it suffices to show $\sum_{1\le n^2+m^2\le R^2}(n+m\tau)^{-2}$ converges as $R\to\infty$. Since $\Im\tau\ne0$, the linear form is non-degenerate and $\abs{x+y\tau}\ge c\sqrt{x^2+y^2}$. Put $\phi(x,y)=(x+y\tau)^{-2}$; on the unit square centred at $(n,m)$ with $n^2+m^2$ large the mean value theorem bounds $\abs{\phi(x,y)-\phi(n,m)}$ by $C(n^2+m^2)^{-3/2}$, and summing these errors over $(n,m)\ne(0,0)$ converges because there are $O(r)$ lattice points at distance comparable to $r$. So the partial sums differ from the integral of $\phi$ over the union of the unit squares by a convergent quantity; replacing that union by the annulus $1\le x^2+y^2\le R^2$ changes the integral by $O(R^{-1})$, only an $O(R)$-area boundary layer being affected, where $\abs\phi=O(R^{-2})$.
:::

:::

::: {.pf-step #annulus-integral}
$\int_{1\le x^2+y^2\le R^2}\dfrac{dx\,dy}{(x+y\tau)^2}=0$.

::: pf-proof
In polar coordinates $x=r\cos\theta$, $y=r\sin\theta$ the integrand is $(r^2(\cos\theta+\tau\sin\theta)^2)^{-1}$ and $dx\,dy=r\,dr\,d\theta$, so the integral is
$$
\Bigl(\int_1^R\frac{dr}{r}\Bigr)\int_0^{2\pi}\frac{d\theta}{(\cos\theta+\tau\sin\theta)^2}=\log R\cdot J.
$$
The denominator never vanishes because $\Im\tau\ne0$, and
$$
\frac{d}{d\theta}\frac{\sin\theta}{\cos\theta+\tau\sin\theta}=\frac{\cos\theta(\cos\theta+\tau\sin\theta)-\sin\theta(-\sin\theta+\tau\cos\theta)}{(\cos\theta+\tau\sin\theta)^2}=\frac{1}{(\cos\theta+\tau\sin\theta)^2},
$$
so $J$ is the change of a $2\pi$-periodic function and vanishes.
:::

:::

::: {.pf-step #part-a}
(a) $S_1(z)=\wp(z)+c_1$ with $c_1=\lim_R\sum_{1\le n^2+m^2\le R^2}(n+m\tau)^{-2}$.

::: pf-proof
Steps [](#circular){.pf-ref} and [](#annulus-integral){.pf-ref} show that the circular partial sums of $\sum_{\omega\ne0}\omega^{-2}$ converge, to $c_1$; step [](#convention){.pf-ref} transfers that to the summand $(z+\omega)^{-2}$. Adding the $1/z^2$ term gives $S_1(z)=\wp(z)+c_1$.
:::

:::

::: {.pf-step #part-b}
(b) $S_2(z)$ exists and equals $\wp(z)+F(\tau)$, where $F(\tau)=\sum_m\bigl(\sum_n^{\ *}(n+m\tau)^{-2}\bigr)$ is the forbidden Eisenstein series.

::: pf-proof
For $m=0$ the inner sum over $n\ne0$ is $2\zeta(2)=\pi^2/3$. For $m\ne0$ one has $\sum_{n\in\ZZ}(n+a)^{-2}=\pi^2\csc^2(\pi a)$ with $a=m\tau$, and $\abs{\csc(\pi m\tau)}=O(e^{-\pi\abs m\abs{\Im\tau}})$ because $\abs{\sin(\pi m\tau)}$ grows like $e^{\pi\abs m\abs{\Im\tau}}$; so the series over $m$ converges absolutely. By step [](#convention){.pf-ref} the same summation applied to the corrected representation gives $S_2(z)=\wp(z)+F(\tau)$.
:::

:::

::: {.pf-step}
(c) $S_3(z)$ exists and equals $\wp(z)+\widetilde F(\tau)$, with $\widetilde F$ the reverse of $F$.

::: pf-proof
Here the inner sum is over $m$: $\sum_{m}(n+m\tau)^{-2}=\tau^{-2}\sum_m(m+n/\tau)^{-2}=\tau^{-2}\pi^2\csc^2(\pi n/\tau)$ for $n\ne0$, and the $n=0$ term is $\tau^{-2}\pi^2/3$. Since $\Im(-1/\tau)>0$ when $\Im\tau>0$, these terms decay exponentially in $\abs n$, so $\widetilde F(\tau)=\sum_n\bigl(\sum_m^{\ *}(n+m\tau)^{-2}\bigr)$ converges absolutely and $S_3(z)=\wp(z)+\widetilde F(\tau)$. Parts (a) and (b) are steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref}, so all three conventions exist and differ only by the constants obtained by summing $\sum_{\omega\ne0}\omega^{-2}$ in the corresponding order.
:::

:::

:::
:::
