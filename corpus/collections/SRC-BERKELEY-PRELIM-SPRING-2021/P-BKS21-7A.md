---
schema: qual/card@1
id: P-BKS21-7A
kind: problem
title: Eigenvalues of an annihilated linear operator
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2021 polynomial-evaluation and factor-by-factor kernel argument. Both parts are correct, including when roots are repeated and without assuming finite dimensionality.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified evaluation on an eigenvector and the first-vanishing-partial-product construction when $P$ splits.
---

::: {.problem}
Let $L$ be a linear operator on a nonzero vector space $V$ over a field $K$, and let $P\in K[x]$ be nonzero with $P(L)=0$.

(a) Show every eigenvalue of $L$ is a root of $P$.

(b) If $P$ splits completely over $K$, show that some root of $P$ is an eigenvalue of $L$.
:::

Write
$$
P(x)=\sum_{i=0}^{d}a_i x^i
$$
with $a_d\neq0$. Necessarily $d\geq1$: if $d=0$, then $P(L)=a_0I\neq0$ because $a_0\neq0$ and $V\neq0$.

::: pf

::: {.pf-step #s1-1}

If $\lambda\in K$ is an eigenvalue of $L$, then
$$
P(L)v=P(\lambda)v
$$
for every eigenvector $v$ with $Lv=\lambda v$.


::: pf-proof

From $Lv=\lambda v$, induction gives
$$
L^iv=\lambda^iv
$$
for every $i\geq0$. Therefore
$$
\begin{aligned}
P(L)v
&=\sum_{i=0}^d a_iL^iv\\
&=\sum_{i=0}^d a_i\lambda^iv\\
&=P(\lambda)v.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

Every eigenvalue of $L$ is a root of $P$.


::: pf-proof

Let $\lambda$ be an eigenvalue and choose a nonzero eigenvector $v$. The hypothesis $P(L)=0$ and step [](#s1-1){.pf-ref} give
$$
0=P(L)v=P(\lambda)v.
$$
Since $v\neq0$ and $K$ is a field, this forces $P(\lambda)=0$.

:::

:::

::: {.pf-step #s1-3}

Assume now that $P$ splits completely over $K$. Then, for some $\lambda_1,\ldots,\lambda_d\in K$,
$$
P(x)=a_d\prod_{j=1}^{d}(x-\lambda_j),
$$
where repetitions are allowed.


::: pf-proof

This is precisely the meaning of complete splitting, with the nonzero leading coefficient $a_d$ factored out.

:::

:::

::: {.pf-step #s1-4}

Choose any nonzero $v\in V$ and define
$$
v_k\coloneqq
\prod_{j=1}^{k}(L-\lambda_jI)v
\qquad(0\leq k\leq d),
$$
where $v_0=v$. Then there is an index $k$ with
$$
0\leq k<d,\qquad v_k\neq0,\qquad v_{k+1}=0.
$$


::: pf-proof

By choice, $v_0=v\neq0$. On the other hand, steps [](#s1-3){.pf-ref} and the hypothesis $P(L)=0$ give
$$
0=P(L)v
=
a_d\prod_{j=1}^{d}(L-\lambda_jI)v
=
a_dv_d.
$$
Since $a_d\neq0$, it follows that $v_d=0$. Therefore among the indices $1,\ldots,d$ there is a least index $k+1$ for which $v_{k+1}=0$. By minimality, $v_k\neq0$.

:::

:::

::: {.pf-step #s1-5}

The scalar $\lambda_{k+1}$ from step [](#s1-4){.pf-ref} is an eigenvalue of $L$ and a root of $P$.


::: pf-proof

All factors $L-\lambda_jI$ are polynomials in $L$, hence commute. In particular,
$$
v_{k+1}
=(L-\lambda_{k+1}I)v_k.
$$
Step [](#s1-4){.pf-ref} gives $v_k\neq0$ and $v_{k+1}=0$, so
$$
Lv_k=\lambda_{k+1}v_k.
$$
Thus $\lambda_{k+1}$ is an eigenvalue. It is also a root of $P$ by the factorization in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::
