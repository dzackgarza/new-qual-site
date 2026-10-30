---
schema: qual/card@1
id: P-UCLAB11S-12
kind: problem
title: Contraction mapping iteration for the equation f prime equals f
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2011.
---
::: {.problem}
Let $0<c<1$ and let $M=C([0,c])$ with the uniform metric
$$
d(f,g)=\sup_{0\le t\le c}\abs{f(t)-g(t)}.
$$
Define
$$
(Tf)(x)=1+\int_0^x f(t)\,dt.
$$
Recall that every contraction of a complete metric space has a unique fixed point.

::: pf

::: pf-step

Use this fixed-point theorem to obtain the solution of
$$
f'(t)=f(t),\qquad f(0)=1,
$$
carefully explaining why the theorem applies.

:::

::: pf-step

Determine the successive approximations $T(0),T^2(0),T^3(0),\ldots$.

:::

:::

:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

The space
$$
M=C([0,c])
$$
with the uniform metric is complete.

::: pf-proof

Let
$$
(f_n)
$$
be a Cauchy sequence in the supremum norm.
For each
$$
x\in[0,c],
$$
the scalar sequence
$$
(f_n(x))
$$
is Cauchy in $\RR$, so define
$$
f(x)=\lim_{n\to\infty}f_n(x).
$$

Given $\varepsilon>0$, choose $N$ such that
$$
\norm{f_n-f_m}_\infty<\varepsilon
$$
for all $m,n\ge N$.
Fix $n\ge N$ and let $m\to\infty$ pointwise.
Then
$$
\abs{f_n(x)-f(x)}
\le
\varepsilon
$$
for every $x$.
Hence
$$
\norm{f_n-f}_\infty\le\varepsilon.
$$
Thus $f_n\to f$ uniformly.
The uniform limit of continuous functions is continuous, so
$$
f\in M.
$$
Therefore $M$ is complete.

:::

:::

::: {.pf-step #p2-s2}

The operator $T$ maps $M$ into itself.

::: pf-proof

If
$$
f\in C([0,c]),
$$
then
$$
x\longmapsto
\int_0^x f(t)\,dt
$$
is continuously differentiable by the fundamental theorem of calculus, hence continuous.
Therefore
$$
(Tf)(x)
=
1+\int_0^x f(t)\,dt
$$
is continuous on $[0,c]$.
Thus
$$
Tf\in M.
$$

:::

:::

::: {.pf-step #p2-s3}

For all
$$
f,g\in M,
$$
one has
$$
\norm{Tf-Tg}_\infty
\le
c\norm{f-g}_\infty.
$$

::: pf-proof

For
$$
x\in[0,c],
$$
$$
\begin{aligned}
\abs{(Tf)(x)-(Tg)(x)}
&=
\abs{
\int_0^x(f(t)-g(t))\,dt
}\\
&\le
\int_0^x\abs{f(t)-g(t)}\,dt\\
&\le
x\norm{f-g}_\infty\\
&\le
c\norm{f-g}_\infty.
\end{aligned}
$$
Taking the supremum over $x$ gives the claim.

:::

:::

::: {.pf-step #p2-s4}

The map $T$ is a contraction of the complete metric space $M$.

::: pf-proof

By step [](#p2-s1){.pf-ref}, $M$ is complete.
By step [](#p2-s2){.pf-ref}, $T:M\to M$.
By step [](#p2-s3){.pf-ref},
$$
d(Tf,Tg)
\le
c\,d(f,g).
$$
Since
$$
0<c<1,
$$
the contraction constant is strictly less than $1$.

:::

:::

::: {.pf-step #p2-s5}

Therefore $T$ has a unique fixed point
$$
f\in M.
$$

::: pf-proof

Apply the contraction mapping theorem to step [](#p2-s4){.pf-ref}.
There exists a unique
$$
f\in M
$$
such that
$$
Tf=f.
$$

:::

:::

::: {.pf-step #p2-s6}

The fixed-point identity is
$$
\boxed{
f(x)
=
1+\int_0^x f(t)\,dt.
}
$$

::: pf-proof

The equation
$$
Tf=f
$$
means exactly the displayed identity by the definition of $T$.

:::

:::

::: {.pf-step #p2-s7}

The fixed point satisfies
$$
f'(x)=f(x)
$$
for
$$
0\le x\le c,
$$
and
$$
f(0)=1.
$$

::: pf-proof

The function $f$ is continuous because
$$
f\in M.
$$
Differentiate the integral equation in step [](#p2-s6){.pf-ref} using the fundamental theorem of calculus:
$$
f'(x)=f(x).
$$
Setting
$$
x=0
$$
in step [](#p2-s6){.pf-ref} gives
$$
f(0)=1.
$$

:::

:::

::: {.pf-step #p2-s8}

The unique fixed point is
$$
\boxed{f(x)=e^x}.
$$

::: pf-proof

The function
$$
e^x
$$
satisfies
$$
\frac d{dx}e^x=e^x
$$
and
$$
e^0=1.
$$
Equivalently,
$$
e^x
=
1+\int_0^xe^t\,dt,
$$
so it is a fixed point of $T$.
By uniqueness from step [](#p2-s5){.pf-ref}, it is the only fixed point.
This solves part step [](#p2-s1){.pf-ref}.

:::

:::

::: {.pf-step #p2-s9}

Starting with the zero function,
$$
\boxed{T(0)=1}.
$$

::: pf-proof

For every $x$,
$$
(T0)(x)
=
1+\int_0^x0\,dt
=1.
$$

:::

:::

::: {.pf-step #p2-s10}

One has
$$
\boxed{T^2(0)(x)=1+x}.
$$

::: pf-proof

Using step [](#p2-s9){.pf-ref},
$$
\begin{aligned}
T^2(0)(x)
&=
T(1)(x)\\
&=
1+\int_0^x1\,dt\\
&=
1+x.
\end{aligned}
$$

:::

:::

::: {.pf-step #p2-s11}

One has
$$
\boxed{
T^3(0)(x)
=
1+x+\frac{x^2}{2}.
}
$$

::: pf-proof

Using step [](#p2-s10){.pf-ref},
$$
\begin{aligned}
T^3(0)(x)
&=
T(1+x)(x)\\
&=
1+\int_0^x(1+t)\,dt\\
&=
1+x+\frac{x^2}{2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #p2-s12}

For every positive integer $n$,
$$
\boxed{
T^n(0)(x)
=
\sum_{k=0}^{n-1}
\frac{x^k}{k!}.
}
$$

::: pf-proof

Proceed by induction on $n$.
The case
$$
n=1
$$
is step [](#p2-s9){.pf-ref}.

Assume
$$
T^n(0)(x)
=
\sum_{k=0}^{n-1}
\frac{x^k}{k!}.
$$
Then
$$
\begin{aligned}
T^{n+1}(0)(x)
&=
1
+
\int_0^x
\sum_{k=0}^{n-1}
\frac{t^k}{k!}
\,dt\\
&=
1
+
\sum_{k=0}^{n-1}
\frac{x^{k+1}}{(k+1)!}\\
&=
\sum_{k=0}^{n}
\frac{x^k}{k!}.
\end{aligned}
$$
Thus the formula holds for all $n$.

:::

:::

::: {.pf-step #p2-s13}

The successive approximations converge uniformly to the fixed point $e^x$ on $[0,c]$.

::: pf-proof

The contraction mapping theorem implies that the iterates of any starting point, in particular the zero function, converge in the uniform metric to the unique fixed point.
Thus
$$
T^n(0)\to e^x
$$
uniformly.
The explicit formula from step [](#p2-s12){.pf-ref} is the sequence of partial sums of the exponential series.

:::

:::

::: pf-qed

Steps [](#p2-s1){.pf-ref}, [](#p2-s2){.pf-ref}, [](#p2-s3){.pf-ref}, [](#p2-s4){.pf-ref}, [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref}, [](#p2-s7){.pf-ref} and [](#p2-s8){.pf-ref} solve part step [](#p2-s1){.pf-ref}, and steps [](#p2-s9){.pf-ref}, [](#p2-s10){.pf-ref}, [](#p2-s11){.pf-ref}, [](#p2-s12){.pf-ref} and [](#p2-s13){.pf-ref} determine the successive approximations in part step [](#p2-s2){.pf-ref}.

:::

:::

:::
