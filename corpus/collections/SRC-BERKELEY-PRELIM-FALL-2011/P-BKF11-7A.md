---
schema: qual/card@1
id: P-BKF11-7A
kind: problem
title: Laurent expansion of $1/(1+z)+1/(z^2-9)$ on $1<\lvert z\rvert<3$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both geometric-series expansions and their respective convergence
    regions; their intersection is exactly the required annulus.
---

::: {.problem}
Find the Laurent expansion of
$$
f(z)=\frac1{1+z}+\frac1{z^2-9}
$$
in the annulus $\{z:1<\abs{z}<3\}$.
:::

::: {.solution}
<1>1. For $\abs{z}>1$,
$$
\frac1{1+z}
=\sum_{n=0}^{\infty}(-1)^n z^{-n-1}.
$$

::: {.proof}
If $\abs{z}>1$, then $\abs{z^{-1}}<1$. Hence the geometric series
gives
$$
\begin{aligned}
\frac1{1+z}
&=\frac1z\frac1{1+z^{-1}}\\
&=\frac1z\sum_{n=0}^{\infty}(-z^{-1})^n\\
&=\sum_{n=0}^{\infty}(-1)^n z^{-n-1}.
\end{aligned}
$$
:::

<1>2. For $\abs{z}<3$,
$$
\frac1{z^2-9}
=-\sum_{n=0}^{\infty}\frac{z^{2n}}{9^{n+1}}.
$$

::: {.proof}
If $\abs{z}<3$, then $\abs{z^2/9}<1$. Therefore
$$
\begin{aligned}
\frac1{z^2-9}
&=-\frac19\frac1{1-z^2/9}\\
&=-\frac19\sum_{n=0}^{\infty}\left(\frac{z^2}{9}\right)^n\\
&=-\sum_{n=0}^{\infty}\frac{z^{2n}}{9^{n+1}}.
\end{aligned}
$$
:::

<1>3. On $1<\abs{z}<3$, the Laurent expansion of $f$ is
$$
\boxed{
f(z)
=\sum_{n=0}^{\infty}(-1)^n z^{-n-1}
-\sum_{n=0}^{\infty}\frac{z^{2n}}{9^{n+1}}
}.
$$

::: {.proof}
Step <1>1 converges for $\abs{z}>1$, and step <1>2 converges for
$\abs{z}<3$. Both therefore converge on the requested annulus, where
their sum equals $f$. Written termwise, the expansion begins
$$
\frac1z-\frac1{z^2}+\frac1{z^3}-\cdots
-\frac19-\frac{z^2}{81}-\frac{z^4}{729}-\cdots,
$$
in agreement with the two series above.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required Laurent expansion on the stated annulus.
:::
:::
