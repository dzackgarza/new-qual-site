---
schema: qual/card@1
id: P-UCLARA11S-11
kind: problem
title: Analytic continuation and residue of a Bose-Einstein integral
classification: {areas: [complex-analysis], topics: [Analytic Continuation, Residues]}
relations: []
review: draft
---

::: {.problem}
For $s\in(1,\infty)$ define
$$
f(s)=\int_0^\infty \frac{x^{s-1}}{e^x-1}\,dx.
$$
Show that $f$ has an analytic continuation to
$$
\{s\in\CC:\operatorname{Re}s>0,\ s\ne1\}
$$
with a simple pole at $s=1$.
Compute the residue at $s=1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x>0$, define
$$
r(x)
\coloneqq
\frac1{e^x-1}-\frac1x.
$$
Then $r$ extends continuously to $x=0$ with
$$
r(0)=-\frac12.
$$


::: pf-proof

Using
$$
e^x-1
=
x+\frac{x^2}{2}+O(x^3),
$$
one gets
$$
\frac1{e^x-1}
=
\frac1x
\frac1{1+x/2+O(x^2)}
=
\frac1x
-\frac12
+O(x).
$$
Hence
$$
r(x)\longrightarrow-\frac12
\qquad
(x\downarrow0).
$$

:::

:::

::: {.pf-step #s1-2}

The function
$$
H(s)
\coloneqq
\int_0^1 x^{s-1}r(x)\,dx
$$
is holomorphic on the half-plane
$$
\operatorname{Re}s>0.
$$


::: pf-proof

Fix a compact set
$$
K\subset\{\operatorname{Re}s>0\}.
$$
There is $\sigma>0$ such that
$$
\operatorname{Re}s\ge\sigma
\qquad
(s\in K).
$$
By step [](#s1-1){.pf-ref}, $r$ is bounded on $[0,1]$, say
$$
\abs{r(x)}\le C.
$$
For $s\in K$,
$$
\abs{x^{s-1}r(x)}
\le
C x^{\sigma-1},
$$
and the right-hand side is integrable on $(0,1)$.

Likewise, for every integer $m\ge1$,
$$
\abs{
\frac{\partial^m}{\partial s^m}
x^{s-1}r(x)
}
\le
C x^{\sigma-1}\abs{\log x}^m,
$$
which is also integrable on $(0,1)$. Therefore differentiation under the integral sign is justified on compact subsets, and $H$ is holomorphic.

:::

:::

::: {.pf-step #s1-3}

The function
$$
J(s)
\coloneqq
\int_1^\infty
\frac{x^{s-1}}{e^x-1}\,dx
$$
is entire.


::: pf-proof

Fix a compact set $K\subset\CC$. Choose $A>0$ such that
$$
\operatorname{Re}s\le A
\qquad
(s\in K).
$$
For $x\ge1$,
$$
e^x-1
\ge
(1-e^{-1})e^x,
$$
so
$$
\abs{
\frac{x^{s-1}}{e^x-1}
}
\le
C_A x^{A-1}e^{-x}.
$$
The right-hand side is integrable on $[1,\infty)$.

After differentiating $m$ times with respect to $s$, an additional factor $(\log x)^m$ appears, and
$$
x^{A-1}(\log x)^m e^{-x}
$$
is still integrable. Hence differentiation under the integral sign is valid on every compact set, so $J$ is entire.

:::

:::

::: {.pf-step #s1-4}

For real $s>1$,
$$
f(s)
=
\frac1{s-1}
+
H(s)
+
J(s).
$$


::: pf-proof

Split the defining integral at $1$:
$$
f(s)
=
\int_0^1
\frac{x^{s-1}}{e^x-1}\,dx
+
\int_1^\infty
\frac{x^{s-1}}{e^x-1}\,dx.
$$
On $(0,1)$, use
$$
\frac1{e^x-1}
=
\frac1x+r(x).
$$
Then
$$
\int_0^1
\frac{x^{s-1}}{e^x-1}\,dx
=
\int_0^1x^{s-2}\,dx
+
\int_0^1x^{s-1}r(x)\,dx.
$$
For $s>1$,
$$
\int_0^1x^{s-2}\,dx
=
\frac1{s-1}.
$$
The remaining two terms are $H(s)$ and $J(s)$.

:::

:::

::: {.pf-step #s1-5}

Define
$$
F(s)
\coloneqq
\frac1{s-1}
+
H(s)
+
J(s)
$$
for
$$
\operatorname{Re}s>0,
\qquad
s\ne1.
$$
Then $F$ is holomorphic on this punctured half-plane and extends the original function $f$.


::: pf-proof

By step [](#s1-2){.pf-ref}, $H$ is holomorphic on $\Re s>0$, and by step [](#s1-3){.pf-ref}, $J$ is entire. The function
$$
\frac1{s-1}
$$
is holomorphic away from $s=1$. Thus $F$ is holomorphic on
$$
\{\Re s>0\}\setminus\{1\}.
$$
Step [](#s1-4){.pf-ref} shows that
$$
F(s)=f(s)
$$
for every real $s>1$, so $F$ is an analytic continuation of $f$.

:::

:::

::: {.pf-step #s1-6}

The point $s=1$ is a simple pole of $F$.


::: pf-proof

The function
$$
H(s)+J(s)
$$
is holomorphic in a neighborhood of $s=1$. Hence
$$
F(s)
=
\frac1{s-1}
+
\text{(holomorphic function near }1).
$$
Thus $s=1$ is a simple pole.

:::

:::

::: {.pf-step #s1-7}

The residue at $s=1$ is
$$
\boxed{1}.
$$


::: pf-proof

From the Laurent expansion in step [](#s1-6){.pf-ref}, the coefficient of $(s-1)^{-1}$ is exactly $1$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required analytic continuation, and steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} identify the pole and its residue.

:::

:::

:::
