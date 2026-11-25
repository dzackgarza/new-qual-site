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
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps and named the machinery each step uses, since the
    prose ran the two directions of the bijection and the extension arguments together. The
    hypotheses are now used explicitly: n = 1 is the classification of maps into a K(pi_1,1); for
    n >= 2 the (n-1)-connectivity gives a CW model with a single 0-cell and no cells in dimensions
    1..n-1, so X^{n-1} is a point and every based map is constant there; C_n(X) has zero boundary,
    so it is the group of cycles; extension over (n+1)-cells is the vanishing on boundaries;
    Hurewicz identifies H_n(X) with pi_n(X); and the higher obstructions lie in pi_i(Y) = 0 for
    i > n. Not checked this session: the printed page of the exercise, and the obstruction theory
    of Section 4.3, which is used at the level of the statements Hatcher proves there rather than
    re-derived.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 17. One citation slip repaired: the step called Proposition
    1B.9 a theorem; the book states it as a proposition, and the step now does too. The proof reads
    correct.
---

::: {.problem}
Show that the map $\langle X, Y \rangle \to \operatorname{Hom}(\pi_n(X), \pi_n(Y))$, $[f] \mapsto f_*$, is a bijection if $X$ is an $(n-1)$-connected CW complex and $Y$ is a path-connected space with $\pi_i(Y) = 0$ for $i > n$.
Deduce that CW complexes $K(G, n)$'s are uniquely determined, up to homotopy type, by $G$ and $n$.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.2 Exercise 17. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 17. Write $\langle X,Y\rangle$ for based homotopy classes of based maps.

::: pf

::: {.pf-step #n1}
For $n=1$ the map $\langle X,Y\rangle\to\operatorname{Hom}\bigl(\pi_{1}(X),\pi_{1}(Y)\bigr)$ is a bijection.

::: pf-proof
Here $X$ is a path-connected CW complex and $Y$ is path-connected with $\pi_{i}(Y)=0$ for $i>1$, so $Y$ is a $K(\pi_{1}(Y),1)$. Hatcher's Proposition 1B.9 states that for such $Y$ the assignment $[f]\mapsto f_{*}$ is a bijection from based homotopy classes $\langle X,Y\rangle$ to homomorphisms $\pi_{1}(X)\to\pi_{1}(Y)$.
:::

:::

::: {.pf-step #model}
For $n\geq2$ we may assume $X$ has a single $0$-cell and no cells in dimensions $1,\dots,n-1$.

::: pf-proof
$X$ is $(n-1)$-connected, so by Hatcher's CW approximation construction it is homotopy equivalent to a CW complex built with a single $0$-cell and one cell for each generator of $\pi_{i}(X)$ at each stage $i$, and $\pi_{i}(X)=0$ for $1\leq i\leq n-1$ means no such cells occur. $\langle X,Y\rangle$ and $\mathrm{Hom}(\pi_{n}X,\pi_{n}Y)$ are both unchanged under replacing $X$ by a homotopy equivalent CW complex.
:::

:::

::: {.pf-step #constant}
With this model, every based map $f\colon X\to Y$ is the constant map on $X^{n-1}=\{x_{0}\}$, and $C_{n}(X)=Z_{n}(X)$.

::: pf-proof
The $(n-1)$-skeleton of the model is the single $0$-cell, which every based map sends to $y_{0}$. Since $C_{n-1}(X)=0$, the cellular boundary $d_{n}\colon C_{n}(X)\to C_{n-1}(X)$ is zero, so every $n$-chain is a cycle.
:::

:::

::: {.pf-step #ncells}
A based map $f$ determines a homomorphism $\theta_{f}\colon C_{n}(X)\to\pi_{n}(Y)$.

::: pf-proof
For each $n$-cell $e^{n}_{\alpha}$ with characteristic map $\Phi_{\alpha}\colon(D^{n},S^{n-1})\to(X^{n},X^{n-1})$, the composite $f\Phi_{\alpha}$ is a based map $(D^{n},S^{n-1})\to(Y,y_{0})$ because $f$ is constant on $X^{n-1}$ by step [](#constant){.pf-ref}; so it represents an element $\theta_{f}(e^{n}_{\alpha})\in\pi_{n}(Y)$. Since $C_{n}(X)$ is free on the $n$-cells, extending by linearity gives a homomorphism, and the pointwise sum of maps on a sphere uses the pinch map, which is why the assignment is additive.
:::

:::

::: {.pf-step #extension}
$f$ extends over $X^{n+1}$ if and only if $\theta_{f}$ vanishes on the image of $d_{n+1}$.

::: pf-proof
This is the first step of obstruction theory (Hatcher, §4.3): the obstruction to extending a map defined on $X^{n}$ over the $(n+1)$-cell $e^{n+1}_{\beta}$ is the class in $\pi_{n}(Y)$ of the composite of $f$ with the attaching map, and that class is exactly $\theta_{f}\bigl(d_{n+1}(e^{n+1}_{\beta})\bigr)$; the extensions over the individual cells are compatible because the obstructions are computed cell by cell in the free group $C_{n}(X)$.
:::

:::

::: {.pf-step #factor}
$\theta_{f}$ factors through $H_{n}(X)$, and $H_{n}(X)\cong\pi_{n}(X)$.

::: pf-proof
By steps [](#constant){.pf-ref} and [](#extension){.pf-ref}, $\theta_{f}$ vanishes on $B_{n}(X)=\operatorname{im}d_{n+1}$ and is defined on $Z_{n}(X)=C_{n}(X)$, so it induces a homomorphism $H_{n}(X)=Z_{n}/B_{n}\to\pi_{n}(Y)$. Since $X$ is $(n-1)$-connected with $n\geq2$, the Hurewicz theorem gives $H_{n}(X)\cong\pi_{n}(X)$.
:::

:::

::: {.pf-step #surjective}
Every homomorphism $\pi_{n}(X)\to\pi_{n}(Y)$ is $f_{*}$ for some based map $f$.

::: pf-proof
A homomorphism $\varphi$ gives, via step [](#factor){.pf-ref}, a compatible choice of maps on the $n$-cells, hence a map on $X^{n}$ constant on $X^{n-1}$; the condition of step [](#extension){.pf-ref} holds because $\varphi$ is defined on $H_{n}$, so the map extends over $X^{n+1}$. The remaining obstructions to extending over cells of dimension $\geq n+2$ lie in $\pi_{i}(Y)$ with $i\geq n+1>n$, and these groups vanish by hypothesis, so $f$ exists on all of $X$ and $f_{*}=\varphi$ after identifying $\pi_{n}(X)$ with $H_{n}(X)$.
:::

:::

::: {.pf-step #injective}
If $f_{*}=g_{*}$ then $f\simeq g$ through based maps.

::: pf-proof
By step [](#factor){.pf-ref} the two maps have the same $\theta$, hence the same class on each $n$-cell, so their restrictions to $X^{n}$ are homotopic rel basepoint. A homotopy on $X^{n}\times I\cup X\times\partial I\to Y$ then has obstructions to extension over the cells $e^{i}\times I$ with $i\geq n+1$, lying in $\pi_{i}(Y)$ for $i>n$, which vanish by hypothesis; so the homotopy extends and $f\simeq g$.
:::

:::

::: {.pf-step #bijection}
$\langle X,Y\rangle\to\operatorname{Hom}(\pi_{n}X,\pi_{n}Y)$ is a bijection.

::: pf-proof
Steps [](#n1){.pf-ref} handle $n=1$; for $n\geq2$, steps [](#surjective){.pf-ref} and [](#injective){.pf-ref} give surjectivity and injectivity of the assignment $[f]\mapsto f_{*}$, which is well defined because homotopic maps induce the same homomorphism.
:::

:::

::: {.pf-step #unique}
CW complexes of type $K(G,n)$ are unique up to homotopy type.

::: pf-proof
Let $X,Y$ be CW complexes with $\pi_{n}=G$ and all other homotopy groups zero. The identity of $G$ corresponds under step [](#bijection){.pf-ref} to based maps $f\colon X\to Y$ and $g\colon Y\to X$. Then $(gf)_{*}=\mathrm{id}$ on $\pi_{n}(X)$, so $gf\simeq\mathrm{id}_{X}$ by the injectivity of step [](#injective){.pf-ref} applied with $f$ and the identity; similarly $fg\simeq\mathrm{id}_{Y}$. Hence $f$ and $g$ are homotopy inverses and $X\simeq Y$.
:::

:::

:::

:::
