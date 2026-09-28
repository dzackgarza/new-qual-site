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
We use cellular obstruction theory. Since \(X\) is \((n-1)\)-connected, it is homotopy equivalent to a CW complex with one \(0\)-cell and no cells in dimensions \(1,\dots,n-1\). We may therefore assume this form.

A based map \(f:X\to Y\) is homotopic to the constant map on \(X^{n-1}\). On each \(n\)-cell its restriction determines an element of \(\pi_n(Y)\). The condition that these choices extend over the \((n+1)\)-cells is exactly that the resulting homomorphism on \(n\)-cycles factor through
\[
H_n(X)\cong\pi_n(X)
\]
(the Hurewicz isomorphism). Thus a map determines a homomorphism
\[
\pi_n(X)\to\pi_n(Y).
\]
Conversely, any such homomorphism prescribes compatible maps on the \(n\)-cells. All higher extension obstructions lie in groups \(\pi_i(Y)\) with \(i>n\), which are zero by hypothesis, so the map extends over all higher cells. The same vanishing says that two extensions inducing the same map on \(\pi_n\) are homotopic rel the \(n\)-skeleton.

Hence
\[
\boxed{\langle X,Y\rangle\xrightarrow{\cong}\operatorname{Hom}(\pi_nX,\pi_nY).}
\]
For \(n=1\) the identical cellular argument is the usual classification of based maps into a \(K(G,1)\) by homomorphisms of fundamental groups.

Now let \(X\) and \(Y\) be CW complexes of type \(K(G,n)\). The identity homomorphism of \(G\) determines maps
\[
f:X\to Y,
\qquad g:Y\to X.
\]
The composites \(gf\) and \(fg\) induce the identity on \(\pi_n\). By the bijection just proved they are homotopic to the identity maps. Therefore \(f\) and \(g\) are homotopy inverses, so
\[
\boxed{K(G,n)\text{ is unique up to homotopy type}.}
\]
:::
