---
schema: qual/card@1
id: P-BKF84-9
kind: problem
title: A contour formula for coefficientwise products of analytic functions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
---

::: {.problem}
Let $f$ and $g$ be analytic in the open unit disk, and let $C_r$ be the positively oriented circle $|w|=r$.

1. Prove that
\[
h(z)=\frac1{2\pi i}\int_{C_r}\frac1w f(w)g\!\left(\frac zw\right)\,dw
\]
is independent of $r$ whenever $|z|<r<1$, and that it defines an analytic function $h$ on $|z|<1$.

2. Prove or give a counterexample: if $f\not\equiv0$ and $g\not\equiv0$, then $h\not\equiv0$.
:::

::: {.solution}
Write
$$
f(w)=\sum_{n=0}^{\infty}a_nw^n,
\qquad
g(w)=\sum_{n=0}^{\infty}b_nw^n
$$
for the Taylor expansions at the origin.

::: pf

::: {.pf-step #s1}

If $\abs{z}<r<1$, then
$$
\frac1{2\pi i}\int_{C_r}\frac1w f(w)g\!\left(\frac zw\right)\,dw
=
\sum_{n=0}^{\infty}a_nb_nz^n.
$$

::: pf-proof

On $C_r$, the series for $f(w)$ converges absolutely and uniformly. Since
$$
\abs{z/w}=\frac{\abs{z}}{r}<1,
$$
the series
$$
g\!\left(\frac zw\right)
=
\sum_{m=0}^{\infty}b_mz^mw^{-m}
$$
also converges absolutely and uniformly on $C_r$. Hence their product may be integrated term by term:
$$
\begin{aligned}
\frac1{2\pi i}\int_{C_r}\frac1w f(w)g\!\left(\frac zw\right)\,dw
&=
\sum_{n,m\geq0}
a_nb_mz^m
\frac1{2\pi i}\int_{C_r}w^{n-m-1}\,dw\\
&=
\sum_{n=0}^{\infty}a_nb_nz^n,
\end{aligned}
$$
because the contour integral is $1$ when $n=m$ and $0$ otherwise.

:::

:::

::: {.pf-step #s2}

The series
$$
\sum_{n=0}^{\infty}a_nb_nz^n
$$
converges locally uniformly on the open unit disk and therefore defines an analytic function there.

::: pf-proof

Fix $0<\rho<1$. Choose $s$ with
$$
\sqrt{\rho}<s<1.
$$
Set
$$
M_f\coloneqq\max_{\abs{w}=s}\abs{f(w)},
\qquad
M_g\coloneqq\max_{\abs{w}=s}\abs{g(w)}.
$$
Cauchy's estimates give
$$
\abs{a_n}\leq \frac{M_f}{s^n},
\qquad
\abs{b_n}\leq \frac{M_g}{s^n}.
$$
Thus, for $\abs{z}\leq\rho$,
$$
\abs{a_nb_nz^n}
\leq
M_fM_g\left(\frac{\rho}{s^2}\right)^n.
$$
Since $\rho/s^2<1$, the Weierstrass $M$-test gives uniform convergence on $\abs{z}\leq\rho$. As $\rho<1$ was arbitrary, the series converges locally uniformly on the unit disk, hence its sum is analytic.

:::

:::

::: {.pf-step #s3}

The integral in part 1 is independent of $r$ whenever $\abs{z}<r<1$, and it defines the analytic function
$$
h(z)=\sum_{n=0}^{\infty}a_nb_nz^n.
$$

::: pf-proof

For every admissible $r$, step [](#s1){.pf-ref} identifies the integral with the same power series, which contains no occurrence of $r$. Step [](#s2){.pf-ref} shows that this common value is analytic for $\abs{z}<1$.

:::

:::

::: {.pf-step #s4}

The assertion in part 2 is false.

::: pf-proof

Take
$$
f(z)=1,
\qquad
g(z)=z.
$$
Both functions are analytic and nonzero. Their Taylor coefficients satisfy
$$
a_0=1,
\quad
a_n=0\ \text{for }n\geq1,
\qquad
b_1=1,
\quad
b_n=0\ \text{for }n\neq1.
$$
Hence $a_nb_n=0$ for every $n$, so step [](#s3){.pf-ref} gives
$$
h(z)\equiv0.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part 1, and step [](#s4){.pf-ref} supplies the required counterexample for part 2.

:::

:::

:::
