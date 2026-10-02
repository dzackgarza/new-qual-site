---
schema: qual/card@1
id: P-CHAVAN-CA-8-1
kind: problem
title: The range of a nonconstant entire function is dense
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Show that the range of every nonconstant entire function is dense in $\mathbb C$.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that the range $f(\CC)$ of a nonconstant
entire function $f$ is not dense in $\CC$.

::: {.proof}
This is the negation of the desired conclusion.
:::

<1>2. There exist $w\in\CC$ and $r>0$ such that
$$
B(w,r)\cap f(\CC)=\varnothing.
$$

::: {.proof}
Since $f(\CC)$ is not dense, its closure is a proper closed subset of $\CC$.
Choose $w\notin\overline{f(\CC)}$. The open complement
$\CC\setminus\overline{f(\CC)}$ then contains some disc $B(w,r)$.
:::

<1>3. The function
$$
g(z)=\frac1{f(z)-w}
$$
is entire and satisfies $\abs{g(z)}\leq1/r$ for every $z\in\CC$.

::: {.proof}
Step <1>2 shows that $f(z)\neq w$ for every $z$, so $g$ is entire. It also gives
$\abs{f(z)-w}\geq r$, hence
$$
\abs{g(z)}=\frac1{\abs{f(z)-w}}\leq\frac1r.
$$
:::

<1>4. The function $f$ is constant.

::: {.proof}
By step <1>3, $g$ is a bounded entire function. Liouville's theorem makes $g$
constant. Since $g=1/(f-w)$, this forces $f$ to be constant as well.
:::

<1>5. Therefore $f(\CC)$ is dense in $\CC$.

::: {.proof}
Step <1>4 contradicts the hypothesis that $f$ is nonconstant, so the assumption
in step <1>1 is false.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
