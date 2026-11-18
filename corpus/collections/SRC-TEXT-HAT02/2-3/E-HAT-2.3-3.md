---
schema: qual/card@1
id: E-HAT-2.3-3
kind: problem
title: Reduced homology theory vanishes on point; suspension isomorphism follows
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
  - Suspension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.3, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both halves: applying exactness to the pair $(*,*)$ makes both maps the identity, so
    $\tilde h_n(*)$ is its own kernel and vanishes; and the exact sequence of $(CX,X)$ with $CX$
    contractible gives a boundary isomorphism $\tilde h_{n+1}(CX/X)\cong\tilde h_n(X)$, with
    $CX/X=SX$.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 3 of §2.3 as printed on p. 165. The vanishing at a point is right:
    in the exact sequence of the pair (*,*) both maps are the identity, so the middle group is
    both zero and the whole group. For the suspension, the cone is contractible, so its h-groups
    vanish by homotopy invariance once h(point) = 0, and the pair sequence of (CX,X) sandwiches
    h~_{n+1}(SX) between two vanishing groups. Axioms (1) and (2) are now cited to p. 160.
    What is not covered: no certificate.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps. Re-read the retained source it cites: DeMason,
    M382C Full Credit HW Problems, Hatcher 2.3.3 at PDF p. 83, which runs the vanishing through the
    exact sequence of the pair (X,X) exactly as the card does and then treats the suspension;
    the two accounts agree. Supplied in the steps: the exactness axiom in the form used, homotopy
    invariance used to kill the reduced groups of a cone once h(point) = 0, and the reduced
    Mayer-Vietoris sequence for the two cones with their intersection X. Not checked this session:
    the printed page 165 of the exercise in Hatcher, and the exact wording of the reduced
    Mayer-Vietoris statement, which is used as Hatcher states it rather than re-read here.
---

::: {.problem}
Show that if $\tilde{h}$ is a reduced homology theory, then $\tilde{h}_n(\text{point}) = 0$ for all $n$.
Deduce that there are suspension isomorphisms $\tilde{h}_n(X) \approx \tilde{h}_{n+1}(SX)$ for all $n$.
:::

::: {.solution}

The argument is that of **Kenneth DeMason, *M382C Full Credit HW Problems* (2021), Hatcher 2.3.3, PDF p. 83** (`tmp/sources/demason-m382c-hatcher-20210404.pdf`): exactness for the pair $(X,X)$, then the two-cone decomposition of the suspension. The statement was checked against Hatcher, *Algebraic Topology* (2002), §2.3 Exercise 3, printed p. 165.

Let $\tilde h$ be a reduced homology theory: functors on CW pairs, homotopy invariant, with the exactness axiom for a CW pair $(X,A)$,
$$
\cdots\to\tilde h_{n+1}(X/A)\xrightarrow{\ \partial\ }\tilde h_{n}(A)\xrightarrow{\ i_{*}\ }\tilde h_{n}(X)\xrightarrow{\ q_{*}\ }\tilde h_{n}(X/A)\xrightarrow{\ \partial\ }\tilde h_{n-1}(A)\to\cdots,
$$
and with the reduced Mayer--Vietoris sequence for a CW triad.

::: pf

::: {.pf-step #point}
$\tilde h_{n}(\mathrm{pt})=0$ for every $n$.

::: pf-proof
Apply the exact sequence to the pair $(X,X)$. The map $i\colon X\to X$ is the identity, so $i_{*}$ is an isomorphism, and $X/X$ is a point. Exactness at $\tilde h_{n}(X)$ gives $\operatorname{im}\partial=\ker i_{*}=0$, so $\partial=0$; exactness at $\tilde h_{n}(\mathrm{pt})$ gives $\operatorname{im}q_{*}=\ker\partial=\tilde h_{n}(\mathrm{pt})$, while exactness at $\tilde h_{n}(X)$ gives $\ker q_{*}=\operatorname{im}i_{*}=\tilde h_{n}(X)$, so $q_{*}=0$. Hence $\tilde h_{n}(\mathrm{pt})=\operatorname{im}q_{*}=0$.
:::

:::

::: {.pf-step #cone}
The cone $CX$ is contractible, so $\tilde h_{k}(CX)=0$ for every $k$.

::: pf-proof
$CX=(X\times I)/(X\times\{0\})$ deformation retracts onto the image of $X\times\{1\}$, a single point, by the homotopy induced by $(x,t)\mapsto(x,1)$. Homotopy invariance gives $\tilde h_{k}(CX)\cong\tilde h_{k}(\mathrm{pt})=0$ by step [](#point){.pf-ref}.
:::

:::

::: {.pf-step #twocones}
In the suspension $SX=(X\times I)/\sim$, with $X\times\{0\}$ and $X\times\{1\}$ crushed to points, the images of $X\times[0,\tfrac12]$ and $X\times[\tfrac12,1]$ are cones $C^{+}X$, $C^{-}X$ with union $SX$ and intersection $X$.

::: pf-proof
The image of $X\times[0,\tfrac12]$ is the quotient of a cone on $X$, the image of $X\times[\tfrac12,1]$ likewise; both contain the image of $X\times\{\tfrac12\}$, which is a copy of $X$, and every point of $SX$ lies in one of them. A point in both images has a representative with parameter in $[0,\tfrac12]$ and one with parameter in $[\tfrac12,1]$, and these agree only at parameter $\tfrac12$.
:::

:::

::: {.pf-step #suspension}
$\tilde h_{n+1}(SX)\cong\tilde h_{n}(X)$ for every $n$.

::: pf-proof
Reduced Mayer--Vietoris for the triad of step [](#twocones){.pf-ref} gives the exact sequence
$$
\tilde h_{n+1}(C^{+}X)\oplus\tilde h_{n+1}(C^{-}X)\to\tilde h_{n+1}(SX)\xrightarrow{\ \Phi\ }\tilde h_{n}(X)\to\tilde h_{n}(C^{+}X)\oplus\tilde h_{n}(C^{-}X).
$$
By step [](#cone){.pf-ref} the two outer groups vanish, so $\ker\Phi=0$ and $\operatorname{coker}\Phi=0$; hence $\Phi$ is an isomorphism.
:::

:::

::: {.pf-step}
$\tilde h_{n}(\mathrm{pt})=0$ for all $n$, and $\tilde h_{n}(X)\cong\tilde h_{n+1}(SX)$.

::: pf-proof
Steps [](#point){.pf-ref} and [](#suspension){.pf-ref} give the two assertions, the second with the index shift written as in the exercise.
:::

:::

:::

:::
