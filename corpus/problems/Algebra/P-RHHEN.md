---
schema: qual/card@1
id: P-RHHEN
kind: problem
title: Hilbert's Nullstellensatz
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Maximal Ideals
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
(a) State the Weak and Strong forms of Hilbert's Nullstellensatz over an algebraically closed field $k$.

(b) State the geometric bijection between radical ideals in $k[x_1, \ldots, x_n]$ and algebraic sets in $\AA^n(k)$.

(c) Sketch the proof of the Nullstellensatz (Zariski's Lemma / Noether Normalization, and the Rabinowitsch trick).
:::

::: {.solution}
Let $k$ be algebraically closed and $R\coloneqq k[x_1,\ldots,x_n]$.

::: pf

::: {.pf-step #statements}
(a) Weak form: every maximal ideal of $R$ is $(x_1-a_1,\ldots,x_n-a_n)$ for some $a\in k^n$; equivalently, every proper ideal of $R$ has a common zero in $k^n$. Strong form: for every ideal $I\subseteq R$, $I(V(I))=\sqrt I$.

::: pf-proof
These are the two forms of Hilbert's Nullstellensatz; steps [](#weak){.pf-ref} and [](#strong){.pf-ref} sketch their proofs.
:::

:::

::: pf-step
(b) The maps $I\mapsto V(I)$ and $X\mapsto I(X)$ are mutually inverse inclusion-reversing bijections between radical ideals of $R$ and algebraic subsets of $\AA^n(k)$. Maximal ideals correspond to points and prime ideals to irreducible algebraic sets.

::: pf-proof
For an algebraic set $X=V(J)$, $V(I(X))=X$ holds over any field. For a radical ideal $I$, the strong form in step [](#statements){.pf-ref} gives $I(V(I))=\sqrt I=I$. The maps reverse inclusions by definition. $X$ is irreducible exactly when $I(X)$ is prime, and the weak form identifies maximal ideals with points.
:::

:::

::: {.pf-step #weak}
(c) The weak form holds.

::: pf-proof
If $\mathfrak m$ is maximal, then $R/\mathfrak m$ is a field that is finitely generated as a $k$-algebra. By Zariski's lemma (a consequence of Noether normalization), it is a finite extension of $k$, hence equal to $k$ because $k$ is algebraically closed. With $a_i$ the image of $x_i$, $\mathfrak m$ contains $(x_1-a_1,\ldots,x_n-a_n)$, which is maximal, so they are equal.
:::

:::

::: {.pf-step #strong}
(c) The strong form holds.

::: pf-proof
The inclusion $\sqrt I\subseteq I(V(I))$ is clear. Let $g$ vanish on $V(I)$, and let $J\coloneqq(I,1-yg)\subseteq k[x_1,\ldots,x_n,y]$ (the Rabinowitsch trick). At a common zero $(a,b)$ of $J$, $a\in V(I)$, so $g(a)=0$ and $1-bg(a)=1\ne0$; hence $V(J)=\varnothing$, and the weak form gives $J=(1)$. Write $1=\sum_j h_jf_j+h(1-yg)$ with $f_j\in I$. Substituting $y=1/g$ in $k(x_1,\ldots,x_n)$ and multiplying by a high power $g^N$ gives $g^N\in I$.
:::

:::

:::
:::
