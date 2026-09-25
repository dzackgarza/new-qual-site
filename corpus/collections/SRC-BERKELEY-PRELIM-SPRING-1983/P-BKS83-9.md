---
schema: qual/card@1
id: P-BKS83-9
kind: problem
title: A continuous lower-Lipschitz self-map of $\mathbb R^n$ is a homeomorphism
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
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked injectivity, closedness of the image, the invariance-of-domain step, and the global Lipschitz estimate for the inverse.
---

::: {.problem}
Let $F:\mathbb R^n\to\mathbb R^n$ be continuous and suppose there is $\lambda>0$ such that
\[
\|F(x)-F(y)\|\ge\lambda\|x-y\|
\]
for all $x,y\in\mathbb R^n$. Prove that $F$ is one-to-one, onto, and has a continuous inverse.
:::

::: {.solution}
<1>1. The map $F$ is injective.

::: {.proof}
If $F(x)=F(y)$, then the assumed inequality gives
$$
0
=
\norm{F(x)-F(y)}
\ge
\lambda\norm{x-y}.
$$
Since $\lambda>0$, this forces $\norm{x-y}=0$, hence $x=y$.
:::

<1>2. The image $F(\mathbb R^n)$ is closed in $\mathbb R^n$.

::: {.proof}
Let
$$
F(x_j)\longrightarrow z
$$
for a sequence of points in the image. For all $j,k$,
$$
\norm{x_j-x_k}
\le
\frac1\lambda\norm{F(x_j)-F(x_k)}.
$$
Thus $(x_j)$ is a Cauchy sequence because $(F(x_j))$ converges. Completeness
of $\mathbb R^n$ gives some $x\in\mathbb R^n$ with $x_j\to x$. By continuity,
$$
F(x_j)\longrightarrow F(x).
$$
Uniqueness of limits yields $F(x)=z$, so $z$ belongs to the image.
:::

<1>3. The image $F(\mathbb R^n)$ is open in $\mathbb R^n$.

::: {.proof}
By step <1>1, $F:\mathbb R^n\to\mathbb R^n$ is continuous and injective.
The invariance of domain theorem therefore implies that $F$ is an open map.
In particular, the image of the open set $\mathbb R^n$ is open.
:::

<1>4. The map $F$ is surjective.

::: {.proof}
The image is nonempty, closed by step <1>2, and open by step <1>3.
Since $\mathbb R^n$ is connected, its only nonempty subset that is both
open and closed is the whole space. Therefore
$$
F(\mathbb R^n)=\mathbb R^n.
$$
:::

<1>5. The inverse $F^{-1}:\mathbb R^n\to\mathbb R^n$ is
$1/\lambda$-Lipschitz, hence continuous.

::: {.proof}
By steps <1>1 and <1>4, the inverse is defined on all of $\mathbb R^n$.
For $u,v\in\mathbb R^n$, write
$$
x=F^{-1}(u),
\qquad
y=F^{-1}(v).
$$
The hypothesis gives
$$
\norm{u-v}
=
\norm{F(x)-F(y)}
\ge
\lambda\norm{x-y},
$$
and hence
$$
\norm{F^{-1}(u)-F^{-1}(v)}
\le
\frac1\lambda\norm{u-v}.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1, <1>4, and <1>5 prove respectively that $F$ is one-to-one,
onto, and has a continuous inverse.
:::
:::
