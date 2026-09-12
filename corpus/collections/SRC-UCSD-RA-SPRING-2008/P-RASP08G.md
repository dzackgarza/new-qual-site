---
schema: qual/card@1
id: P-RASP08G
kind: problem
title: "Distributional derivative of H(x) log|x|"
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
  note: Checked against Problem 7 of the official UCSD Spring 2008 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
(a) For $\phi \in C_0^\infty(\mathbb{R})$ show that the expression
$$
T(\phi) := \lim_{\epsilon \to 0^+} \left[\int_\epsilon^\infty \frac{\phi(x)}{x}\,dx + \phi(0)\log\epsilon\right]
$$
defines a distribution on $\mathbb{R}$.

(b) Show that the function $f(x) := H(x)\log x$ is locally integrable on $\mathbb{R}$ (where $H$ is the Heaviside function).
Express the derivative of $f$ in the sense of distributions in terms of the distribution $T$ given in (a).
:::


::: solution
<1>1. Rewrite the limiting expression in a manifestly finite form.
::: proof
For $0<\varepsilon<1$,
\[
\begin{aligned}
\int_\varepsilon^\infty\frac{\phi(x)}x\,dx+\phi(0)\log\varepsilon
&=\int_\varepsilon^1\frac{\phi(x)-\phi(0)}x\,dx
+\int_1^\infty\frac{\phi(x)}x\,dx.
\end{aligned}
\]
Indeed,
\[
\int_\varepsilon^1\frac{\phi(0)}x\,dx
=-\phi(0)\log\varepsilon.
\]
Since
\[
\frac{\phi(x)-\phi(0)}x\longrightarrow\phi'(0)
\qquad(x\downarrow0),
\]
the first integrand extends continuously to $x=0$. Hence the limit exists and
\[
\boxed{
T(\phi)
=\int_0^1\frac{\phi(x)-\phi(0)}x\,dx
+\int_1^\infty\frac{\phi(x)}x\,dx.}
\]
:::

<1>2. Prove that $T$ is a distribution.
::: proof
Linearity is immediate. Let $K\subset\mathbb R$ be compact and suppose $\operatorname{supp}\phi\subset K$. By the mean-value estimate,
\[
|\phi(x)-\phi(0)|\le x\sup_{0\le t\le1}|\phi'(t)|
\qquad(0\le x\le1),
\]
so
\[
\left|\int_0^1\frac{\phi(x)-\phi(0)}x\,dx\right|
\le \sup_{0\le t\le1}|\phi'(t)|.
\]
If $K\cap[1,\infty)\subset[1,R]$, then
\[
\left|\int_1^\infty\frac{\phi(x)}x\,dx\right|
\le (\log R)\sup_K|\phi|
\]
(with this term absent if $K\cap[1,\infty)=\varnothing$). Thus on every fixed compact support,
\[
|T(\phi)|\le C_K\bigl(\sup_K|\phi|+\sup_K|\phi'|\bigr).
\]
This is precisely the required continuity estimate for a distribution. Therefore
\[
\boxed{T\in\mathcal D'(\mathbb R).}
\]
:::

<1>3. Show that $H(x)\log x$ is locally integrable.
::: proof
Let
\[
f(x)=H(x)\log x,
\]
so $f(x)=0$ for $x<0$ and $f(x)=\log x$ for $x>0$. The only possible local singularity is at $0$, but
\[
\int_0^1|\log x|\,dx=1<\infty.
\]
Away from $0$, $\log x$ is locally integrable. Hence
\[
\boxed{f\in L^1_{\mathrm{loc}}(\mathbb R).}
\]
:::

<1>4. Compute the distributional derivative.
::: proof
For $\phi\in C_c^\infty(\mathbb R)$,
\[
f'(\phi)
=-\int_0^\infty \log x\,\phi'(x)\,dx.
\]
For $\varepsilon>0$, integration by parts gives
\[
-\int_\varepsilon^\infty\log x\,\phi'(x)\,dx
=\int_\varepsilon^\infty\frac{\phi(x)}x\,dx
+\phi(\varepsilon)\log\varepsilon.
\]
Since
\[
(\phi(\varepsilon)-\phi(0))\log\varepsilon\longrightarrow0
\]
as $\varepsilon\downarrow0$, we obtain
\[
\begin{aligned}
f'(\phi)
&=\lim_{\varepsilon\downarrow0}
\left[
\int_\varepsilon^\infty\frac{\phi(x)}x\,dx
+\phi(0)\log\varepsilon
\right]\\
&=T(\phi).
\end{aligned}
\]
Therefore
\[
\boxed{(H\log x)'=T\quad\text{in }\mathcal D'(\mathbb R).}
\]
:::
:::
