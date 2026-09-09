---
schema: qual/card@1
id: P-JP74P
kind: problem
title: 'Weyl''s equidistribution theorem: $\frac1N\sum_{n=1}^N f(n\alpha)\to\int_0^1
  f$ for continuous $1$-periodic $f$ and irrational $\alpha$'
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Integrals
  - Fourier Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the recorded UGA Spring 2015 real-analysis exam source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f: \RR \to \CC$ be continuous with period 1. Prove that
\[
\lim _{N \rightarrow \infty} \frac{1}{N} \sum_{n=1}^{N} f(n \alpha)=\int_{0}^{1} f(t) d t \quad \forall \alpha \in \RR\setminus\QQ.
\]

> Hint: show this first for the functions $f(t) = e^{2\pi i k t}$ for $k\in \ZZ$.
:::

::: solution
<1>1. Prove the limit for the exponential basis functions.
::: proof
For $k\in\mathbb Z$, let
\[
e_k(t)=e^{2\pi i kt}.
\]
If $k=0$, then
\[
\frac1N\sum_{n=1}^Ne_k(n\alpha)=1=\int_0^1e_k(t)\,dt.
\]
If $k\ne0$, put
\[
z=e^{2\pi i k\alpha}.
\]
Because $\alpha$ is irrational, $k\alpha\notin\mathbb Z$, so $z\ne1$. The geometric-series formula gives
\[
\sum_{n=1}^Nz^n=z\frac{1-z^N}{1-z}.
\]
Hence
\[
\left|\frac1N\sum_{n=1}^Ne^{2\pi i kn\alpha}\right|
\le \frac{2}{N|1-e^{2\pi i k\alpha}|}
\longrightarrow0.
\]
Also
\[
\int_0^1e^{2\pi i kt}\,dt=0.
\]
Thus the desired limit holds for every exponential $e_k$, and therefore for every trigonometric polynomial by linearity.
:::

<1>2. Pass from trigonometric polynomials to continuous periodic functions.
::: proof
Trigonometric polynomials are uniformly dense in the continuous $1$-periodic functions. Fix $\varepsilon>0$ and choose a trigonometric polynomial $P$ with
\[
\|f-P\|_\infty<\varepsilon.
\]
Then for every $N$,
\[
\left|\frac1N\sum_{n=1}^N(f-P)(n\alpha)\right|
\le\varepsilon,
\]
and
\[
\left|\int_0^1(f-P)(t)\,dt\right|
\le\varepsilon.
\]
By Step 1,
\[
\frac1N\sum_{n=1}^NP(n\alpha)
\longrightarrow\int_0^1P(t)\,dt.
\]
Therefore
\[
\limsup_{N\to\infty}
\left|
\frac1N\sum_{n=1}^Nf(n\alpha)-\int_0^1f(t)\,dt
\right|
\le2\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\boxed{
\frac1N\sum_{n=1}^Nf(n\alpha)
\longrightarrow\int_0^1f(t)\,dt.}
\]
:::
:::
