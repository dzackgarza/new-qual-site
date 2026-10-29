---
schema: qual/card@1
id: P-3WZH2
kind: problem
title: Implicit function theorem for $f(s,t)=s^3-6st+t^2$ at $(1,3-2\sqrt2)$, over $\RR$
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

::: {.problem}
Let $P=(1,3-2\sqrt2)$ and define $f(s,t)=s^3-6st+t^2$. Then $f(P)=0$.

(a) State the conclusion of the Implicit Function Theorem concerning $f(s, t) = 0$ when $f$ is considered a function $\RR^2\to\RR$.

(b) State the above conclusion when $f$ is considered a function $\CC^2\to \CC$.

(c) Use the implicit function theorem for a function $\RR^2 \times \RR^2 \to \RR^2$ to prove (b).
:::

::: {.solution}

Write $P=(s_0,t_0)$.
Then $f_t(s,t)=-6s+2t$, so $f_t(P)=-6+2(3-2\sqrt2)=-4\sqrt2\neq0$.

::: pf

::: pf-step
(a) There are open intervals $U\ni s_0$ and $V\ni t_0$ and a unique function $g:U\to V$ with $f(s,t)=0\iff t=g(s)$ for $(s,t)\in U\times V$; $g$ is $C^\infty$, $g(s_0)=t_0$, and $g'(s)=-\dfrac{f_s(s,g(s))}{f_t(s,g(s))}$.

::: pf-proof
This is the real implicit function theorem, since $f$ is a polynomial and $f_t(P)\neq0$.
:::

:::

::: pf-step
(b) There are open discs $U\ni s_0$ and $V\ni t_0$ in $\CC$ and a unique function $g:U\to V$ with $f(s,t)=0\iff t=g(s)$ for $(s,t)\in U\times V$; $g$ is holomorphic, $g(s_0)=t_0$, and $g'(s)=-\dfrac{f_s(s,g(s))}{f_t(s,g(s))}$.

::: pf-proof
This is the conclusion of the holomorphic implicit function theorem; part (c) proves it.
:::

:::

::: pf-step
(c) The conclusion of (b) follows from the real implicit function theorem.

::: pf-proof

Write $s=x+iy$, $t=u+iv$, $f=F_1+iF_2$, and $F\coloneqq(F_1,F_2):\RR^2\times\RR^2\to\RR^2$.

::: {.pf-step #jacobian}
For a complex number $c=a+ib$, write $M(c)\coloneqq\begin{pmatrix}a&-b\\b&a\end{pmatrix}$. Then $D_tF=M(f_t)$ and $D_sF=M(f_s)$, and $\det D_tF=\abs{f_t}^2$.

::: pf-proof
$f$ is holomorphic in each variable, so the Cauchy--Riemann equations in $t$ and in $s$ give these real Jacobians.
:::

:::

::: {.pf-step #real-ift}
There are neighborhoods $U\ni s_0$, $V\ni t_0$ and a unique $C^1$ map $g:U\to V$ with $F(s,t)=0\iff t=g(s)$ on $U\times V$.

::: pf-proof
By step [](#jacobian){.pf-ref}, $\det D_tF(P)=\abs{f_t(P)}^2=32\neq0$, so the real implicit function theorem applies.
:::

:::

::: pf-step
The map $g$ of step [](#real-ift){.pf-ref} is holomorphic with $g'=-f_s/f_t$.

::: pf-proof
Differentiating $F(s,g(s))=0$ gives $Dg=-(D_tF)^{-1}D_sF=-M(f_t)^{-1}M(f_s)=M(-f_s/f_t)$ by step [](#jacobian){.pf-ref}, because $c\mapsto M(c)$ is multiplicative and $M(c)^{-1}=M(c^{-1})$.
So $g$ is $C^1$ and satisfies the Cauchy--Riemann equations, hence is holomorphic with derivative $-f_s/f_t$.
:::

:::

:::

:::

:::

:::
