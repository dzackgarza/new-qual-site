---
schema: qual/card@1
id: P-5QNZJ
kind: problem
title: Translation is continuous in $L^1$; $L^1*L^\infty$ convolutions are bounded
  and uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the UGA Fall 2014 real-analysis qualifying exam recorded by the collection source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
1. Let $f \in C_c^0(\RR^n)$, and show
\[
\lim _{t \to 0} \int_{\RR^n} |f(x+t) - f(x)| \, dx = 0
.\]

2. Extend the above result to $f\in L^1(\RR^n)$ and show that
\[
f\in L^1(\RR^n), \quad g\in L^\infty(\RR^n) \quad
\implies f \ast g \text{ is bounded and uniformly continuous. }
\]
:::

::: solution
<1>1. Prove translation continuity for $f\in C_c(\mathbb R^n)$.
::: proof
Let $K=\operatorname{supp}f$. For $|t|\le1$, the function
\[
x\longmapsto f(x+t)-f(x)
\]
vanishes outside the bounded set $K+B(0,1)$. Since $f$ is uniformly continuous, its modulus of continuity
\[
\omega_f(r):=\sup_{|x-y|\le r}|f(x)-f(y)|
\]
satisfies $\omega_f(r)\to0$ as $r\downarrow0$. Hence, for $|t|\le1$,
\[
\int_{\mathbb R^n}|f(x+t)-f(x)|\,dx
\le m(K+B(0,1))\,\omega_f(|t|)\longrightarrow0.
\]
:::

<1>2. Extend translation continuity to every $f\in L^1(\mathbb R^n)$.
::: proof
Write $\tau_t f(x)=f(x+t)$. Fix $\varepsilon>0$. Choose $\varphi\in C_c(\mathbb R^n)$ with
\[
\|f-\varphi\|_1<\frac\varepsilon3.
\]
Translation invariance of Lebesgue measure gives
\[
\|\tau_t(f-\varphi)\|_1=\|f-\varphi\|_1.
\]
Therefore
\[
\|\tau_t f-f\|_1
\le 2\|f-\varphi\|_1+\|\tau_t\varphi-\varphi\|_1.
\]
By Step 1, the last term is below $\varepsilon/3$ for all sufficiently small $t$. Thus
\[
\boxed{\|\tau_t f-f\|_1\to0\quad(t\to0).}
\]
:::

<1>3. Prove boundedness of $f*g$ for $f\in L^1$ and $g\in L^\infty$.
::: proof
Using
\[
(f*g)(x)=\int_{\mathbb R^n} f(x-y)g(y)\,dy,
\]
we obtain for every $x$,
\[
|(f*g)(x)|
\le \|g\|_\infty\int_{\mathbb R^n}|f(x-y)|\,dy
=\|f\|_1\|g\|_\infty.
\]
Hence $f*g$ is bounded.
:::

<1>4. Prove uniform continuity of $f*g$.
::: proof
For $t\in\mathbb R^n$,
\[
\begin{aligned}
|(f*g)(x+t)-(f*g)(x)|
&\le \int |f(x+t-y)-f(x-y)|\,|g(y)|\,dy\\
&\le \|g\|_\infty\int |f(u+t)-f(u)|\,du\\
&=\|g\|_\infty\,\|\tau_t f-f\|_1.
\end{aligned}
\]
The right-hand side is independent of $x$ and tends to $0$ as $t\to0$ by Step 2. Therefore
\[
\boxed{f*g\text{ is bounded and uniformly continuous}.}
\]
:::
:::
