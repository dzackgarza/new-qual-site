---
schema: qual/card@1
id: E-HAT-4.2-3
kind: problem
title: "Homotopy groups of punctured lens spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 3 (AT.txt 19336-19338) and correct as it stands. Verified
    each step: the preimage of the deleted point is one free G-orbit, so the universal cover is
    S^{2n+1} minus m points, which is homotopy equivalent to a wedge of m-1 copies of S^{2n}; Hurewicz
    applies since this is (2n-1)-connected; and the module is computed by equivariant Alexander duality
    as the reduced H^0 of the free G-set, which is Z[G]/Z.N. Checked the isomorphism Z[G]/Z.N = I_G
    directly: ker(t-1) on Z[G] is exactly Z.N, since (t-1)x = 0 forces all coefficients of x to be equal;
    so the displayed exact sequence is right and the answer I_G = (t-1)Z[G] is correct. Not checked:
    nothing outside this exercise.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Supplied the two identifications the
    prose used in a clause: that a sphere with m points removed is homotopy equivalent to a wedge of
    m-1 spheres of one dimension lower, here S^{2n}, and that the covering projection induces
    isomorphisms on pi_k for k >= 2 so that pi_{2n}(X) = pi_{2n}(X-tilde), together with the
    naturality that makes the Hurewicz identification one of Z[G]-modules. Also justified the
    computation of the kernel of multiplication by t-1 on Z[G] (an element fixed by t is a multiple
    of N) and that the image is I_G, and recorded that pi_1(X) = G because deleting a point from a
    manifold of dimension at least 3 changes nothing. The exercise was then located in the retained
    PDF at tmp/sources/hatcher-2002-algebraic-topology.pdf: it is Exercise 3 of section 4.2, printed
    p. 389 (PDF 398), and it prints the statement with no hint, so there is no printed hint for this
    card to have missed.

---

::: {.problem}
Let $X$ be obtained from a lens space of dimension $2n+1$ by deleting a point.
Compute $\pi_{2n}(X)$ as a module over $\ZZ[\pi_1(X)]$.
:::

::: {.solution}
This is Hatcher Exercise 4.2.3. No published solution set is transcribed: the argument is the card's own, and it is the computation Hatcher's Example after Theorem 4.2 suggests.

::: pf

::: {.pf-step #cover}
With $L^{2n+1}=S^{2n+1}/G$, $G\cong\ZZ_{m}$, and $X=L-\{x\}$, the universal cover of $X$ is $\widetilde X=S^{2n+1}-G\tilde x$, a sphere with $m$ points deleted, which is homotopy equivalent to a wedge of $m-1$ copies of $S^{2n}$.

::: pf-proof
The covering $S^{2n+1}\to L$ restricts over $X$ to a covering with fibre $G$, and the inverse image of the deleted point is the free orbit $G\tilde x$; so $\widetilde X=S^{2n+1}-G\tilde x$. A sphere with $m$ points removed deformation retracts onto a wedge of $m-1$ spheres of one dimension lower — each puncture contributes a sphere of dimension $2n+1-1=2n$ — so $\widetilde X\simeq\bigvee_{m-1}S^{2n}$, which is $(2n-1)$-connected.
:::
:::

::: {.pf-step #hurewicz}
$\pi_{2n}(X)\cong\ZZ^{m-1}$ as abelian groups, and $\pi_{2n}(X)\cong H_{2n}(\widetilde X)$ as $\ZZ[G]$-modules.

::: pf-proof
The covering map $\widetilde X\to X$ induces isomorphisms on $\pi_{k}$ for $k\geq2$, so $\pi_{2n}(X)\cong\pi_{2n}(\widetilde X)$ for $n\geq1$. Since $\widetilde X$ is $(2n-1)$-connected, Hurewicz gives $\pi_{2n}(\widetilde X)\cong H_{2n}(\widetilde X)$, and that group is $\ZZ^{m-1}$ because $\widetilde X\simeq\bigvee_{m-1}S^{2n}$. The identification is natural, hence compatible with the action of the deck group $G=\pi_{1}(X)$, which is what makes $\pi_{2n}(X)$ a $\ZZ[G]$-module isomorphic to $H_{2n}(\widetilde X)$.
:::
:::

::: {.pf-step #duality}
$H_{2n}(\widetilde X)\cong\widetilde H^{0}(G\tilde x)$ as $G$-modules, and $\widetilde H^{0}(G\tilde x)\cong\ZZ[G]/\ZZ N$ for $N=1+t+\cdots+t^{m-1}$.

::: pf-proof
Alexander duality in $S^{2n+1}$ for the finite set $A=G\tilde x$ gives $\widetilde H_{i}(S^{2n+1}-A)\cong\widetilde H^{2n+1-i-1}(A)$, so with $i=2n$ one gets $\widetilde H^{0}(A)$, and the duality is natural, hence $G$-equivariant. For a $G$-set $A$ one has $\widetilde H^{0}(A)=\ZZ^{A}/\ZZ$, the quotient of the free abelian group on $A$ by the constants; for $A=G$ acting freely, $\ZZ^{A}=\ZZ[G]$ and the constants span $\ZZ N$ with $N$ the sum of the group elements. So $\widetilde H^{0}(G\tilde x)\cong\ZZ[G]/\ZZ N$.
:::
:::

::: {.pf-step #ideal}
$\ZZ[G]/\ZZ N\cong I_{G}=\ker(\varepsilon\colon\ZZ[G]\to\ZZ)$, the augmentation ideal, as $\ZZ[G]$-modules.

::: pf-proof
With $\ZZ[G]=\ZZ[t]/(t^{m}-1)$, multiplication by $t-1$ has image exactly $I_{G}$, because $I_{G}$ is generated by $t-1$ and every element $(t-1)b$ has augmentation $\varepsilon(t-1)\varepsilon(b)=0$. Its kernel is $\ZZ N$: $N=(t^{m}-1)/(t-1)$ satisfies $(t-1)N=t^{m}-1=0$, and if $(t-1)b=0$ then $b$ is invariant under multiplication by $t$, hence a multiple of $N$. So there is an exact sequence $0\to\ZZ N\to\ZZ[G]\xrightarrow{t-1}I_{G}\to0$, and the first isomorphism theorem gives $\ZZ[G]/\ZZ N\cong I_{G}$.
:::
:::

::: {.pf-step #conclusion}
$\pi_{2n}(X)\cong I_{G}=(t-1)\ZZ[G]$ as a module over $\ZZ[\pi_{1}(X)]=\ZZ[G]$.

::: pf-proof
$\pi_{1}(X)=G$ since $X$ is a $(2n+1)$-manifold with $2n+1\geq3$ and deleting a point does not change the fundamental group of a manifold of dimension at least $3$. Combining steps [](#hurewicz){.pf-ref}, [](#duality){.pf-ref} and [](#ideal){.pf-ref} gives the isomorphism of $\ZZ[G]$-modules $\pi_{2n}(X)\cong I_{G}$, and $I_{G}$ is by construction the principal ideal $(t-1)\ZZ[G]$.
:::
:::
:::

:::
