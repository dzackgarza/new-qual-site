---
schema: qual/card@1
id: P-RAF23G
kind: problem
title: "Ratio of L^n norms converges to L^infinity norm"
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
  note: Checked against Problem 7 of the official UCSD Fall 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(X, \mu)$ be a nonempty measurable space with $\mu(X) < \infty$, $f \in L^\infty(\mu)$ and $\|f\|_\infty > 0$.
Define $\alpha_n := \int_X |f|^n$ for $n = 1, 2, 3, \ldots$.
Prove that
$$
\lim_{n \to \infty} \frac{\alpha_{n+1}}{\alpha_n} = \|f\|_\infty.
$$
:::

::: {.solution}

::: pf

::: pf-step

Obtain the immediate upper bound.

::: pf-proof

Let
\[
M:=\|f\|_\infty>0.
\]
Since $|f|\le M$ almost everywhere,
\[
\alpha_{n+1}
=\int |f|^{n+1}\,d\mu
\le M\int |f|^n\,d\mu
=M\alpha_n.
\]
Hence
\[
\frac{\alpha_{n+1}}{\alpha_n}\le M.
\]
Also $M>0$ implies $\alpha_n>0$ for every $n$.

:::

:::

::: pf-step

Reinterpret the ratio as an expectation.

::: pf-proof

Define a probability measure $\nu_n$ by
\[
d\nu_n
:=\frac{|f|^n}{\alpha_n}\,d\mu.
\]
Then
\[
\frac{\alpha_{n+1}}{\alpha_n}
=\int |f|\,d\nu_n.
\]
Thus it is enough to show that $\nu_n$ concentrates near the set where $|f|$ is close to $M$.

:::

:::

::: pf-step

Show exponential concentration near the essential supremum.

::: pf-proof

Fix $\varepsilon>0$ with $2\varepsilon<M$. By definition of essential supremum,
\[
A_\varepsilon:=\{|f|>M-\varepsilon\}
\]
has positive measure. Therefore
\[
\alpha_n
\ge \int_{A_\varepsilon}|f|^n\,d\mu
\ge (M-\varepsilon)^n\mu(A_\varepsilon).
\]

Set
\[
B_\varepsilon:=\{|f|\le M-2\varepsilon\}.
\]
Then
\[
\begin{aligned}
\nu_n(B_\varepsilon)
&=\frac{1}{\alpha_n}
\int_{B_\varepsilon}|f|^n\,d\mu\\
&\le
\frac{\mu(X)}{\mu(A_\varepsilon)}
\left(\frac{M-2\varepsilon}{M-\varepsilon}\right)^n
\longrightarrow0.
\end{aligned}
\]

:::

:::

::: pf-step

Pass to the limit.

::: pf-proof

Using Step 2 and restricting the integral to $X\setminus B_\varepsilon$,
\[
\frac{\alpha_{n+1}}{\alpha_n}
=\int |f|\,d\nu_n
\ge (M-2\varepsilon)
\nu_n(X\setminus B_\varepsilon).
\]
By Step 3,
\[
\liminf_{n\to\infty}
\frac{\alpha_{n+1}}{\alpha_n}
\ge M-2\varepsilon.
\]
Since $\varepsilon>0$ is arbitrary and Step 1 gives the opposite upper bound,
\[
\boxed{
\lim_{n\to\infty}\frac{\alpha_{n+1}}{\alpha_n}=M=\|f\|_\infty.}
\]

:::

:::

:::

:::
