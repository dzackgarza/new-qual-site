---
schema: qual/card@1
id: P-3SSNK
kind: problem
title: Riemann–Stieltjes integral against a jump at $0$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(June 2014 1)Define $\alpha \colon [-1,1] \to \mathbb{R}$ by $$\alpha(x) := \begin{cases} -1 & x \in [-1,0] \\ 1 & x \in (0,1]. \end{cases}$$ Let $f \colon [-1,1] \to \mathbb{R}$ be a function that is uniformly bounded on $[-1,1]$ and continuous at $x=0$, but not necessarily continuous for $x \neq 0$.
Prove that $f$ is Riemann-Stieltjes integrable with respect to $\alpha$ over $[-1,1]$ and that $$\int_{-1}^1 f(x)d\alpha(x) = 2f(0).$$
:::

::: {.solution}

::: pf

::: pf-step

$\alpha$ has bounded variation and is constant on each side of its single jump at $0$: $\alpha \equiv -1$ on $[-1,0]$ and $\alpha \equiv 1$ on $(0,1]$, with jump $\alpha(0+) - \alpha(0-) = 2$.

::: pf-proof

By definition, $\alpha$ is nondecreasing and has total variation $\alpha(1)-\alpha(-1)=2$. Its sole increment occurs across an interval whose left endpoint is at most zero and whose right endpoint is strictly positive. In particular, $\alpha(0)=-1$ fixes which partition interval carries that increment.

:::

:::

::: {.pf-step #s2}

For every tagged partition $(P,\tau)$ of $[-1,1]$, exactly one subinterval has nonzero $\alpha$-increment, equal to $2$, and its closure contains $0$.

::: pf-proof

Write $P=(-1=x_0<\cdots<x_m=1)$. There is a unique index $j$ with $x_{j-1}\leq0<x_j$. The values of $\alpha$ at both endpoints of every other subinterval agree, whereas $\alpha(x_j)-\alpha(x_{j-1})=2$. Thus the tagged sum equals $2f(\tau_j)$, with $\tau_j\in[x_{j-1},x_j]$.

:::

:::

::: {.pf-step #s3}

For every $\varepsilon>0$, there is $\delta>0$ such that every tagged partition of mesh less than $\delta$ satisfies
\[
|S_\alpha(f;P,\tau)-2f(0)|<\varepsilon.
\]

::: pf-proof

Continuity of $f$ at zero gives $\delta>0$ such that $|f(t)-f(0)|<\varepsilon/2$ whenever $|t|<\delta$. If the mesh is less than $\delta$, the interval $[x_{j-1},x_j]$ of step [](#s2){.pf-ref} lies in $(-\delta,\delta)$, including its endpoints. Therefore
\[
|S_\alpha(f;P,\tau)-2f(0)|
=2|f(\tau_j)-f(0)|<\varepsilon.
\]

:::

:::

::: {.pf-step #s4}

The function $f$ is Riemann–Stieltjes integrable with respect to $\alpha$ and
\[
\boxed{\int_{-1}^1 f(x)\,d\alpha(x)=2f(0)}.
\]

::: pf-proof

Step [](#s3){.pf-ref} proves convergence of all tagged Stieltjes sums, uniformly in the tags, to $2f(0)$ as the mesh tends to zero. This is the defining criterion for Riemann–Stieltjes integrability. The boundedness hypothesis ensures all tagged sums are finite.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} establishes both assertions.

:::

:::

:::
