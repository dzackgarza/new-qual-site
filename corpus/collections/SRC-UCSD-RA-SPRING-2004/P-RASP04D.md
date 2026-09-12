---
schema: qual/card@1
id: P-RASP04D
kind: problem
title: "Differentiation and approximation properties of convolution"
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
  note: Checked against Problem 4 of the official UCSD Spring 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\varphi \in C_c^\infty(\mathbb{R})$ and $f : \mathbb{R} \to \mathbb{R}$ be an absolutely continuous function with compact support, and $\varphi * f$ be the convolution of $\varphi$ and $f$:
$$
(\varphi * f)(x) := \int_{\mathbb{R}} \varphi(x - y) f(y)\,dy.
$$

(a) Show $\frac{d}{dx}(\varphi * f)(x) = (\varphi' * f)(x)$ for all $x \in \mathbb{R}$.

(b) Show $(\varphi' * f)(x) = (\varphi * f')(x)$ for all $x \in \mathbb{R}$.

(c) Explain why there exists $f_n \in C_c^\infty(\mathbb{R})$ such that
$$
\lim_{n \to \infty} \|f_n - f\|_{L^\infty(\mathbb{R}, m)} = 0 = \lim_{n \to \infty} \|f' - f_n'\|_{L^1(\mathbb{R}, m)}.
$$
:::

::: solution
<1>1. Differentiate the convolution in $x$.
::: proof
Because $f$ has compact support and $\varphi'\in C_c(\mathbb R)$, differentiation under the integral is justified by dominated convergence. Thus for every $x$,
\[
\frac d{dx}(\varphi*f)(x)
=\int_{\mathbb R}\varphi'(x-y)f(y)\,dy
=(\varphi'*f)(x).
\]
:::

<1>2. Move the derivative from $\varphi$ to $f$.
::: proof
Since
\[
\frac d{dy}\varphi(x-y)=-\varphi'(x-y),
\]
integration by parts gives
\[
\begin{aligned}
(\varphi'*f)(x)
&=-\int_{\mathbb R}\frac d{dy}\bigl(\varphi(x-y)\bigr)f(y)\,dy\\
&=\int_{\mathbb R}\varphi(x-y)f'(y)\,dy.
\end{aligned}
\]
There is no boundary term because both factors have compact support. Hence
\[
\boxed{\varphi'*f=\varphi*f'.}
\]
:::

<1>3. Approximate $f$ by smooth compactly supported functions.
::: proof
Let $\rho\in C_c^\infty(\mathbb R)$ be nonnegative with
\[
\int_{\mathbb R}\rho=1,
\]
and set
\[
\rho_\varepsilon(x)=\varepsilon^{-1}\rho(x/\varepsilon),
\qquad
f_\varepsilon=\rho_\varepsilon*f.
\]
Then $f_\varepsilon\in C_c^\infty(\mathbb R)$.

Because $f$ is continuous with compact support, it is uniformly continuous on $\mathbb R$. Therefore
\[
\begin{aligned}
|f_\varepsilon(x)-f(x)|
&\le \int \rho_\varepsilon(y)|f(x-y)-f(x)|\,dy\\
&\le \sup_{|y|\le C\varepsilon}|f(x-y)-f(x)|,
\end{aligned}
\]
where $C$ bounds the support of $\rho$. Hence
\[
\|f_\varepsilon-f\|_\infty\longrightarrow0.
\]

Since $f$ is absolutely continuous with compact support, $f'\in L^1(\mathbb R)$. By Step 2,
\[
f_\varepsilon'=\rho_\varepsilon*f'.
\]
The family $(\rho_\varepsilon)$ is an approximate identity in $L^1$, so
\[
\|f_\varepsilon'-f'\|_1
=\|\rho_\varepsilon*f'-f'\|_1
\longrightarrow0.
\]
Choosing any sequence $\varepsilon_n\downarrow0$ and setting $f_n=f_{\varepsilon_n}$ gives
\[
\boxed{
\|f_n-f\|_\infty\to0,
\qquad
\|f_n'-f'\|_1\to0.}
\]
:::
:::
