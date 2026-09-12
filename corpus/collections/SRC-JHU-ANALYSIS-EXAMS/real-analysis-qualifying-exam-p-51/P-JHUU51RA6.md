---
schema: qual/card@1
id: P-JHUU51RA6
kind: problem
title: "The principal value distribution is the derivative of log |x|"
classification:
  areas:
  - real-analysis
  topics:
  - Distributions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 6 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Define $u\in\mathcal D'(\mathbb R)$ formally by
\[
\langle u,\varphi\rangle
=
\lim_{\varepsilon\to0^+}
\left(
\int_{-\infty}^{-\varepsilon}\frac{\varphi(x)}x\,dx
+
\int_{\varepsilon}^{\infty}\frac{\varphi(x)}x\,dx
\right),
\qquad \varphi\in C_c^\infty(\mathbb R).
\]
Show that the limit exists and that
\[
u=(\log|x|)'
\]
in the sense of distributions.
:::

::: {.solution}
<1>1. The principal-value limit exists.
::: {.proof}
Fix $\varphi\in C_c^\infty(\mathbb R)$. For $0<\varepsilon<1$, symmetry gives
\[
\int_{-1}^{-\varepsilon}\frac{\varphi(0)}x\,dx
+
\int_{\varepsilon}^{1}\frac{\varphi(0)}x\,dx=0.
\]
Hence the truncated principal value can be rewritten as
\[
\begin{aligned}
&\int_{\varepsilon<|x|<1}\frac{\varphi(x)-\varphi(0)}x\,dx
+
\int_{|x|\ge1}\frac{\varphi(x)}x\,dx.
\end{aligned}
\]
The second integral is absolutely convergent because $\varphi$ has compact support. Near $0$, the mean-value theorem gives
\[
|\varphi(x)-\varphi(0)|\le C|x|,
\]
so
\[
\left|\frac{\varphi(x)-\varphi(0)}x\right|\le C.
\]
Thus the first integral converges absolutely as $\varepsilon\to0^+$. Therefore the principal-value limit exists.
:::

<1>2. The locally integrable function $\log|x|$ defines a distribution.
::: {.proof}
Since
\[
\int_0^1|\log x|\,dx<\infty,
\]
we have $\log|x|\in L^1_{\mathrm{loc}}(\mathbb R)$. Hence it defines a distribution by
\[
\langle \log|x|,\varphi\rangle
=
\int_{\mathbb R}\log|x|\,\varphi(x)\,dx.
\]
:::

<1>3. Its distributional derivative equals $u$.
::: {.proof}
By definition,
\[
\langle (\log|x|)',\varphi\rangle
=-\int_{\mathbb R}\log|x|\,\varphi'(x)\,dx.
\]
Split at $\pm\varepsilon$ and integrate by parts:
\[
\begin{aligned}
&-\int_{-\infty}^{-\varepsilon}\log|x|\,\varphi'(x)\,dx
-\int_{\varepsilon}^{\infty}\log x\,\varphi'(x)\,dx\\
&\qquad=
\int_{-\infty}^{-\varepsilon}\frac{\varphi(x)}x\,dx
+
\int_{\varepsilon}^{\infty}\frac{\varphi(x)}x\,dx
+
\log\varepsilon\,[\varphi(\varepsilon)-\varphi(-\varepsilon)].
\end{aligned}
\]
Because $\varphi$ is smooth,
\[
\varphi(\varepsilon)-\varphi(-\varepsilon)=O(\varepsilon),
\]
and therefore
\[
\log\varepsilon\,[\varphi(\varepsilon)-\varphi(-\varepsilon)]\to0
\]
as $\varepsilon\to0^+$. Taking the limit yields
\[
\langle (\log|x|)',\varphi\rangle
=\operatorname{p.v.}\int_{\mathbb R}\frac{\varphi(x)}x\,dx
=\langle u,\varphi\rangle.
\]
Thus
\[
\boxed{u=(\log|x|)'}
\]
in $\mathcal D'(\mathbb R)$.
:::
:::
