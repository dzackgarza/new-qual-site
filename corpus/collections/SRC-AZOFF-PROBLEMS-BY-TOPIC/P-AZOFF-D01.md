---
schema: qual/card@1
id: P-AZOFF-D01
kind: problem
title: Riemann integrability of $g$ when $|g(x)-g(y)|\le|f(x)-f(y)|$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Compared Darboux oscillations interval by interval. The hypothesis gives
    osc_I(g)<=osc_I(f) on every subinterval, so every partition whose upper
    and lower sums for f differ by less than epsilon has the same property
    for g. The source compilation contains no worked solution.
---

::: {.problem}
Suppose $f , g : [ 0 , 1 ] \to \mathbb { R }$ with f Riemann integrable and

$$
| g ( x ) - g ( y ) | \leq | f ( x ) - f ( y ) | , \qquad x , y \in [ 0 , 1 ] .
$$

Prove that g is also Riemann integrable.
:::

::: {.solution}
<1>1. The function $g$ is bounded on $[0,1]$.

::: {.proof}
Since $f$ is Riemann integrable, it is bounded. Thus there is $M\geq0$ such
that
$$
\abs{f(x)}\leq M
$$
for every $x\in[0,1]$.

Fix $y_0\in[0,1]$. For every $x\in[0,1]$,
$$
\begin{aligned}
\abs{g(x)}
&\leq
\abs{g(y_0)}
+
\abs{g(x)-g(y_0)}\\
&\leq
\abs{g(y_0)}
+
\abs{f(x)-f(y_0)}\\
&\leq
\abs{g(y_0)}+2M.
\end{aligned}
$$
Hence $g$ is bounded.
:::

<1>2. For every nonempty interval $I\subseteq[0,1]$, the oscillations satisfy
$$
\operatorname{osc}_I(g)
\leq
\operatorname{osc}_I(f),
$$
where
$$
\operatorname{osc}_I(h)
=
\sup_I h-\inf_I h.
$$

::: {.proof}
For all $x,y\in I$, the hypothesis gives
$$
\abs{g(x)-g(y)}
\leq
\abs{f(x)-f(y)}
\leq
\sup_I f-\inf_I f.
$$
Taking the supremum over $x,y\in I$ on the left gives
$$
\sup_I g-\inf_I g
\leq
\sup_I f-\inf_I f.
$$
:::

<1>3. For every partition
$$
P:\quad
0=x_0<x_1<\cdots<x_n=1,
$$
one has
$$
U(g,P)-L(g,P)
\leq
U(f,P)-L(f,P).
$$

::: {.proof}
Let
$$
I_j=[x_{j-1},x_j].
$$
By the definitions of the upper and lower Darboux sums,
$$
U(h,P)-L(h,P)
=
\sum_{j=1}^n
\operatorname{osc}_{I_j}(h)(x_j-x_{j-1})
$$
for any bounded real-valued function $h$. Applying step <1>2 to each
$I_j$ gives the displayed inequality.
:::

<1>4. For every $\varepsilon>0$, there is a partition $P$ such that
$$
U(g,P)-L(g,P)<\varepsilon.
$$

::: {.proof}
Since $f$ is Riemann integrable, the Darboux criterion gives a partition $P$
with
$$
U(f,P)-L(f,P)<\varepsilon.
$$
Step <1>3 then gives
$$
U(g,P)-L(g,P)
\leq
U(f,P)-L(f,P)
<
\varepsilon.
$$
:::

<1>5. The function $g$ is Riemann integrable on $[0,1]$.

::: {.proof}
Step <1>1 gives boundedness, and step <1>4 verifies the Darboux criterion for
Riemann integrability.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
