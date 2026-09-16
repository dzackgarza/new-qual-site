---
schema: qual/card@1
id: P-E6DTF
kind: problem
title: 'Schur''s lemma: $\operatorname{Hom}_{kG}(V,V)=k$ for an irreducible representation
  over an algebraically closed field'
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a finite group, $k$ an algebraically closed field, and $V$ an irreducible $k$-linear representation of $G$.

- Show that $\hom_{kG}(V,V)$ is a division algebra with $k$ in its center.

- Show that $V$ is finite-dimensional over $k$, and conclude that $\hom_{kG}(V,V)$ is also finite dimensional.

- Show the inclusion $k\hookrightarrow\hom_{kG}(V,V)$ found in (a) is an isomorphism.
  (For $f\in\hom_{kG}(V,V)$, view $f$ as a linear transformation and consider $f-\alpha I$, where $\alpha$ is an eigenvalue of $f$).
:::


::: {.solution}
<1>1. Every nonzero element of $\operatorname{Hom}_{kG}(V,V)$ is invertible, so $\operatorname{Hom}_{kG}(V,V)$ is a division algebra.
::: {.proof}
Let $0\ne f\in\operatorname{Hom}_{kG}(V,V)$. Both $\ker f$ and $\operatorname{im}f$ are $kG$-submodules of $V$. Since $V$ is irreducible,
\[
\ker f\in\{0,V\},\qquad \operatorname{im}f\in\{0,V\}.
\]
Because $f\ne0$, one cannot have $\ker f=V$ or $\operatorname{im}f=0$. Hence $\ker f=0$ and $\operatorname{im}f=V$, so $f$ is bijective. Its inverse is again $kG$-linear: if $v=f(u)$, then for $g\in G$,
\[
f^{-1}(gv)=f^{-1}(gf(u))=f^{-1}(f(gu))=gu=g f^{-1}(v).
\]
Thus every nonzero endomorphism is a unit.
:::

<1>2. The scalar maps embed $k$ into the center of $\operatorname{Hom}_{kG}(V,V)$.
::: {.proof}
For $\lambda\in k$, the map $\lambda I_V$ is $kG$-linear, and
\[
(\lambda I_V)f=f(\lambda I_V)
\]
for every $k$-linear endomorphism $f$. The map $\lambda\mapsto\lambda I_V$ is injective because $V\ne0$.
:::

<1>3. The representation $V$ is finite-dimensional over $k$.
::: {.proof}
Choose $0\ne v\in V$. The $k$-span
\[
W=\operatorname{span}_k\{gv:g\in G\}
\]
is a nonzero $kG$-submodule of $V$. Since $V$ is irreducible, $W=V$. Because $G$ is finite, $W$ is spanned by at most $|G|$ vectors, hence
\[
\dim_kV\le |G|<\infty.
\]
:::

<1>4. The algebra $\operatorname{Hom}_{kG}(V,V)$ is finite-dimensional over $k$.
::: {.proof}
It is a $k$-linear subspace of the finite-dimensional vector space $\operatorname{End}_k(V)$, whose dimension is $(\dim_kV)^2$.
:::

<1>5. Every $kG$-endomorphism of $V$ is scalar. Therefore
\[
k\xrightarrow{\ \sim\ }\operatorname{Hom}_{kG}(V,V),
\qquad
\lambda\longmapsto\lambda I_V.
\]
::: {.proof}
Let $f\in\operatorname{Hom}_{kG}(V,V)$. Since $V$ is finite-dimensional and $k$ is algebraically closed, the characteristic polynomial of $f$ has a root $\alpha\in k$. Hence $f-\alpha I_V$ has nonzero kernel and is therefore not invertible. But by <1>1 every nonzero element of $\operatorname{Hom}_{kG}(V,V)$ is invertible. Consequently
\[
f-\alpha I_V=0,
\]
so $f=\alpha I_V$. Together with <1>2, this proves the scalar inclusion is an isomorphism.
:::
:::
