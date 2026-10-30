---
schema: qual/card@1
id: P-TIE-S14-08
kind: problem
title: Fundamental theorem of algebra via Rouché's theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2014, question 8.
---

::: {.problem}
Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra: If
$$
P_{n}(z) = a_{0} + a_{1}z + \cdots + a_{n-1}z^{n-1} + a_{n}z^{n} \quad (a_{n} \neq 0)
$$
is a polynomial of degree $n$, then it has $n$ zeros in $\CC$.
:::

::: {.solution}

Write
$$
P_n(z)=a_nz^n+Q(z),
\qquad
Q(z)\coloneqq\sum_{k=0}^{n-1}a_kz^k.
$$

::: pf

::: {.pf-step #s1-1}

There exists $R>0$ such that on $\abs{z}=R$,
$$
\abs{Q(z)}<\abs{a_nz^n}.
$$


::: pf-proof

For $\abs{z}=R$,
$$
\begin{aligned}
\frac{\abs{Q(z)}}{\abs{a_nz^n}}
&\le
\sum_{k=0}^{n-1}
\frac{\abs{a_k}}{\abs{a_n}}R^{k-n}.
\end{aligned}
$$
For every $k<n$, the exponent $k-n$ is negative, so each term tends to $0$ as $R\to\infty$. The finite sum therefore tends to $0$. Choose $R$ so large that the sum is less than $1$. Then
$$
\abs{Q(z)}<\abs{a_nz^n}
$$
on the circle.

:::

:::

::: {.pf-step #s1-2}

The polynomials $P_n$ and $a_nz^n$ have the same number of zeros in $\abs{z}<R$, counted with multiplicity.


::: pf-proof

On $\abs{z}=R$,
$$
\abs{P_n(z)-a_nz^n}
=
\abs{Q(z)}
<
\abs{a_nz^n}
$$
by step [](#s1-1){.pf-ref}. Rouché's theorem therefore gives the same number of zeros for $P_n$ and $a_nz^n$ inside the circle, counted with multiplicity.

:::

:::

::: {.pf-step #s1-3}

The polynomial $P_n$ has exactly $n$ zeros in $\CC$, counted with multiplicity.


::: pf-proof

The polynomial $a_nz^n$ has the single zero $0$ with multiplicity $n$. By step [](#s1-2){.pf-ref}, $P_n$ has exactly $n$ zeros in $\abs{z}<R$, counted with multiplicity. Hence it has $n$ complex zeros in total.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the Fundamental Theorem of Algebra.

:::

:::

:::
