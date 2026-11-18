---
schema: qual/card@1
id: E-UWGCC
kind: problem
title: The fundamental group of the torus via the circle covering
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 54: Problem 7 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-54-the-fundamental-group-of-the-circle/problem-7-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-54-the-fundamental-group-of-the-circle/problem-7-solution.txt), and against Munkres,
    Topology (2000), Section 54 Exercise 7, printed p. 348. dbFin gives the correspondence $\phi$ and says the product of two loops lifts to a path ending at the sum; the card writes out that $\phi$ is a well defined homomorphism, surjective (by the paths $(mt,nt)$) and injective (a lift that is a loop in the simply connected plane is nullhomotopic). Nothing needed repair.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for Munkres, Topology (2000), Section 54 Exercise 7, printed p. 348, generalising the proof of Theorem 54.5 (printed pp. 342-345); the correspondence and the lifting of a product of loops are dbFin's, "Section 54: Problem 7 Solution". Every clause of the prose is now a step with its justification, and three facts the prose used without argument are proved: that a product of two covering maps is a covering map, that the fibre over the basepoint is Z^2 (so the endpoint of a lift really lies in the target group), and that the lift of a concatenation is the first lift followed by a translate of the second, which is what makes Phi a homomorphism. Also made explicit: a lift of the constant path is constant, which is what forces the lifted homotopy to keep the basepoint fixed and makes Phi well defined. No statement repair.
---

::: {.exercise}

Generalize the proof of Theorem 54.5 to show that the fundamental group of the torus is isomorphic to the group $\ZZ \times \ZZ$.
:::

::: {.solution}
The argument is dbFin's, **dbFin, "Section 54: Problem 7 Solution"** (Munkres, *Topology*, Section 54, Problem 7), which gives the correspondence $\Phi$ and observes that a product of loops lifts to a path ending at the sum; the exercise is Munkres, *Topology* (2000), Section 54 Exercise 7, printed p. 348, and the proof being generalised is that of Theorem 54.5, printed pp. 342--345.

Write $T=S^1\times S^1$ and $p(s,t)=\bigl(e^{2\pi is},e^{2\pi it}\bigr)$, with basepoints $(1,1)\in T$ and $(0,0)\in\RR^2$.

::: pf

::: {.pf-step #covering}
$p:\RR^2\to T$ is a covering map and $\RR^2$ is simply connected.

::: pf-proof
$p$ is the product of the covering map $q:\RR\to S^1$, $q(s)=e^{2\pi is}$, with itself, and a product of two covering maps is a covering map: if $q^{-1}(U)=\bigsqcup_i U_i$ and $q^{-1}(V)=\bigsqcup_j V_j$ with $q$ restricting to a homeomorphism on each $U_i$ and on each $V_j$, then $p^{-1}(U\times V)=\bigsqcup_{i,j}U_i\times V_j$ and $p$ restricts to a homeomorphism on each $U_i\times V_j$. The space $\RR^2$ is convex, hence contractible, hence simply connected: for a loop $f$ the straight-line homotopy $(x,s)\mapsto(1-s)f(x)$ joins $f$ to a constant map.
:::

:::

::: {.pf-step #fibre}
$p^{-1}(1,1)=\ZZ^2$, and the unique lift of a loop $f$ at $(1,1)$ beginning at $(0,0)$ ends in $\ZZ^2$.

::: pf-proof
$p(s,t)=(1,1)$ exactly when $e^{2\pi is}=e^{2\pi it}=1$, that is $s,t\in\ZZ$. A loop $f$ is a path beginning at $(1,1)$, so by the path-lifting theorem its lift $\tilde f$ starting at $(0,0)$ satisfies $p\big(\tilde f(1)\big)=f(1)=(1,1)$, giving $\tilde f(1)\in\ZZ^2$. Lifts starting at a prescribed point exist and are unique because $p$ is a covering map and $\RR^2$ is simply connected (step [](#covering){.pf-ref}).
:::

:::

::: {.pf-step #welldefined}
$\Phi:\pi_1\big(T,(1,1)\big)\to\ZZ^2$, $\Phi([f])=\tilde f(1)$, is well defined.

::: pf-proof
Let $f\simeq g$ rel $\{0,1\}$ by $H:I\times I\to T$, and let $\widetilde H:I\times I\to\RR^2$ be the lift of $H$ with $\widetilde H(0,0)=(0,0)$, which exists by the homotopy lifting theorem. For fixed $s$ the path $t\mapsto\widetilde H(0,s)$ is a lift of the constant path at $(1,1)$, so it is constant; hence $\widetilde H(0,s)=(0,0)$ for all $s$. The path $t\mapsto\widetilde H(t,1)$ is then a lift of $g$ starting at $(0,0)$, so it equals $\tilde g$; therefore $\tilde f(1)=\widetilde H(1,0)=\widetilde H(1,1)=\tilde g(1)$. So $\Phi$ does not depend on the representative.
:::

:::

::: {.pf-step #homomorphism}
$\Phi([f]*[g])=\Phi([f])+\Phi([g])$.

::: pf-proof
Let $\tau_v$ denote translation of $\RR^2$ by $v\in\ZZ^2$. Since $p$ is $\ZZ^2$-periodic, $p\circ\tau_v=p$, so $\tau_v\circ\tilde g$ is a lift of $g$ beginning at $v$; hence the lift of the concatenation $f*g$, which begins at $(0,0)$, is $\tilde f$ followed by $\tau_{\tilde f(1)}\circ\tilde g$. Its endpoint is $\tilde f(1)+\tilde g(1)$, so $\Phi([f]*[g])=\tilde f(1)+\tilde g(1)$.
:::

:::

::: {.pf-step #surjective}
$\Phi$ is surjective.

::: pf-proof
For $(m,n)\in\ZZ^2$ let $\tilde f(t)=(mt,nt)$, a path from $(0,0)$ to $(m,n)$. Its projection $f=p\circ\tilde f$ is a loop at $(1,1)$ because $p(m,n)=(1,1)$ by step [](#fibre){.pf-ref}, and $\tilde f$ is the lift of $f$ starting at $(0,0)$ by uniqueness of lifts; so $\Phi([f])=(m,n)$.
:::

:::

::: {.pf-step #injective}
$\Phi$ is injective.

::: pf-proof
Suppose $\Phi([f])=(0,0)$, that is, $\tilde f$ is a loop at $(0,0)$. Since $\RR^2$ is simply connected (step [](#covering){.pf-ref}) there is a homotopy $\widetilde H:I\times I\to\RR^2$ from $\tilde f$ to the constant path at $(0,0)$, rel $\{0,1\}$. Then $p\circ\widetilde H$ is a homotopy rel $\{0,1\}$ from $p\circ\tilde f=f$ to the constant loop at $(1,1)$, so $[f]$ is the identity of $\pi_1\big(T,(1,1)\big)$; as $\Phi$ is a homomorphism (step [](#homomorphism){.pf-ref}) with trivial kernel, it is injective.
:::

:::

::: {.pf-step #conclusion}
$\pi_1(S^1\times S^1,(1,1))\cong\ZZ\times\ZZ$.

::: pf-proof
By steps [](#welldefined){.pf-ref}, [](#homomorphism){.pf-ref}, [](#surjective){.pf-ref} and [](#injective){.pf-ref}, $\Phi$ is an isomorphism of groups onto $\ZZ^2$.
:::

:::

:::
:::
