---
schema: qual/card@1
id: P-NQAQK
kind: problem
title: $F[x]$-modules of linear operators, similarity, and simplicity in dimension $2$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Linear Algebra
relations: []
review: draft
---
::: {.problem}
Let $F$ be a field and let $V$ and $W$ be vector spaces over $F$. Make $V$ and $W$ into $F[x]$-modules via linear operators $T \in \operatorname{End}_F(V)$ and $S \in \operatorname{End}_F(W)$ by defining $x \cdot v = T(v)$ for all $v \in V$ and $x \cdot w = S(w)$ for all $w \in W$. Denote the resulting $F[x]$-modules by $V_T$ and $W_S$ respectively.

(a) Show that an $F[x]$-module homomorphism from $V_T$ to $W_S$ consists of an $F$-linear transformation $R: V \to W$ such that $R T = S R$.

(b) Show that $V_T \cong W_S$ as $F[x]$-modules if and only if there is an $F$-linear isomorphism $P: V \to W$ such that $T = P^{-1} S P$.

(c) Recall that a module $M$ is *simple* (or irreducible) if $M \ne \{0\}$ and its only submodules are $\{0\}$ and $M$. Suppose that $\dim_F V = 2$. Give an example of $F$ and $T$ with $V_T$ simple.

(d) Assume $F$ is algebraically closed. Prove that if $\dim_F V = 2$, then $V_T$ is never simple.
:::

::: {.solution}
For $h(x)=\sum_{j=0}^m a_jx^j\in F[x]$, the module action on $V_T$ is $h\cdot v=\sum_{j=0}^m a_jT^jv$, and similarly for $W_S$.

::: pf

::: {.pf-step #s1}

An additive map $R:V_T\to W_S$ is $F[x]$-linear if and only if it is $F$-linear and $RT=SR$.

::: pf-proof

An $F[x]$-linear map is $F$-linear by restriction along $F\hookrightarrow F[x]$, and compatibility with multiplication by $x$ gives $RT=SR$. Conversely, if $R$ is $F$-linear and $RT=SR$, induction on $j$ gives $RT^j=S^jR$. Hence for every polynomial $h=\sum a_jx^j$ and $v\in V$, one has
\[
R(h\cdot v)=\sum_j a_jRT^jv=\sum_j a_jS^jRv=h\cdot R(v).
\]
Thus $R$ is an $F[x]$-module homomorphism.

:::

:::

::: {.pf-step #s2}

The modules $V_T$ and $W_S$ are isomorphic if and only if there is an $F$-linear isomorphism $P:V\to W$ such that $T=P^{-1}SP$.

::: pf-proof

By step [](#s1){.pf-ref}, an $F[x]$-linear isomorphism $P$ is an invertible $F$-linear map satisfying $PT=SP$, which is equivalent to $T=P^{-1}SP$. Conversely, an invertible $F$-linear map satisfying this relation is $F[x]$-linear by step [](#s1){.pf-ref}, and its inverse is automatically $F[x]$-linear by applying the intertwining identity to the inverse.

:::

:::

::: {.pf-step #s3}

A simple two-dimensional example is
\[
\boxed{F=\RR,\quad V=\RR^2,\quad T=\begin{pmatrix}0&-1\\1&0\end{pmatrix}}.
\]

::: pf-proof

The $F[x]$-submodules of $V_T$ are precisely the $T$-invariant $F$-linear subspaces. Every proper nonzero subspace of $\RR^2$ is one-dimensional. Such a subspace is $T$-invariant only when it is an eigenspace of $T$ over $\RR$. But the characteristic polynomial $x^2+1$ has no real root, so $T$ has no nonzero real eigenvector. Hence $V_T$ has no proper nonzero submodule and is simple.

:::

:::

::: {.pf-step #s4}

If $F$ is algebraically closed and $\dim_F V=2$, then $V_T$ is not simple.

::: pf-proof

The characteristic polynomial of $T$ has degree two and therefore has a root $\lambda\in F$. Consequently there exists a nonzero eigenvector $v\in V$ with $Tv=\lambda v$. The one-dimensional subspace $Fv$ is stable under $T$, hence is an $F[x]$-submodule. Since $0\neq Fv\neq V$, this proves that $V_T$ is not simple.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a)--(d), respectively.

:::

:::

:::
