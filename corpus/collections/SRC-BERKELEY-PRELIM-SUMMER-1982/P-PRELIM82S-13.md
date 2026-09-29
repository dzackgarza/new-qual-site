---
schema: qual/card@1
id: P-PRELIM82S-13
kind: problem
title: Vanishing Fourier sine coefficients of a continuous function on $[0,\pi]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Writing sin(nx)=sin(x)U_{n-1}(cos x), the hypotheses become
    vanishing polynomial moments of g(t)=f(arccos t) on [-1,1].
    The U_m form a triangular polynomial basis, so g is orthogonal to
    every polynomial. Uniform polynomial approximation to g then gives
    integral g^2=0, and continuity forces g, hence f, to vanish.
---

::: {.problem}
Let $f:[0,\pi]\to\mathbb R$ be continuous and suppose
\[
\int_0^\pi f(x)\sin(nx)\,dx=0
\]
for every integer $n\ge1$.
Must $f$ be identically zero?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There are polynomials $U_m\in\RR[t]$ such that
$$
\sin((m+1)x)
=
\sin x\,U_m(\cos x)
$$
for every integer $m\geq0$, and $U_m$ has degree $m$ with leading
coefficient $2^m$.

::: pf-proof

::: {.pf-step #s1-1}

Define
$$
U_0(t)=1,
\qquad
U_1(t)=2t,
$$
and recursively
$$
U_{m+1}(t)=2tU_m(t)-U_{m-1}(t)
$$
for $m\geq1$.

::: pf-proof

This recursion defines a polynomial $U_m$ for every $m\geq0$.

:::

:::

::: {.pf-step #s1-2}

For every $m\geq0$,
$$
\sin((m+1)x)
=
\sin x\,U_m(\cos x).
$$

::: pf-proof

For $m=0$ and $m=1$, this is
$$
\sin x=\sin x
$$
and
$$
\sin(2x)=2\sin x\cos x.
$$
If the identity holds for $m$ and $m-1$, then the trigonometric
recurrence
$$
\sin((m+2)x)
=
2\cos x\sin((m+1)x)-\sin(mx)
$$
and step [](#s1-1){.pf-ref} give
$$
\sin((m+2)x)
=
\sin x\,U_{m+1}(\cos x).
$$
Induction proves the identity.

:::

:::

::: {.pf-step #s1-3}

The polynomial $U_m$ has degree $m$ and leading coefficient
$2^m$.

::: pf-proof

This is clear for $U_0$ and $U_1$. If it holds for $U_m$ and
$U_{m-1}$, then
$$
U_{m+1}(t)=2tU_m(t)-U_{m-1}(t).
$$
The first term has degree $m+1$ and leading coefficient $2^{m+1}$,
whereas the second has smaller degree. The claim follows by induction.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} establish step [](#s1){.pf-ref}.

:::

:::

:::

::: {.pf-step #s2}

Every polynomial in $\RR[t]$ is a finite linear combination of
the polynomials
$$
U_0,U_1,U_2,\ldots.
$$

::: pf-proof

For each $N\geq0$, step [](#s1){.pf-ref} shows that
$$
U_0,U_1,\ldots,U_N
$$
have respective degrees $0,1,\ldots,N$ and nonzero leading
coefficients. They are therefore linearly independent. Since the vector
space of real polynomials of degree at most $N$ has dimension $N+1$,
they form a basis of that space.

:::

:::

::: {.pf-step #s3}

Define
$$
g:[-1,1]\longrightarrow\RR,
\qquad
g(t)=f(\arccos t).
$$
Then for every polynomial $P\in\RR[t]$,
$$
\int_{-1}^1 g(t)P(t)\,dt=0.
$$

::: pf-proof

The function $g$ is continuous. For $m\geq0$, the hypothesis with
$n=m+1$ and step [](#s1){.pf-ref} give
$$
0
=
\int_0^\pi
f(x)\sin x\,U_m(\cos x)\,dx.
$$
With the substitution
$$
t=\cos x,
\qquad
dt=-\sin x\,dx,
$$
this becomes
$$
0
=
\int_{-1}^1 g(t)U_m(t)\,dt.
$$
By linearity and step [](#s2){.pf-ref}, the same identity holds with $U_m$ replaced
by any polynomial $P$.

:::

:::

::: {.pf-step #s4}

One has
$$
\int_{-1}^1 g(t)^2\,dt=0.
$$

::: pf-proof

By the Weierstrass approximation theorem, there is a sequence of
polynomials $P_k$ converging uniformly to $g$ on $[-1,1]$. Step [](#s3){.pf-ref}
gives
$$
\int_{-1}^1 g(t)P_k(t)\,dt=0
$$
for every $k$. Hence
$$
\begin{aligned}
\left|
\int_{-1}^1g(t)^2\,dt
\right|
&=
\left|
\int_{-1}^1g(t)(g(t)-P_k(t))\,dt
\right|\\
&\leq
2\norm{g}_{\infty}\norm{g-P_k}_{\infty}.
\end{aligned}
$$
The right-hand side tends to zero, proving the claim.

:::

:::

::: {.pf-step #s5}

The function $g$ is identically zero on $[-1,1]$.

::: pf-proof

The function $g^2$ is continuous and nonnegative. If
$g(t_0)\neq0$ at some $t_0\in[-1,1]$, continuity would make $g^2$
strictly positive on a nonempty interval relative to $[-1,1]$, giving
$$
\int_{-1}^1g(t)^2\,dt>0,
$$
contrary to step [](#s4){.pf-ref}. Thus $g\equiv0$.

:::

:::

::: {.pf-step #s6}

Therefore
$$
\boxed{f\equiv0\text{ on }[0,\pi]}.
$$

::: pf-proof

For every $x\in[0,\pi]$, one has
$$
\arccos(\cos x)=x.
$$
Thus step [](#s5){.pf-ref} gives
$$
f(x)=g(\cos x)=0.
$$

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} answers the question affirmatively.

:::

:::

:::
