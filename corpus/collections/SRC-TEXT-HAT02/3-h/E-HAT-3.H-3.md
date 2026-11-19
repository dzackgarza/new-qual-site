---
schema: qual/card@1
id: E-HAT-3.H-3
kind: problem
title: "Classification of group bundles via $B\\operatorname{Aut}(G)$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, which is complete. Split the two
    directions of the bundle-of-groups dictionary into a step for the correspondence with
    homomorphisms and a step identifying the ambiguity as conjugation in Aut(G), since the prose ran
    them together; recorded explicitly that pulling back composes monodromy with f_*, which is what
    makes the classifying map and f^*(E_0) correspond; and made the disconnected case a step, both
    sides splitting as products over the path components. Not checked: Hatcher's page numbers, which
    are the card's citations and were not re-read in this pass.
---

::: {.problem}
Let $\mathcal{B}(X; G)$ be the set of isomorphism classes of bundles of groups $E \to X$ with fiber $G$, and let $E_0 \to B\operatorname{Aut}(G)$ be the bundle corresponding to the "identity" action $\rho: \operatorname{Aut}(G) \to \operatorname{Aut}(G)$.
Show that the map $[X, B\operatorname{Aut}(G)] \to \mathcal{B}(X; G)$, $[f] \mapsto f^*(E_0)$, is a bijection if $X$ is a CW complex, where $[X, Y]$ denotes the set of homotopy classes of maps $X \to Y$.
:::

::: {.solution}
This is Hatcher Exercise 3.H.3. No published solution set is transcribed: the argument is the card's own. The numbered results are Hatcher's Theorem 1B.8 (p. 90), Proposition 1B.9 (p. 90), the classification of covering spaces (Theorem 1.38, p. 67), and the dictionary of §3.H (p. 331).

::: pf

::: {.pf-step #model}
$B\Aut(G)$ may be taken to be $K(\Aut(G),1)$ with $\Aut(G)$ discrete, and the bundle $E_{0}\to B\Aut(G)$ corresponding to the identity action is the universal bundle of groups with fibre $G$.

::: pf-proof
By Theorem 1B.8 (p. 90) the space $B\Gamma$ of a discrete group $\Gamma$ is a $K(\Gamma,1)$, whose homotopy type depends only on $\Gamma$. With $\Gamma=\Aut(G)$ acting on $G$ by the identity homomorphism, the associated bundle over $B\Gamma$ has fibre $G$ and total space $E\Gamma\times_{\Gamma}G$; running over the classifying map of any bundle of groups recovers it, which is what makes $E_{0}$ universal.
:::
:::

::: {.pf-step #dictionary}
For connected $X$ with a basepoint, isomorphism classes of bundles of groups $E\to X$ with fibre $G$ correspond to homomorphisms $\rho\colon\pi_{1}(X)\to\Aut(G)$ modulo conjugation in $\Aut(G)$; the correspondence sends $E$ to its monodromy $\rho_{E}$.

::: pf-proof
Such a bundle is in particular a covering space with fibre $G$, so the classification of covering spaces (§1.3, Theorem 1.38, p. 67 and the permutation description, pp. 68--70) applies: it is classified by the action of $\pi_{1}(X)$ on the fibre, which for a bundle of groups is an action by group automorphisms, that is a homomorphism $\rho\colon\pi_{1}(X)\to\Aut(G)$. Inverting this dictionary, the bundle with monodromy $\rho$ is $\widetilde{X}\times_{\pi_{1}(X)}G\to X$ with the deck group acting through $\rho$. The monodromy depends on the identification of the fibre with $G$: changing the identification by $c\in\Aut(G)$ replaces $\rho$ by $c\rho c^{-1}$, so the invariant of the bundle is the conjugacy class.
:::
:::

::: {.pf-step #isomorphisms}
An isomorphism between $\widetilde{X}\times_{\rho}G$ and $\widetilde{X}\times_{\rho'}G$ over $X$ exists exactly when $\rho'=c\rho c^{-1}$ for some $c\in\Aut(G)$.

::: pf-proof
An isomorphism over $X$ of bundles with fibre $G$ is a $\pi_{1}(X)$-equivariant family of group automorphisms of the fibre, hence a single element $c\in\Aut(G)$ satisfying $c\rho(\gamma)=\rho'(\gamma)c$ for every $\gamma\in\pi_{1}(X)$; that is $\rho'=c\rho c^{-1}$. Combined with step [](#dictionary){.pf-ref},
$$\mathcal{B}(X;G)\cong\Hom(\pi_{1}X,\Aut(G))/\text{conjugacy in }\Aut(G).$$
:::
:::

::: {.pf-step #maps}
For a connected CW complex $X$ there is a bijection $[X,B\Aut(G)]\cong\Hom(\pi_{1}X,\Aut(G))$ modulo conjugation.

::: pf-proof
$B\Aut(G)$ is a $K(\Gamma,1)$ with $\Gamma=\Aut(G)$ by step [](#model){.pf-ref}, so Proposition 1B.9 (p. 90) applies: every homomorphism $\pi_{1}(X)\to\Gamma$ is realised by a map $X\to B\Gamma$, and based maps inducing it are unique up to based homotopy. Dropping the basepoint allows translation of the image of the basepoint along a path in $B\Gamma$, which conjugates the induced homomorphism by the class of that path; since $\Gamma$ need not be abelian this is a genuine ambiguity, and it is the only one. So the unbased homotopy classes correspond to homomorphisms modulo conjugation.
:::
:::

::: {.pf-step #pullback}
Under the identifications of steps [](#isomorphisms){.pf-ref} and [](#maps){.pf-ref} the map $[f]\mapsto f^{*}(E_{0})$ is the identity on the quotient set, hence a bijection.

::: pf-proof
Pulling back a bundle of groups along $f$ composes the classifying monodromy with $f_{*}$: the bundle $f^{*}E_{0}$ has monodromy $\operatorname{id}_{\Gamma}\circ f_{*}=f_{*}$. Since the two sides of the required bijection are, by the two preceding steps, the same quotient set and the map between them acts as the identity there, it is a bijection.
:::
:::

::: {.pf-step #disconnected}
For a general CW complex $X$ the same map is a bijection.

::: pf-proof
Both $\mathcal{B}(X;G)$ and $[X,B\Aut(G)]$ split as products over the path components of $X$, and the map acts componentwise; each component is a connected CW complex, where steps [](#dictionary){.pf-ref} to [](#pullback){.pf-ref} apply. A product of bijections is a bijection.
:::
:::
:::

:::
