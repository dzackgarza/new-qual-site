---
schema: qual/card@1
id: P-6EVID
kind: problem
title: Deck transformations sending $y_0$ to $y_1$ iff $p_*(\pi_1(\widetilde{X},y_0))=p_*(\pi_1(\widetilde{X},y_1))$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Group Actions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked the statement against Section B, problem B4 of the January 18,
    2002 topology qualifying exam. The printed line reads "with X and locally
    path-connected," omitting the second space name; the card retains the
    evident intended reading that X and X-tilde are locally path-connected.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Applied the lifting criterion on the path components containing y0 and y1.
    Equality of the two fundamental-group images gives inverse covering
    isomorphisms between those components; local path-connectedness makes
    components open, so the isomorphism extends to a deck transformation of
    the whole, possibly disconnected, covering space.
---

::: {.problem}
Let $p : \widetilde{X} \to X$ be a covering map, with $X$ and $\widetilde{X}$ locally path-connected, and $x_0 \in X$.
Show that for $y_0, y_1 \in p^{-1}(\{x_0\})$, there is a deck transformation of $\widetilde{X}$ taking $y_0$ to $y_1$ if and only if $$p_*(\pi_1(\widetilde{X},y_0)) = p_*(\pi_1(\widetilde{X},y_1)).$$
:::

::: {.solution}
For $j=0,1$, let $C_j$ be the connected component of $\widetilde X$ containing $y_j$, and let $X_0$ be the connected component of $X$ containing $x_0$.

<1>1. Each $C_j$ and $X_0$ is open and path-connected, and $p_j\coloneqq p|_{C_j}\colon C_j\to X_0$ is a covering map.

::: {.proof}
In a locally path-connected space, connected components are open and path-connected.
Hence $C_j$ and $X_0$ have these properties.

The image of $C_j$ under $p$ is all of $X_0$.
Indeed, if $x\in X_0$, choose a path in $X_0$ from $x_0$ to $x$.
Its lift starting at $y_j$ remains in $C_j$ and ends over $x$.

Finally, around any $x\in X_0$, choose a path-connected evenly covered neighborhood $U\subseteq X_0$.
Every sheet over $U$ is path-connected, so each sheet that meets $C_j$ lies entirely in $C_j$.
Thus the sheets lying in $C_j$ evenly cover $U$ for $p_j$.
:::

<1>2. If a deck transformation $T\colon\widetilde X\to\widetilde X$ satisfies $T(y_0)=y_1$, then $p_*(\pi_1(\widetilde X,y_0))=p_*(\pi_1(\widetilde X,y_1))$.

::: {.proof}
Since $T$ is a deck transformation, $p\circ T=p$, so $p_*\circ T_*=p_*$ with the indicated basepoints.
Because $T$ is a homeomorphism taking $y_0$ to $y_1$, $T_*\colon\pi_1(\widetilde X,y_0)\to\pi_1(\widetilde X,y_1)$ is an isomorphism.
Therefore
$$\begin{aligned}
p_*(\pi_1(\widetilde X,y_0))
&=p_*\bigl(T_*(\pi_1(\widetilde X,y_0))\bigr)\\
&=p_*(\pi_1(\widetilde X,y_1)).
\end{aligned}$$
:::

<1>3. If $p_*(\pi_1(\widetilde X,y_0))=p_*(\pi_1(\widetilde X,y_1))$, then there is a map $h\colon C_0\to C_1$ with $p_1\circ h=p_0$ and $h(y_0)=y_1$.

::: {.proof}
Every loop in $\widetilde X$ based at $y_j$ lies in $C_j$, so $\pi_1(\widetilde X,y_j)=\pi_1(C_j,y_j)$.
The assumed equality therefore gives $(p_0)_*(\pi_1(C_0,y_0))\subseteq(p_1)_*(\pi_1(C_1,y_1))$.
By step <1>1, $C_0$ is path-connected and locally path-connected and $p_1\colon C_1\to X_0$ is a covering map.
The lifting criterion for covering spaces therefore gives a lift $h$ of $p_0$ through $p_1$ with $h(y_0)=y_1$.
:::

<1>4. The map $h$ of step <1>3 is a homeomorphism $C_0\to C_1$ with $p_1\circ h=p_0$.

::: {.proof}
The assumed equality also gives the reverse inclusion, so the lifting criterion gives $k\colon C_1\to C_0$ with $k(y_1)=y_0$ and $p_0\circ k=p_1$.
Then $k\circ h$ and $\operatorname{id}_{C_0}$ are two lifts of $p_0\colon C_0\to X_0$ through the covering $p_0\colon C_0\to X_0$, and both take $y_0$ to $y_0$.
Since $C_0$ is connected, uniqueness of lifts gives $k\circ h=\operatorname{id}_{C_0}$.
Similarly, $h\circ k=\operatorname{id}_{C_1}$.
Hence $h$ is a homeomorphism with inverse $k$.
:::

<1>5. The homeomorphism $h$ extends to a deck transformation $T$ of $\widetilde X$ with $T(y_0)=y_1$.

::: {.proof}
Every connected component of $\widetilde X$ is open, because $\widetilde X$ is locally path-connected.

If $C_0=C_1$, define $T$ to equal $h$ on $C_0$ and the identity on every other component.

If $C_0\neq C_1$, define $T$ to equal $h$ on $C_0$, $h^{-1}$ on $C_1$, and the identity on every other component.

Because the components are disjoint open sets, $T$ is continuous, and so is its inverse, which is defined in the same way with $h$ and $h^{-1}$ exchanged.
In either case $p\circ T=p$, since $p_1\circ h=p_0$ and $p_0\circ h^{-1}=p_1$ by step <1>4, and $T(y_0)=y_1$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves that a deck transformation taking $y_0$ to $y_1$ forces $p_*(\pi_1(\widetilde X,y_0))=p_*(\pi_1(\widetilde X,y_1))$.
Steps <1>3, <1>4, and <1>5 prove the converse.
:::
:::
