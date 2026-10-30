---
schema: qual/card@1
id: T-BFOJT
kind: theorem
title: Continuity of translation in $L^1$
prompts:
- State continuity of translation in $L^1(\RR^n)$.
slogan: 'For each $f\in L^1(\RR^n)$, $\norm{\tau_hf-f}_1\to0$ as $h\to0$.'
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Equicontinuity
  - Density
  - Lp Spaces
  - Uniform Continuity
relations: []
review: draft
---

::: {.theorem}
For $h\in\RR^n$ and $f\in L^1(\RR^n)$ let $(\tau_hf)(x)\coloneqq f(x-h)$.
For every $f\in L^1(\RR^n)$,
$$
\lim_{h\to 0}\norm{\tau_h f - f}_1 = 0 .
$$
:::

::: {.remark title="Variations"}
(a) For $1\leq p<\infty$ and $f\in L^p(\RR^n)$, $\norm{\tau_h f-f}_p\to0$ as $h\to0$ [@Fol99].

(b) The statement fails for $p=\infty$: for $f\coloneqq\chi_{[0,\infty)}\in L^\infty(\RR)$ and $h\neq0$, $\tau_h f-f=\pm\chi_I$ for the half-open interval $I$ between $0$ and $h$, so $\norm{\tau_h f-f}_\infty=1$.

(c) In the sup norm the statement characterizes uniform continuity: a function $f\colon\RR^n\to\CC$ is [[D-WGYSB|uniformly continuous]] if and only if $\sup_{x\in\RR^n}\abs{f(x-h)-f(x)}\to0$ as $h\to0$.
This is the definition of uniform continuity with $y=x-h$.
:::

::: {.remark}
Each $\tau_h$ is a linear isometry of $L^1(\RR^n)$, so the family $\theset{\tau_h\suchthat h\in\RR^n}$ is equicontinuous as a family of maps $L^1(\RR^n)\to L^1(\RR^n)$.
Together with the pointwise convergence $\tau_hf\to f$ of the theorem, this makes the convergence uniform on compact subsets $K\subseteq L^1(\RR^n)$:
$$
\lim_{h\to0}\sup_{f\in K}\norm{\tau_hf-f}_1=0 .
$$
:::
