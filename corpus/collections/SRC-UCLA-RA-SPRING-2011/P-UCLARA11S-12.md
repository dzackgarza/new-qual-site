---
schema: qual/card@1
id: P-UCLARA11S-12
kind: problem
title: Finiteness and parameter-independence of the solutions to $\log z=t/z$
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Let
\[
\Omega=\mathbb C\setminus(-\infty,0]
\]
and let $\log z$ denote the branch of the complex logarithm on $\Omega$ that is real on the positive real axis.
Show that for every $0<t<\infty$, the number of solutions $z\in\Omega$ to
\[
\log z=\frac{t}{z}
\]
is finite and independent of $t$.
:::

::: pf

::: pf-step

The principal logarithm is a biholomorphism
\[
\log:
\Omega
\longrightarrow
S,
\qquad
S
\coloneqq
\{w\in\mathbb C:-\pi<\operatorname{Im}w<\pi\},
\]
with inverse
\[
w\longmapsto e^w.
\]


::: pf-proof

This is the defining property of the branch of the logarithm on the slit plane
\[
\mathbb C\setminus(-\infty,0].
\]
Its argument takes values in $(-\pi,\pi)$, so its image is exactly the stated horizontal strip, and exponentiation is its inverse.

:::

:::

::: pf-step

A point $z\in\Omega$ solves
\[
\log z=\frac tz
\]
if and only if
\[
w e^w=t,
\qquad
w=\log z\in S.
\]


::: pf-proof

Since
\[
z=e^w,
\]
the equation becomes
\[
w
=
t e^{-w},
\]
equivalently
\[
w e^w=t.
\]
The equivalence is reversible because $z=e^w$ and $w=\log z$ are inverse coordinates by step <1>1.

:::

:::

::: pf-step

Let
\[
w=a+ib\in S
\]
satisfy
\[
w e^w=t>0.
\]
Then
\[
a\sin b+b\cos b=0.
\]


::: pf-proof

Compute
\[
\begin{aligned}
w e^w
&=
(a+ib)e^a(\cos b+i\sin b)\\
&=
e^a
\bigl(
a\cos b-b\sin b
\bigr)
+
i e^a
\bigl(
a\sin b+b\cos b
\bigr).
\end{aligned}
\]
Because $t$ is real, the imaginary part must vanish.

:::

:::

::: pf-step

No solution in the strip can have
\[
b\ne0.
\]


::: pf-proof

Suppose $b\ne0$. Since
\[
-\pi<b<\pi,
\]
one has
\[
\sin b\ne0.
\]
From step <1>3,
\[
a
=
-b\cot b.
\]
Substitute this into the real part:
\[
\begin{aligned}
a\cos b-b\sin b
&=
-b\frac{\cos^2b}{\sin b}
-b\sin b\\
&=
-b
\frac{\cos^2b+\sin^2b}{\sin b}\\
&=
-\frac b{\sin b}.
\end{aligned}
\]
For
\[
0<|b|<\pi,
\]
the numbers $b$ and $\sin b$ have the same sign, so
\[
-\frac b{\sin b}<0.
\]
Hence
\[
\operatorname{Re}(we^w)
=
e^a
\left(
-\frac b{\sin b}
\right)
<
0,
\]
contradicting
\[
we^w=t>0.
\]
Therefore $b=0$.

:::

:::

::: pf-step

Every solution has
\[
w=a\in(0,\infty)
\]
and satisfies
\[
a e^a=t.
\]


::: pf-proof

Step <1>4 gives $w=a\in\mathbb R$. The equation becomes
\[
a e^a=t.
\]
Since $e^a>0$ and $t>0$, necessarily $a>0$.

:::

:::

::: pf-step

For each $t>0$, the equation
\[
a e^a=t
\]
has exactly one solution $a>0$.


::: pf-proof

Define
\[
\phi(a)=a e^a
\qquad
(a>0).
\]
Then
\[
\phi'(a)
=
e^a(1+a)
>
0,
\]
so $\phi$ is strictly increasing. Moreover,
\[
\lim_{a\downarrow0}\phi(a)=0,
\qquad
\lim_{a\to\infty}\phi(a)=\infty.
\]
By the intermediate value theorem, for each $t>0$ there is exactly one $a>0$ with $\phi(a)=t$.

:::

:::

::: pf-step

For every $t>0$, the original equation has exactly one solution in $\Omega$.


::: pf-proof

By steps <1>2--<1>6, there is exactly one solution
\[
w=a>0
\]
of
\[
w e^w=t
\]
in the strip $S$. Step <1>1 gives the corresponding unique point
\[
z=e^a\in(1,\infty)\subset\Omega.
\]

:::

:::

::: pf-step

Therefore the number of solutions is finite and independent of $t$:
\[
\boxed{
\#\left\{
z\in\Omega:
\log z=\frac tz
\right\}
=
1
\qquad
(t>0).
}
\]


::: pf-proof

This is exactly step <1>7, now stated as the requested count.

:::

:::

::: pf-qed

Step <1>8 proves both finiteness and independence of $t$.

:::

:::
