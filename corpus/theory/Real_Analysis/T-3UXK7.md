---
schema: qual/card@1
id: T-3UXK7
kind: theorem
title: Convolutions of bounded integrable functions vanish at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
  - Limits
relations: []
review: draft
---

::: {.theorem}
Let $f,g\in L^1(\RR^n)$ be essentially bounded.
Then the [[D-TS42Y|convolution]] $f*g$ is defined at every $x\in\RR^n$ and
$$
\lim_{\abs{x}\to\infty}(f*g)(x)=0 .
$$
:::

::: {.proof}
For $u\in L^\infty(\RR^n)$ and $v\in L^1(\RR^n)$, the integral defining $(u*v)(x)$ converges absolutely at every $x$ and $\sup_x\abs{(u*v)(x)}\leq\norm{u}_\infty\norm{v}_1$; the same holds with the roles of $u$ and $v$ exchanged.
In particular $f*g$ is defined everywhere.

Let $\varepsilon>0$.
Continuous compactly supported functions are dense in $L^1(\RR^n)$, so there is $g_1\in C_c(\RR^n)$ with $\norm{f}_\infty\norm{g-g_1}_1<\varepsilon$, and then $f_1\in C_c(\RR^n)$ with $\norm{f-f_1}_1\norm{g_1}_\infty<\varepsilon$.
For every $x$,
$$
\abs{(f*g)(x)-(f_1*g_1)(x)}\leq\abs{(f*(g-g_1))(x)}+\abs{((f-f_1)*g_1)(x)}<2\varepsilon .
$$
If $f_1$ and $g_1$ vanish outside the ball of radius $r$ about $0$, then $(f_1*g_1)(x)=0$ for $\abs{x}>2r$.
Hence $\abs{(f*g)(x)}<2\varepsilon$ for $\abs{x}>2r$.
:::
