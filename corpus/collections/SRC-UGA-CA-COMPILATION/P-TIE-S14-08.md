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
Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in C.
:::

::: {.solution}
Write
$$
P_n(z)=a_nz^n+Q(z),
\qquad
Q(z)\coloneqq\sum_{k=0}^{n-1}a_kz^k.
$$

<1>1. There exists $R>0$ such that on $\abs{z}=R$,
$$
\abs{Q(z)}<\abs{a_nz^n}.
$$

::: {.proof}
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

<1>2. The polynomials $P_n$ and $a_nz^n$ have the same number of zeros in $\abs{z}<R$, counted with multiplicity.

::: {.proof}
On $\abs{z}=R$,
$$
\abs{P_n(z)-a_nz^n}
=
\abs{Q(z)}
<
\abs{a_nz^n}
$$
by step <1>1. Rouché's theorem therefore gives the same number of zeros for $P_n$ and $a_nz^n$ inside the circle, counted with multiplicity.
:::

<1>3. The polynomial $P_n$ has exactly $n$ zeros in $\CC$, counted with multiplicity.

::: {.proof}
The polynomial $a_nz^n$ has the single zero $0$ with multiplicity $n$. By step <1>2, $P_n$ has exactly $n$ zeros in $\abs{z}<R$, counted with multiplicity. Hence it has $n$ complex zeros in total.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the Fundamental Theorem of Algebra.
:::
:::
