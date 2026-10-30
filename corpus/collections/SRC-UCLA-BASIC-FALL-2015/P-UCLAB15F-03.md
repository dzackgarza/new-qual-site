---
schema: qual/card@1
id: P-UCLAB15F-03
kind: problem
title: Continuity of the pointwise limit of an alternating monotone series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $\{f_n\}$ be continuous functions $f_n:[-1,1]\to[0,1]$ such that for each $x\in[-1,1]$:

1. the sequence $\{f_n(x)\}_{n=1}^{\infty}$ is non-increasing;

2. $\lim_{n\to\infty}f_n(x)=0$.

Define
$$
g_n(x):=\sum_{m=1}^n(-1)^m f_m(x).
$$
Prove that $g_n(x)$ converges to some $g(x)\in\RR$ for every $x\in[-1,1]$ and that the resulting function $g:[-1,1]\to\RR$ is continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For each fixed $x\in[-1,1]$, the series
$$
\sum_{m=1}^{\infty}(-1)^mf_m(x)
$$
converges.


::: pf-proof

For fixed $x$, the numbers
$$
f_1(x)\ge f_2(x)\ge\cdots\ge0
$$
decrease to $0$ by hypothesis. The alternating-series test therefore gives convergence.
Denote its sum by
$$
g(x).
$$
Thus
$$
g_n(x)\to g(x)
$$
for every fixed $x$.

:::

:::

::: {.pf-step #s1-2}

The sequence $(f_n)$ converges uniformly to $0$ on $[-1,1]$.


::: pf-proof

Fix $\varepsilon>0$ and define
$$
U_n=\{x\in[-1,1]:f_n(x)<\varepsilon\}.
$$
Each $U_n$ is open in $[-1,1]$ because $f_n$ is continuous.
Since
$$
f_{n+1}(x)\le f_n(x),
$$
the sets are nested:
$$
U_n\subseteq U_{n+1}.
$$
Pointwise convergence $f_n(x)\to0$ gives
$$
[-1,1]=\bigcup_{n=1}^{\infty}U_n.
$$
Compactness of $[-1,1]$ yields a finite subcover
$$
U_{n_1},\ldots,U_{n_r}.
$$
Let
$$
N=\max\{n_1,\ldots,n_r\}.
$$
Nesting gives
$$
[-1,1]=U_N.
$$
Hence
$$
0\le f_n(x)\le f_N(x)<\varepsilon
$$
for every $n\ge N$ and every $x\in[-1,1]$.
Therefore
$$
\norm{f_n}_\infty\to0.
$$

:::

:::

::: {.pf-step #s1-3}

For every $n$ and every $x\in[-1,1]$,
$$
\abs{g(x)-g_n(x)}
\le
f_{n+1}(x).
$$


::: pf-proof

For fixed $x$, the series from step [](#s1-1){.pf-ref} is an alternating series whose term magnitudes
$$
f_m(x)
$$
decrease to zero.
The alternating-series remainder estimate therefore gives
$$
\abs{
\sum_{m=n+1}^{\infty}(-1)^mf_m(x)
}
\le
f_{n+1}(x).
$$
The left side is exactly
$$
\abs{g(x)-g_n(x)}.
$$

:::

:::

::: {.pf-step #s1-4}

The convergence
$$
g_n\to g
$$
is uniform on $[-1,1]$.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\norm{g-g_n}_\infty
\le
\norm{f_{n+1}}_\infty.
$$
The right side tends to zero by step [](#s1-2){.pf-ref}.
Therefore
$$
\norm{g-g_n}_\infty\to0.
$$

:::

:::

::: {.pf-step #s1-5}

Each $g_n$ is continuous on $[-1,1]$.


::: pf-proof

The function
$$
g_n
=
\sum_{m=1}^n(-1)^mf_m
$$
is a finite linear combination of continuous functions.

:::

:::

::: {.pf-step #s1-6}

The limit function $g$ is continuous on $[-1,1]$.


::: pf-proof

By step [](#s1-4){.pf-ref}, $g_n\to g$ uniformly, and by step [](#s1-5){.pf-ref} every $g_n$ is continuous.
A uniform limit of continuous functions is continuous.
Thus
$$
\boxed{g\in C([-1,1])}.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves pointwise existence of the limit, and steps [](#s1-2){.pf-ref} through [](#s1-6){.pf-ref} prove continuity of the resulting function.

:::

:::

:::
