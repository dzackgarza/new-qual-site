---
schema: qual/card@1
id: P-BKS09-1A
kind: problem
title: Limit of $\alpha\int_0^1 x^{\alpha-1}f(x)\,dx$ as $\alpha\to 0^+$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed the retained proof.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently verified the epsilon-splitting argument with absolute-value bounds
    on f-f(0), correcting the source solution's omitted absolute values.
---

::: {.problem}
Suppose that f is a continuous real function on [0, 1]. Prove that

$$
\operatorname* { l i m } _ { \alpha \to 0 ^ { + } } \alpha \int _ { 0 } ^ { 1 } x ^ { \alpha - 1 } f ( x ) d x = f ( 0 ) .
$$
:::

::: {.solution}
Set
$$
g(x)\coloneqq f(x)-f(0).
$$

<1>1. For every $\alpha>0$,
$$
\alpha\int_0^1 x^{\alpha-1}f(0)\,dx=f(0).
$$

::: {.proof}
Since $\alpha>0$,
$$
\alpha\int_0^1x^{\alpha-1}\,dx
=
\alpha\left[\frac{x^\alpha}{\alpha}\right]_0^1
=
1.
$$
Multiplying by $f(0)$ gives the claim.
:::

<1>2. One has
$$
\lim_{\alpha\to0^+}
\alpha\int_0^1x^{\alpha-1}g(x)\,dx
=
0.
$$

::: {.proof}
Let $\varepsilon>0$. By continuity of $g$ at $0$ and $g(0)=0$, choose
$\delta\in(0,1)$ such that
$$
\abs{g(x)}<\frac{\varepsilon}{2}
$$
for $0\leq x\leq\delta$. Since $g$ is continuous on $[0,1]$, set
$$
M\coloneqq\max_{0\leq x\leq1}\abs{g(x)}.
$$
Then, for every $\alpha>0$,
$$
\begin{aligned}
\abs{
\alpha\int_0^1x^{\alpha-1}g(x)\,dx
}
&\leq
\alpha\int_0^\delta x^{\alpha-1}\abs{g(x)}\,dx
+
\alpha\int_\delta^1x^{\alpha-1}\abs{g(x)}\,dx\\
&\leq
\frac{\varepsilon}{2}\delta^\alpha
+
M(1-\delta^\alpha)\\
&\leq
\frac{\varepsilon}{2}
+
M(1-\delta^\alpha).
\end{aligned}
$$
Because $0<\delta<1$,
$$
\delta^\alpha\longrightarrow1
$$
as $\alpha\to0^+$. Hence, for all sufficiently small $\alpha>0$,
$$
M(1-\delta^\alpha)<\frac{\varepsilon}{2}.
$$
The displayed estimate is then $<\varepsilon$, proving the limit.
:::

<1>3. Therefore
$$
\lim_{\alpha\to0^+}
\alpha\int_0^1x^{\alpha-1}f(x)\,dx
=
\boxed{f(0)}.
$$

::: {.proof}
Since $f=g+f(0)$, split the integral into these two terms. Step <1>1
evaluates the constant term, and step <1>2 shows that the remaining term
tends to $0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required limit.
:::
:::
