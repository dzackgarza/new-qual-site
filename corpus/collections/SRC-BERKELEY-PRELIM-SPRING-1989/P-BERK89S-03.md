---
schema: qual/card@1
id: P-BERK89S-03
kind: problem
title: The maximum over a compact parameter of a continuous function is continuous
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the extreme-value theorem to realize each maximum and uniform
    continuity of f on the compact square to compare the values at a
    maximizing y-coordinate for x and for x'.
---

::: {.problem}
Let $f:[0,1]\times[0,1]\to\mathbb R$ be continuous and define
\[
g(x)=\max\{f(x,y):y\in[0,1]\}.
\]
Prove that $g$ is continuous on $[0,1]$.
:::

::: {.solution}
::: pf

::: {.pf-step #maximizer-exists}
For every $x\in[0,1]$, there exists $y_x\in[0,1]$ such that
$$
g(x)=f(x,y_x).
$$

::: pf-proof
For fixed $x$, the function
$$
y\longmapsto f(x,y)
$$
is continuous on the compact interval $[0,1]$. By the extreme-value
theorem, it attains its maximum at some $y_x\in[0,1]$.
:::

:::

::: {.pf-step #uniform-continuity}
For every $\varepsilon>0$, there exists $\delta>0$ such that
$$
\abs{x-x'}<\delta
\quad\Longrightarrow\quad
\abs{f(x,y)-f(x',y)}<\varepsilon
$$
for all $x,x',y\in[0,1]$.

::: pf-proof
The square $[0,1]^2$ is compact, and $f$ is continuous on it. Hence $f$
is uniformly continuous. Therefore, for the given $\varepsilon>0$, there
exists $\delta>0$ such that points of the square at Euclidean distance
less than $\delta$ have $f$-values differing by less than
$\varepsilon$.

For fixed $y$,
$$
\operatorname{dist}((x,y),(x',y))=\abs{x-x'},
$$
which gives the stated implication.
:::

:::

::: {.pf-step #upper-comparison}
If $\abs{x-x'}<\delta$, with $\delta$ as in step [](#uniform-continuity){.pf-ref}, then
$$
g(x)\leq g(x')+\varepsilon.
$$

::: pf-proof
Choose $y_x$ as in step [](#maximizer-exists){.pf-ref}. Then step [](#uniform-continuity){.pf-ref} gives
$$
\begin{aligned}
g(x)
&=f(x,y_x)\\
&<f(x',y_x)+\varepsilon\\
&\leq g(x')+\varepsilon.
\end{aligned}
$$
The displayed strict inequality implies the stated weak inequality.
:::

:::

::: {.pf-step #lower-comparison}
Under the same hypothesis,
$$
g(x')\leq g(x)+\varepsilon.
$$

::: pf-proof
Interchanging $x$ and $x'$ in step [](#upper-comparison){.pf-ref} gives the claim, since
$\abs{x'-x}=\abs{x-x'}<\delta$.
:::

:::

::: {.pf-step #g-continuous}
The function $g$ is continuous on $[0,1]$.

::: pf-proof
By steps [](#upper-comparison){.pf-ref} and [](#lower-comparison){.pf-ref}, whenever $\abs{x-x'}<\delta$,
$$
\abs{g(x)-g(x')}\leq\varepsilon.
$$
Applying steps [](#uniform-continuity){.pf-ref}, [](#upper-comparison){.pf-ref}, and [](#lower-comparison){.pf-ref} with $\varepsilon/2$ in place of
$\varepsilon$ yields
$$
\abs{g(x)-g(x')}<\varepsilon.
$$
Thus $g$ is uniformly continuous, hence continuous, on $[0,1]$.
:::

:::

::: pf-qed
Step [](#g-continuous){.pf-ref} proves the required continuity.
:::

:::
:::
