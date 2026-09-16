---
schema: qual/card@1
id: PR-2C3SZ
kind: proposition
title: Young's convolution inequality
prompts:
- What is Young's inequality?
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

::: {.proposition}
Let $1\le p,q,r\le\infty$ satisfy
$$
\frac1r = \frac1p + \frac1q - 1 .
$$
If $f\in L^p(\RR^n)$ and $g\in L^q(\RR^n)$, then the [[D-TS42Y|convolution]] $f\ast g$ is defined almost everywhere, $f\ast g\in L^r(\RR^n)$, and
$$
\norm{f \ast g}_{r} \leq \norm{f}_{p} \norm{g}_{q}
$$
[@Fol13, §8.2].
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
