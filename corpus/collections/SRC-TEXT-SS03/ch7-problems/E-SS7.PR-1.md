---
schema: qual/card@1
id: E-SS7.PR-1
kind: problem
title: Mean square of a Dirichlet series with bounded coefficients, and uniqueness of coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Dirichlet Series
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
    Restructured into a structured proof under #2. Re-checked: $\abs{a_n}n^{-\sigma}\le Mn^{-\sigma}$
    and $\zeta(\sigma)<\infty$ for $\sigma>1$ give absolute and uniform convergence; the double
    series for $\abs F^2$ is dominated by $M^2\zeta(\sigma)^2$, which justifies termwise integration;
    the kernel is $K_T(n,m)=\sin(T\log(n/m))/(T\log(n/m))$ for $n\ne m$, tending to $0$, with
    $\abs{K_T}\le1$; dominated convergence for double series then yields the identity, whose right
    side is the coefficient $\ell^2$ sum, the Parseval--Plancherel analogy; and (b) shifts by $k$ to
    make the coefficients bounded and applies (a) at any $\sigma>1$, the non-negative sum vanishing
    termwise. Added: the explicit majorant in each limit step and the reason a vanishing sum of
    non-negative terms kills each term, which the prose compressed. No defect found in the statement,
    Problem 1 of Chapter 7; no retained solution set covers it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` at its printed folio (the scan runs nineteen pages ahead of the
    printed page): the statement is Problem 1 at the head of the Chapter 7 Problems, printed
    p. 203, and its printed words are the card's. The chapter, the problem number and the page
    are now named in the solution's opening sentence. Not checked in this pass: the argument, which
    the edit does not touch.
---

::: {.exercise}
This is Problem 1 of Chapter 7 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, printed p. 203; the statement below is its wording.

Let $F(s) = \sum_{n=1}^{\infty} a_n/n^s$, where $\abs{a_n} \leq M$ for all $n$.

(a) Then
$$
\lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} \abs{F(\sigma + it)}^2\, dt = \sum_{n=1}^{\infty} \frac{\abs{a_n}^2}{n^{2\sigma}} \quad \text{if } \sigma > 1.
$$
How is this reminiscent of the Parseval-Plancherel theorem? See e.g. Chapter 3 in Book I.

(b) Show as a consequence the uniqueness of Dirichlet series: If $F(s) = \sum_{n=1}^{\infty} a_n n^{-s}$ where the coefficients are assumed to satisfy $\abs{a_n} \leq cn^k$ for some $k$, and $F(s) \equiv 0$, then $a_n = 0$ for all $n$.

Hint: For part (a) use the fact that
$$
\frac{1}{2T} \int_{-T}^{T} (nm)^{-\sigma} n^{-it} m^{it}\, dt \to \begin{cases} n^{-2\sigma} & \text{if } n = m, \\ 0 & \text{if } n \neq m. \end{cases}
$$
:::

::: {.solution}
No retained solution set covers this problem, so the argument is the card's own; it is the printed hint's kernel computation, with the summability made explicit.

::: pf

::: {.pf-step #absolute}
(a) For $\sigma>1$ the series for $F(\sigma+it)$ converges absolutely and uniformly in $t$, and
$$
\abs{F(\sigma+it)}^2=\sum_{n,m\ge1}a_n\overline{a_m}(nm)^{-\sigma}e^{-it\log(n/m)}
$$
with the double series absolutely summable.

::: pf-proof
$\abs{a_n/n^{\sigma+it}}=\abs{a_n}n^{-\sigma}\le Mn^{-\sigma}$ and $\sum_n n^{-\sigma}=\zeta(\sigma)<\infty$ for $\sigma>1$, so the series converges absolutely and uniformly in $t$ by the Weierstrass $M$-test. Multiplying the series by its conjugate and using $n^{-it}\overline{m^{-it}}=e^{-it\log(n/m)}$ gives the displayed expansion, and $\sum_{n,m}\abs{a_na_m}(nm)^{-\sigma}\le M^2\zeta(\sigma)^2<\infty$ makes it absolutely summable, so the rearrangement is legitimate.
:::

:::

::: {.pf-step #termwise}
(a) For every $T>0$,
$$
\frac1{2T}\int_{-T}^T\abs{F(\sigma+it)}^2\,dt=\sum_{n,m\ge1}a_n\overline{a_m}(nm)^{-\sigma}K_T(n,m),\qquad K_T(n,m)=\frac1{2T}\int_{-T}^Te^{-it\log(n/m)}\,dt.
$$

::: pf-proof
Absolute summability of the double series by step [](#absolute){.pf-ref} permits integrating termwise over the finite interval $[-T,T]$ and interchanging the sum with the integral; the factor $K_T(n,m)$ collects the integral of the exponential.
:::

:::

::: {.pf-step #kernel}
(a) $K_T(n,n)=1$; for $n\ne m$, $K_T(n,m)=\sin(T\log(n/m))/(T\log(n/m))\to0$ as $T\to\infty$; and $\abs{K_T(n,m)}\le1$.

::: pf-proof
If $n=m$ the integrand is $1$ and the average is $1$. If $n\ne m$ then $\log(n/m)\ne0$ and the integral of $e^{-it\lambda}$ over $[-T,T]$ is $2\sin(T\lambda)/\lambda$ with $\lambda=\log(n/m)$, which gives the displayed quotient, tending to $0$. The bound holds because the average of a function of modulus $1$ has modulus at most $1$.
:::

:::

::: {.pf-step #part-a}
(a) $\displaystyle\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}\abs{F(\sigma+it)}^2dt=\sum_{n=1}^{\infty}\frac{\abs{a_n}^2}{n^{2\sigma}}$ for $\sigma>1$.

::: pf-proof
By step [](#kernel){.pf-ref} the summands of step [](#termwise){.pf-ref} converge for each pair $(n,m)$ to $a_n\overline{a_m}(nm)^{-\sigma}$ when $n=m$ and to $0$ otherwise, and they are dominated in modulus by $\abs{a_na_m}(nm)^{-\sigma}$, which is summable by step [](#absolute){.pf-ref}. So dominated convergence for double series applies and the limit is $\sum_n\abs{a_n}^2n^{-2\sigma}$. This is the Dirichlet-series analogue of Parseval--Plancherel: the vertical average annihilates the cross terms $n\ne m$ and leaves the sum of the squared coefficient moduli, just as the mean square of a Fourier series is the sum of the squared moduli of its coefficients.
:::

:::

::: {.pf-step #shift}
(b) If $\abs{a_n}\le cn^k$ and $F\equiv0$, then $G(s)=F(s+k)=\sum_n b_nn^{-s}$ with $b_n=a_nn^{-k}$ satisfies $\abs{b_n}\le c$ and $G\equiv0$.

::: pf-proof
$a_nn^{-k}n^{-s}=a_nn^{-(s+k)}$, so the series for $G$ is the series for $F$ with $s$ replaced by $s+k$, and it vanishes identically because $F$ does. The bound is $\abs{b_n}=\abs{a_n}n^{-k}\le c$.
:::

:::

::: {.pf-step}
(b) $\boxed{a_n=0\text{ for all }n}$, so a Dirichlet series with polynomially bounded coefficients is determined by its values.

::: pf-proof
Apply step [](#part-a){.pf-ref} to $G$, whose coefficients are bounded by $c$: for each $\sigma>1$,
$$
0=\lim_{T\to\infty}\frac1{2T}\int_{-T}^T\abs{G(\sigma+it)}^2dt=\sum_{n\ge1}\frac{\abs{b_n}^2}{n^{2\sigma}},
$$
the left-hand side being $0$ because $G\equiv0$. Every term of the right-hand series is non-negative, so the sum vanishes only if each $\abs{b_n}^2=0$, that is $b_n=0$ and hence $a_n=n^kb_n=0$ for every $n$.
:::

:::

:::
:::
