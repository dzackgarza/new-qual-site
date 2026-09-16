---
schema: qual/card@1
id: P-AGH525INVARIANTE
kind: problem
title: Which values of the invariant $e$ occur for ruled surfaces over a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
---

::: {.problem}
Let $C$ be a curve of genus $g \geqslant 1$.

a. Show that for each $0 \leqslant e \leqslant 2 g-2$ there is a ruled surface $X$ over $C$ with invariant $e$, corresponding to an indecomposable $\mathcal{E}$.
Cf.
(2.12).

b. Let $e<0$, let $D$ be any divisor of degree $d=-e$, and let $\xi \in H^1(\mathcal{L}(-D))$ be a nonzero element defining an extension
\[
0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{E} \rightarrow \mathcal{L}(D) \rightarrow 0 .
\]
Let $H \subseteq|D+K|$ be the sublinear system of codimension 1 defined by $\ker \xi$, where $\xi$ is considered as a linear functional on $H^0(\mathcal{L}(D+K))$.
For any effective divisor $E$ of degree $d-1$, let $L_E \subseteq|D+K|$ be the sublinear system $|D+K-E|+E$.
Show that $\mathcal{E}$ is normalized if and only if for each $E$ as above, $L_E \nsubseteq H$.
Cf.
proof of $(2.15)$.

c. Now show that if $-g \leqslant e<0$, there exists a ruled surface $X$ over $C$ with invariant $e$.

Hint: For any given $D$ in (b), show that a suitable $\xi$ exists, using an argument similar to the proof of (II, 8.18).

d. For $g=2$, show that $e \geqslant-2$ is also necessary for the existence of $X$.

Note.
It has been shown that $e \geqslant-g$ for any ruled surface (Nagata [8]).
:::
