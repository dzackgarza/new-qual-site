---
schema: qual/card@1
id: E-HAT-4.2-7
kind: problem
title: "CW complexes with prescribed homotopy groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 7; the stored statement matches.
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
    Proof read against Hatcher Sec. 4.2 Exercise 7 (AT.txt 19354-19355) and correct as it stands. The Borel
    construction EG_1 x_{G_1} F is the right device: it is a fibre bundle over K(G_1,1) with simply
    connected fibre F = prod_{i>1} K(G_i,i), so the long exact sequence gives pi_1(X) = G_1 and
    pi_i(X) = G_i for i>1; the universal cover is EG_1 x F, which is homotopy equivalent to F, and the
    deck transformation by g acts on pi_i through rho_i(g) by construction. Checked that the prescribed
    G_i must be abelian for i>1, which the card states, and that functorial Eilenberg-MacLane models
    supply the G_1-action. Not checked: any construction of the functorial models, which is standard and
    cited rather than built. Nothing outside this exercise.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof, with one repair of the mathematics. The prose
    took $F=\prod_{i>1}K(G_i,i)$ and asserted $\pi_i(F)\cong G_i$; that is false, since
    $K(G_j,j)$ has nonzero homotopy above degree $j$, so $\pi_i(F)$ is the whole product and
    is strictly larger than $G_i$ in general. The card now starts from that product, notes
    the surjection onto $G_k$, and kills the excess in increasing degree by equivariant
    attachment of cells, an induction whose two lemmas (the effect of attaching cells on
    $\pi_m$, and the invariance of $\pi_k$ for $k\le m-1$ under cellular approximation) are
    stated and justified; the colimit then has $\pi_k=G_k$ with the prescribed action, and the
    Borel construction over $K(G_1,1)$ gives the complex. Cited: Theorem 4.8 printed p. 349
    for cellular approximation, the killing procedure described on printed p. 403, the bundle
    sequence on printed p. 376, and the exercise on printed p. 389. Not claimed: a retained
    solution set, so the construction is the card's own.
---

::: {.problem}
Construct a CW complex $X$ with prescribed homotopy groups $\pi_i(X)$ and prescribed actions of $\pi_1(X)$ on the $\pi_i(X)$'s.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 7, printed p. 389. No retained solution set covers this exercise, so the construction and its verification below are the card's own. It replaces the previous prose construction, which took $F=\prod_{i>1}K(G_i,i)$; that product does **not** have $\pi_i(F)=G_i$, because $K(G_j,j)$ has nontrivial homotopy above degree $j$, so $\pi_i(F)=\prod_{j}\pi_i(K(G_j,j))$ is strictly larger than $G_i$ in general. The excess is killed here, in increasing degree, and the killing is done equivariantly so that the prescribed $\pi_1$-action survives.

Throughout, $G_1$ is a group, $G_i$ for $i>1$ is an abelian group with a homomorphism $\rho_i:G_1\to\operatorname{Aut}(G_i)$, and "prescribed action" means the action of $G_1$ on $\pi_i$ through $\rho_i$; $EG_1$ is a free contractible $G_1$-CW complex.

::: pf

::: {.pf-step #kill}
Let $X$ be a $G_1$-CW complex, $m\ge1$, and $A\subset\pi_m(X)$ a $G_1$-invariant set of classes whose normal closure $N(A)$ is $G_1$-invariant. Then there is a $G_1$-CW complex $X'\supset X$ with $\pi_m(X')=\pi_m(X)/N(A)$, with $\pi_k(X')\cong\pi_k(X)$ for $k\le m-1$, and with the $G_1$-action compatible with the isomorphism.

::: pf-proof
Choose a representative map $f_\alpha:S^m\to X$ for each class $\alpha\in A$ and attach a free $G_1$-orbit of $(m+1)$-cells along the maps $g\circ f_\alpha$ for $g\in G_1$; the result $X'$ is again a $G_1$-CW complex. Attaching an $(m+1)$-cell along $f_\alpha$ kills the class of $f_\alpha$ in $\pi_m$ and imposes no other relation, which is the procedure the book describes when it kills $\pi_{n+1}(S^n)$ by attaching $(n+2)$-cells (printed p. 403); attaching the whole orbit kills the orbit of the class, and the classes killed generate $N(A)$ by construction, so $\pi_m(X')=\pi_m(X)/N(A)$. Since $N(A)$ is $G_1$-invariant, the quotient inherits the action. For the lower groups, a map $S^k\to X'$ and a homotopy of such maps can be pushed off the open $(m+1)$-cells when $k\le m-1$, by cellular approximation (Theorem 4.8, printed p. 349), so the inclusion induces an isomorphism $\pi_k(X)\cong\pi_k(X')$ for $k\le m-1$; the action is transported along it because the inclusion is equivariant.

:::

:::

::: {.pf-step #start}
There is a simply connected $G_1$-CW complex $F_0$ with $\pi_k(F_0)$ mapping onto $G_k$ for every $k\ge2$, the map being a homomorphism of $G_1$-groups onto the prescribed module.

::: pf-proof
Take a $G_1$-CW model of $K(G_k,k)$ on which $G_1$ acts through $\rho_k$; such a model exists because $G_k$ is a $\ZZ[G_1]$-module by $\rho_k$, so an equivariant Moore space $M(G_k,k)$ with $\pi_k=G_k$ is built from a free $\ZZ[G_1]$-resolution of $G_k$ by attaching free orbits of $k$- and $(k+1)$-cells, and the remaining homotopy is then killed in higher degrees by step [](#kill){.pf-ref}. Let $F_0=\prod_{k\ge2}K(G_k,k)$ with the diagonal $G_1$-action. For a product of spaces, $\pi_k$ of the product is the product of the $\pi_k$ of the factors (a map into a product is a tuple of maps), so $\pi_k(F_0)=\prod_{j\ge2}\pi_k(K(G_j,j))$, which projects onto the factor $\pi_k(K(G_k,k))=G_k$; the projection is $G_1$-equivariant because the action is diagonal and the factor action is $\rho_k$. Finally $\pi_1(F_0)=\prod_{j\ge2}\pi_1(K(G_j,j))=0$.

:::

:::

::: {.pf-step #induction}
There is a chain $F_0\subset F_1\subset F_2\subset\cdots$ of $G_1$-CW complexes with: $\pi_k(F_m)=G_k$ for $2\le k\le m$ as $G_1$-modules, and $\pi_k(F_m)\twoheadrightarrow G_k$ a $G_1$-equivariant surjection for $k>m$.

::: pf-proof
Induction on $m$. The case $m=0$ is step [](#start){.pf-ref}. For the step, let $A\subset\pi_{m+1}(F_m)$ be the kernel of the surjection onto $G_{m+1}$; it is a $G_1$-invariant subset, and its normal closure is a $G_1$-invariant subgroup, so step [](#kill){.pf-ref} applies with $m+1$ in place of $m$ and produces $F_{m+1}$ with $\pi_{m+1}(F_{m+1})=G_{m+1}$ and $\pi_k(F_{m+1})\cong\pi_k(F_m)$ for $k\le m$. Those isomorphisms give $\pi_k(F_{m+1})=G_k$ for $2\le k\le m$, and the surjections onto $G_k$ for $k>m+1$ survive because the composite $\pi_k(F_{m+1})\to\pi_k(F_m)\twoheadrightarrow G_k$ is still onto.

:::

:::

::: {.pf-step #colimit}
The colimit $F=\bigcup_m F_m$ is a simply connected $G_1$-CW complex with $\pi_k(F)\cong G_k$ as $G_1$-modules for every $k\ge2$.

::: pf-proof
Homotopy groups of a CW colimit are the colimit of the homotopy groups of the stages, because a map $S^k\to F$ and a homotopy of such maps have compact image and so land in some finite stage. For $m\ge k$ the group $\pi_k(F_m)$ is the fixed group $G_k$ by step [](#induction){.pf-ref}, so the colimit is $G_k$. Each stage is simply connected and the isomorphisms are equivariant, so $F$ is simply connected and the action on $\pi_k(F)=G_k$ is $\rho_k$.

:::

:::

::: {.pf-step #borel}
For a simply connected $G_1$-space $F$ with $\pi_k(F)\cong G_k$ as $G_1$-modules, the Borel construction $X=EG_1\times_{G_1}F$ satisfies $\pi_1(X)\cong G_1$, $\pi_k(X)\cong G_k$ for $k\ge2$, and the action of $\pi_1(X)$ on $\pi_k(X)$ is $\rho_k$.

::: pf-proof
$X$ is the total space of the fiber bundle $F\to X\to BG_1=K(G_1,1)$ associated to $EG_1\to BG_1$. Its fibre is simply connected, so the long exact sequence of the bundle (printed p. 376) gives $\pi_1(X)\cong\pi_1(BG_1)=G_1$ and $\pi_k(X)\cong\pi_k(F)$ for $k\ge2$. The total space $EG_1\times F$ of the pullback over $EG_1$ is homotopy equivalent to $F$, hence simply connected, and it is the universal cover of $X$; its group of deck transformations is $G_1$, acting by $g\cdot(e,y)=(ge,y)$, so the action of $\pi_1(X)$ on $\pi_k(X)=\pi_k(F)$ is the given action of $G_1$ on $\pi_k(F)$, which is $\rho_k$ by step [](#colimit){.pf-ref}.

:::

:::

::: {.pf-step #conclusion}
There is a CW complex $X$ with $\pi_1(X)=G_1$, $\pi_i(X)=G_i$ for $i>1$, and with $\pi_1(X)$ acting on $\pi_i(X)$ through $\rho_i$.

::: pf-proof
Step [](#colimit){.pf-ref} supplies $F$ and step [](#borel){.pf-ref} supplies $X=EG_1\times_{G_1}F$ with the required homotopy groups and actions; $X$ is a CW complex because $EG_1$ and $F$ are $G_1$-CW complexes and the Borel construction of a $G_1$-CW pair is a CW complex.

:::

:::

:::
:::
