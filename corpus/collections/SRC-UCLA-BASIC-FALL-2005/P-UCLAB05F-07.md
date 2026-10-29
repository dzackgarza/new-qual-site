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

::: {.solution}

Let
$$
T:\RR^m\to\RR^n
$$
be the linear map whose standard matrix is $A$.

::: pf

::: {.pf-step #s1-1}

The column rank of $A$ is
$$
\operatorname{rank}(T).
$$


::: pf-proof

The columns of $A$ are
$$
T(e_1),\ldots,T(e_m),
$$
where $e_1,\ldots,e_m$ is the standard basis of $\RR^m$. Hence their span is exactly $\operatorname{im}T$, so the maximum number of linearly independent columns is
$$
\dim\operatorname{im}T=\operatorname{rank}(T).
$$

:::

:::

::: {.pf-step #s1-2}

The row rank of $A$ is
$$
\operatorname{rank}(T^t).
$$


::: pf-proof

The standard matrix of the transpose map
$$
T^t:(\RR^n)^*\to(\RR^m)^*
$$
is $A^t$. The columns of $A^t$ are the rows of $A$. By step [](#s1-1){.pf-ref} applied to $T^t$, the maximum number of linearly independent rows of $A$ is therefore
$$
\operatorname{rank}(T^t).
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\ker(T^t)=(\operatorname{im}T)^0,
$$
the annihilator of $\operatorname{im}T$ in $(\RR^n)^*$.


::: pf-proof

Let $\varphi\in(\RR^n)^*$. Then
$$
T^t\varphi=0
$$
if and only if
$$
(T^t\varphi)(v)=\varphi(Tv)=0
$$
for every $v\in\RR^m$. This holds exactly when $\varphi$ vanishes on every vector in $\operatorname{im}T$.

:::

:::

::: {.pf-step #s1-4}

If $Y$ is a subspace of a finite-dimensional vector space $W$, then
$$
\dim Y^0=\dim W-\dim Y.
$$


::: pf-proof

Choose a basis
$$
y_1,\ldots,y_r
$$
of $Y$ and extend it to a basis
$$
y_1,\ldots,y_r,w_{r+1},\ldots,w_s
$$
of $W$. In the dual basis of $W^*$, the annihilator $Y^0$ is spanned by
$$
w_{r+1}^*,\ldots,w_s^*.
$$
Thus
$$
\dim Y^0=s-r=\dim W-\dim Y.
$$

:::

:::

::: {.pf-step #s1-5}

The ranks of $T$ and $T^t$ are equal.


::: pf-proof

By rank-nullity for
$$
T^t:(\RR^n)^*\to(\RR^m)^*,
$$
steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} give
$$
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
$$

:::

:::

::: {.pf-step #s1-6}

The row rank of $A$ equals its column rank.


::: pf-proof

By step [](#s1-1){.pf-ref}, the column rank is $\operatorname{rank}(T)$. By step [](#s1-2){.pf-ref}, the row rank is $\operatorname{rank}(T^t)$. These are equal by step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
