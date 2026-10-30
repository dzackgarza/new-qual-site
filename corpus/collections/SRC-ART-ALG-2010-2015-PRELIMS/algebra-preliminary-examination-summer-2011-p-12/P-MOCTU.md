---
schema: qual/card@1
id: P-MOCTU
kind: problem
title: Free $R$-modules of rank at most $n$ in an $n$-dimensional vector space over
  a PID
classification:
  areas:
  - prelim
  topics:
  - Modules
  - Free Modules
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---
::: {.problem}
Let $R$ be a PID with field of fractions $F$.
Let $V$ be an $n$-dimensional vector space over $F$.

(a) Show that every finitely generated $R$-submodule $M \subseteq V$ is free of rank $\le n$.

(b) Let $M$ and $N$ be free $R$-submodules of rank $n$ in $V$.
Show that there exists a nonzero element $\alpha \in R$ such that $\alpha M \subseteq N$.
Use this to show that there exists an $R$-basis $\{e_1, \dots, e_n\}$ of $M$ and nonzero elements $\beta_1, \dots, \beta_n \in F$ such that $\{\beta_1 e_1, \dots, \beta_n e_n\}$ is an $R$-basis of $N$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every finitely generated $R$-submodule $M\subseteq V$ is
torsion-free.

::: pf-proof

If $0\ne r\in R$ and $v\in M$ satisfy $rv=0$, then $r$ is invertible
in the fraction field $F$. Since $V$ is an $F$-vector space,
$$
v=r^{-1}(rv)=0.
$$
Thus $M$ has no nonzero torsion.

:::

:::

::: {.pf-step #s2}

The module $M$ is free of rank at most $n$.

::: pf-proof

By the structure theorem for finitely generated modules over the PID
$R$, a finitely generated torsion-free module is free. Write
$$
M\cong R^k.
$$
Let $m_1,\ldots,m_k$ be an $R$-basis. If
$$
\sum_{i=1}^k c_i m_i=0
$$
with $c_i\in F$, choose $0\ne d\in R$ clearing all denominators, so
$dc_i\in R$ for every $i$. Then
$$
\sum_{i=1}^k (dc_i)m_i=0.
$$
The $R$-linear independence of the $m_i$ gives $dc_i=0$, hence $c_i=0$.
Therefore the same family is $F$-linearly independent in the
$n$-dimensional vector space $V$, so $k\le n$.

:::

:::

::: {.pf-step #s3}

If $M$ and $N$ are free of rank $n$ in $V$, then there is
$0\ne\alpha\in R$ such that
$$
\alpha M\subseteq N.
$$

::: pf-proof

Choose $R$-bases $u_1,\ldots,u_n$ of $M$ and
$w_1,\ldots,w_n$ of $N$. By step [](#s2){.pf-ref} applied to $N$, the vectors
$w_1,\ldots,w_n$ are $F$-linearly independent. Since there are $n$ of
them, they form an $F$-basis of $V$.

Write
$$
u_i=\sum_{j=1}^n c_{ij}w_j,
\qquad c_{ij}\in F.
$$
Choose one nonzero $\alpha\in R$ clearing all finitely many denominators
of the $c_{ij}$. Then $\alpha c_{ij}\in R$ for every $i,j$, so
$$
\alpha u_i
=\sum_{j=1}^n (\alpha c_{ij})w_j\in N.
$$
Since the $u_i$ generate $M$, this gives $\alpha M\subseteq N$.

:::

:::

::: {.pf-step #s4}

There exist an $R$-basis $e_1,\ldots,e_n$ of $M$ and nonzero
$\beta_1,\ldots,\beta_n\in F$ such that
$$
\beta_1e_1,\ldots,\beta_ne_n
$$
is an $R$-basis of $N$.

::: pf-proof

By step [](#s3){.pf-ref}, choose $0\ne\alpha\in R$ with
$\alpha M\subseteq N$. Both $\alpha M$ and $N$ are free of rank $n$.
The invariant-factor theorem for a full-rank submodule of a free module
over a PID gives an $R$-basis
$w_1',\ldots,w_n'$ of $N$ and nonzero elements
$d_1,\ldots,d_n\in R$ such that
$$
d_1w_1',\ldots,d_nw_n'
$$
is an $R$-basis of $\alpha M$.

Set
$$
e_i=\frac{d_i}{\alpha}w_i',
\qquad
\beta_i=\frac{\alpha}{d_i}.
$$
Because multiplication by $1/\alpha$ carries the basis of
$\alpha M$ to a basis of $M$, the $e_i$ form an $R$-basis of $M$.
Moreover,
$$
\beta_i e_i=w_i',
$$
so $\beta_1e_1,\ldots,\beta_ne_n$ is the chosen $R$-basis of $N$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (b).

:::

:::

:::
