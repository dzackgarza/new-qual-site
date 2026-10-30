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
Because $a_n$ has period $q$,
$$
\sum_{n=1}^\infty a_ne^{-nx}
=\sum_{k=0}^\infty\sum_{r=1}^q a_re^{-(kq+r)x}
=\frac{\sum_{r=1}^q a_re^{-rx}}{1-e^{-qx}}
=\frac{Q(x)}{e^{qx}-1}.
\tag{1}
$$
For $\Re s>1$, absolute convergence permits termwise integration, and
$$
\int_0^\infty e^{-nx}x^{s-1}\,dx=\Gamma(s)n^{-s}.
$$
Using (1),
$$
\Gamma(s)L(s)
=\int_0^\infty\frac{Q(x)x^{s-1}}{e^{qx}-1}\,dx,
$$
which proves the asserted formula.

For continuation, split the integral at $1$. The integral over $[1,\infty)$ is entire in $s$, because its integrand decays exponentially in $x$ uniformly on compact subsets of the $s$-plane.

Near $x=0$, the function
$$
H(x)=\frac{xQ(x)}{e^{qx}-1}
$$
is holomorphic, with
$$
H(0)=\frac{Q(0)}q=\frac1q\sum_{r=1}^q a_r.
$$
Write its Taylor expansion $H(x)=\sum_{m\ge0}c_mx^m$. For each $N$,
$$
\int_0^1\frac{Q(x)x^{s-1}}{e^{qx}-1}\,dx
=\sum_{m=0}^N\frac{c_m}{s+m-1}+R_N(s),
$$
where $R_N$ is holomorphic for $\Re s>-N$. Multiplication by $1/\Gamma(s)$ cancels every possible pole at $s=0,-1,-2,\ldots$. Hence $L(s)$ continues meromorphically to the whole plane with only a possible pole at $s=1$.

At $s=1$, its residue is
$$
\frac{c_0}{\Gamma(1)}=\frac1q\sum_{r=1}^q a_r.
$$
Therefore $L$ is regular at $s=1$ exactly when
$$
\sum_{r=1}^q a_r=0.
$$
For a nontrivial Dirichlet character modulo $q$, this sum is zero, whereas for the principal character it is nonzero; this gives the stated application to Dirichlet $L$-series.
:::
