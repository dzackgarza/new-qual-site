---
schema: qual/card@1
id: P-UCLAB04F-06
kind: problem
title: Bolzano--Weierstrass in the plane from the one-dimensional theorem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the official UCLA Basic Exam Fall 2004 PDF.
---

::: {.problem}
The Bolzano--Weierstrass theorem in $\RR^n$ states that if $S\subset\RR^n$ is bounded and closed and $(x_k)$ is a sequence taking values in $S$, then $(x_k)$ has a subsequence converging to a point of $S$.

Assume this theorem for $n=1$ and use it to prove the theorem for $n=2$.
:::

::: {.solution}

Let
$$
x_k=(a_k,b_k)\in S\subseteq\RR^2.
$$

::: pf

::: {.pf-step #s1-1}

The real sequence $(a_k)$ is bounded.


::: pf-proof

Since $S$ is bounded in $\RR^2$, there is $R>0$ such that
$$
\|(a,b)\|\le R
$$
for every $(a,b)\in S$. Hence
$$
|a_k|\le R
$$
for every $k$.

:::

:::

::: pf-step

There is a subsequence
$$
(a_{k_j})
$$
converging to some $a\in\RR$.


::: pf-proof

By step [](#s1-1){.pf-ref}, $(a_k)$ is bounded. Apply the one-dimensional Bolzano--Weierstrass theorem to obtain a convergent subsequence.

:::

:::

::: {.pf-step #s1-3}

The real sequence
$$
(b_{k_j})
$$
has a convergent subsequence.


::: pf-proof

The same bound on $S$ gives
$$
|b_{k_j}|\le R
$$
for every $j$. The one-dimensional Bolzano--Weierstrass theorem therefore gives indices $j_\ell$ and a real number $b$ such that
$$
b_{k_{j_\ell}}\to b.
$$

:::

:::

::: {.pf-step #s1-4}

The subsequence
$$
x_{k_{j_\ell}}
$$
converges in $\RR^2$ to
$$
(a,b).
$$


::: pf-proof

Because $(a_{k_j})\to a$, every subsequence also converges to $a$, so
$$
a_{k_{j_\ell}}\to a.
$$
By step [](#s1-3){.pf-ref},
$$
b_{k_{j_\ell}}\to b.
$$
Therefore
$$
\|x_{k_{j_\ell}}-(a,b)\|^2
=
|a_{k_{j_\ell}}-a|^2
+
|b_{k_{j_\ell}}-b|^2
\longrightarrow0.
$$
Thus $x_{k_{j_\ell}}\to(a,b)$.

:::

:::

::: {.pf-step #s1-5}

The limit $(a,b)$ belongs to $S$.


::: pf-proof

Every term $x_{k_{j_\ell}}$ lies in $S$, and $S$ is closed. A closed subset of $\RR^2$ contains the limits of all convergent sequences of its points. Hence
$$
(a,b)\in S.
$$

:::

:::

::: {.pf-step #s1-6}

The Bolzano--Weierstrass theorem holds in $\RR^2$.


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} produce a subsequence of the arbitrary sequence $(x_k)$ converging to a point of $S$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is exactly the desired $n=2$ case.

:::

:::

:::
