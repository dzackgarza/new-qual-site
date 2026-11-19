---
schema: qual/card@1
id: E-SS7.EX-4
kind: problem
title: "Dirichlet L-series for periodic coefficients"
classification:
  areas:
  - complex-analysis
  topics: ['Zeta Function', 'Prime Number Theorem', 'Dirichlet Series']
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
    Lamport structure over the prose that was already there. The Mellin identity and the
    interchange of sum and integral are now separate steps with the absolute convergence
    that licenses the interchange named, the identity sum a_n e^(-nx) = Q(x)/(e^(qx)-1) is
    derived from the geometric series with the reindexing m = q - r written out, the
    holomorphy of xQ(x)/(e^(qx)-1) at 0 is proved from the vanishing of its numerator to
    first order, and the subtraction of Taylor terms is stated for each N with the range of
    holomorphy of the remainder. The cancellation by 1/Gamma and the residue at s = 1 are
    their own steps. Not checked: the book's own text of the exercise, since no copy of
    Stein and Shakarchi is retained in this checkout; the statement is as transcribed on the
    card. No retained solution set covers the exercise (the collection's provenance is a
    Google Books record), so the argument is the card's own. No statement repair.
---

::: {.exercise}
Suppose $\{a_n\}_{n=1}^{\infty}$ is a sequence of complex numbers such that $a_n = a_m$ if $n \equiv m \bmod q$ for some positive integer $q$. Define the Dirichlet $L$-series associated to $\{a_n\}$ by
$$
L(s) = \sum_{n=1}^{\infty} \frac{a_n}{n^s} \quad \text{for } \Re(s) > 1.
$$
Also, with $a_0 = a_q$, let
$$
Q(x) = \sum_{m=0}^{q-1} a_{q-m} e^{mx}.
$$
Show, as in Exercises 15 and 16 of the previous chapter, that
$$
L(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} \frac{Q(x)\, x^{s-1}}{e^{qx} - 1}\, dx, \quad \text{for } \Re(s) > 1.
$$
Prove as a result that $L(s)$ is continuable into the complex plane, with the only possible singularity a pole at $s = 1$. In fact, $L(s)$ is regular at $s = 1$ if and only if $\sum_{m=0}^{q-1} a_m = 0$. Note the connection with the Dirichlet $L(s, \chi)$ series, taken up in Book I, Chapter 8, and that as a consequence, $L(s, \chi)$ is regular at $s = 1$ if and only if $\chi$ is a non-trivial character.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Fix $q\ge1$ and a $q$-periodic sequence $(a_n)$ with $a_0:=a_q$, put
$$
Q(x)=\sum_{m=0}^{q-1}a_{q-m}e^{mx},\qquad A=\sum_{r=1}^{q}a_r=Q(0),
$$
note $Q(x)=\sum_{r=1}^{q}a_re^{(q-r)x}$ by the change of index $m=q-r$, and let $L(s)=\sum_{n\ge1}a_nn^{-s}$ for $\operatorname{Re}s>1$, absolutely convergent there since $(a_n)$ is bounded and $\sum n^{-\sigma}$ converges for $\sigma>1$.

::: pf

::: {.pf-step #mellin}
For $\operatorname{Re}s>1$ and $n\ge1$, $\displaystyle n^{-s}=\frac{1}{\Gamma(s)}\int_0^\infty x^{s-1}e^{-nx}\,dx$.

::: pf-proof
In the gamma integral substitute $x=u/n$, $dx=du/n$: $\int_0^\infty x^{s-1}e^{-nx}dx=n^{-s}\int_0^\infty u^{s-1}e^{-u}du=n^{-s}\Gamma(s)$. The substitution is legitimate for $\operatorname{Re}s>0$ by the change of variables formula for the convergent integral, and $\Gamma(s)\ne0$, so division is allowed.
:::

:::

::: {.pf-step #geometric}
For $x>0$, $\displaystyle\sum_{n\ge1}a_ne^{-nx}=\frac{Q(x)}{e^{qx}-1}$.

::: pf-proof
Group the series by residue class modulo $q$: $\sum_{n\ge1}a_ne^{-nx}=\sum_{k\ge0}\sum_{r=1}^{q}a_re^{-(kq+r)x}$. Since $\abs{e^{-qx}}<1$, the inner expression factors as $\bigl(\sum_r a_re^{-rx}\bigr)\sum_ke^{-kqx}=\bigl(\sum_ra_re^{-rx}\bigr)/(1-e^{-qx})$ by the geometric series, the double series converging absolutely for $x>0$ because $(a_n)$ is bounded. Multiplying numerator and denominator by $e^{qx}$ turns this into $\sum_ra_re^{(q-r)x}/(e^{qx}-1)=Q(x)/(e^{qx}-1)$, using the display of the introduction.
:::

:::

::: {.pf-step #formula}
For $\operatorname{Re}s>1$,
$$
L(s)=\frac{1}{\Gamma(s)}\int_0^\infty\frac{Q(x)\,x^{s-1}}{e^{qx}-1}\,dx .
$$

::: pf-proof
Insert step [](#mellin){.pf-ref} into the series and interchange sum and integral:
$$
L(s)=\frac{1}{\Gamma(s)}\sum_{n\ge1}a_n\int_0^\infty x^{s-1}e^{-nx}dx=\frac{1}{\Gamma(s)}\int_0^\infty x^{s-1}\sum_{n\ge1}a_ne^{-nx}\,dx=\frac{1}{\Gamma(s)}\int_0^\infty\frac{Q(x)x^{s-1}}{e^{qx}-1}dx,
$$
the last equality by step [](#geometric){.pf-ref}. The interchange is Fubini's theorem for the double integral of $\abs{a_n}x^{\sigma-1}e^{-nx}$, whose total is $\Gamma(\sigma)\sum\abs{a_n}n^{-\sigma}<\infty$ by step [](#mellin){.pf-ref} and the absolute convergence of $L(\sigma)$.
:::

:::

::: {.pf-step #H}
$H(x)=\dfrac{xQ(x)}{e^{qx}-1}$ extends holomorphically to a neighbourhood of $0$, with $H(0)=\dfrac{Q(0)}{q}=\dfrac{A}{q}$; and $\dfrac{\abs{Q(x)}}{e^{qx}-1}\le Ce^{-qx/2}$ for $x\ge1$.

::: pf-proof
Both $xQ(x)$ and $e^{qx}-1$ are holomorphic near $0$, and the denominator vanishes only at the points $2\pi ik/q$, so away from $0$ it is nonzero near $0$; at $0$ both vanish to first order: $(e^{qx}-1)'=qe^{qx}$ is $q\ne0$ at $0$, and $(xQ(x))'=Q(0)=A$. So the quotient has a removable singularity at $0$ and extends holomorphically, with value $A/q$ by the quotient of the first-order terms. For $x\ge1$: $Q$ is a continuous $q$-periodic function of $x$ times a bounded factor, so $\abs{Q(x)}\le C_1$, and $e^{qx}-1\ge\frac12e^{qx}$ once $x\ge1$, giving the display with $C=2C_1$.
:::

:::

::: {.pf-step #subtract}
With $H(x)=\sum_{m\ge0}c_mx^m$ near $0$, for every $N\ge1$ and every $s$ with $\operatorname{Re}s>1-N$,
$$
\int_0^1\frac{Q(x)x^{s-1}}{e^{qx}-1}\,dx=\sum_{m=0}^{N-1}\frac{c_m}{s+m-1}+R_N(s),
$$
where $R_N$ is holomorphic on $\operatorname{Re}s>1-N$.

::: pf-proof
Since $H(x)=xQ(x)/(e^{qx}-1)$, the integrand is $x^{s-2}H(x)$. Subtract the Taylor polynomial of order $N-1$: $H(x)=\sum_{m<N}c_mx^m+x^{N}H_N(x)$ with $H_N$ holomorphic near $0$, so the integrand is $\sum_{m<N}c_mx^{s+m-2}+x^{s+N-2}H_N(x)$. Term by term, $\int_0^1x^{s+m-2}dx=\frac{1}{s+m-1}$ for $\operatorname{Re}s>1-m$, which is the case when $\operatorname{Re}s>1-N$; and $\abs{x^{s+N-2}H_N(x)}\le C_Nx^{\sigma+N-2}$ near $0$, integrable exactly when $\sigma>1-N$, while holomorphy in $s$ follows from dominated convergence on compact subsets. Summing the finitely many terms gives the display with $R_N(s)=\int_0^1x^{s+N-2}H_N(x)dx$.
:::

:::

::: {.pf-step #continue}
$L$ extends to a meromorphic function on $\CC$ whose only possible pole is $s=1$, where the residue is $A/q$.

::: pf-proof
By step [](#formula){.pf-ref} and step [](#subtract){.pf-ref} applied to $[0,1]$, and the exponential decay of step [](#H){.pf-ref} on $[1,\infty)$ which gives an entire function $\int_1^\infty x^{s-1}Q(x)/(e^{qx}-1)dx$,
$$
\Gamma(s)L(s)=\sum_{m=0}^{N-1}\frac{c_m}{s+m-1}+R_N(s)+G(s)
$$
on $\operatorname{Re}s>1-N$, with $G$ entire. The right side is meromorphic on that half-plane with possible simple poles at $s=1-m$, $m=0,\dots,N-1$, that is at $s=1,0,-1,\dots,2-N$. For $m\ge1$ the factor $1/\Gamma(s)$ vanishes at $s=1-m$, a non-positive integer, so those poles disappear in $L=\Gamma(s)L(s)/\Gamma(s)$; the term $m=0$ contributes $c_0/(s-1)$, and $c_0=H(0)=A/q$ by step [](#H){.pf-ref}. Since $N$ was arbitrary, $L$ is meromorphic on all of $\CC$ with $s=1$ the only possible pole, of residue $c_0/\Gamma(1)=A/q$ because $\Gamma(1)=1$.
:::

:::

::: {.pf-step #regular}
$L$ is regular at $s=1$ if and only if $\sum_{r=1}^{q}a_r=0$.

::: pf-proof
By step [](#continue){.pf-ref}, $\Gamma(s)L(s)=\frac{c_0}{s-1}+(\text{holomorphic near }1)$ with $c_0=A/q$. If $A\ne0$ then $\Gamma(s)L(s)$ has a simple pole at $1$ with nonzero residue, and since $\Gamma$ is holomorphic and nonzero at $1$, $L$ itself has a simple pole there. If $A=0$ then $\Gamma(s)L(s)$ is holomorphic near $1$, so $L=\Gamma(s)L(s)/\Gamma(s)$ is holomorphic near $1$ because $\Gamma(1)=1\ne0$.
:::

:::

::: {.pf-step #characters}
For a Dirichlet character $\chi$ modulo $q$, $L(s,\chi)$ is regular at $s=1$ if and only if $\chi$ is nontrivial.

::: pf-proof
A character modulo $q$ gives the $q$-periodic sequence $a_n=\chi(n)$, with the convention $\chi(n)=0$ when $q\mid n$; then $L(s,\chi)$ is the Dirichlet series above, and its behaviour at $1$ is governed by $\sum_{r=1}^{q}\chi(r)$ by step [](#regular){.pf-ref}. For $\chi$ nontrivial the values $\chi(r)$ over a complete residue system sum to $0$: choosing $c$ with $\chi(c)\ne1$ and $r\mapsto cr$ permuting the reduced classes, $\sum_r\chi(r)=\sum_r\chi(cr)=\chi(c)\sum_r\chi(r)$ forces the sum to vanish. For the principal character $\chi_0$ the sum is $\varphi(q)\ne0$ for $q\ge2$, so $L(s,\chi_0)$ has the pole at $s=1$, as $\zeta$ does when $q=1$. This is the stated connection with Book I, Chapter 8.
:::

:::

:::

:::
