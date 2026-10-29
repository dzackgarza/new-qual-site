---
schema: qual/card@1
id: P-UGAP08S-04
kind: problem
title: A basis adapted to the kernel maps to a basis of the range
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction drops T, V, k, and several repeated T/V symbols; the basis/kernel/range statement uniquely determines those missing symbols.
---

::: {.problem}
Let $T$ be a linear transformation on a finite-dimensional vector space $V$. Suppose
$$
x_1,x_2,\ldots,x_n
$$
is a basis for $V$, with the first $k$ of these vectors forming a basis for $\ker T$.
Prove that
$$
Tx_{k+1},Tx_{k+2},\ldots,Tx_n
$$
is a basis for $\operatorname{range}T$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The vectors
$$
Tx_{k+1},\dots,Tx_n
$$
span
$$
\operatorname{range}T.
$$


::: pf-proof

Let
$$
y\in\operatorname{range}T.
$$
Then there exists
$$
v\in V
$$
such that
$$
y=T(v).
$$

Since
$$
x_1,dots,x_n
$$
is a basis of $V$, write
$$
v
=
a_1x_1+cdots+a_nx_n.
$$
By linearity,
$$
\begin{aligned}
y
&=
T(v)\\
&=
a_1Tx_1+cdots+a_nTx_n.
\end{aligned}
$$

For
$$
1\le i\le k,
$$
one has
$$
x_i\in\ker T,
$$
so
$$
Tx_i=0.
$$
Therefore
$$
y
=
a_{k+1}Tx_{k+1}
+\cdots+
a_nTx_n.
$$
Thus the displayed vectors span the range.

:::

:::

::: {.pf-step #s1-2}

Suppose
$$
a_{k+1}Tx_{k+1}
+\cdots+
a_nTx_n
=
0.
$$
Then
$$
a_{k+1}x_{k+1}
+\cdots+
a_nx_n
\in
\ker T.
$$


::: pf-proof

By linearity,
$$
T
\left(
a_{k+1}x_{k+1}
+\cdots+
a_nx_n
\right)
=
0.
$$
This is exactly the condition for the vector in parentheses to lie in the
kernel.

:::

:::

::: {.pf-step #s1-3}

Since
$$
x_1,dots,x_k
$$
is a basis of
$$
\ker T,
$$
there exist scalars
$$
b_1,dots,b_k
$$
such that
$$
a_{k+1}x_{k+1}
+\cdots+
a_nx_n
=
b_1x_1+cdots+b_kx_k.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} places the left-hand side in
$$
\ker T.
$$
Every vector in the kernel is a linear combination of its basis
$$
x_1,dots,x_k.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
b_1x_1+cdots+b_kx_k
-
a_{k+1}x_{k+1}
-\cdots-
a_nx_n
=
0.
$$


::: pf-proof

Move all terms in step [](#s1-3){.pf-ref} to one side.

:::

:::

::: {.pf-step #s1-5}

Because
$$
x_1,dots,x_n
$$
is a basis of $V$, every coefficient in step [](#s1-4){.pf-ref} is zero.
In particular,
$$
a_{k+1}
=
\cdots
=
a_n
=
0.
$$


::: pf-proof

A basis is linearly independent.
Thus the only linear relation among the basis vectors is the trivial one.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
Tx_{k+1},\dots,Tx_n
$$
are linearly independent.


::: pf-proof

Step [](#s1-5){.pf-ref} shows that every linear relation among them has only zero
coefficients.

:::

:::

::: {.pf-step #s1-7}

Combining spanning and independence,
$$
\boxed{
Tx_{k+1},Tx_{k+2},\ldots,Tx_n
}
$$
is a basis of
$$
\operatorname{range}T.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives spanning and step [](#s1-6){.pf-ref} gives linear independence.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the desired conclusion.

:::

:::

:::
