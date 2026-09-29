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
Use this to show that there exists an $R$-basis $\{e_1, \dots, e_n\}$ of $M$ and nonzero elements $\beta_1, \dots, \beta_n \in F$ such that $\{\beta_1 e_1, \dots, \beta_n e_n\}$ is an $R$-basis of $N$ (Invariant Factor Theorem for Lattices).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

An $R$-linearly independent subset of $V$ is $F$-linearly independent.

::: pf-proof

Let $m_1,\ldots,m_k\in V$ be $R$-linearly independent and suppose $\sum_i c_im_i=0$ with $c_i\in F$.
Choose $d\in R\setminus\{0\}$ with $dc_i\in R$ for all $i$. Then $\sum_i(dc_i)m_i=0$, so $dc_i=0$ and hence $c_i=0$ for all $i$.

:::

:::

::: {.pf-step #s2}

In part (a), every finitely generated $R$-submodule $M\subseteq V$ is free of rank at most $n$.

::: pf-proof

If $r\in R\setminus\{0\}$ and $v\in M$ satisfy $rv=0$, then $v=r^{-1}(rv)=0$ in the $F$-vector space $V$; so $M$ is torsion-free.
By the structure theorem for finitely generated modules over a PID, $M\cong R^k$ for some $k\ge0$ [@DF04].
An $R$-basis of $M$ is $F$-linearly independent by step [](#s1){.pf-ref}, so $k\le\dim_FV=n$.

For part (b), let $u_1,\ldots,u_n$ be an $R$-basis of $M$ and $w_1,\ldots,w_n$ an $R$-basis of $N$.

:::

:::

::: {.pf-step #s3}

There is $\alpha\in R\setminus\{0\}$ with $\alpha M\subseteq N$.

::: pf-proof

By step [](#s1){.pf-ref}, $w_1,\ldots,w_n$ are $n$ linearly independent vectors in the $n$-dimensional space $V$, so they form an $F$-basis.
Write $u_i=\sum_j(a_{ij}/b_{ij})w_j$ with $a_{ij},b_{ij}\in R$ and $b_{ij}\ne0$, and put $\alpha=\prod_{i,j}b_{ij}\ne0$.
Then each $\alpha u_i=\sum_j(\alpha a_{ij}/b_{ij})w_j$ has coefficients in $R$, so $\alpha u_i\in N$; since the $u_i$ generate $M$, $\alpha M\subseteq N$.

:::

:::

::: {.pf-step #s4}

There are an $R$-basis $e_1,\ldots,e_n$ of $M$ and $\beta_1,\ldots,\beta_n\in F^\times$ such that $\beta_1e_1,\ldots,\beta_ne_n$ is an $R$-basis of $N$.

::: pf-proof

Multiplication by $\alpha$ is an injective $R$-linear map $M\to\alpha M$, so $\alpha M$ is a free submodule of rank $n$ of the free module $N$ of rank $n$, by step [](#s3){.pf-ref}.
By the stacked-bases theorem for submodules of free modules over a PID [@DF04], there are an $R$-basis $w_1',\ldots,w_n'$ of $N$ and $d_1,\ldots,d_n\in R\setminus\{0\}$ such that $d_1w_1',\ldots,d_nw_n'$ is an $R$-basis of $\alpha M$.
Then $e_i\coloneqq(d_i/\alpha)w_i'$ form an $R$-basis of $M=\alpha^{-1}(\alpha M)$, and with $\beta_i\coloneqq\alpha/d_i\in F^\times$ we get $\beta_ie_i=w_i'$, an $R$-basis of $N$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} answers part (a), and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} answer part (b).

:::

:::

:::
