---
schema: qual/card@1
id: P-AZOFF-B03
kind: problem
title: Real differentiability, the inverse function theorem, and complex differentiability in $\mathbb R^2$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Several variables, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Gave the linear-remainder definition of real differentiability and a
    standard C^1 inverse-function theorem in R^2. For the complex criterion,
    proved that real differentiability upgrades to complex differentiability
    exactly when the real derivative is C-linear, equivalently when its
    matrix has the Cauchy-Riemann form. The source compilation contains no
    worked solution for this problem.
---

::: {.problem}
Let $f : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$

a) Define in terms of linear transformations, what it means for f to be differentiable at a point $( a , b ) \in \mathbb { R } ^ { 2 }$

b) State a version of the inverse function theorem in this setting.

c) Identifying C with $\mathbb { R } ^ { 2 }$ in the usual way, give, with proof, a necessary and sufficient condition for a function satisfying the definition of real differentiability in Part a) to be complex differentiable at the point $a + i b$
:::

::: {.solution}
Put
$$
p=(a,b)\in\RR^2,
\qquad
z_0=a+ib\in\CC.
$$
When convenient, write
$$
f=(u,v)
$$
and identify $(x,y)\in\RR^2$ with $x+iy\in\CC$.

<1>1. Part (a): $f$ is real differentiable at $p$ exactly when there is a
real-linear map
$$
L:\RR^2\longrightarrow\RR^2
$$
such that
$$
\lim_{h\to0}
\frac{\norm{f(p+h)-f(p)-Lh}}{\norm h}
=
0.
$$
In that case $L$ is unique and is denoted $Df(p)$.

::: {.proof}
The displayed condition is the definition of Fréchet differentiability in
finite-dimensional real vector spaces.

For uniqueness, suppose both $L$ and $M$ satisfy the condition. For every
fixed nonzero $w\in\RR^2$ and every nonzero real $t$,
$$
\frac{\norm{(L-M)(tw)}}{\abs t\,\norm w}
=
\frac{\norm{(L-M)w}}{\norm w}.
$$
On the other hand,
$$
(L-M)(tw)
=
\bigl(f(p+tw)-f(p)-M(tw)\bigr)
-
\bigl(f(p+tw)-f(p)-L(tw)\bigr),
$$
so the defining limits for $L$ and $M$ force the left-hand side to tend to
$0$ as $t\to0$. Thus $(L-M)w=0$ for every nonzero $w$, and the same is
trivial for $w=0$. Hence $L=M$.
:::

<1>2. Part (b): a version of the inverse function theorem is the following.
If $f$ is $C^1$ on a neighborhood of $p$ and
$$
\det Df(p)\neq0,
$$
then there are open neighborhoods
$$
p\in U\subseteq\RR^2,
\qquad
f(p)\in V\subseteq\RR^2
$$
such that
$$
f|_U:U\longrightarrow V
$$
is a $C^1$ diffeomorphism. Moreover,
$$
D(f|_U^{-1})(f(x))
=
\bigl(Df(x)\bigr)^{-1}
$$
for $x\in U$ after $U$ is chosen small enough that $Df(x)$ remains
invertible.

::: {.proof}
This is the inverse function theorem specialized to maps
$\RR^2\to\RR^2$.
:::

<1>3. If the real-differentiable map $f$ is complex differentiable at
$z_0$, then $Df(p)$ is complex-linear.

::: {.proof}
Let
$$
\lambda=f_{\CC}'(z_0).
$$
Complex differentiability means
$$
f(z_0+h)-f(z_0)
=
\lambda h+r(h),
\qquad
\frac{\abs{r(h)}}{\abs h}\longrightarrow0.
$$
Under the identification $\CC\cong\RR^2$, multiplication by $\lambda$ is a
real-linear map. The displayed estimate therefore also exhibits
multiplication by $\lambda$ as the real derivative of $f$ at $p$. By the
uniqueness in step <1>1,
$$
Df(p)(h)=\lambda h.
$$
Hence $Df(p)$ is complex-linear.
:::

<1>4. A real-linear map $L:\CC\to\CC$ is complex-linear if and only if
$$
L(ih)=iL(h)
$$
for every $h\in\CC$.

::: {.proof}
Complex-linearity immediately implies the displayed identity.

Conversely, suppose the identity holds. For
$$
\alpha+i\beta\in\CC
$$
and $h\in\CC$, real-linearity gives
$$
\begin{aligned}
L((\alpha+i\beta)h)
&=
\alpha L(h)+\beta L(ih)\\
&=
\alpha L(h)+i\beta L(h)\\
&=
(\alpha+i\beta)L(h).
\end{aligned}
$$
Thus $L$ is complex-linear.
:::

<1>5. If $f=(u,v)$ is real differentiable at $p$, then $Df(p)$ is
complex-linear if and only if the Cauchy--Riemann equations
$$
u_x(p)=v_y(p),
\qquad
u_y(p)=-v_x(p)
$$
hold.

::: {.proof}
Real differentiability gives
$$
Df(p)
=
\begin{pmatrix}
u_x(p)&u_y(p)\\
v_x(p)&v_y(p)
\end{pmatrix}.
$$
Let
$$
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
$$
the real matrix of multiplication by $i$. By step <1>4, $Df(p)$ is
complex-linear exactly when
$$
Df(p)J=JDf(p).
$$
Writing out this matrix equation gives
$$
u_x(p)=v_y(p),
\qquad
u_y(p)=-v_x(p).
$$
:::

<1>6. Conversely, if the Cauchy--Riemann equations in step <1>5 hold, then
$f$ is complex differentiable at $z_0$.

::: {.proof}
By step <1>5, the real derivative $Df(p)$ is complex-linear. Hence there is
some $\lambda\in\CC$ such that
$$
Df(p)(h)=\lambda h.
$$
Real differentiability gives
$$
f(z_0+h)-f(z_0)
=
\lambda h+r(h),
\qquad
\frac{\abs{r(h)}}{\abs h}\longrightarrow0.
$$
For $h\neq0$,
$$
\frac{f(z_0+h)-f(z_0)}h
=
\lambda+\frac{r(h)}h.
$$
Since
$$
\abs{\frac{r(h)}h}
=
\frac{\abs{r(h)}}{\abs h}
\longrightarrow0,
$$
the complex difference quotient tends to $\lambda$. Thus $f$ is complex
differentiable at $z_0$.
:::

<1>7. Part (c): for a real-differentiable $f=(u,v)$,
$$
\boxed{
f\text{ is complex differentiable at }a+ib
\iff
\begin{cases}
u_x(a,b)=v_y(a,b),\\
u_y(a,b)=-v_x(a,b).
\end{cases}
}
$$
Equivalently, $Df(a,b)$ is complex-linear.

::: {.proof}
Necessity follows from steps <1>3 and <1>5. Sufficiency follows from steps
<1>5--<1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>7 answer parts (a), (b), and (c), respectively.
:::
:::
