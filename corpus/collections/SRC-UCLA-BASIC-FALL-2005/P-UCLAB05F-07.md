---
schema: qual/card@1
id: P-UCLAB05F-07
kind: problem
title: Equality of row rank and column rank
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the official UCLA Basic Examination, September 2005 PDF. Existing corpus candidates either restrict to square matrices or add an additional interpretive task, so this rectangular source problem is retained as its own canonical card.
---

::: {.problem}
Let $A$ be a real $n\times m$ matrix.
Prove that the maximum number of linearly independent rows of $A$ equals the maximum number of linearly independent columns of $A$.
:::

Let
\[
T:\mathbb R^m\to\mathbb R^n
\]
be the linear map whose standard matrix is $A$.

::: pf

::: pf-step

The column rank of $A$ is
\[
\operatorname{rank}(T).
\]


::: pf-proof

The columns of $A$ are
\[
T(e_1),\ldots,T(e_m),
\]
where $e_1,\ldots,e_m$ is the standard basis of $\mathbb R^m$. Hence their span is exactly $\operatorname{im}T$, so the maximum number of linearly independent columns is
\[
\dim\operatorname{im}T=\operatorname{rank}(T).
\]

:::

:::

::: pf-step

The row rank of $A$ is
\[
\operatorname{rank}(T^t).
\]


::: pf-proof

The standard matrix of the transpose map
\[
T^t:(\mathbb R^n)^*\to(\mathbb R^m)^*
\]
is $A^t$. The columns of $A^t$ are the rows of $A$. By step <1>1 applied to $T^t$, the maximum number of linearly independent rows of $A$ is therefore
\[
\operatorname{rank}(T^t).
\]

:::

:::

::: pf-step

One has
\[
\ker(T^t)=(\operatorname{im}T)^0,
\]
the annihilator of $\operatorname{im}T$ in $(\mathbb R^n)^*$.


::: pf-proof

Let $\varphi\in(\mathbb R^n)^*$. Then
\[
T^t\varphi=0
\]
if and only if
\[
(T^t\varphi)(v)=\varphi(Tv)=0
\]
for every $v\in\mathbb R^m$. This holds exactly when $\varphi$ vanishes on every vector in $\operatorname{im}T$.

:::

:::

::: pf-step

If $Y$ is a subspace of a finite-dimensional vector space $W$, then
\[
\dim Y^0=\dim W-\dim Y.
\]


::: pf-proof

Choose a basis
\[
y_1,\ldots,y_r
\]
of $Y$ and extend it to a basis
\[
y_1,\ldots,y_r,w_{r+1},\ldots,w_s
\]
of $W$. In the dual basis of $W^*$, the annihilator $Y^0$ is spanned by
\[
w_{r+1}^*,\ldots,w_s^*.
\]
Thus
\[
\dim Y^0=s-r=\dim W-\dim Y.
\]

:::

:::

::: pf-step

The ranks of $T$ and $T^t$ are equal.


::: pf-proof

By rank-nullity for
\[
T^t:(\mathbb R^n)^*\to(\mathbb R^m)^*,
\]
steps <1>3--<1>4 give
\[
\begin{aligned}
\operatorname{rank}(T^t)
&=
n-\dim\ker(T^t)\\
&=
n-\dim(\operatorname{im}T)^0\\
&=
n-(n-\dim\operatorname{im}T)\\
&=
\operatorname{rank}(T).
\end{aligned}
\]

:::

:::

::: pf-step

The row rank of $A$ equals its column rank.


::: pf-proof

By step <1>1, the column rank is $\operatorname{rank}(T)$. By step <1>2, the row rank is $\operatorname{rank}(T^t)$. These are equal by step <1>5.

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
