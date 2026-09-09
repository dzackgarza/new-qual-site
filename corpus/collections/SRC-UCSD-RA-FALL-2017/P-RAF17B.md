---
schema: qual/card@1
id: P-RAF17B
kind: problem
title: "True/false on convergence in L^p and pointwise convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(\Omega, \mathcal{B}, \mu)$ be a measure space and $f_n, f : \Omega \to \mathbb{C}$ be measurable functions.
Determine which of the following statements are true.
For the true statements give a brief reason and for the false statements give a counterexample.

1. If $f_n \to f$ in $L^2(\mu)$, then $\lim_{n \to \infty} f_n(\omega) = f(\omega)$ for $\mu$-a.e. $\omega$.

2. Suppose that $\omega_0 \in \Omega$ is a point such that $\{\omega_0\} \in \mathcal{B}$ and $0 < \mu(\{\omega_0\}) < \infty$.
   If $f_n \to f$ in $L^2(\mu)$, then $f(\omega_0) = \lim_{n \to \infty} f_n(\omega_0)$.

3. If $f(\omega) = \lim_{n \to \infty} f_n(\omega)$ for $\mu$-a.e. $\omega$, then $f_n \to f$ in measure, i.e. $\lim_{n \to \infty} \mu(|f - f_n| \geq \varepsilon) = 0$ for all $\varepsilon > 0$.

4. If $\mu(\Omega) < \infty$ and $f_n \to f$ in $L^3(\mu)$, then $f_n \to f$ in $L^1(\mu)$.
:::

::: solution
<1>1. Statement 1 is false.
::: proof
Take $\Omega=[0,1]$ with Lebesgue measure and enumerate the dyadic intervals level by level:
\[
f_n=\mathbf1_{[j2^{-k},(j+1)2^{-k})}
\]
for $0\le j<2^k$, with $k\to\infty$ along the enumeration. Then
\[
\|f_n\|_2=2^{-k/2}\longrightarrow0,
\]
so $f_n\to0$ in $L^2$.

For every non-dyadic $x\in[0,1]$, at each level $k$ exactly one dyadic interval contains $x$, while the other intervals at that level do not. Hence $f_n(x)$ takes both values $1$ and $0$ infinitely often. Thus the full sequence does not converge pointwise at almost every $x$.
:::

<1>2. Statement 2 is true.
::: proof
Since the singleton $\{\omega_0\}$ has positive finite measure,
\[
\|f_n-f\|_2^2
\ge
\int_{\{\omega_0\}}|f_n-f|^2\,d\mu
=|f_n(\omega_0)-f(\omega_0)|^2\mu(\{\omega_0\}).
\]
Therefore
\[
|f_n(\omega_0)-f(\omega_0)|
\le
\frac{\|f_n-f\|_2}{\mu(\{\omega_0\})^{1/2}}
\longrightarrow0.
\]
:::

<1>3. Statement 3 is false in general.
::: proof
Take $\Omega=\mathbb R$ with Lebesgue measure,
\[
f_n=\mathbf1_{[n,n+1]},
\qquad
f=0.
\]
Then $f_n(x)\to0$ for every $x\in\mathbb R$. But for $\varepsilon=1/2$,
\[
m\bigl(\{|f_n-f|\ge1/2\}\bigr)
=m([n,n+1])=1
\]
for every $n$. Hence $f_n$ does not converge to $f$ in measure.
:::

<1>4. Statement 4 is true.
::: proof
Let $h_n=f_n-f$. Hölder's inequality with exponents $3$ and $3/2$ gives
\[
\|h_n\|_1
=\int_\Omega |h_n|\cdot1\,d\mu
\le
\|h_n\|_3\,\|1\|_{3/2}
=\mu(\Omega)^{2/3}\|h_n\|_3.
\]
Since $\|h_n\|_3\to0$,
\[
\boxed{\|f_n-f\|_1\to0.}
\]
:::
:::
