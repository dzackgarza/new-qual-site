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
<1>1. There are polynomials $U_m\in\RR[t]$ such that
$$
\sin((m+1)x)
=
\sin x\,U_m(\cos x)
$$
for every integer $m\geq0$, and $U_m$ has degree $m$ with leading
coefficient $2^m$.

<2>1. Define
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

::: {.proof}
This recursion defines a polynomial $U_m$ for every $m\geq0$.
:::

<2>2. For every $m\geq0$,
$$
\sin((m+1)x)
=
\sin x\,U_m(\cos x).
$$

::: {.proof}
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
and step <2>1 give
$$
\sin((m+2)x)
=
\sin x\,U_{m+1}(\cos x).
$$
Induction proves the identity.
:::

<2>3. The polynomial $U_m$ has degree $m$ and leading coefficient
$2^m$.

::: {.proof}
This is clear for $U_0$ and $U_1$. If it holds for $U_m$ and
$U_{m-1}$, then
$$
U_{m+1}(t)=2tU_m(t)-U_{m-1}(t).
$$
The first term has degree $m+1$ and leading coefficient $2^{m+1}$,
whereas the second has smaller degree. The claim follows by induction.
:::

<2>4. Q.E.D.

::: {.proof}
Steps <2>2 and <2>3 establish step <1>1.
:::

<1>2. Every polynomial in $\RR[t]$ is a finite linear combination of
the polynomials
$$
U_0,U_1,U_2,\ldots.
$$

::: {.proof}
For each $N\geq0$, step <1>1 shows that
$$
U_0,U_1,\ldots,U_N
$$
have respective degrees $0,1,\ldots,N$ and nonzero leading
coefficients. They are therefore linearly independent. Since the vector
space of real polynomials of degree at most $N$ has dimension $N+1$,
they form a basis of that space.
:::

<1>3. Define
$$
g:[-1,1]\longrightarrow\RR,
\qquad
g(t)=f(\arccos t).
$$
Then for every polynomial $P\in\RR[t]$,
$$
\int_{-1}^1 g(t)P(t)\,dt=0.
$$

::: {.proof}
The function $g$ is continuous. For $m\geq0$, the hypothesis with
$n=m+1$ and step <1>1 give
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
By linearity and step <1>2, the same identity holds with $U_m$ replaced
by any polynomial $P$.
:::

<1>4. One has
$$
\int_{-1}^1 g(t)^2\,dt=0.
$$

::: {.proof}
By the Weierstrass approximation theorem, there is a sequence of
polynomials $P_k$ converging uniformly to $g$ on $[-1,1]$. Step <1>3
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

<1>5. The function $g$ is identically zero on $[-1,1]$.

::: {.proof}
The function $g^2$ is continuous and nonnegative. If
$g(t_0)\neq0$ at some $t_0\in[-1,1]$, continuity would make $g^2$
strictly positive on a nonempty interval relative to $[-1,1]$, giving
$$
\int_{-1}^1g(t)^2\,dt>0,
$$
contrary to step <1>4. Thus $g\equiv0$.
:::

<1>6. Therefore
$$
\boxed{f\equiv0\text{ on }[0,\pi]}.
$$

::: {.proof}
For every $x\in[0,\pi]$, one has
$$
\arccos(\cos x)=x.
$$
Thus step <1>5 gives
$$
f(x)=g(\cos x)=0.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 answers the question affirmatively.
:::
:::
