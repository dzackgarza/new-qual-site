---
schema: qual/card@1
id: PR-JX4YU
kind: proposition
title: Continuity of translation in $L^p$ for $1\leq p<\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Uniform Continuity
  - Continuity
relations: []
review: draft
---

::: {.proposition}
For $h\in\RR^n$ and $f\colon\RR^n\to\CC$, let $(\tau_h f)(x)\coloneqq f(x-h)$.

(a) If $1\leq p<\infty$ and $f\in L^p(\RR^n)$, then $\norm{\tau_h f-f}_{L^p}\to0$ as $h\to0$ [@Fol13, Proposition 8.5].

(b) A function $f\colon\RR^n\to\CC$ is [[D-WGYSB|uniformly continuous]] if and only if $\sup_{x\in\RR^n}\abs{f(x-h)-f(x)}\to0$ as $h\to0$.
:::

::: {.example}
Part (a) fails for $p=\infty$: for $f\coloneqq\chi_{[0,\infty)}\in L^\infty(\RR)$ and $h\neq0$, $\tau_h f-f=\pm\chi_I$ for the half-open interval $I$ between $0$ and $h$, so $\norm{\tau_h f-f}_{L^\infty}=1$.
:::
