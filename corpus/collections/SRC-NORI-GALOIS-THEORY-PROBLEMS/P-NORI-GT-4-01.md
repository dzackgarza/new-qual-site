---
schema: qual/card@1
id: P-NORI-GT-4-01
kind: problem
title: Adjugate matrix and solving $Tw=\det(T)v$ over a commutative ring
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.1 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $R$ be a commutative ring and let $T \in \Mat_{n}(R)$. Show that for every $v \in R^{n}$ there exists $w \in R^{n}$ such that $Tw = \det(T)v$.

Hint: This is a consequence of the definition of the adjoint matrix $\operatorname{adj}(T)$ and the fact that $T \cdot \operatorname{adj}(T)$ equals the scalar matrix $\det(T)$.

Remark: In reality, the above adjoint matrix is simply $\Lambda^{n-1}(T)$. Therefore this problem could be stated and solved entirely within the framework of exterior algebras, with no reference to matrices.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $\operatorname{adj}(T)$ be the adjugate matrix of $T$, whose $(i,j)$ entry is the $(j,i)$ cofactor of $T$.
Then
$$
T\operatorname{adj}(T)=\det(T)I_n.
$$


::: pf-proof

The $(i,j)$ entry of $T\operatorname{adj}(T)$ is
$$
\sum_{k=1}^n t_{ik}C_{jk},
$$
where $C_{jk}$ is the $(j,k)$ cofactor of $T$.

If $i=j$, this is the Laplace expansion of $\det(T)$ along row $i$.
If $i\ne j$, it is the determinant of the matrix obtained from $T$ by replacing row $j$ with row $i$; that matrix has two equal rows, so its determinant is $0$.
Thus the product has diagonal entries $\det(T)$ and off-diagonal entries $0$.

The argument uses only addition, multiplication, and signs, so it is valid over any commutative ring.

:::

:::

::: {.pf-step #s1-2}

For $v\in R^n$, define
$$
w=\operatorname{adj}(T)v.
$$
Then
$$
Tw=\det(T)v.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
Tw
=T\operatorname{adj}(T)v
=\det(T)I_nv
=\det(T)v.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore for every $v\in R^n$ there exists $w\in R^n$ satisfying
$$
\boxed{Tw=\det(T)v}.
$$


::: pf-proof

The vector constructed in step [](#s1-2){.pf-ref} has the required property.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is exactly the assertion of the problem.

:::

:::

:::
