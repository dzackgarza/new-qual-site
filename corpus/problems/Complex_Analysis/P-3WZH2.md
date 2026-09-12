---
schema: qual/card@1
id: P-3WZH2
kind: problem
title: Implicit function theorem for $f(s,t)=ps^3-6st+t^2$ at $(1,3)$, over $\RR$
  and $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $P=(1,3-2\sqrt2)$ and define $f(s,t)=s^3-6st+t^2$. Then $f(P)=0$.

a. State the conclusion of the Implicit Function Theorem concerning $f(s, t) = 0$ when $f$ is considered a function $\mathbb{R}^2\to\mathbb{R}$.

b. State the above conclusion when $f$ is considered a function $\mathbb{C}^2\to \mathbb{C}$.

c. Use the implicit function theorem for a function $\mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$ to prove (b).
:::

::: solution
Let
\[
P=(s_0,t_0)=(1,3-2\sqrt2).
\]
Then $f(P)=0$ and
\[
f_t(s,t)=-6s+2t,
\qquad
f_t(P)=-4\sqrt2\ne0.
\]

<1>1. Over $\mathbb R$, the implicit-function theorem gives neighborhoods $U\ni s_0$ and $V\ni t_0$ and a unique $C^1$ function
\[
g:U\to V
\]
with
\[
g(s_0)=t_0,
\qquad
f(s,g(s))=0.
\]
Moreover,
\[
g'(s)=-\frac{f_s(s,g(s))}{f_t(s,g(s))}.
\]

<1>2. Over $\mathbb C$, regarding the same polynomial as holomorphic on $\mathbb C^2$, the complex implicit-function theorem gives neighborhoods $U,V\subset\mathbb C$ and a unique holomorphic map $g:U\to V$ satisfying the same equations.

<1>3. To derive the complex theorem from the real one, write
\[
s=x+iy,
\qquad
t=u+iv,
\qquad
f=F_1+iF_2,
\]
and set
\[
F=(F_1,F_2):\mathbb R^2\times\mathbb R^2\to\mathbb R^2.
\]
The real Jacobian with respect to $(u,v)$ is
\[
D_tF=
\begin{pmatrix}
a&-b\\
b&a
\end{pmatrix},
\qquad
a+ib=f_t.
\]
Hence
\[
\det D_tF=|f_t|^2.
\]
At $P$ this determinant is nonzero, so the real implicit-function theorem gives a unique $C^1$ map $g$.

<1>4. Differentiating $F(s,g(s))=0$ gives
\[
Dg=-(D_tF)^{-1}D_sF.
\]
Both $D_tF$ and $D_sF$ are real matrices representing multiplication by complex numbers. Such matrices are closed under multiplication and inversion, so $Dg$ has the form
\[
\begin{pmatrix}
\alpha&-\beta\\
\beta&\alpha
\end{pmatrix}.
\]
Thus $g$ satisfies the Cauchy--Riemann equations. Since $g$ is $C^1$, it is holomorphic, proving the complex conclusion from the real theorem.
:::
