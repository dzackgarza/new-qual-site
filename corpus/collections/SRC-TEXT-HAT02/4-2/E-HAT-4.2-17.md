---
schema: qual/card@1
id: E-HAT-4.2-17
kind: problem
title: "Maps to $K(G,n)$ are determined by $\\pi_n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 17; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Show that the map $\langle X, Y \rangle \to \operatorname{Hom}(\pi_n(X), \pi_n(Y))$, $[f] \mapsto f_*$, is a bijection if $X$ is an $(n-1)$-connected CW complex and $Y$ is a path-connected space with $\pi_i(Y) = 0$ for $i > n$.
Deduce that CW complexes $K(G, n)$'s are uniquely determined, up to homotopy type, by $G$ and $n$.
:::

::: {.solution}
For $n=1$, the assertion is the classification of based maps into a $K(\pi_1(Y),1)$ by homomorphisms of fundamental groups. Suppose $n\ge2$. We use cellular obstruction theory. Since $X$ is $(n-1)$-connected, it is homotopy equivalent to a CW complex with one $0$-cell and no cells in dimensions $1,\dots,n-1$. We may therefore assume this form.

A based map $f:X\to Y$ is constant on $X^{n-1}$. On each $n$-cell its restriction determines an element of $\pi_n(Y)$. Since the chosen CW structure has no cells in dimensions $1,\dots,n-1$, its cellular group $C_n(X)$ is the group of $n$-cycles. The choices extend over the $(n+1)$-cells exactly when the resulting homomorphism $C_n(X)\to\pi_n(Y)$ vanishes on the cellular boundaries. It then factors through
$$
H_n(X)\cong\pi_n(X)
$$
(the Hurewicz isomorphism). Thus a map determines a homomorphism
$$
\pi_n(X)\to\pi_n(Y).
$$
Conversely, any such homomorphism prescribes compatible maps on the $n$-cells. After the $(n+1)$-cell condition, all higher extension obstructions lie in groups $\pi_i(Y)$ with $i>n$, which are zero by hypothesis. If two maps induce the same homomorphism on $\pi_n$, their restrictions to the $n$-skeleton can first be made equal up to based homotopy. The vanishing of the higher homotopy groups then extends this homotopy over the remaining cells.

Hence
$$
\boxed{\langle X,Y\rangle\xrightarrow{\cong}\operatorname{Hom}(\pi_nX,\pi_nY).}
$$
Now let $X$ and $Y$ be CW complexes of type $K(G,n)$. The identity homomorphism of $G$ determines maps
$$
f:X\to Y,
\qquad g:Y\to X.
$$
The composites $gf$ and $fg$ induce the identity on $\pi_n$. By the bijection just proved they are homotopic to the identity maps. Therefore $f$ and $g$ are homotopy inverses, so
$$
\boxed{K(G,n)\text{ is unique up to homotopy type}.}
$$
:::
