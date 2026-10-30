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

::: {.problem}
(a) Let $f \in C_c^0(\RR^n)$, and show
$$
\lim _{t \to 0} \int_{\RR^n} \abs{f(x+t) - f(x)} \, dx = 0
.$$

(b) Extend the above result to $f\in L^1(\RR^n)$ and show that
$$
f\in L^1(\RR^n), \quad g\in L^\infty(\RR^n) \quad
\implies f \ast g \text{ is bounded and uniformly continuous. }
$$
:::

::: {.solution}

::: pf

::: pf-step

Prove translation continuity for $f\in C_c(\RR^n)$.

::: pf-proof

Let $K=\operatorname{supp}f$. For $\norm{t}\le1$, the function
$$
x\longmapsto f(x+t)-f(x)
$$
vanishes outside the bounded set $K+B(0,1)$. Since $f$ is uniformly continuous, its modulus of continuity
$$
\omega_f(r):=\sup_{\norm{x-y}\le r}\abs{f(x)-f(y)}
$$
satisfies $\omega_f(r)\to0$ as $r\downarrow0$. Hence, for $\norm{t}\le1$,
$$
\int_{\RR^n}\abs{f(x+t)-f(x)}\,dx
\le m(K+B(0,1))\,\omega_f(\norm{t})\longrightarrow0.
$$

:::

:::

::: pf-step

Extend translation continuity to every $f\in L^1(\RR^n)$.

::: pf-proof

Write $\tau_t f(x)=f(x+t)$. Fix $\varepsilon>0$. Choose $\varphi\in C_c(\RR^n)$ with
$$
\norm{f-\varphi}_1<\frac\varepsilon3.
$$
Translation invariance of Lebesgue measure gives
$$
\norm{\tau_t(f-\varphi)}_1=\norm{f-\varphi}_1.
$$
Therefore
$$
\norm{\tau_t f-f}_1
\le 2\norm{f-\varphi}_1+\norm{\tau_t\varphi-\varphi}_1.
$$
By Step 1, the last term is below $\varepsilon/3$ for all sufficiently small $t$. Thus
$$
\boxed{\norm{\tau_t f-f}_1\to0\quad(t\to0).}
$$

:::

:::

::: pf-step

Prove boundedness of $f*g$ for $f\in L^1$ and $g\in L^\infty$.

::: pf-proof

Using
$$
(f*g)(x)=\int_{\RR^n} f(x-y)g(y)\,dy,
$$
we obtain for every $x$,
$$
\abs{(f*g)(x)}
\le \norm{g}_\infty\int_{\RR^n}\abs{f(x-y)}\,dy
=\norm{f}_1\norm{g}_\infty.
$$
Hence $f*g$ is bounded.

:::

:::

::: pf-step

Prove uniform continuity of $f*g$.

::: pf-proof

For $t\in\RR^n$,
$$
\begin{aligned}
\abs{(f*g)(x+t)-(f*g)(x)}
&\le \int \abs{f(x+t-y)-f(x-y)}\,\abs{g(y)}\,dy\\
&\le \norm{g}_\infty\int \abs{f(u+t)-f(u)}\,du\\
&=\norm{g}_\infty\,\norm{\tau_t f-f}_1.
\end{aligned}
$$
The right-hand side is independent of $x$ and tends to $0$ as $t\to0$ by Step 2. Therefore
$$
\boxed{f*g\text{ is bounded and uniformly continuous}.}
$$

:::

:::

:::

:::
