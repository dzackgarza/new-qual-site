---
schema: qual/card@1
id: PR-EDD7U
kind: proposition
title: Characteristic polynomials via traces of exterior powers
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
  - Trace
relations: []
review: draft
---

:::{.proposition}
A trick for finding characteristic polynomials:^[Useful computational trick.]
\[
\chi_A(t) &= \sum_{k=0}^n (-1)^k \trace\qty{\Extpower^k A} t^{n-k} \\
&= t^n - \trace\qty{A} t^{n-1} + \trace\qty{\Extpower^2 A}t^{n-2} - \cdots \pm \trace\qty{\Extpower^{n-1} A} t \mp \det(A)
,\]
using that

\[
{\Extpower^0 A} \da 1 \\
{\Extpower^1 A} \da A \\
\trace\qty{\Extpower^n A} = \det(A)
.\]

Moreover, the intermediate traces are easy to compute by hand:
\[
\trace\qty{\Extpower^\ell A} = \sum \det\qty{M^{\ell}}
,\]
where the sum is taken over all $\ell\times\ell$ **principal minors**: determinants of the $n \choose \ell$ principal matrices which are obtained by choosing $\ell$ diagonal entries to keep and and deleting the rows and columns for every entry not chosen.
Equivalently, one can select $n-\ell$ diagonal entries and delete the corresponding row/column for each.


:::{.example}

![](../../assets/figures/2021-07-24_19-48-11.png)

:::


To factor this polynomial, the **rational roots test** can be useful: for $f(t) = a_nt^n + \cdots + a_1 t + a_0$, rational roots in lowest terms are of the form $p/q$ where $p \divides a_0$ and $q\divides a_n$.
The numerator divides the **constant** term and the denominator the **leading** coefficient.
Note that this simplifies greatly for $f$ monic, where $q \divides 1$ forces every rational root to be an integer dividing $a_0$.
Once you have a root, apply **polynomial long division** to get a smaller problem, and hopefully this continues to work until it's factored.
:::
