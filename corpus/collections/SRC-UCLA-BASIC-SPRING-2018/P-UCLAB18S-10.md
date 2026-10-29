---
schema: qual/card@1
id: P-UCLAB18S-10
kind: problem
title: Vanishing partial derivatives on a connected open set
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Let $U\subset\RR^n$ be nonempty, open, and connected.
Suppose $f:U\to\RR$ has all first partial derivatives at every point of $U$, and all of them vanish.
Prove that $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f$ is constant on a neighborhood of each point of $U$.


::: pf-proof

Fix $x=(x_1,\ldots,x_n)\in U$. Since $U$ is open, there exists $r>0$ such that the open cube
$$
Q=\prod_{j=1}^n(x_j-r,x_j+r)
$$
is contained in $U$.

Let $y=(y_1,\ldots,y_n)\in Q$, and define
$$
z^{(0)}=x,
\qquad
z^{(k)}=(y_1,\ldots,y_k,x_{k+1},\ldots,x_n)
$$
for $1\le k\le n$. Each segment from $z^{(k-1)}$ to $z^{(k)}$ lies in $Q$ and varies only in the $k$-th coordinate.

For fixed $k$, define the one-variable function
$$
g_k(t)=f(y_1,\ldots,y_{k-1},t,x_{k+1},\ldots,x_n)
$$
on the interval between $x_k$ and $y_k$. Its derivative exists at every interior point and equals the $k$-th partial derivative of $f$, hence is identically zero. By the one-variable mean value theorem, $g_k(y_k)=g_k(x_k)$. Thus
$$
f(z^{(k)})=f(z^{(k-1)})
$$
for every $k$. Chaining these equalities gives $f(y)=f(x)$. Since $y\in Q$ was arbitrary, $f$ is constant on $Q$.

:::

:::

::: {.pf-step #s1-2}

For any $c\in\RR$, the level set
$$
E_c=\{x\in U:f(x)=c\}
$$
is open in $U$.


::: pf-proof

If $x\in E_c$, step [](#s1-1){.pf-ref} gives an open neighborhood $Q\subset U$ of $x$ on which $f$ is constant with value $f(x)=c$. Hence $Q\subset E_c$, so $E_c$ is open in the subspace topology of $U$.

:::

:::

::: {.pf-step #s1-3}

Fix $x_0\in U$ and put $c=f(x_0)$. Then $E_c=U$.


::: pf-proof

The set $E_c$ is nonempty because $x_0\in E_c$, and it is open by step [](#s1-2){.pf-ref}. Its complement is
$$
U\setminus E_c=\bigcup_{d\ne c}E_d,
$$
which is open by step [](#s1-2){.pf-ref}. Thus $E_c$ is both open and closed in the connected space $U$. Since it is nonempty, connectedness forces $E_c=U$.

:::

:::

::: pf-qed

By step [](#s1-3){.pf-ref}, every $x\in U$ satisfies $f(x)=f(x_0)$, so $f$ is constant on $U$.

:::

:::

:::
