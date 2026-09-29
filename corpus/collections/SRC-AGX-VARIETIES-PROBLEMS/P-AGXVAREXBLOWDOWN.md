---
schema: qual/card@1
id: P-AGXVAREXBLOWDOWN
kind: problem
title: The map $(x,y)\mapsto (x, xy)$ of the affine plane and its fibers
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dominant Morphisms
  - Finite Morphisms
  - Fibers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 4.7 in the recorded source. It asks exactly for
    finiteness, dominance, openness, closedness, and the fibers of
    (x,y) -> (x,xy), under the notes' standing algebraically-closed
    characteristic-zero base-field convention.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the complete fiber calculation, density of D(u), the
    positive-dimensional origin fiber obstruction to finiteness, failure of
    openness from the image of A^2, and failure of closedness using
    V(xy-1).
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic zero. Consider the
morphism
$$
\begin{aligned}
f:\AA^2_k&\longrightarrow\AA^2_k,\\
(x,y)&\longmapsto(x,xy).
\end{aligned}
$$
Is this finite? Dominant? Open? Closed? What are the fibers?
:::

::: {.solution}
Write $(u,v)$ for the coordinates on the target $\AA^2_k$.

::: pf

::: {.pf-step #fibers-computation}
For $(a,b)\in\AA^2(k)$, the fibers are
$$
\boxed{
f^{-1}(a,b)
=
\begin{cases}
\{(a,b/a)\},&a\neq0,\\
\{0\}\times\AA^1_k,&a=0,\ b=0,\\
\emptyset,&a=0,\ b\neq0.
\end{cases}}
$$
Consequently,
$$
f(\AA^2_k)
=
D(u)\cup\{(0,0)\}.
$$

::: pf-proof
A point $(x,y)$ belongs to the fiber over $(a,b)$ exactly when
$$
x=a,
\qquad
xy=b.
$$
If $a\neq0$, these equations force
$$
x=a,
\qquad
y=b/a,
$$
so the fiber is a singleton. If $a=0$, the second equation becomes
$$
0=b.
$$
Thus for $(a,b)=(0,0)$ every point $(0,y)$ lies in the fiber, while for
$a=0$ and $b\neq0$ the fiber is empty. The displayed description of the
image follows immediately.
:::

:::

::: {.pf-step #f-is-dominant}
The morphism $f$ is dominant.

::: pf-proof
By step [](#fibers-computation){.pf-ref},
$$
D(u)\subseteq f(\AA^2_k).
$$
The affine plane is irreducible, so its nonempty open subset $D(u)$ is dense
([[P-AGXVARDENSEOPEN|density of nonempty Zariski-open subsets]]). Therefore
$$
\overline{f(\AA^2_k)}
\supseteq
\overline{D(u)}
=
\AA^2_k.
$$
Hence the image of $f$ is dense, which is exactly dominance.
:::

:::

::: {.pf-step #f-not-finite}
The morphism $f$ is not finite.

::: pf-proof
By step [](#fibers-computation){.pf-ref},
$$
f^{-1}(0,0)=\{0\}\times\AA^1_k,
$$
which is a positive-dimensional, hence infinite, fiber. A finite morphism has
finite fibers. Therefore $f$ is not finite.
:::

:::

::: {.pf-step #f-not-open}
The morphism $f$ is not open.

::: pf-proof
The whole source $\AA^2_k$ is open. If $f$ were an open map, its image
$$
f(\AA^2_k)=D(u)\cup\{(0,0)\}
$$
would be open in the target.

Let
$$
L=V(u)\cong\AA^1_k
$$
be the vertical coordinate line. Step [](#fibers-computation){.pf-ref} gives
$$
f(\AA^2_k)\cap L=\{(0,0)\}.
$$
If $f(\AA^2_k)$ were open, this singleton would be open in $L$. But $L$ is
an infinite curve whose Zariski topology is cofinite
([[P-AGXVARCURVECOFIN|cofinite topology on curves]]), so a singleton is not
open. This contradiction proves that $f$ is not open.
:::

:::

::: {.pf-step #f-not-closed}
The morphism $f$ is not closed.

::: pf-proof
Consider the closed hyperbola
$$
H=V(xy-1)\subseteq\AA^2_k.
$$
For $(x,y)\in H$ one has $xy=1$, so
$$
f(x,y)=(x,1).
$$
Conversely, for every $a\in k^\times$,
$$
f(a,a^{-1})=(a,1).
$$
Hence
$$
f(H)
=
\{(a,1):a\in k^\times\}
=
V(v-1)\setminus\{(0,1)\}.
$$
The line $V(v-1)\cong\AA^1_k$ has the cofinite Zariski topology, so deleting
one point gives a dense proper subset. Thus $f(H)$ is not closed in the line,
and therefore is not closed in $\AA^2_k$. Since $H$ is closed, $f$ is not a
closed map.
:::

:::

::: {.pf-step #summary-of-properties}
The four requested properties are
$$
\boxed{
\text{$f$ is dominant, but it is neither finite, open, nor closed.}
}
$$

::: pf-proof
Dominance is step [](#f-is-dominant){.pf-ref}, non-finiteness is step [](#f-not-finite){.pf-ref}, failure of openness is
step [](#f-not-open){.pf-ref}, and failure of closedness is step [](#f-not-closed){.pf-ref}. The fibers were computed
in step [](#fibers-computation){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#fibers-computation){.pf-ref}, [](#f-is-dominant){.pf-ref}, [](#f-not-finite){.pf-ref}, [](#f-not-open){.pf-ref}, [](#f-not-closed){.pf-ref} and [](#summary-of-properties){.pf-ref} answer every part of the problem.
:::

:::

:::
