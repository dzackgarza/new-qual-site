---
schema: qual/card@1
id: P-CWELY
kind: problem
title: The plane $3x+4y+5z=0$ as kernel or image of an endomorphism of $\mathbb{R}^3$
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced two overlapping solutions with one structured proof.
---

::: problem
Let
\[
V=\{(x,y,z)\in\mathbb R^3:3x+4y+5z=0\}.
\]

1. Show that $V$ is a linear subspace of $\mathbb R^3$.
2. Prove or disprove that some linear map $S:\mathbb R^3\to\mathbb R^3$ has kernel $V$.
3. Prove or disprove that some linear map $T:\mathbb R^3\to\mathbb R^3$ has image $V$.
4. Prove or disprove that some linear map $U:\mathbb R^3\to\mathbb R^3$ has both kernel and image equal to $V$.
:::

::: {.solution}
Let $\varphi\colon\mathbb R^3\to\mathbb R$ be $\varphi(x,y,z)=3x+4y+5z$, so that $V=\ker\varphi$.

<1>1. $V$ is a linear subspace of $\mathbb R^3$ of dimension $2$, with basis $v_1=(4,-3,0)$, $v_2=(5,0,-3)$.
::: {.proof}
$V$ is the kernel of the linear map $\varphi$, hence a subspace.
Since $\varphi(1,0,0)=3\neq0$, the image of $\varphi$ is $\mathbb R$, and rank--nullity gives $\dim V=\dim\mathbb R^3-\dim\operatorname{im}\varphi=3-1=2$.
Both $v_1$ and $v_2$ satisfy $3x+4y+5z=0$, and they are linearly independent: if $av_1+bv_2=0$, the third coordinate gives $-3b=0$ and then the second gives $-3a=0$. Two independent vectors in a $2$-dimensional space form a basis.
:::

<1>2. Some linear map $S\colon\mathbb R^3\to\mathbb R^3$ has kernel $V$.
::: {.proof}
Let
\[
S=\begin{pmatrix}3&4&5\\0&0&0\\0&0&0\end{pmatrix},
\qquad
S(x,y,z)^T=(3x+4y+5z,0,0)^T.
\]
Then $S\mathbf x=0$ exactly when $3x+4y+5z=0$, so $\ker S=V$.
:::

<1>3. Some linear map $T\colon\mathbb R^3\to\mathbb R^3$ has image $V$.
::: {.proof}
Let $T$ be the matrix with columns $v_1$, $v_2$, $0$:
\[
T=\begin{pmatrix}4&5&0\\-3&0&0\\0&-3&0\end{pmatrix}.
\]
The image of $T$ is its column space, $\operatorname{span}\{v_1,v_2\}=V$ by <1>1.
:::

<1>4. No linear map $U\colon\mathbb R^3\to\mathbb R^3$ has $\ker U=\operatorname{im}U=V$.
::: {.proof}
Rank--nullity gives $\dim\ker U+\dim\operatorname{im}U=\dim\mathbb R^3=3$.
If both equalled $V$, the left side would be $2\dim V=4$ by <1>1, a contradiction.
:::
:::
