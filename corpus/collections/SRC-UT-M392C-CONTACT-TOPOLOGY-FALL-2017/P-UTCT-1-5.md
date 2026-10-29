---
schema: qual/card@1
id: P-UTCT-1-5
kind: problem
title: $C^k$ hyperplane fields are locally kernels of $C^k$ 1-forms
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 1.5 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
---

::: {.problem}
Show that a hyperplane ﬁeld isCk if and only if it is locally the kernel of a nonzeroCk 1-form.
:::

::: {.solution}

Let $M$ be an $n$-manifold and let
$$
\xi\subset TM
$$
be a hyperplane field, so each fiber $\xi_p\subset T_pM$ has dimension
$n-1$.

## Forward implication

Assume $\xi$ is a $C^k$ hyperplane field.

::: pf

::: {.pf-step #s1-1}

For every $p\in M$, there is a neighborhood $U$ of $p$ and
$C^k$ vector fields
$$
X_1,\dots,X_{n-1}
$$
on $U$ that form a basis of $\xi_q$ for every $q\in U$.


::: pf-proof

A $C^k$ hyperplane field is, by definition, a $C^k$ rank-$(n-1)$
subbundle of $TM$. Every vector bundle is locally trivial, so around $p$
there is a local $C^k$ frame for $\xi$.

:::

:::

::: {.pf-step #s1-2}

After shrinking $U$ if necessary, one can choose a $C^k$ vector
field $Y$ on $U$ such that
$$
\boxed{
X_1(q),\dots,X_{n-1}(q),Y(q)}
$$
is a basis of $T_qM$ for every $q\in U$.


::: pf-proof

Choose any vector
$$
v\in T_pM-\xi_p.
$$
Extend $v$ to a local $C^k$ vector field $Y$. At $p$, the $n$
vectors
$$
X_1(p),\dots,X_{n-1}(p),Y(p)
$$
are linearly independent. Linear independence is an open condition, so after
shrinking $U$, they remain a frame of $TM|_U$.

:::

:::

::: {.pf-step #s1-3}

Let
$$
\theta^1,\dots,\theta^{n}
$$
be the dual coframe to
$$
X_1,\dots,X_{n-1},Y.
$$
Then each $\theta^i$ is a $C^k$ $1$-form.


::: pf-proof

The matrix whose columns are the frame vectors is $C^k$ and invertible at
every point of $U$. Its inverse matrix is also $C^k$, and its rows are
the coefficients of the dual coframe.

:::

:::

::: {.pf-step #s1-4}

Define
$$
\boxed{\alpha=\theta^n}.
$$
Then
$$
\boxed{
\alpha(X_i)=0
\quad(1\le i\le n-1)}
$$
and
$$
\boxed{\alpha(Y)=1}.
$$


::: pf-proof

This is the defining property of the dual coframe.

:::

:::

::: {.pf-step #s1-5}

The form $\alpha$ is nowhere zero on $U$.


::: pf-proof

At every point $q\in U$,
$$
\alpha_q(Y(q))=1.
$$
Hence $\alpha_q\ne0$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{\xi|_U=\ker\alpha}.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, each $X_i$ lies in $\ker\alpha$, so
$$
\xi_q
=
\operatorname{span}\{X_1(q),\dots,X_{n-1}(q)\}
\subseteq
\ker\alpha_q.
$$
Because $\alpha_q\ne0$, its kernel is a hyperplane in $T_qM$, hence has
dimension $n-1$. The two subspaces have the same dimension, so they are
equal.

:::

:::

::: {.pf-step #s1-7}

Thus every $C^k$ hyperplane field is locally the kernel of a
nowhere-zero $C^k$ $1$-form.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} construct such a form around an arbitrary point.

:::

:::

::: pf-step

Fix $p\in U$. Since $\alpha_p\ne0$, there is a tangent vector
$$
v\in T_pM
$$
with
$$
\alpha_p(v)\ne0.
$$


::: pf-proof

A nonzero linear functional cannot vanish on every vector.

:::

:::

::: {.pf-step #s1-9}

Extend $v$ to a local $C^k$ vector field $Y$, and shrink $U$
so that
$$
\boxed{\alpha(Y)\ne0}
$$
everywhere on $U$.


::: pf-proof

The function
$$
q\longmapsto \alpha_q(Y(q))
$$
is $C^k$, hence continuous, and is nonzero at $p$. It remains nonzero on
a sufficiently small neighborhood of $p$.

:::

:::

::: {.pf-step #s1-10}

After rescaling $Y$, assume
$$
\boxed{\alpha(Y)=1}.
$$


::: pf-proof

Replace $Y$ by
$$
\frac{Y}{\alpha(Y)}.
$$
The denominator is a nowhere-zero $C^k$ function by step [](#s1-9){.pf-ref}, so the
rescaled field is $C^k$.

:::

:::

::: pf-step

Choose any local $C^k$ frame
$$
Y,E_1,\dots,E_{n-1}
$$
of $TM|_U$.


::: pf-proof

Extend the nonzero vector field $Y$ to a local frame of the tangent bundle.

:::

:::

::: {.pf-step #s1-12}

Define
$$
\boxed{
X_i
=
E_i-\alpha(E_i)Y}
\qquad(1\le i\le n-1).
$$


::: pf-proof

The coefficients $\alpha(E_i)$ are $C^k$ functions, so each $X_i$ is
a $C^k$ vector field.

:::

:::

::: {.pf-step #s1-13}

Each $X_i$ lies in $\ker\alpha$.


::: pf-proof

Using step [](#s1-10){.pf-ref},
$$
\begin{aligned}
\alpha(X_i)
&=
\alpha(E_i)
-
\alpha(E_i)\alpha(Y)\\
&=
\alpha(E_i)-\alpha(E_i)\\
&=
0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-14}

The vectors
$$
X_1(q),\dots,X_{n-1}(q)
$$
are linearly independent for every $q\in U$.


::: pf-proof

Suppose
$$
\sum_{i=1}^{n-1}c_iX_i=0.
$$
Substituting step [](#s1-12){.pf-ref} gives
$$
\sum_i c_iE_i
-
\left(
\sum_i c_i\alpha(E_i)
\right)Y
=
0.
$$
Since
$$
Y,E_1,\dots,E_{n-1}
$$
is a basis, all coefficients $c_i$ must vanish.

:::

:::

::: {.pf-step #s1-15}

Hence
$$
\boxed{
\ker\alpha
=
\operatorname{span}
\{X_1,\dots,X_{n-1}\}}.
$$


::: pf-proof

By step [](#s1-13){.pf-ref}, the span lies in $\ker\alpha$. Step [](#s1-14){.pf-ref} shows that the
span has dimension $n-1$. Since $\alpha$ is nonzero, $\ker\alpha$ also
has dimension $n-1$. Therefore the two subspaces are equal.

:::

:::

::: {.pf-step #s1-16}

Thus $\ker\alpha$ is a $C^k$ hyperplane field.


::: pf-proof

Step [](#s1-15){.pf-ref} gives a local $C^k$ frame for $\ker\alpha$ around every point.
Therefore it is a $C^k$ rank-$(n-1)$ subbundle of $TM$.

:::

:::

::: {.pf-step #s1-17}

Consequently,
$$
\boxed{
\xi\text{ is }C^k
\iff
\xi\text{ is locally the kernel of a nowhere-zero }C^k\ 1\text{-form}.}
$$


::: pf-proof

The forward implication is step [](#s1-7){.pf-ref}, and the reverse implication is step
[](#s1-16){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-17){.pf-ref} is the required equivalence.

:::

:::

:::
