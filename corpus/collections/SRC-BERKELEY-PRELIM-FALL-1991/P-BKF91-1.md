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

::: pf

::: {.pf-step #s1}

If $G$ is nonabelian, then $G$ has a nontrivial automorphism.

::: pf-proof

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

:::

::: {.pf-step #s2}

Suppose $G$ is abelian. Then inversion
$$
\iota:G\longrightarrow G,
\qquad
\iota(x)=x^{-1},
$$
is an automorphism.

::: pf-proof

For $x,y\in G$, commutativity gives
$$
\iota(xy)
=(xy)^{-1}
=x^{-1}y^{-1}
=\iota(x)\iota(y).
$$
Also $\iota^2=\operatorname{id}_G$, so $\iota$ is bijective.

:::

:::

::: {.pf-step #s3}

If the inversion automorphism in step [](#s2){.pf-ref} is nontrivial, then
$G$ has a nontrivial automorphism.

::: pf-proof

This is immediate from step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

If the inversion automorphism is the identity, then every element
of $G$ has order at most $2$.

::: pf-proof

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

:::

::: {.pf-step #s5}

Under the hypotheses of step [](#s4){.pf-ref}, the group $G$ is a vector
space over $\FF_2$ of dimension at least $2$.

::: pf-proof

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

:::

::: {.pf-step #s6}

Under the hypotheses of step [](#s5){.pf-ref}, $G$ has a nontrivial
automorphism.

::: pf-proof

Choose a basis
$$
e_1,e_2,e_3,\ldots,e_r
$$
with $r\geq2$. The linear map that interchanges $e_1$ and $e_2$ and
fixes every other basis vector is an invertible $\FF_2$-linear map.
Hence it is a group automorphism of $G$, and it is nontrivial because
it sends $e_1$ to $e_2\neq e_1$.

:::

:::

::: {.pf-step #s7}

Every finite group of order at least $3$ has a nontrivial
automorphism.

::: pf-proof

If $G$ is nonabelian, apply step [](#s1){.pf-ref}. If $G$ is abelian, either
inversion is nontrivial, in which case step [](#s3){.pf-ref} applies, or inversion
is the identity, in which case step [](#s6){.pf-ref} applies.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::
