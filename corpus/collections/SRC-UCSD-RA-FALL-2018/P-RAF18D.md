---
schema: qual/card@1
id: P-RAF18D
kind: problem
title: "Integral of |f(x) - f(y)| over a thin diagonal strip"
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
  note: Checked against Problem 4 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^1([0,1], m)$, $m^2$ be Lebesgue measure on $\mathbb{R}^2$, and
$$
A_\varepsilon = \{(x,y) \in [0,1] \times [0,1] : |x - y| \leq \varepsilon\} \quad \text{for all } \varepsilon > 0.
$$
Prove that

1) $\displaystyle\int_{A_\varepsilon} |f(x) - f(y)|\,dm^2(x,y) \leq 4\varepsilon \cdot \|f\|_{L^1([0,1], m)}$ and

2) $\displaystyle\lim_{\varepsilon \downarrow 0} \varepsilon^{-1} \int_{A_\varepsilon} |f(x) - f(y)|\,dm^2(x,y) = 0.$
:::

::: solution
<1>1. Prove the $4\varepsilon\|f\|_1$ estimate.
::: proof
Using
\[
|f(x)-f(y)|\le |f(x)|+|f(y)|,
\]
we obtain
\[
\begin{aligned}
\int_{A_\varepsilon}|f(x)-f(y)|\,dx\,dy
&\le
\int_{A_\varepsilon}|f(x)|\,dx\,dy
+\int_{A_\varepsilon}|f(y)|\,dx\,dy.
\end{aligned}
\]
For each fixed $x\in[0,1]$, the section
\[
\{y\in[0,1]:|x-y|\le\varepsilon\}
\]
has length at most $2\varepsilon$. Hence, by Tonelli,
\[
\int_{A_\varepsilon}|f(x)|\,dx\,dy
\le2\varepsilon\|f\|_1.
\]
The same estimate holds for the second term by symmetry. Therefore
\[
\boxed{
\int_{A_\varepsilon}|f(x)-f(y)|\,dx\,dy
\le4\varepsilon\|f\|_1.}
\]
:::

<1>2. Rewrite the thin-strip integral using translations.
::: proof
Extend $f$ by zero outside $[0,1]$, still denoting the extension by $f$. Then $f\in L^1(\mathbb R)$. With $h=y-x$, the original domain is contained in the set $|h|\le\varepsilon$, so
\[
\begin{aligned}
\int_{A_\varepsilon}|f(x)-f(y)|\,dx\,dy
&\le
\int_{-\varepsilon}^{\varepsilon}
\int_{\mathbb R}|f(x)-f(x+h)|\,dx\,dh\\
&=
\int_{-\varepsilon}^{\varepsilon}
\|\tau_hf-f\|_1\,dh,
\end{aligned}
\]
where $(\tau_hf)(x)=f(x+h)$.
:::

<1>3. Use continuity of translations in $L^1$.
::: proof
It is standard that
\[
\|\tau_hf-f\|_1\longrightarrow0
\qquad(h\to0).
\]
Given $\eta>0$, choose $\delta>0$ such that
\[
|h|<\delta
\quad\Longrightarrow\quad
\|\tau_hf-f\|_1<\eta.
\]
Then for $0<\varepsilon<\delta$, Step 2 gives
\[
\frac1\varepsilon
\int_{A_\varepsilon}|f(x)-f(y)|\,dx\,dy
\le
\frac1\varepsilon
\int_{-\varepsilon}^{\varepsilon}\eta\,dh
=2\eta.
\]
Since $\eta>0$ is arbitrary,
\[
\boxed{
\lim_{\varepsilon\downarrow0}
\frac1\varepsilon
\int_{A_\varepsilon}|f(x)-f(y)|\,dx\,dy=0.}
\]
:::
:::
