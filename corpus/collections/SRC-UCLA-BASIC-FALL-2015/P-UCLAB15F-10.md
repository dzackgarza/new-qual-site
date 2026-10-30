---
schema: qual/card@1
id: P-UCLAB15F-10
kind: problem
title: Exponential of commuting linear operators
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
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $F,G:\RR^n\to\RR^n$ be linear operators, with
$$
\exp(F)=\sum_{k=0}^{\infty}\frac1{k!}F^k.
$$

1. Prove that if $FG=GF$, then
$$
\exp(F+G)=\exp(F)\exp(G).
$$

2. Give an example of non-commuting linear operators for which this equality fails.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $FG=GF$, then for every integer $n\ge0$,
$$
(F+G)^n
=
\sum_{k=0}^n
\binom nk
F^kG^{n-k}.
$$


::: pf-proof

This is the binomial theorem for commuting operators.
The ordinary inductive proof applies because $F$ and $G$ commute, hence every power of $F$ commutes with every power of $G$.

:::

:::

::: {.pf-step #s1-2}

The exponential series
$$
\sum_{n=0}^{\infty}\frac{F^n}{n!}
$$
converges absolutely in any operator norm, and likewise for $G$ and $F+G$.


::: pf-proof

In finite dimension, fix a submultiplicative operator norm.
Then
$$
\norm{
\frac{F^n}{n!}
}
\le
\frac{\norm{F}^n}{n!}.
$$
The scalar series
$$
\sum_{n=0}^{\infty}\frac{\norm{F}^n}{n!}
=
e^{\norm{F}}
$$
converges.
Thus the operator series converges absolutely.
The same argument applies to $G$ and $F+G$.

:::

:::

::: {.pf-step #s1-3}

If $FG=GF$, then
$$
\exp(F)\exp(G)
=
\sum_{n=0}^{\infty}
\sum_{k=0}^n
\frac{F^kG^{n-k}}{k!(n-k)!}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, both exponential series converge absolutely.
Therefore their product may be computed by the Cauchy product:
$$
\begin{aligned}
\exp(F)\exp(G)
&=
\left(
\sum_{k=0}^{\infty}\frac{F^k}{k!}
\right)
\left(
\sum_{\ell=0}^{\infty}\frac{G^\ell}{\ell!}
\right)\\
&=
\sum_{n=0}^{\infty}
\sum_{k=0}^n
\frac{F^kG^{n-k}}{k!(n-k)!}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

If $FG=GF$, then
$$
\boxed{\exp(F+G)=\exp(F)\exp(G)}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\exp(F+G)
&=
\sum_{n=0}^{\infty}
\frac1{n!}
\sum_{k=0}^n
\binom nk F^kG^{n-k}\\
&=
\sum_{n=0}^{\infty}
\sum_{k=0}^n
\frac{F^kG^{n-k}}{k!(n-k)!}.
\end{aligned}
$$
This is exactly the expression from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For part 2, take
$$
F=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
G=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
$$
Then
$$
FG\ne GF.
$$


::: pf-proof

Direct multiplication gives
$$
FG=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
GF=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
$$
Thus they do not commute.

:::

:::

::: {.pf-step #s1-6}

Since
$$
F^2=G^2=0,
$$
one has
$$
\exp(F)\exp(G)
=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}.
$$


::: pf-proof

Nilpotence gives
$$
\exp(F)=I+F
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
$$
$$
\exp(G)=I+G
=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}.
$$
Multiplying yields the displayed matrix.

:::

:::

::: {.pf-step #s1-7}

One has
$$
(F+G)^2=I,
$$
and therefore
$$
\exp(F+G)
=
\begin{pmatrix}
\cosh1&\sinh1\\
\sinh1&\cosh1
\end{pmatrix}.
$$


::: pf-proof

Here
$$
F+G
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
$$
whose square is $I$.
Thus even powers equal $I$ and odd powers equal $F+G$.
Separating the exponential series into even and odd terms gives
$$
\exp(F+G)
=
\left(
\sum_{j=0}^{\infty}\frac1{(2j)!}
\right)I
+
\left(
\sum_{j=0}^{\infty}\frac1{(2j+1)!}
\right)(F+G),
$$
which is the displayed matrix.

:::

:::

::: {.pf-step #s1-8}

The matrices in steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} are unequal.


::: pf-proof

The upper-right entry of
$$
\exp(F)\exp(G)
$$
is $1$.
The upper-right entry of
$$
\exp(F+G)
$$
is
$$
\sinh1
=
1+\frac1{3!}+\frac1{5!}+\cdots
>
1.
$$
Hence
$$
\exp(F+G)\ne\exp(F)\exp(G).
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part 1, and steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} give the requested noncommuting counterexample for part 2.

:::

:::

:::
