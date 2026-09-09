---
schema: qual/card@1
id: P-UCTOP-SU12-4
kind: problem
title: Homology of RP^2 × X where H_k(X;Z) = Z/kZ
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

::: problem
Let $X$ be a path-connected topological space whose integer homology groups in positive dimensions are:
$$H_0(X; \mathbb{Z}) \cong \mathbb{Z}, \qquad H_k(X; \mathbb{Z}) \cong \mathbb{Z}/k\mathbb{Z} \quad \text{for all } k \ge 1.$$
Compute the integer homology groups $H_n(\mathbb{RP}^2 \times X; \mathbb{Z})$ for all $n \ge 0$.
:::

::: solution
<1>1. The integral homology of $\mathbb{RP}^2$ is
$$
H_i(\mathbb{RP}^2;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/2,&i=1,\\
0,&i\ge2.
\end{cases}
$$

<1>2. The homological Künneth theorem gives, noncanonically,
$$
H_n(\mathbb{RP}^2\times X;\mathbb Z)
\cong H_n(X)
\oplus ((\mathbb Z/2)\otimes H_{n-1}(X))
\oplus \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,H_{n-2}(X)),
$$
where groups with negative indices are interpreted as zero.

<1>3. In degrees $0,1,2$ this yields
$$
H_0\cong\mathbb Z,
\qquad
H_1\cong\mathbb Z/2,
\qquad
H_2\cong\mathbb Z/2,
$$
because $H_1(X)=\mathbb Z/1=0$ and $H_2(X)=\mathbb Z/2$.

<1>4. Let $n\ge3$.
<2>1. The first summand is $H_n(X)\cong\mathbb Z/n$.
<2>2. For positive $m$,
$$
(\mathbb Z/2)\otimes(\mathbb Z/m)
\cong
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/m)
\cong \mathbb Z/\gcd(2,m).
$$
<2>3. Therefore the tensor summand is $\mathbb Z/2$ exactly when $n-1$ is even, while the Tor summand is $\mathbb Z/2$ exactly when $n-2$ is even.
<2>4. Exactly one of the consecutive integers $n-1,n-2$ is even, so exactly one of these two summands is nonzero. Hence
$$
H_n(\mathbb{RP}^2\times X;\mathbb Z)
\cong \mathbb Z/n\oplus\mathbb Z/2
\qquad(n\ge3).
$$

<1>5. Thus
$$
H_n(\mathbb{RP}^2\times X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z/2,&n=1,2,\\
\mathbb Z/n\oplus\mathbb Z/2,&n\ge3.
\end{cases}
$$
:::
