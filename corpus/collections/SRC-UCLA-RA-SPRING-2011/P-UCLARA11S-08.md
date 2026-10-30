---
schema: qual/card@1
id: P-UCLARA11S-08
kind: problem
title: Subharmonic functions, pointwise extrema, and norms of holomorphic matrix functions
classification: {areas: [complex-analysis], topics: [Subharmonic Functions, Holomorphic Functions]}
relations: []
review: draft
---

::: {.problem}
(a) Define upper-semicontinuity for functions $f:\CC\to[-\infty,\infty)$.

(b) Define what it means for such an upper-semicontinuous function to be subharmonic.

(c) Prove or refute, with a counterexample, each statement:

- The pointwise supremum of a bounded family of subharmonic functions is subharmonic.

- The pointwise infimum of a family of subharmonic functions is subharmonic.

(d) Let $A(z)$ be a $2\times2$ matrix-valued holomorphic function, meaning that its entries are holomorphic.
Show that
$$
z\longmapsto \log\norm{A(z)}
$$
is subharmonic, where $\norm{A(z)}$ is the operator norm on $\CC^2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A function
$$
u:\CC\to[-\infty,\infty)
$$
is upper-semicontinuous if for every $z_0\in\CC$,
$$
\limsup_{z\to z_0}u(z)
\le
u(z_0).
$$


::: pf-proof

This is the definition. Equivalently, for every $a\in\RR$, the sublevel set
$$
\{z:u(z)<a\}
$$
is open.

:::

:::

::: {.pf-step #s1-2}

An upper-semicontinuous function
$$
u:\CC\to[-\infty,\infty)
$$
is subharmonic if it is not identically $-\infty$ and for every closed disk
$$
\overline{B(z_0,r)}
\subset\CC,
$$
one has the sub-mean-value inequality
$$
u(z_0)
\le
\frac1{2\pi}
\int_0^{2\pi}
u(z_0+re^{i\theta})\,d\theta.
$$


::: pf-proof

This is the standard definition of subharmonicity on an open set, specialized to the whole plane.

:::

:::

::: {.pf-step #s1-3}

The pointwise supremum of a bounded family of subharmonic functions need not be subharmonic.


::: pf-proof

For $n\ge1$, define
$$
u_n(z)
\coloneqq
\frac1n\log\abs{z},
$$
with
$$
u_n(0)=-\infty.
$$
Each $u_n$ is subharmonic on $\CC$. The family is locally uniformly bounded above: on
$$
\abs{z}\le R,
$$
one has
$$
u_n(z)
\le
\max\{0,\log R\}.
$$

Its pointwise supremum is
$$
u(z)
\coloneqq
\sup_{n\ge1}u_n(z)
=
\begin{cases}
-\infty,&z=0,\\
0,&0<\abs{z}\le1,\\
\log\abs{z},&\abs{z}>1.
\end{cases}
$$
Indeed, when $0<\abs{z}<1$, the negative numbers
$$
\frac1n\log\abs{z}
$$
increase to $0$, while for $\abs{z}>1$ their supremum occurs at $n=1$.

But
$$
\limsup_{z\to0}u(z)=0
>
-\infty=u(0),
$$
so $u$ is not upper-semicontinuous and therefore not subharmonic.

:::

:::

::: {.pf-step #s1-4}

The pointwise infimum of a family of subharmonic functions need not be subharmonic.


::: pf-proof

The harmonic functions
$$
u_1(z)=\operatorname{Re}z,
\qquad
u_2(z)=-\operatorname{Re}z
$$
are subharmonic. Their pointwise infimum is
$$
u(z)
=
\min\{\operatorname{Re}z,-\operatorname{Re}z\}
=
-\abs{\operatorname{Re}z}.
$$
At $z=0$,
$$
u(0)=0.
$$
On the circle $\abs{z}=r$,
$$
u(re^{i\theta})
=
-r\abs{\cos\theta}.
$$
Hence
$$
\frac1{2\pi}
\int_0^{2\pi}
u(re^{i\theta})\,d\theta
<
0
=
u(0).
$$
Thus the sub-mean-value inequality fails at $0$, so $u$ is not subharmonic.

:::

:::

::: {.pf-step #s1-5}

This settles part (c): both assertions are false.


::: pf-proof

Step [](#s1-3){.pf-ref} refutes the supremum assertion, and step [](#s1-4){.pf-ref} refutes the infimum assertion.

:::

:::

::: {.pf-step #s1-6}

Let
$$
v(z)
\coloneqq
\log\norm{A(z)},
$$
with the convention
$$
v(z)=-\infty
$$
when $A(z)=0$. Then $v$ is upper-semicontinuous.


::: pf-proof

The matrix entries of $A$ are holomorphic, hence continuous, and the operator norm is a continuous function of the matrix entries. Thus
$$
z\longmapsto\norm{A(z)}
$$
is continuous.

At points where $\norm{A(z_0)}>0$, composition with the continuous logarithm gives continuity of $v$. If $A(z_0)=0$, then
$$
\norm{A(z)}\to0
\qquad
(z\to z_0),
$$
so
$$
\log\norm{A(z)}\to-\infty=v(z_0).
$$
Hence $v$ is upper-semicontinuous everywhere.

:::

:::

::: {.pf-step #s1-7}

Suppose $A(z_0)\ne0$. There exist unit vectors $x,y\in\CC^2$ such that
$$
\abs{\langle A(z_0)x,y\rangle}
=
\norm{A(z_0)}.
$$


::: pf-proof

Because the unit sphere of $\CC^2$ is compact, there is a unit vector $x$ with
$$
\norm{A(z_0)x}
=
\norm{A(z_0)}.
$$
Set
$$
y
\coloneqq
\frac{A(z_0)x}{\norm{A(z_0)x}}.
$$
Then $\norm{y}=1$ and
$$
\abs{\langle A(z_0)x,y\rangle}
=
\norm{A(z_0)x}
=
\norm{A(z_0)}.
$$

:::

:::

::: {.pf-step #s1-8}

For fixed vectors $x,y\in\CC^2$, the scalar function
$$
h(z)
\coloneqq
\langle A(z)x,y\rangle
$$
is holomorphic, and
$$
\log\abs{h(z)}
$$
is subharmonic.


::: pf-proof

The function $h$ is a fixed complex linear combination of the holomorphic entries of $A$, hence holomorphic. The logarithm of the modulus of a holomorphic function is subharmonic, with value $-\infty$ at its zeros.

:::

:::

::: {.pf-step #s1-9}

For every disk centered at $z_0$,
$$
v(z_0)
\le
\frac1{2\pi}
\int_0^{2\pi}
v(z_0+re^{i\theta})\,d\theta.
$$


::: pf-proof

If $A(z_0)=0$, then
$$
v(z_0)=-\infty,
$$
so the inequality is automatic.

Assume $A(z_0)\ne0$ and choose unit vectors $x,y$ as in step [](#s1-7){.pf-ref}. By step [](#s1-8){.pf-ref} and the sub-mean-value inequality,
$$
\begin{aligned}
v(z_0)
&=
\log\norm{A(z_0)}\\
&=
\log\abs{\langle A(z_0)x,y\rangle}\\
&\le
\frac1{2\pi}
\int_0^{2\pi}
\log\abs{
\langle A(z_0+re^{i\theta})x,y\rangle
}\,d\theta.
\end{aligned}
$$
For every $z$,
$$
\abs{\langle A(z)x,y\rangle}
\le
\norm{A(z)x}\norm{y}
\le
\norm{A(z)}.
$$
Therefore the last integral is at most
$$
\frac1{2\pi}
\int_0^{2\pi}
\log\norm{A(z_0+re^{i\theta})}\,d\theta.
$$
This is the required inequality.

:::

:::

::: {.pf-step #s1-10}

The function
$$
\boxed{
z\longmapsto\log\norm{A(z)}
}
$$
is subharmonic.


::: pf-proof

Step [](#s1-6){.pf-ref} gives upper-semicontinuity, and step [](#s1-9){.pf-ref} gives the sub-mean-value inequality. Unless $A\equiv0$, the function is not identically $-\infty$ and hence is subharmonic by step [](#s1-2){.pf-ref}. If $A\equiv0$, the conventional extended-valued function is identically $-\infty$; under conventions that permit this degenerate subharmonic function, the conclusion holds verbatim.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} answer parts (a) and (b), step [](#s1-5){.pf-ref} answers part (c), and step [](#s1-10){.pf-ref} proves part (d).

:::

:::

:::
