---
schema: qual/card@1
id: P-BERK95S-17
kind: problem
title: Coprime factors of the characteristic polynomial split the vector space
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $V$ be finite-dimensional over a field $F$, and let $L:V\to V$ have characteristic polynomial
\[
\chi=\chi_1\chi_2,
\]
where $\chi_1,\chi_2\in F[x]$ are relatively prime. Prove that
\[
V=V_1\oplus V_2
\]
for subspaces $V_1,V_2$ satisfying
\[
\chi_i(L)V_i=0,
\qquad i=1,2.
\]
:::

::: {.solution}
Set
$$
V_1\coloneqq\ker\chi_1(L),
\qquad
V_2\coloneqq\ker\chi_2(L).
$$

<1>1. There exist polynomials $a,b\in F[x]$ such that
$$
a\chi_1+b\chi_2=1.
$$

::: {.proof}
The polynomials $\chi_1$ and $\chi_2$ are relatively prime, so Bézout's
identity in the Euclidean domain $F[x]$ gives such $a$ and $b$.
:::

<1>2. Every $v\in V$ can be written as a sum $v=v_1+v_2$ with
$v_i\in V_i$.

::: {.proof}
For $v\in V$, define
$$
v_1\coloneqq b(L)\chi_2(L)v,
\qquad
v_2\coloneqq a(L)\chi_1(L)v.
$$
Evaluating the identity from step <1>1 at $L$ gives
$$
I_V=a(L)\chi_1(L)+b(L)\chi_2(L),
$$
so $v=v_1+v_2$.

By the Cayley--Hamilton theorem,
$$
\chi(L)=\chi_1(L)\chi_2(L)=0.
$$
Since all polynomials in $L$ commute,
$$
\chi_1(L)v_1
=b(L)\chi_1(L)\chi_2(L)v
=0,
$$
and similarly
$$
\chi_2(L)v_2
=a(L)\chi_2(L)\chi_1(L)v
=0.
$$
Hence $v_1\in V_1$ and $v_2\in V_2$.
:::

<1>3. One has $V_1\cap V_2=\{0\}$.

::: {.proof}
Let $w\in V_1\cap V_2$. Then
$$
\chi_1(L)w=0
\qquad\text{and}\qquad
\chi_2(L)w=0.
$$
Applying the operator identity from step <1>2 gives
$$
w
=a(L)\chi_1(L)w+b(L)\chi_2(L)w
=0.
$$
Thus the intersection is trivial.
:::

<1>4. The required decomposition is
$$
\boxed{V=V_1\oplus V_2},
$$
and $\chi_i(L)V_i=0$ for $i=1,2$.

::: {.proof}
Step <1>2 gives $V=V_1+V_2$, while step <1>3 shows that the sum is
direct. By the definition of $V_i$, the operator $\chi_i(L)$ vanishes
on $V_i$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required conclusion.
:::
:::
