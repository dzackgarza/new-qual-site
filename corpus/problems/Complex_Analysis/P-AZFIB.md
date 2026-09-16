---
schema: qual/card@1
id: P-AZFIB
kind: problem
title: $2|f'(0)|\le\operatorname{diam} f(\DD)$, with equality iff $f$ is linear
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Schwarz Lemma
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.problem}
Suppose $f: \DD \to \CC$ is holomorphic and let $d \definedas \sup_{z, w\in \DD}\abs{f(z) - f(w)}$ be the diameter of the image of $f$.
Show that $2 \abs{f'(0)} \leq d$, and that equality holds iff $f$ is linear, so $f(z) = a_1 z + a_2$.

> Hint:
\[
2f'(0) = \frac{1}{2\pi i} \int_{\abs \xi = r} \frac{ f(\xi) - f(-\xi)  }{\xi^2} ~d\xi
\]
whenever $0<r<1$.
:::

::: {.solution}
Let
\[
d=\operatorname{diam}f(\mathbb D).
\]
If $d=0$, then $f$ is constant and the result is immediate. Assume $d>0$ and
define the odd part
\[
h(z)=\frac{f(z)-f(-z)}{d}.
\]
Then $h(0)=0$ and $|h(z)|\le1$ on $\mathbb D$. Schwarz's lemma gives
\[
|h'(0)|\le1.
\]
Since $h'(0)=2f'(0)/d$, this is exactly
\[
\boxed{2|f'(0)|\le d}.
\]

Every affine function $f(z)=a_1z+a_2$ satisfies
\[
d=2|a_1|=2|f'(0)|,
\]
so it remains to prove rigidity in the equality case.

Assume $2|f'(0)|=d$. After replacing $f$ by
\[
F(z)=\frac{f(z)-f(0)}{f'(0)},
\]
we may assume
\[
F(0)=0,\qquad F'(0)=1,\qquad \operatorname{diam}F(\mathbb D)=2.
\]
We prove $F(z)=z$.

The odd part
\[
F_o(z)=\frac{F(z)-F(-z)}2
\]
maps $\mathbb D$ into $\overline{\mathbb D}$, satisfies $F_o(0)=0$, and has
$F_o'(0)=1$. The equality case of Schwarz's lemma therefore gives
\[
\boxed{F(z)-F(-z)=2z.}\tag{1}
\]

For $0<r<1$, let
\[
D_r=\operatorname{diam}F(r\mathbb D).
\]
The diameter is attained on the boundary circle $|z|=r$: if one point of a
maximizing pair were interior, the open mapping theorem would let its image be
moved slightly farther from the other image point, contradicting maximality.
Hence
\[
D_r=\max_{|z|=|w|=r}|F(z)-F(w)|.
\]
For $|u|=1$, set
\[
H_u(z)=\frac{F(z)-F(-uz)}{z},
\]
with the removable value at $z=0$. By the maximum modulus principle,
\[
\frac{D_r}{r}
=\max_{|u|=1}\max_{|z|\le r}|H_u(z)|,
\]
so $D_r/r$ is nondecreasing in $r$. On the other hand, (1) gives
$D_r\ge2r$, while $D_r\le2$. Therefore
\[
2\le\frac{D_r}{r}\le\frac2r.
\]
Since the left-hand side is nondecreasing and its limsup as $r\uparrow1$ is at
most $2$, we obtain
\[
\boxed{D_r=2r\qquad(0<r<1).}\tag{2}
\]

Fix $w\in\mathbb D\setminus\{0\}$ and put $r=|w|$. Define
\[
G_w(z)=\frac{F(z)-F(-w)}2.
\]
By (2), $|G_w(z)|\le r$ for $|z|\le r$, and by (1),
\[
G_w(w)=w.
\]
Thus the function
\[
\phi(\theta)=|G_w(we^{i\theta})|^2
\]
has a maximum at $\theta=0$. Differentiating there gives
\[
0=\phi'(0)=-2|w|^2\operatorname{Im}G_w'(w),
\]
so
\[
\operatorname{Im}F'(w)=0.
\]
Hence the holomorphic function $F'$ takes values in $\mathbb R$. By the open
mapping theorem it is constant; since $F'(0)=1$, we get $F'\equiv1$. Together
with $F(0)=0$, this yields $F(z)=z$.

Undoing the normalization shows
\[
\boxed{f(z)=a_1z+a_2.}
\]
Thus equality holds exactly for affine-linear $f$.
:::
