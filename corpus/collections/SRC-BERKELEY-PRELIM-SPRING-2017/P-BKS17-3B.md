---
schema: qual/card@1
id: P-BKS17-3B
kind: problem
title: Maximal degree of exactness and positive weights of quadrature rules
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 14 problem 3B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 quadrature argument. In the printed second test polynomial, the product indexed by $k\neq j$ has the factor $(x-x_j)^2$; to isolate the $j$-th weight it must instead use $(x-x_k)^2$. The solution below uses the corrected polynomial and verifies both positivity claims directly.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the degree-$2p+2$ obstruction, positivity of its integral, the degree-$2p$ cardinal test polynomial, and positivity of every resulting weight.
---

::: {.problem}
The error of a quadrature rule with $p + 1$ distinct points $x_j$, weights $w_j$ is

$$
E_p(f) = \int_a^b f(x) \, dx - \sum_{j=0}^{p} w_j f(x_j).
$$

Suppose that $E_p(f) = 0$ whenever $f$ is a polynomial of degree $\leq q$. Show that $q \leq 2p + 1$ and if $q \geq 2p$ then $w_j > 0$ for all $j$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has $q\leq 2p+1$.


::: pf-proof

Define
$$
F(x)\coloneqq\prod_{k=0}^p(x-x_k)^2.
$$
Then $F$ has degree $2p+2$, satisfies $F(x_j)=0$ for every $j$, and is nonnegative on $[a,b]$. Since $F$ is a nonzero polynomial, it is not identically zero on the nondegenerate interval $[a,b]$; hence
$$
\int_a^b F(x)\,dx>0.
$$
Therefore
$$
E_p(F)
=
\int_a^bF(x)\,dx
-
\sum_{j=0}^p w_jF(x_j)
=
\int_a^bF(x)\,dx
>0.
$$
If $q\geq2p+2$, exactness would instead give $E_p(F)=0$, a contradiction. Thus $q\leq2p+1$.

:::

:::

::: {.pf-step #s1-2}

Assume $q\geq2p$, fix $j\in\{0,\ldots,p\}$, and define
$$
F_j(x)\coloneqq\prod_{\substack{0\leq k\leq p\\k\neq j}}(x-x_k)^2.
$$
Then $F_j$ has degree $2p$, satisfies $F_j(x_k)=0$ for $k\neq j$, and satisfies
$$
F_j(x_j)=\prod_{k\neq j}(x_j-x_k)^2>0.
$$


::: pf-proof

There are exactly $p$ factors in the defining product, each of degree $2$, so $\deg F_j=2p$. If $k\neq j$, the factor indexed by that same $k$ vanishes at $x=x_k$. At $x=x_j$, every factor is strictly positive because the nodes are distinct.

:::

:::

::: {.pf-step #s1-3}

Under the hypothesis $q\geq2p$, every weight is positive; more precisely,
$$
\boxed{
w_j
=
\frac{\displaystyle\int_a^b F_j(x)\,dx}
{\displaystyle\prod_{k\neq j}(x_j-x_k)^2}
>0
}.
$$


::: pf-proof

Since $\deg F_j=2p\leq q$, exactness and step [](#s1-2){.pf-ref} give
$$
\begin{aligned}
\int_a^b F_j(x)\,dx
&=\sum_{k=0}^p w_kF_j(x_k)\\
&=w_jF_j(x_j).
\end{aligned}
$$
The denominator $F_j(x_j)$ is positive by step [](#s1-2){.pf-ref}. Also $F_j$ is continuous, nonnegative, and not identically zero on $[a,b]$, so its integral is positive. Dividing yields the displayed formula and $w_j>0$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the degree bound, and steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} prove positivity of every weight when $q\geq2p$.

:::

:::

:::
