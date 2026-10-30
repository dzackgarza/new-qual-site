---
schema: qual/card@1
id: P-RAF22C
kind: problem
title: "High-frequency parity oscillations integrate to zero against any $L^1$ function"
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Density Arguments
  - Oscillatory Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Set $E = \bigcup_{m \in \ZZ} [2m, 2m+1)$ and $P = \chi_E - \chi_{\RR \setminus E}$, so that $P(x)$ is $1$ if the greatest integer less than or equal to $x$ is even and is $-1$ if it is odd.
Define $S_n(x) = P(10^n x)$.
Prove that for every $f \in L^1(\RR)$
$$
\int_\RR S_n(x) f(x) \, dx \to 0 \quad \text{as } n \to \infty.
$$
:::

::: {.solution}

::: pf

::: pf-step

The primitive $F_n(x)\coloneqq\int_0^xS_n(t)\,dt$ satisfies $\norm{F_n}_\infty\le10^{-n}$.

::: pf-proof

The function $P$ has period $2$ and has mean zero on each period. Hence $S_n(x)=P(10^n x)$ has period
$$
2\cdot 10^{-n}
$$
and mean zero on each period.

Define
$$
F_n(x):=\int_0^x S_n(t)\,dt.
$$
Because the integral over every full period is zero, $F_n$ is periodic with the same period. On each half-period, $S_n$ is constant equal to $1$ or $-1$, so the oscillation of $F_n$ is at most $10^{-n}$. Therefore
$$
\norm{F_n}_\infty\le 10^{-n}.
$$

:::

:::

::: {.pf-step #s2}

$\int_{\RR}S_n\varphi\to0$ for every $\varphi\in C_c^1(\RR)$.

::: pf-proof

Let $\varphi\in C_c^1(\RR)$. Since $F_n'=S_n$ almost everywhere and $\varphi$ has compact support, integration by parts gives
$$
\int_{\RR}S_n(x)\varphi(x)\,dx
=-\int_{\RR}F_n(x)\varphi'(x)\,dx.
$$
Hence
$$
\abs{\int S_n\varphi}
\le \norm{F_n}_\infty\,\norm{\varphi'}_1
\le 10^{-n}\norm{\varphi'}_1
\longrightarrow0.
$$

:::

:::

::: pf-step

$\int_{\RR}S_nf\to0$ for every $f\in L^1(\RR)$.

::: pf-proof

Fix $f\in L^1(\RR)$ and $\varepsilon>0$. Choose $\varphi\in C_c^1(\RR)$ such that
$$
\norm{f-\varphi}_1<\varepsilon.
$$
Since $\abs{S_n}=1$ almost everywhere,
$$
\abs{\int S_n(f-\varphi)}
\le \norm{f-\varphi}_1<\varepsilon.
$$
By step [](#s2){.pf-ref}, for all sufficiently large $n$,
$$
\abs{\int S_n\varphi}<\varepsilon.
$$
Therefore
$$
\abs{\int S_nf}<2\varepsilon
$$
for all sufficiently large $n$. Since $\varepsilon$ is arbitrary,
$$
\boxed{\int_{\RR}S_n(x)f(x)\,dx\longrightarrow0.}
$$

:::

:::

:::

:::
