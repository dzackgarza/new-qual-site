---
schema: qual/card@1
id: P-BKF91-1
kind: problem
title: Every finite group of order at least $3$ has a nontrivial automorphism
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    For a nonabelian group, conjugation by a noncentral element is a
    nonidentity automorphism. For an abelian group, inversion works
    unless every element has order at most two; in that remaining
    case the group is an F_2-vector space of dimension at least two
    and a basis transposition gives a nontrivial automorphism.
---

::: {.problem}
Prove that every finite group of order at least $3$ has a nontrivial automorphism.
:::

::: {.solution}
Let $G$ be a finite group with $\abs{G}\geq3$.

<1>1. If $G$ is nonabelian, then $G$ has a nontrivial automorphism.

::: {.proof}
Since $G$ is nonabelian, its center is a proper subgroup:
$$
Z(G)\neq G.
$$
Choose $g\in G\setminus Z(G)$. Conjugation by $g$,
$$
c_g:G\longrightarrow G,
\qquad
c_g(x)=gxg^{-1},
$$
is an automorphism. Because $g$ is not central, there is some $x\in G$
with
$$
gxg^{-1}\neq x.
$$
Thus $c_g$ is not the identity automorphism.
:::

<1>2. Suppose $G$ is abelian. Then inversion
$$
\iota:G\longrightarrow G,
\qquad
\iota(x)=x^{-1},
$$
is an automorphism.

::: {.proof}
For $x,y\in G$, commutativity gives
$$
\iota(xy)
=(xy)^{-1}
=x^{-1}y^{-1}
=\iota(x)\iota(y).
$$
Also $\iota^2=\operatorname{id}_G$, so $\iota$ is bijective.
:::

<1>3. If the inversion automorphism in step <1>2 is nontrivial, then
$G$ has a nontrivial automorphism.

::: {.proof}
This is immediate from step <1>2.
:::

<1>4. If the inversion automorphism is the identity, then every element
of $G$ has order at most $2$.

::: {.proof}
If $\iota=\operatorname{id}_G$, then
$$
x=x^{-1}
$$
for every $x\in G$. Hence
$$
x^2=e
$$
for every $x\in G$.
:::

<1>5. Under the hypotheses of step <1>4, the group $G$ is a vector
space over $\FF_2$ of dimension at least $2$.

::: {.proof}
Because $G$ is abelian and every element has order dividing $2$, its
group law makes it an elementary abelian $2$-group, equivalently an
$\FF_2$-vector space. Since $G$ is finite,
$$
\abs{G}=2^{\dim_{\FF_2}G}.
$$
The hypothesis $\abs{G}\geq3$ rules out dimensions $0$ and $1$.
Therefore
$$
\dim_{\FF_2}G\geq2.
$$
:::

<1>6. Under the hypotheses of step <1>5, $G$ has a nontrivial
automorphism.

::: {.proof}
Choose a basis
$$
e_1,e_2,e_3,\ldots,e_r
$$
with $r\geq2$. The linear map that interchanges $e_1$ and $e_2$ and
fixes every other basis vector is an invertible $\FF_2$-linear map.
Hence it is a group automorphism of $G$, and it is nontrivial because
it sends $e_1$ to $e_2\neq e_1$.
:::

<1>7. Every finite group of order at least $3$ has a nontrivial
automorphism.

::: {.proof}
If $G$ is nonabelian, apply step <1>1. If $G$ is abelian, either
inversion is nontrivial, in which case step <1>3 applies, or inversion
is the identity, in which case step <1>6 applies.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
