---
schema: qual/card@1
id: P-APAF20F
kind: problem
title: Elementary symmetric polynomial in doubled variables, and a Schur coefficient
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $e_n$ denote the $n$-th elementary symmetric polynomial.

(a) Write $e_4(x_1,x_2,\ldots,x_{10},x_1,x_2,\ldots,x_{10})$ as a linear combination of Schur polynomials in $x_1,\ldots,x_{10}$.

(b) If we expand $s_{5,4,1}(x_1,x_2,x_3,1,1,1)$ into a linear combination of Schur polynomials, what is the coefficient of $s_{3,2}(x_1,x_2,x_3)$?
:::

::: {.solution}

Let $X=(x_1,\ldots,x_{10})$.

::: pf

::: {.pf-step #e4-doubled-alphabet-convolution}
One has
\[
e_4(X,X)=\sum_{i=0}^4 e_i(X)e_{4-i}(X).
\]

::: pf-proof
The generating function for elementary symmetric functions is
\[
E_X(t)=\sum_{r\ge0}e_r(X)t^r=\prod_{j=1}^{10}(1+x_jt).
\]
For the doubled alphabet $(X,X)$,
\[
E_{(X,X)}(t)=E_X(t)^2.
\]
Comparing coefficients of $t^4$ gives the formula.
:::

:::

::: {.pf-step #schur-expansions-of-e-products}
The products appearing in step [](#e4-doubled-alphabet-convolution){.pf-ref} satisfy
\[
e_4=s_{(1,1,1,1)},
\]
\[
e_1e_3=s_{(2,1,1)}+s_{(1,1,1,1)},
\]
and
\[
e_2^2=s_{(2,2)}+s_{(2,1,1)}+s_{(1,1,1,1)}.
\]

::: pf-proof
Since $e_r=s_{(1^r)}$, the first identity is immediate. The other two follow from the vertical-strip Pieri rule. Multiplying $s_{(1,1,1)}$ by $e_1$ adds one box in a vertical strip, yielding $(2,1,1)$ and $(1,1,1,1)$. Multiplying $s_{(1,1)}$ by $e_2$ adds two boxes with no two in the same row, yielding $(2,2)$, $(2,1,1)$, and $(1,1,1,1)$.
:::

:::

::: {.pf-step #e4-doubled-schur-expansion}
Therefore
\[
\boxed{
e_4(X,X)
=5s_{(1,1,1,1)}(X)
+3s_{(2,1,1)}(X)
+s_{(2,2)}(X).}
\]

::: pf-proof
By step [](#e4-doubled-alphabet-convolution){.pf-ref},
\[
e_4(X,X)=2e_4+2e_1e_3+e_2^2.
\]
Substitute the expansions from step [](#schur-expansions-of-e-products){.pf-ref} and collect coefficients.
:::

:::

::: {.pf-step #coefficient-as-skew-schur}
Let $Y=(1,1,1)$. In the alphabet-sum expansion
\[
s_{(5,4,1)}(X+Y)
=\sum_{\mu\subseteq(5,4,1)}s_\mu(X)s_{(5,4,1)/\mu}(Y),
\]
the coefficient of $s_{(3,2)}(X)$ is
\[
s_{(5,4,1)/(3,2)}(1,1,1).
\]

::: pf-proof
This is the standard skew-Schur decomposition for a sum of alphabets:
\[
s_\lambda(X+Y)=\sum_{\mu\subseteq\lambda}s_\mu(X)s_{\lambda/\mu}(Y).
\]
Taking $\lambda=(5,4,1)$ and selecting the coefficient of $s_{(3,2)}(X)$ gives the claim.
:::

:::

::: {.pf-step #skew-schur-541-32-expansion}
The skew Schur function is
\[
s_{(5,4,1)/(3,2)}
=s_{(4,1)}+2s_{(3,2)}+s_{(3,1,1)}+s_{(2,2,1)}.
\]

::: pf-proof
The skew Jacobi--Trudi determinant is
\[
s_{(5,4,1)/(3,2)}
=\det
\begin{pmatrix}
h_2&h_4&h_7\\
1&h_2&h_5\\
0&0&h_1
\end{pmatrix}
=h_1(h_2^2-h_4).
\]
Now
\[
h_2^2=s_{(2)}s_{(2)}=s_{(4)}+s_{(3,1)}+s_{(2,2)}
\]
by the horizontal-strip Pieri rule, while $h_4=s_{(4)}$. Hence
\[
h_2^2-h_4=s_{(3,1)}+s_{(2,2)}.
\]
Multiplying by $h_1=s_{(1)}$ and applying Pieri once more gives
\[
s_{(3,1)}h_1=s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)},
\]
\[
s_{(2,2)}h_1=s_{(3,2)}+s_{(2,2,1)}.
\]
Adding these identities gives the stated expansion.
:::

:::

::: {.pf-step #weyl-dimension-values-at-111}
For a partition $(a,b,c)$ with at most three parts,
\[
s_{(a,b,c)}(1,1,1)
=\frac{(a-b+1)(a-c+2)(b-c+1)}2.
\]
Consequently
\[
s_{(4,1)}(1^3)=24,
\quad s_{(3,2)}(1^3)=15,
\quad s_{(3,1,1)}(1^3)=6,
\quad s_{(2,2,1)}(1^3)=3.
\]

::: pf-proof
The displayed formula is the Weyl dimension formula for the irreducible polynomial representation of $\mathrm{GL}_3$ of highest weight $(a,b,c)$. Substituting the four partitions gives the four numerical values.
:::

:::

::: {.pf-step #coefficient-value-63}
Hence the coefficient of $s_{(3,2)}(x_1,x_2,x_3)$ in $s_{(5,4,1)}(x_1,x_2,x_3,1,1,1)$ is
\[
\boxed{63}.
\]

::: pf-proof
By steps [](#coefficient-as-skew-schur){.pf-ref}, [](#skew-schur-541-32-expansion){.pf-ref} and [](#weyl-dimension-values-at-111){.pf-ref} the coefficient equals
\[
24+2\cdot15+6+3=63.
\]
:::

:::

::: pf-qed
Step [](#e4-doubled-schur-expansion){.pf-ref} answers part (a); step [](#coefficient-value-63){.pf-ref} answers part (b).
:::

:::

:::
