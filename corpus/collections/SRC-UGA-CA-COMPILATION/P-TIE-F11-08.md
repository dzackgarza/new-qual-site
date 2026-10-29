---
schema: qual/card@1
id: P-TIE-F11-08
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 8.
---

::: {.problem}
Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in $\CC .$
:::

::: {.solution}

Write
$$
P_n(z)=a_nz^n+Q(z),
\qquad
Q(z)=\sum_{j=0}^{n-1}a_jz^j.
$$

::: pf

::: {.pf-step #s1-1}

There exists $R>0$ such that on the circle $\abs{z}=R$,
$$
\abs{Q(z)}<\abs{a_nz^n}.
$$


::: pf-proof

For $R>0$ and $\abs{z}=R$,
$$
\frac{\abs{Q(z)}}{\abs{a_nz^n}}
\le
\sum_{j=0}^{n-1}\frac{\abs{a_j}}{\abs{a_n}}R^{j-n}.
$$
Each exponent $j-n$ is negative, so the finite sum on the right tends to $0$ as $R\to\infty$. Hence $R$ can be chosen so large that this sum is strictly less than $1$, which gives the desired inequality.

:::

:::

::: {.pf-step #s1-2}

The polynomials $P_n(z)$ and $a_nz^n$ have the same number of zeros in $\abs{z}<R$, counted with multiplicity.


::: pf-proof

On $\abs{z}=R$, step [](#s1-1){.pf-ref} gives
$$
\abs{P_n(z)-a_nz^n}
=
\abs{Q(z)}
<
\abs{a_nz^n}.
$$
Rouché's theorem therefore implies that $P_n$ and $a_nz^n$ have the same number of zeros inside the circle, counted with multiplicity.

:::

:::

::: {.pf-step #s1-3}

The polynomial $P_n$ has exactly $n$ zeros in $\CC$, counted with multiplicity.


::: pf-proof

The polynomial $a_nz^n$ has exactly one zero, namely $0$, of multiplicity $n$. By step [](#s1-2){.pf-ref}, $P_n$ therefore has exactly $n$ zeros in the disk $\abs{z}<R$, counted with multiplicity. In particular, these are $n$ complex zeros of $P_n$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the Fundamental Theorem of Algebra for the given polynomial.

:::

:::

:::
