---
schema: qual/card@1
id: P-AGH3O
kind: problem
title: The maximal function of an $L^1$ function need not be locally integrable
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - L¹
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Consider the function
\[
f(x) \da 
\begin{cases}
{1\over \abs{x} \qty{ \log\qty{1\over x}}^2 } &  \abs{x} \leq {1\over 2}
\\
0 & \text{else}.
\end{cases}
\]

a. Show that $f \in L^1(\RR)$.

b. Show that there exists a $c>0$ such that for all $\abs{x} \leq 1/2$,
\[
Hf(x) \geq {c \over \abs{x} \log\qty{1\over \abs x} }
.\]
Conclude that $Hf$ is not locally integrable.
:::

::: {.solution}
Here $Hf(x) = \sup_{r>0}\frac{1}{2r}\int_{x-r}^{x+r}|f(t)|\,dt$ is the Hardy--Littlewood maximal function, and $f(x) = \frac{1}{|x|\log^2(1/|x|)}$ for $0 < |x| \le 1/2$.

::: pf

::: {.pf-step #s1}

For $0 < s \le 1/2$, $\int_{-s}^{s} f = \frac{2}{\log(1/s)}$. In particular $\int_\RR f = \frac{2}{\log 2}$, so $f \in L^1(\RR)$.

::: pf-proof

$f$ is even, and the substitution $u = \log(1/t)$, $du = -dt/t$, gives $\int_0^{s}\frac{dt}{t\log^2(1/t)} = \int_{\log(1/s)}^\infty u^{-2}\,du = \frac{1}{\log(1/s)}$.

:::

:::

::: {.pf-step #s2}

For $0 < |x| \le 1/2$, $Hf(x) \ge \frac{1}{2|x|\log(1/|x|)}$.

::: pf-proof

Take $r = 2|x|$. The interval $(x - r, x + r)$ contains $(-|x|, |x|)$ and $f \ge 0$, so by step [](#s1){.pf-ref}
$$
Hf(x) \ge \frac{1}{4|x|}\int_{-|x|}^{|x|} f = \frac{1}{4|x|}\cdot\frac{2}{\log(1/|x|)}.
$$
So part (b) holds with $c = 1/2$.

:::

:::

::: pf-step

$Hf$ is not integrable on any neighborhood of $0$.

::: pf-proof

For $0 < \delta \le 1/2$, step [](#s2){.pf-ref} and the substitution $u = \log(1/x)$ give
$$
\int_{-\delta}^{\delta} Hf \ge 2 \cdot \frac12\int_0^{\delta}\frac{dx}{x\log(1/x)} = \int_{\log(1/\delta)}^\infty \frac{du}{u} = \infty.
$$

:::

:::

:::

:::

::: {.remark}
For $x < 0$ the formula is read with $\log(1/|x|)$ in place of $\log(1/x)$, so that $f$ is even.
:::
