---
schema: qual/card@1
id: P-UCLAB06W-08
kind: problem
title: Existence and uniqueness of the adjoint of a linear map
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $T:V\to W$ be a linear transformation of finite-dimensional real inner product spaces.
Show that there exists a unique linear transformation $T^t:W\to V$ such that
$$
\langle T(v),w\rangle_W=\langle v,T^t(w)\rangle_V
$$
for all $v\in V$ and $w\in W$, where $\langle\ ,\ \rangle_X$ denotes the inner product on $X=V$ or $W$.
:::

::: {.solution}

Choose an orthonormal basis
$$
e_1,\ldots,e_n
$$
of $V$.

::: pf

::: {.pf-step #s1-1}

For $w\in W$, define
$$
T^t(w)=\sum_{j=1}^n\langle T(e_j),w\rangle_W e_j.
$$
Then $T^t(w)\in V$ is well defined.


::: pf-proof

The displayed sum is a finite linear combination of basis vectors of $V$, so it defines a vector of $V$ for each $w\in W$.

:::

:::

::: {.pf-step #s1-2}

The map
$$
T^t:W\to V
$$
is linear.


::: pf-proof

Let $w_1,w_2\in W$ and $a,b\in\RR$. By linearity of the real inner product in either variable,
$$
\begin{aligned}
T^t(aw_1+bw_2)
&=\sum_{j=1}^n
\langle T(e_j),aw_1+bw_2\rangle_W e_j\\
&=a\sum_{j=1}^n\langle T(e_j),w_1\rangle_W e_j
+b\sum_{j=1}^n\langle T(e_j),w_2\rangle_W e_j\\
&=aT^t(w_1)+bT^t(w_2).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

For every $v\in V$ and $w\in W$,
$$
\langle T(v),w\rangle_W
=
\langle v,T^t(w)\rangle_V.
$$


::: pf-proof

Write
$$
v=\sum_{j=1}^n v_j e_j.
$$
Then linearity of $T$ and of the inner product gives
$$
\langle T(v),w\rangle_W
=
\sum_{j=1}^n v_j\langle T(e_j),w\rangle_W.
$$
On the other hand, by step [](#s1-1){.pf-ref} and orthonormality,
$$
\begin{aligned}
\langle v,T^t(w)\rangle_V
&=
\left\langle
\sum_{i=1}^n v_i e_i,
\sum_{j=1}^n\langle T(e_j),w\rangle_W e_j
\right\rangle_V\\
&=
\sum_{j=1}^n v_j\langle T(e_j),w\rangle_W.
\end{aligned}
$$
Thus the two sides are equal.

:::

:::

::: {.pf-step #s1-4}

The map satisfying the adjoint identity is unique.


::: pf-proof

Suppose $A,B:W\to V$ both satisfy
$$
\langle T(v),w\rangle_W
=
\langle v,A(w)\rangle_V
=
\langle v,B(w)\rangle_V
$$
for all $v\in V$ and $w\in W$. Fix $w$. Then
$$
\langle v,A(w)-B(w)\rangle_V=0
$$
for every $v\in V$. Taking
$$
v=A(w)-B(w)
$$
gives
$$
\norm{A(w)-B(w)}^2=0,
$$
so $A(w)=B(w)$. Since $w$ was arbitrary, $A=B$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} construct a linear map $T^t$ satisfying the required identity, and step [](#s1-4){.pf-ref} proves uniqueness.

:::

:::

:::
