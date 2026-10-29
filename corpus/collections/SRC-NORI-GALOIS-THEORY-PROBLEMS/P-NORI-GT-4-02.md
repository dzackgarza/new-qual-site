---
schema: qual/card@1
id: P-NORI-GT-4-02
kind: problem
title: Injectivity of a matrix over an integral domain and its determinant
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.2 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
With $R , n , T$ as above, assume that R is an integral domain.
Prove that $T$ : $R ^ { n } \to R ^ { n }$ is one-to-one if and only if det(T ) is nonzero.

Hint: Let K be the fraction field of R. We may regard $T$ as a member of $\mathrm { M } _ { n } ( K )$
:::

::: {.solution}

Let $K=\operatorname{Frac}(R)$.

::: pf

::: {.pf-step #s1-1}

If
$$
\det(T)\ne0,
$$
then $T:R^n\to R^n$ is injective.


::: pf-proof

Suppose
$$
Tv=0
$$
for some $v\in R^n$. By the adjugate identity from Problem 4.1,
$$
\operatorname{adj}(T)T=\det(T)I_n.
$$
Therefore
$$
0=\operatorname{adj}(T)Tv=\det(T)v.
$$
Since $R$ is an integral domain and $\det(T)\ne0$, multiplication by $\det(T)$ is injective on $R$. Hence every coordinate of $v$ is zero, so $v=0$.

:::

:::

::: {.pf-step #s1-2}

If
$$
\det(T)=0,
$$
then the induced $K$-linear map
$$
T_K:K^n\to K^n
$$
is not injective.


::: pf-proof

The same matrix $T$ may be viewed in $\Mat_n(K)$. Its determinant in $K$ is still $0$. Over a field, a square matrix is invertible if and only if its determinant is nonzero. Thus $T_K$ is singular and has a nonzero kernel vector.

:::

:::

::: {.pf-step #s1-3}

Under the hypothesis of step [](#s1-2){.pf-ref}, there exists a nonzero vector $v\in R^n$ satisfying
$$
Tv=0.
$$


::: pf-proof

Choose
$$
0\ne x=(x_1,\ldots,x_n)\in K^n
$$
with $Tx=0$. Write the coordinates of $x$ with denominators in $R$. There is a nonzero common denominator $d\in R$ such that
$$
v=dx\in R^n.
$$
Since $d\ne0$ and $x\ne0$, the vector $v$ is nonzero in the $K$-vector space $K^n$, hence nonzero in $R^n$. Moreover,
$$
Tv=T(dx)=dTx=0.
$$
Thus $T:R^n\to R^n$ is not injective.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
T:R^n\to R^n\text{ is injective}
\quad\Longleftrightarrow\quad
\det(T)\ne0.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} proves the forward condition from nonvanishing determinant, while steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} prove that vanishing determinant forces failure of injectivity.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is exactly the required equivalence.

:::

:::

:::
