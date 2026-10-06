---
schema: qual/card@1
id: P-UCLARA11S-08
kind: problem
title: Subharmonic functions, pointwise extrema, and norms of holomorphic matrix functions
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
(a) Define upper-semicontinuity for functions $f:\mathbb C\to[-\infty,\infty)$.

(b) Define what it means for such an upper-semicontinuous function to be subharmonic.

(c) Prove or refute, with a counterexample, each statement:

- The pointwise supremum of a bounded family of subharmonic functions is subharmonic.

- The pointwise infimum of a family of subharmonic functions is subharmonic.

(d) Let $A(z)$ be a $2\times2$ matrix-valued holomorphic function, meaning that its entries are holomorphic.
Show that
\[
z\longmapsto \log\|A(z)\|
\]
is subharmonic, where $\|A(z)\|$ is the operator norm on $\mathbb C^2$.
:::

::: {.solution}
<1>1. A function
\[
u:\mathbb C\to[-\infty,\infty)
\]
is upper-semicontinuous if for every $z_0\in\mathbb C$,
\[
\limsup_{z\to z_0}u(z)
\le
u(z_0).
\]

::: {.proof}
This is the definition. Equivalently, for every $a\in\mathbb R$, the sublevel set
\[
\{z:u(z)<a\}
\]
is open.
:::

<1>2. An upper-semicontinuous function
\[
u:\mathbb C\to[-\infty,\infty)
\]
is subharmonic if it is not identically $-\infty$ and for every closed disk
\[
\overline{B(z_0,r)}
\subset\mathbb C,
\]
one has the sub-mean-value inequality
\[
u(z_0)
\le
\frac1{2\pi}
\int_0^{2\pi}
u(z_0+re^{i\theta})\,d\theta.
\]

::: {.proof}
This is the standard definition of subharmonicity on an open set, specialized to the whole plane.
:::

<1>3. The pointwise supremum of a bounded family of subharmonic functions need not be subharmonic.

::: {.proof}
For $n\ge1$, define
\[
u_n(z)
\coloneqq
\frac1n\log|z|,
\]
with
\[
u_n(0)=-\infty.
\]
Each $u_n$ is subharmonic on $\mathbb C$. The family is locally uniformly bounded above: on
\[
|z|\le R,
\]
one has
\[
u_n(z)
\le
\max\{0,\log R\}.
\]

Its pointwise supremum is
\[
u(z)
\coloneqq
\sup_{n\ge1}u_n(z)
=
\begin{cases}
-\infty,&z=0,\\
0,&0<|z|\le1,\\
\log|z|,&|z|>1.
\end{cases}
\]
Indeed, when $0<|z|<1$, the negative numbers
\[
\frac1n\log|z|
\]
increase to $0$, while for $|z|>1$ their supremum occurs at $n=1$.

But
\[
\limsup_{z\to0}u(z)=0
>
-\infty=u(0),
\]
so $u$ is not upper-semicontinuous and therefore not subharmonic.
:::

<1>4. The pointwise infimum of a family of subharmonic functions need not be subharmonic.

::: {.proof}
The harmonic functions
\[
u_1(z)=\operatorname{Re}z,
\qquad
u_2(z)=-\operatorname{Re}z
\]
are subharmonic. Their pointwise infimum is
\[
u(z)
=
\min\{\operatorname{Re}z,-\operatorname{Re}z\}
=
-|\operatorname{Re}z|.
\]
At $z=0$,
\[
u(0)=0.
\]
On the circle $|z|=r$,
\[
u(re^{i\theta})
=
-r|\cos\theta|.
\]
Hence
\[
\frac1{2\pi}
\int_0^{2\pi}
u(re^{i\theta})\,d\theta
<
0
=
u(0).
\]
Thus the sub-mean-value inequality fails at $0$, so $u$ is not subharmonic.
:::

<1>5. This settles part (c): both assertions are false.

::: {.proof}
Step <1>3 refutes the supremum assertion, and step <1>4 refutes the infimum assertion.
:::

<1>6. Let
\[
v(z)
\coloneqq
\log\|A(z)\|,
\]
with the convention
\[
v(z)=-\infty
\]
when $A(z)=0$. Then $v$ is upper-semicontinuous.

::: {.proof}
The matrix entries of $A$ are holomorphic, hence continuous, and the operator norm is a continuous function of the matrix entries. Thus
\[
z\longmapsto\|A(z)\|
\]
is continuous.

At points where $\|A(z_0)\|>0$, composition with the continuous logarithm gives continuity of $v$. If $A(z_0)=0$, then
\[
\|A(z)\|\to0
\qquad
(z\to z_0),
\]
so
\[
\log\|A(z)\|\to-\infty=v(z_0).
\]
Hence $v$ is upper-semicontinuous everywhere.
:::

<1>7. Suppose $A(z_0)\ne0$. There exist unit vectors $x,y\in\mathbb C^2$ such that
\[
|\langle A(z_0)x,y\rangle|
=
\|A(z_0)\|.
\]

::: {.proof}
Because the unit sphere of $\mathbb C^2$ is compact, there is a unit vector $x$ with
\[
\|A(z_0)x\|
=
\|A(z_0)\|.
\]
Set
\[
y
\coloneqq
\frac{A(z_0)x}{\|A(z_0)x\|}.
\]
Then $\|y\|=1$ and
\[
|\langle A(z_0)x,y\rangle|
=
\|A(z_0)x\|
=
\|A(z_0)\|.
\]
:::

<1>8. For fixed vectors $x,y\in\mathbb C^2$, the scalar function
\[
h(z)
\coloneqq
\langle A(z)x,y\rangle
\]
is holomorphic, and
\[
\log|h(z)|
\]
is subharmonic.

::: {.proof}
The function $h$ is a fixed complex linear combination of the holomorphic entries of $A$, hence holomorphic. The logarithm of the modulus of a holomorphic function is subharmonic, with value $-\infty$ at its zeros.
:::

<1>9. For every disk centered at $z_0$,
\[
v(z_0)
\le
\frac1{2\pi}
\int_0^{2\pi}
v(z_0+re^{i\theta})\,d\theta.
\]

::: {.proof}
If $A(z_0)=0$, then
\[
v(z_0)=-\infty,
\]
so the inequality is automatic.

Assume $A(z_0)\ne0$ and choose unit vectors $x,y$ as in step <1>7. By step <1>8 and the sub-mean-value inequality,
\[
\begin{aligned}
v(z_0)
&=
\log\|A(z_0)\|\\
&=
\log|\langle A(z_0)x,y\rangle|\\
&\le
\frac1{2\pi}
\int_0^{2\pi}
\log|
\langle A(z_0+re^{i\theta})x,y\rangle
|\,d\theta.
\end{aligned}
\]
For every $z$,
\[
|\langle A(z)x,y\rangle|
\le
\|A(z)x\|\|y\|
\le
\|A(z)\|.
\]
Therefore the last integral is at most
\[
\frac1{2\pi}
\int_0^{2\pi}
\log\|A(z_0+re^{i\theta})\|\,d\theta.
\]
This is the required inequality.
:::

<1>10. The function
\[
\boxed{
z\longmapsto\log\|A(z)\|
}
\]
is subharmonic.

::: {.proof}
Step <1>6 gives upper-semicontinuity, and step <1>9 gives the sub-mean-value inequality. Unless $A\equiv0$, the function is not identically $-\infty$ and hence is subharmonic by step <1>2. If $A\equiv0$, the conventional extended-valued function is identically $-\infty$; under conventions that permit this degenerate subharmonic function, the conclusion holds verbatim.
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 answer parts (a) and (b), step <1>5 answers part (c), and step <1>10 proves part (d).
:::
:::
