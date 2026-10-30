---
schema: qual/card@1
id: T-JRTS2
kind: theorem
title: Hilbert's Nullstellensatz
slogan: 'Over an algebraically closed field, affine geometry sees exactly radicals: $I(V(J))=\sqrt J$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nullstellensatz
  - Varieties
relations: []
review: draft
prompts:
- State the Nullstellensatz.
- What is $I(V(J))$?
- Where does the Nullstellensatz use that $k$ is algebraically closed?
- How is the Nullstellensatz proved?
- If $L/k$ is a field extension and $L$ is a finitely generated $k$-algebra, show that $L/k$ is algebraic.
- State the weak Nullstellensatz in terms of maximal ideals and in terms of systems of polynomial equations, and deduce the strong form by the Rabinowitsch trick.
---

::: {.theorem title="Hilbert's Nullstellensatz"}
Let $k$ be algebraically closed and let $J \subseteq k[x_1, \ldots, x_n]$ be an ideal.
Then
$$
I(V(J)) = \sqrt{J} .
$$
[@Har77, Theorem I.1.3A]
:::

::: {.theorem title="Zariski's lemma and the weak Nullstellensatz"}
If $L/k$ is a field extension and $L$ is finitely generated as a $k$-algebra, then $L/k$ is finite algebraic.

Consequently, if $k$ is algebraically closed, every maximal ideal of $k[x_1,\ldots,x_n]$ has the form
$$
(x_1-a_1,\ldots,x_n-a_n)
$$
for a unique point $a=(a_1,\ldots,a_n)\in k^n$. Equivalently, every proper ideal $J\subsetneq k[x_1,\ldots,x_n]$ has $V(J)\ne\varnothing$.
:::

::: {.proof title="Zariski's lemma"}
Write $L=k[a_1,\ldots,a_n]$. If the extension were not algebraic, after reordering choose a transcendence basis $a_1,\ldots,a_r$ with $r>0$. The remaining generators are algebraic over
$$
K=k(a_1,\ldots,a_r).
$$
Clearing the finitely many denominators in their monic equations produces a nonzero
$$
f\in k[a_1,\ldots,a_r]
$$
such that $L$ is integral, indeed finite, over
$$
R=k[a_1,\ldots,a_r,f^{-1}].
$$
Because $L$ is a field and is integral over $R$, the ring $R$ must be a field. But $R$ is not a field when $r>0$: choose an irreducible polynomial in $k[a_1]$ that does not divide $f$; it remains a nonunit in $R$. This contradiction gives $r=0$, so $L/k$ is algebraic, and finite generation then makes it finite.

For a maximal ideal $\mfm\subseteq k[x_1,\ldots,x_n]$, the residue field is a finitely generated $k$-algebra and hence a finite algebraic extension of $k$. Algebraic closedness gives
$$
k[x_1,\ldots,x_n]/\mfm\cong k,
$$
so the images of the coordinates are scalars $a_i\in k$ and $\mfm=(x_1-a_1,\ldots,x_n-a_n)$.
:::

::: {.proof title="Strong Nullstellensatz from the weak form"}
The inclusion $\sqrt J\subseteq I(V(J))$ is immediate. Let $f\in I(V(J))$ and consider
$$
J'=(J,1-yf)\subseteq k[x_1,\ldots,x_n,y].
$$
If $J'$ were proper, the weak Nullstellensatz would give a point $(a,b)$ in its zero locus. Then $a\in V(J)$, hence $f(a)=0$, while $1-bf(a)=0$, a contradiction. Thus $J'=(1)$.

Apply the homomorphism
$$
k[x_1,\ldots,x_n,y]\longrightarrow k[x_1,\ldots,x_n]_f,
\qquad y\longmapsto f^{-1}.
$$
The generator $1-yf$ maps to zero, so $1\in Jk[x_1,\ldots,x_n]_f$. Clearing denominators gives $f^N\in J$ for some $N$, hence $f\in\sqrt J$.
:::

::: {.remark}
The algebraic-closure hypothesis is essential for the geometric statement.

Over $\RR$ the ideal $(x^2+1)$ is prime, hence radical, but $V(x^2+1) = \emptyset$ in $\AA^1_\RR$, so $I(V(J)) = (1) \neq \sqrt{J}$.
:::
