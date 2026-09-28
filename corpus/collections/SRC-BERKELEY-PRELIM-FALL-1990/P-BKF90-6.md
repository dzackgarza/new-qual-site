---
schema: qual/card@1
id: P-BKF90-6
kind: problem
title: An entire function with sublinear growth is constant
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Applied Liouville's theorem to the entire removable extension of
    (f(z)-f(0))/z, which tends to zero at infinity.
---

::: {.problem}
Let $f$ be entire and suppose
\[
\frac{f(z)}{z}\longrightarrow0
\qquad\text{as }|z|\to\infty.
\]
Prove that $f$ is constant.
:::

::: {.solution}
<1>1. The function
$$
g(z)\coloneqq
\begin{cases}
\dfrac{f(z)-f(0)}{z},&z\ne0,\\
f'(0),&z=0,
\end{cases}
$$
is entire.

::: {.proof}
For $z\ne0$, the displayed quotient is holomorphic. Since $f$ is differentiable at $0$,
$$
\lim_{z\to0}\frac{f(z)-f(0)}{z}=f'(0).
$$
Thus the apparent singularity at $0$ is removable, and the stated value gives its holomorphic extension.
:::

<1>2. One has
$$
g(z)\longrightarrow0
\qquad\text{as }\abs{z}\to\infty.
$$

::: {.proof}
For $z\ne0$,
$$
g(z)=\frac{f(z)}{z}-\frac{f(0)}{z}.
$$
The first term tends to $0$ by hypothesis, and the second tends to $0$ because $f(0)$ is constant.
:::

<1>3. The entire function $g$ is bounded on $\CC$.

::: {.proof}
By step <1>2, there is $R>0$ such that $\abs{g(z)}\le1$ whenever $\abs{z}\ge R$. On the compact disk $\abs{z}\le R$, continuity of $g$ gives a finite maximum. Combining these two bounds shows that $g$ is bounded on all of $\CC$.
:::

<1>4. One has $g\equiv0$.

::: {.proof}
By step <1>3 and Liouville's theorem, $g$ is constant. Step <1>2 shows that this constant has limit $0$ at infinity, so the constant is $0$.
:::

<1>5. The function $f$ is constant.

::: {.proof}
By step <1>4, for every $z\ne0$,
$$
0=g(z)=\frac{f(z)-f(0)}{z},
$$
so $f(z)=f(0)$. The same equality is trivial at $z=0$. Hence
$$
\boxed{f\equiv f(0)}.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
