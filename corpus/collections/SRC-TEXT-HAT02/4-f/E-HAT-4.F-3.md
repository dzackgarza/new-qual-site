---
schema: qual/card@1
id: E-HAT-4.F-3
kind: problem
title: "Homotopy colimit commutes with loop space"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.F, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the argument into numbered steps and proved the compactness lemma it rests on rather
    than asserting it: a map from a compact space into a mapping telescope has image in a finite
    sub-telescope, and a finite sub-telescope deformation retracts onto its last stage, so homotopy
    classes into the telescope are the direct limit of homotopy classes into the stages. The map
    kappa is defined explicitly, and the comparison of the two direct limits is carried out with the
    loop-space identity pi_j(Omega Z) = pi_{j+1}(Z). Every macro used is one the preamble defines.
    Not checked this session: the printed page 455 of Hatcher that the card cites.
---

::: {.problem}
Show that for any sequence $Z_1 \to Z_2 \to \cdots$, the natural map $\varinjlim \Omega Z_n \to \Omega \varinjlim Z_n$ is a weak homotopy equivalence, where the direct limits mean mapping telescopes.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.F Exercise 3. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.F Exercise 3.

For a sequence $Z_{1}\to Z_{2}\to\cdots$ with maps $i_{n}\colon Z_{n}\to Z_{n+1}$, the mapping telescope is $T=\bigsqcup_{n}Z_{n}\times[n-1,n]/\sim$ with $(z,n)\sim(i_{n}z,n)$ where the first copy of $n$ is an endpoint of the $n$-th block and the second of the $(n+1)$-st.

::: pf

::: {.pf-step #kappa}
The rule $(\omega,n)\mapsto(\omega,{\cdot})$ obtained by viewing a loop in $Z_{n}$ as a loop in the corresponding block defines a continuous map $\kappa\colon T_{\Omega}=\operatorname{hocolim}\Omega Z_{n}\to\Omega T$.

::: pf-proof
An element of $T_{\Omega}$ is represented by $(\omega,s)$ with $\omega\colon I\to Z_{n}$ a based loop and $s\in[n-1,n]$. Send it to the loop $t\mapsto$ the point of $T$ represented by $(\omega(t),s)$. This is continuous in $(t,\omega,s)$ on each block, is based because $\omega(0)=\omega(1)$ gives the basepoint class, and is compatible with the identifications in both telescopes, so it descends to a continuous map of the homotopy colimits, natural in the sequence.
:::

:::

::: {.pf-step #compact}
For every space $Y$ and every $n$, a map $f\colon S^{n}\to T$ factors through the inclusion of a finite sub-telescope $T_{\leq N}=\bigcup_{k\leq N}Z_{k}\times[k-1,k]$, and $T_{\leq N}$ deformation retracts onto $Z_{N}$.

::: pf-proof
$S^{n}$ is compact and the sub-telescopes $T_{\leq N}$ are closed with union $T$; a compact subset of $T$ meets only finitely many blocks $Z_{k}\times(k-1,k)$ that are open in $T$, and their closures lie in a finite $T_{\leq N}$, so the image of $f$ lies in $T_{\leq N}$ for $N$ large. The deformation retraction is the map that, on the $k$-th block with $k\leq N$, sends $(z,s)$ to $(i_{N-1}\cdots i_{k}z,N-1)$ along the linear homotopy in the $s$-coordinate and then uses the $\sim$-identifications; it is continuous and fixes $T_{\leq N}$'s last block pointwise.
:::

:::

::: {.pf-step #limitpi}
$\pi_{j}(T)\cong\varinjlim_{n}\pi_{j}(Z_{n})$ and $\pi_{j}(T_{\Omega})\cong\varinjlim_{n}\pi_{j}(\Omega Z_{n})$ for every $j\geq0$.

::: pf-proof
By step [](#compact){.pf-ref} a map $S^{j}\to T$ lands in some $T_{\leq N}$ and, up to homotopy, in $Z_{N}\subset T$, since $T_{\leq N}\simeq Z_{N}$ by the deformation retraction; a homotopy $S^{j}\times I\to T$ is likewise confined to a finite sub-telescope by compactness of $S^{j}\times I$. So $[S^{j},T]=\varinjlim_{n}[S^{j},Z_{n}]$, and based versions and the resulting group isomorphisms follow by the same argument applied to $S^{j}\times I$ and to basepoints, using that the deformation retractions are homotopic to the identity through maps preserving the basepoint. The same argument with $Z_{n}$ replaced by $\Omega Z_{n}$ gives the second isomorphism.
:::

:::

::: {.pf-step #loopspace}
$\pi_{j}(\Omega Z_{n})=\pi_{j+1}(Z_{n})$ naturally in $n$.

::: pf-proof
A based loop in $\Omega Z_{n}$ is a based map $S^{1}\to\Omega Z_{n}$; under the adjunction between maps $S^{1}\to\operatorname{Map}(S^{j},Z_{n})$ and maps $S^{1}\wedge S^{j}\to Z_{n}$, based homotopy classes on the left correspond to elements of $\pi_{1}(S^{j}\wedge S^{1},*)=\pi_{j+1}(Z_{n})$. The correspondence is natural in $Z_{n}$, hence compatible with the maps $i_{n}$.
:::

:::

::: {.pf-step #isomorphism}
$\kappa_{*}\colon\pi_{j}(T_{\Omega})\to\pi_{j}(\Omega T)$ is an isomorphism for every $j\geq0$.

::: pf-proof
Both sides are identified with $\varinjlim_{n}\pi_{j+1}(Z_{n})$: the left by steps [](#limitpi){.pf-ref} and [](#loopspace){.pf-ref}, the right by step [](#limitpi){.pf-ref} with $Z_{n}$ in place of $\Omega Z_{n}$ and $\pi_{j}(\Omega T)=\pi_{j+1}(T)$, again by step [](#loopspace){.pf-ref}. Under these identifications $\kappa_{*}$ carries the class of the stage-$n$ loop $\omega$ to the class of the same loop viewed in $T$, which is exactly the structure map of the direct limit; so $\kappa_{*}$ is the identity on the direct limit.
:::

:::

::: {.pf-step #components}
$\kappa$ induces a bijection on path components.

::: pf-proof
The argument of steps [](#compact){.pf-ref} and [](#limitpi){.pf-ref} with $j=0$ and unbased maps gives $\pi_{0}(T)\cong\varinjlim_{n}\pi_{0}(Z_{n})$ and $\pi_{0}(T_{\Omega})\cong\varinjlim_{n}\pi_{0}(\Omega Z_{n})$ as sets, and $\pi_{0}(\Omega Z)\cong\pi_{1}(Z)$; the induced map on $\pi_{0}$ is again the identity of the direct limit.
:::

:::

::: {.pf-step}
$\kappa\colon\operatorname{hocolim}\Omega Z_{n}\to\Omega\operatorname{hocolim}Z_{n}$ is a weak homotopy equivalence.

::: pf-proof
By steps [](#isomorphism){.pf-ref} and [](#components){.pf-ref} $\kappa_{*}$ is an isomorphism on $\pi_{j}$ for every $j\geq0$ and a bijection on path components; that is the definition of a weak homotopy equivalence.
:::

:::

:::

:::
