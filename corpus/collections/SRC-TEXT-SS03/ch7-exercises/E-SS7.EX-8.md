---
schema: qual/card@1
id: E-SS7.EX-8
kind: problem
title: Infinitely many zeta zeros in the critical strip
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
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 8, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a)--(c) and the hint; the defect the card's own remark records (the book's
    $\xi$ has poles at $0$ and $1$, so $F$ has poles at $\pm\frac12$ and its $G$ is not entire) was
    confirmed against the print.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved with the pole-cancelling factor the remark asks for: $\Xi(s)=\frac12s(s-1)\xi(s)$ is
    entire, $\Xi(s)=\Xi(1-s)$, so $F_0(s)=\Xi(\frac12+s)=\frac12(s^2-\frac14)\xi(\frac12+s)$ is even and
    entire and equals $G_0(s^2)$ for an entire $G_0$ given by its power series in $s^2$. (b) bounds
    $(s-1)\zeta(s)$ on $\operatorname{Re}s\ge\frac12$ by Proposition 2.7 of Chapter 6 and on
    $\operatorname{Re}s\le\frac12$ by the functional equation with Stirling's formula, and transfers
    the bound to $G_0$ through $w=s^2$, giving order $\frac12$. (c) applies Hadamard's theorem
    (Chapter 5, Exercise 14) to $G_0$; its zeros $w$ give zeros $s$ of $F_0$, hence nontrivial zeros
    $\frac12+s$ of $\zeta$. Nothing is left in outline.
---

::: {.exercise}
The function $\zeta$ has infinitely many zeros in the critical strip. The book proposes the following argument.

(a) Let $F(s)=\xi(1/2+s)$, where $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$. Show that $F$ is even and that there exists $G$ with $G(s^2)=F(s)$.

(b) Show that $(s-1)\zeta(s)$ is entire of growth order $1$; that is, for every $\varepsilon>0$,
$$
\abs{(s-1)\zeta(s)}\leq A_\varepsilon e^{a_\varepsilon\abs{s}^{1+\varepsilon}}.
$$
As a consequence, show that $G$ has growth order $1/2$.

(c) Deduce that $\zeta$ has infinitely many zeros in the critical strip.
:::

::: {.hint}
For (a) and (b), use the functional equation for $\zeta$. For (c), use the result of Hadamard that an entire function of fractional order has infinitely many zeros (Chapter 5, Exercise 14).
:::

::: {.remark}
As printed, $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ has simple poles at $s=0$ and $s=1$. Thus $F$ has poles at $s=\pm1/2$, and the $G$ in (a) is meromorphic, so (b) cannot give it an entire growth order. The argument needs a pole-canceling factor before Hadamard's theorem applies.
:::

::: {.solution}

Put $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$, which is meromorphic with poles exactly at $s=0$ and $s=1$ and satisfies $\xi(s)=\xi(1-s)$, and set
$$
\Xi(s)=\tfrac12s(s-1)\,\xi(s),
$$
which is entire, because $s(s-1)$ cancels the two poles, and satisfies $\Xi(s)=\Xi(1-s)$ since $s(s-1)$ is unchanged under $s\mapsto1-s$. Its zeros are the zeros of $\Gamma(s/2)\zeta(s)$ other than $0$ and $1$; as $\Gamma$ has no zeros, they are exactly the nontrivial zeros of $\zeta$.

::: pf

::: {.pf-step #s1}

Part (a): $F_0(s)=\Xi\bigl(\tfrac12+s\bigr)$ is even and entire, and there is an entire $G_0$ with $G_0(s^2)=F_0(s)$.

::: pf-proof

By the functional equation,
$$
F_0(-s)=\Xi\bigl(\tfrac12-s\bigr)=\Xi\bigl(1-(\tfrac12+s)\bigr)=\Xi\bigl(\tfrac12+s\bigr)=F_0(s),
$$
so $F_0$ is even and entire. Write the power series $F_0(s)=\sum_{n\ge0}a_ns^n$; since $F_0$ is entire the series converges on $\CC$, and since $F_0$ is even the coefficients $a_n$ vanish for odd $n$. Hence
$$
G_0(w)=\sum_{k\ge0}a_{2k}w^k
$$
is an entire function of $w$ with $G_0(s^2)=F_0(s)$. Explicitly,
$$
F_0(s)=\tfrac12\Bigl(s^2-\tfrac14\Bigr)\xi\bigl(\tfrac12+s\bigr),
$$
which shows the evenness directly and shows that $F_0$ vanishes exactly where $\xi(\frac12+s)$ does, away from $s=\pm\frac12$.

This is the corrected form of the exercise's part (a): with the book's $\xi$ itself, $F(s)=\xi(\frac12+s)$ has poles at $s=\pm\frac12$, so only a *meromorphic* $G$ with $G(s^2)=F(s)$ exists. Multiplying by $s(s-1)$ is exactly the factor that makes it entire, and it is what allows part (b) to be applied in part (c).

:::

:::

::: {.pf-step #s2}

Part (b), first assertion: for every $\varepsilon>0$ there are constants with
$$
\abs{(s-1)\zeta(s)}\le A_\varepsilon e^{a_\varepsilon\abs{s}^{1+\varepsilon}} .
$$

::: pf-proof

The product $(s-1)\zeta(s)$ is entire (the simple pole of $\zeta$ at $s=1$ is cancelled).

*In the half-plane $\operatorname{Re}s\ge\tfrac12$.* By Proposition 2.7 of Chapter 6 with $\sigma_0=\tfrac12$, for $\abs{t}\ge1$,
$$
\abs{\zeta(s)}\le c_\varepsilon\abs{t}^{1-\frac12+\varepsilon}=c_\varepsilon\abs{t}^{\frac12+\varepsilon}\le c_\varepsilon(1+\abs{s})^{\frac12+\varepsilon},
$$
and $\abs{\zeta(s)}\le\zeta(\operatorname{Re}s)\le\zeta(\frac12)\cdot$ … for $\abs{t}\le1$ the function is continuous, so in all of $\operatorname{Re}s\ge\frac12$,
$$
\abs{(s-1)\zeta(s)}\le C_\varepsilon(1+\abs{s})^{\frac32+\varepsilon}\le A_\varepsilon e^{a_\varepsilon\abs{s}^{1+\varepsilon}} .
$$

*In the half-plane $\operatorname{Re}s\le\tfrac12$.* Here $\operatorname{Re}(1-s)\ge\frac12$, so by the previous paragraph applied at $1-s$,
$$
\abs{s\,\zeta(1-s)}\le C_\varepsilon(1+\abs{s})^{\frac32+\varepsilon},
$$
and by the functional equation $\zeta(s)=\pi^{s-1/2}\Gamma\bigl(\frac{1-s}{2}\bigr)\zeta(1-s)\big/\Gamma\bigl(\frac{s}{2}\bigr)$,
$$
\abs{(s-1)\zeta(s)}\le\pi^{\sigma-1/2}\abs{\frac{\Gamma\bigl(\frac{1-s}{2}\bigr)}{\Gamma\bigl(\frac{s}{2}\bigr)}}\cdot C_\varepsilon(1+\abs{s})^{\frac32+\varepsilon}.
$$
Stirling's formula (Chapter 6) in the form
$$
\log\abs{\Gamma(z)}=\bigl(\operatorname{Re}z-\tfrac12\bigr)\log\abs{z}-\operatorname{Re}z-\operatorname{Im}z\,\arg z+O(1)
$$
applied to $z_1=\frac{1-s}{2}$ and $z_2=\frac{s}{2}$, for which $\operatorname{Im}z_1=-\operatorname{Im}z_2=-\frac{t}{2}$ and $\arg z_1-\arg z_2$ stays in a bounded set once $\operatorname{Re}s\le\frac12$, gives
$$
\log\Bigl|\frac{\Gamma(z_1)}{\Gamma(z_2)}\Bigr|=\Bigl(\frac{1-\sigma}{2}-\frac{\sigma}{2}\Bigr)\log\tfrac{\abs{s}}{2}+O(1)+O\bigl(\abs{t}\bigr)\le O\bigl(\abs{s}\bigr),
$$
because the difference of the terms $-\operatorname{Im}z\,\arg z$ is $\frac{t}{2}\bigl(\arg z_1-\arg z_2\bigr)$ and $\arg z_1-\arg z_2$ is bounded. Hence $\abs{\Gamma(z_1)/\Gamma(z_2)}\le Ce^{c\abs{s}}$ and
$$
\abs{(s-1)\zeta(s)}\le C'_\varepsilon e^{c\abs{s}}(1+\abs{s})^{\frac32+\varepsilon}\le A_\varepsilon e^{a_\varepsilon\abs{s}^{1+\varepsilon}} .
$$
Enlarging the constants covers both half-planes.

:::

:::

::: {.pf-step #s3}

Part (b), second assertion: $G_0$ has growth order $\tfrac12$, that is $\abs{G_0(w)}\le A_\varepsilon e^{a_\varepsilon\abs{w}^{1/2+\varepsilon}}$.

::: pf-proof

First bound $\xi$: since $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)=\pi^{-s/2}\Gamma(s/2)(s-1)\zeta(s)/(s-1)$ and $\abs{\Gamma(s/2)}\le Ce^{c\abs{s}}$ by Stirling's formula as in step [](#s2){.pf-ref}, step [](#s2){.pf-ref} gives, for $\abs{s-1}\ge\frac12$,
$$
\abs{\xi(s)}\le C_\varepsilon e^{c_\varepsilon\abs{s}}e^{a_\varepsilon\abs{s}^{1+\varepsilon}}\le A'_\varepsilon e^{a'_\varepsilon\abs{s}^{1+\varepsilon}} .
$$
Hence
$$
\abs{F_0(s)}=\tfrac12\abs{s^2-\tfrac14}\abs{\xi\bigl(\tfrac12+s\bigr)}\le A''_\varepsilon e^{a''_\varepsilon\abs{s}^{1+\varepsilon}} .
$$
Now let $w\in\CC$ and choose $s$ with $s^2=w$; then $\abs{s}=\abs{w}^{1/2}$ and
$$
\abs{G_0(w)}=\abs{F_0(s)}\le A''_\varepsilon e^{a''_\varepsilon\abs{s}^{1+\varepsilon}}=A''_\varepsilon e^{a''_\varepsilon\abs{w}^{(1+\varepsilon)/2}}\le A''_\varepsilon e^{a''_\varepsilon\abs{w}^{1/2+\varepsilon'}}
$$
with $\varepsilon'=\varepsilon/2$ after enlarging the exponent. So $G_0$ is of growth order $\frac12$.

:::

:::

::: {.pf-step #s4}

Part (c): $\zeta$ has infinitely many zeros in the critical strip.

::: pf-proof

$G_0$ is entire of growth order $\frac12$, which is not an integer. By Hadamard's theorem as stated in Chapter 5, Exercise 14, an entire function whose order is finite and not an integer has infinitely many zeros.

Let $w$ be a zero of $G_0$ and $s$ with $s^2=w$; then $F_0(s)=G_0(s^2)=0$, so $\Xi\bigl(\frac12+s\bigr)=0$, so $\frac12+s$ is a zero of $\zeta$ at which $\Gamma\bigl(\frac{1}{4}+\frac{s}{2}\bigr)\ne0$, that is a nontrivial zero. Distinct zeros $w$ give distinct such zeros of $\zeta$ up to the sign of $s$, and the zeros of an even entire function come in pairs $\pm s$; hence infinitely many zeros of $G_0$ produce infinitely many nontrivial zeros of $\zeta$. By Theorem 1.1 those lie in $0\le\operatorname{Re}s\le1$, i.e. in the critical strip.

:::

:::

:::

:::
