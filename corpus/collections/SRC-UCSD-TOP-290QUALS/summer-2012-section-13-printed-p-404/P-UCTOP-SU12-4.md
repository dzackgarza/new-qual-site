---
schema: qual/card@1
id: P-UCTOP-SU12-4
kind: problem
title: 'Homology of $\RP^2\times X$ where $H_k(X;\ZZ)\cong\ZZ/k\ZZ$'
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be a path-connected topological space whose integer homology groups in positive dimensions are:
$$H_0(X; \ZZ) \cong \ZZ, \qquad H_k(X; \ZZ) \cong \ZZ/k\ZZ \quad \text{for all } k \ge 1.$$
Compute the integer homology groups $H_n(\RP^2 \times X; \ZZ)$ for all $n \ge 0$.
:::

::: {.solution}

::: pf

::: pf-step
The integral homology of $\RP^2$ is
$$
H_i(\RP^2;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/2,&i=1,\\
0,&i\ge2.
\end{cases}
$$

:::

::: pf-step
The homological Künneth theorem gives, noncanonically,
$$
H_n(\RP^2\times X;\ZZ)
\cong H_n(X)
\oplus ((\ZZ/2)\otimes H_{n-1}(X))
\oplus \operatorname{Tor}_1^{\ZZ}(\ZZ/2,H_{n-2}(X)),
$$
where groups with negative indices are interpreted as zero.

:::

::: pf-step
In degrees $0,1,2$ this yields
$$
H_0\cong\ZZ,
\qquad
H_1\cong\ZZ/2,
\qquad
H_2\cong\ZZ/2,
$$
because $H_1(X)=\ZZ/1=0$ and $H_2(X)=\ZZ/2$.

:::

::: pf-step
Let $n\ge3$.

::: pf-proof

::: pf-step
The first summand is $H_n(X)\cong\ZZ/n$.
:::

::: pf-step
For positive $m$,
$$
(\ZZ/2)\otimes(\ZZ/m)
\cong
\operatorname{Tor}_1^{\ZZ}(\ZZ/2,\ZZ/m)
\cong \ZZ/\gcd(2,m).
$$
:::

::: pf-step
Therefore the tensor summand is $\ZZ/2$ exactly when $n-1$ is even, while the Tor summand is $\ZZ/2$ exactly when $n-2$ is even.
:::

::: pf-step
Exactly one of the consecutive integers $n-1,n-2$ is even, so exactly one of these two summands is nonzero. Hence
$$
H_n(\RP^2\times X;\ZZ)
\cong \ZZ/n\oplus\ZZ/2
\qquad(n\ge3).
$$
:::

:::

:::

::: pf-step
Thus
$$
H_n(\RP^2\times X;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ/2,&n=1,2,\\
\ZZ/n\oplus\ZZ/2,&n\ge3.
\end{cases}
$$

:::

:::

:::
