---
schema: qual/card@1
id: FF-AVCZA
kind: fact
title: Young's inequality for convolutions
prompts:
- State Young's inequality for convolutions.
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
  - Norms
relations: []
review: draft
---

::: {.fact}
Let $1\leq p, q, r\leq\infty$ with $\frac1p + \frac1q = 1 + \frac1r$, and let $f\in L^p(\RR^n)$ and $g\in L^q(\RR^n)$.
Then the [[D-TS42Y|convolution]] $(f\ast g)(x)$ converges absolutely for almost every $x\in\RR^n$, $f\ast g\in L^r(\RR^n)$, and
$$
\norm{f\ast g}_r \leq \norm{f}_p \norm{g}_q.
$$
:::

::: {.example}
The following are the cases $p=q=r=1$; $p=1$ and $q=r$; $r=\infty$ with $\frac1p+\frac1q=1$; and $p=q=2$, $r=\infty$:
$$
\begin{aligned}
\norm{f\ast g}_1 & \leq \norm{f}_1 \norm{g}_1, \\
\norm{f\ast g}_q & \leq \norm{f}_1 \norm{g}_q, \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q, \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2.
\end{aligned}
$$
:::
