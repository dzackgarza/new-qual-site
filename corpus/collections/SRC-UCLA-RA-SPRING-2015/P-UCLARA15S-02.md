---
schema: qual/card@1
id: P-UCLARA15S-02
kind: problem
title: Dyadic annulus bounds imply $fg\in L^1$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^2_{\mathrm{loc}}(\RR^n)$ and $g\in L^3_{\mathrm{loc}}(\RR^n)$.
Assume that for all real $r\ge1$,
$$
\int_{r\le|x|\le2r}|f(x)|^2\,dx\le r^a,
\qquad
\int_{r\le|x|\le2r}|g(x)|^3\,dx\le r^b.
$$
Here $a,b\in\RR$ satisfy $3a+2b+n<0$.
Show that $fg\in L^1(\RR^n)$.
:::

::: {.solution}

Let
$$
E_0\coloneqq\{x:|x|\le1\},
\qquad
E_k\coloneqq
\{x:2^{k-1}\le|x|\le2^k\}
\quad(k\ge1).
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\int_{E_0}|f(x)g(x)|\,dx<\infty.
$$


::: pf-proof

On the bounded set $E_0$, Hölder's inequality with exponents $2$, $3$, and $6$ gives
$$
\begin{aligned}
\int_{E_0}|fg|
&\le
\left(\int_{E_0}|f|^2\right)^{1/2}
\left(\int_{E_0}|g|^3\right)^{1/3}
m(E_0)^{1/6}.
\end{aligned}
$$
The first two factors are finite by local $L^2$ and $L^3$ integrability, and $m(E_0)<\infty$.

:::

:::

::: {.pf-step #s1-2}

For every $k\ge1$,
$$
\int_{E_k}|fg|
\le
C_n
2^{(k-1)(n/6+a/2+b/3)}
$$
for a constant $C_n$ independent of $k$.


::: pf-proof

Apply Hölder's inequality on $E_k$ with exponents $6$, $2$, and $3$:
$$
\int_{E_k}|fg|
\le
m(E_k)^{1/6}
\left(\int_{E_k}|f|^2\right)^{1/2}
\left(\int_{E_k}|g|^3\right)^{1/3}.
$$
Since
$$
E_k
\subset
[-2^k,2^k]^n,
$$
there is a dimensional constant $C_n$ such that
$$
m(E_k)^{1/6}
\le
C_n2^{kn/6}.
$$
Using the hypotheses with $r=2^{k-1}$,
$$
\left(\int_{E_k}|f|^2\right)^{1/2}
\le
2^{(k-1)a/2},
$$
and
$$
\left(\int_{E_k}|g|^3\right)^{1/3}
\le
2^{(k-1)b/3}.
$$
Therefore
$$
\int_{E_k}|fg|
\le
C_n
2^{kn/6}
2^{(k-1)a/2}
2^{(k-1)b/3}.
$$
Absorbing the fixed factor $2^{n/6}$ into $C_n$ gives the claimed estimate.

:::

:::

::: {.pf-step #s1-3}

The series
$$
\sum_{k=1}^{\infty}
\int_{E_k}|fg|
$$
converges.


::: pf-proof

Set
$$
\gamma
\coloneqq
\frac n6+\frac a2+\frac b3
=
\frac{n+3a+2b}{6}.
$$
The hypothesis gives $\gamma<0$. By step [](#s1-2){.pf-ref},
$$
\sum_{k=1}^{\infty}
\int_{E_k}|fg|
\le
C_n
\sum_{k=1}^{\infty}
2^{(k-1)\gamma}.
$$
The last series is geometric with ratio $2^\gamma<1$, hence converges.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{fg\in L^1(\RR^n)}.
$$


::: pf-proof

The sets
$$
E_0,E_1,E_2,\dots
$$
cover $\RR^n$ up to their boundary overlaps, which have measure zero. Hence, by nonnegativity,
$$
\int_{\RR^n}|fg|
\le
\int_{E_0}|fg|
+
\sum_{k=1}^{\infty}\int_{E_k}|fg|.
$$
The first term is finite by step [](#s1-1){.pf-ref} and the series is finite by step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
