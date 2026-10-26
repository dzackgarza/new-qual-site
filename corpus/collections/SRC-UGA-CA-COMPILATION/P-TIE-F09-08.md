---
schema: qual/card@1
id: P-TIE-F09-08
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 8.
---

::: {.problem}
Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in C.
:::

Write
$$
P_n(z)=a_nz^n+Q(z),
\qquad
Q(z)=a_0+a_1z+\cdots+a_{n-1}z^{n-1}.
$$

::: pf

::: {.pf-step #s1-1}

There exists $R>0$ such that on $|z|=R$,
$$
|Q(z)|<|a_nz^n|.
$$


::: pf-proof

For $|z|=R\ge1$,
$$
|Q(z)|
\le
\sum_{j=0}^{n-1}|a_j|R^j
\le
\left(\sum_{j=0}^{n-1}|a_j|\right)R^{n-1}.
$$
Choose $R$ so large that
$$
R>
\frac{\sum_{j=0}^{n-1}|a_j|}{|a_n|}.
$$
Then
$$
|Q(z)|
<
|a_n|R^n
=
|a_nz^n|
$$
on the circle $|z|=R$.

:::

:::

::: {.pf-step #s1-2}

The polynomials $P_n(z)$ and $a_nz^n$ have the same number of zeros in
$|z|<R$, counted with multiplicity.


::: pf-proof

On $|z|=R$, step [](#s1-1){.pf-ref} gives
$$
|P_n(z)-a_nz^n|
=
|Q(z)|
<
|a_nz^n|.
$$
Rouché's theorem therefore gives the asserted equality of zero counts.

:::

:::

::: {.pf-step #s1-3}

The polynomial $P_n$ has exactly
$$
\boxed{n}
$$
zeros in $\CC$, counted with multiplicity.


::: pf-proof

The polynomial $a_nz^n$ has exactly one zero, namely $0$, with multiplicity $n$.
Hence step [](#s1-2){.pf-ref} shows that $P_n$ has exactly $n$ zeros in $|z|<R$, counted with
multiplicity.

A nonzero polynomial of degree $n$ cannot have more than $n$ zeros counted with
multiplicity. Therefore these are all of the zeros of $P_n$ in $\CC$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the Fundamental Theorem of Algebra in the required form.

:::

:::
