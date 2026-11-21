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
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.2 Exercise 7, Theorem 4.8, the
    long exact sequence of a fibration, and the theory of G-CW complexes. Two defects repaired, both in
    the card's own framing rather than in its conclusion. First, the preamble justified replacing the
    product construction by saying that F = prod K(G_i,i) "does not have pi_i(F) = G_i" because
    K(G_j,j) has nontrivial homotopy above degree j. That is false: pi_i(K(G_j,j)) vanishes for i != j
    by the definition of an Eilenberg-MacLane space, and pi_i of a product is the product of the
    pi_i of the factors, so the product has exactly the prescribed groups. What the product fails to
    be is a CW complex, an infinite product of CW complexes with cells in unboundedly many dimensions
    being none, and a CW complex is what the cell attachments and the colimit require. The preamble now
    says that, and step `start` takes an equivariant CW approximation of the product instead of the
    product. Second, step `start` computed pi_k of the product as merely projecting onto G_k; it now
    records the exact identification pi_k = G_k as G_1-modules. Step `induction` notes that with such
    an F_0 the kernel it kills is trivial, so the machinery is stated for the general case and the
    construction completes at once. Steps `kill`, `colimit`, `borel` and `conclusion` are unchanged and
    correct: attaching a free orbit of (m+1)-cells kills a G_1-invariant normal closure without
    disturbing lower groups by cellular approximation, the colimit computes homotopy groups by
    compactness, and the Borel construction EG_1 x_{G_1} F has the stated fundamental group, homotopy
    groups and action. No page locator remains in the card text.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Independent referee read of the card's own construction, step by step against Hatcher,
    Algebraic Topology (2002), §4.2 Exercise 7, Theorem 4.8 and the long exact sequence of a
    fibration. Two defects repaired, both in a proof's justification, neither in the
    construction or in a step statement. (1) The proof of step `induction` claimed that the
    surjections onto $G_k$ for $k>m+1$ survive attaching the cells that kill the kernel in
    degree $m+1$, through a composite $\pi_k(F_{m+1})\to\pi_k(F_m)\twoheadrightarrow G_k$.
    No such map exists, the inclusion inducing $\pi_k(F_m)\to\pi_k(F_{m+1})$, and attaching
    $(m+2)$-cells can destroy classes in $\pi_k$ for $k\ge m+2$, so the claim is false for a
    starting space with excess; the solution block's sentence that the excess left by the
    approximation is killed in increasing degree is corrected with it, a weak equivalence
    leaving none. The proof is now the induction that shows no cell is ever
    attached: step `start` gives $\pi_k(F_0)\cong G_k$ in every degree, so the kernel at each
    stage is empty and $F_{m+1}=F_m$ serves. (2) The proof of step `borel` named the deck
    transformation $g\cdot(e,y)=(ge,y)$; that map sends $[e,y]$ to $[e,g^{-1}y]$, so it does
    not cover the identity of $EG_1\times_{G_1}F$ and is not a deck transformation, and the
    action it induces on $\pi_k(F)$ is trivial, which contradicts the step's conclusion. It
    now reads $g\cdot(e,y)=(ge,gy)$, which is equivariant for the diagonal action, covers the
    identity and induces the prescribed action. Steps `kill`, `start`, `colimit` and
    `conclusion` were read and are unchanged. Not checked: the existence of the equivariant
    CW approximation $F_0\to P$ in step `start`, which holds for a discrete group but is not
    a numbered statement of the book and is not built on the card. No retained solution set
    covers this exercise, so nothing here is transcribed.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Re-read against the numbered statements it cites. One citation defect repaired: the card used G-CW
    complexes, equivariant CW approximation and EG without saying that Hatcher does not treat them, so a
    reader would take them for the book's. The opening now states that this machinery is standard
    equivariant homotopy theory used on the card's own authority, and separates it from what the card
    does take from Hatcher — Theorem 4.8, the cellular approximation theorem, in the killing lemma, and
    the long exact sequence of a fibration in the last step, which is now cited there as Theorem 4.41
    rather than referred to as "the long exact sequence of the bundle". The mathematics is unchanged:
    the product has pi_i = G_i exactly, the equivariant approximation is a weak equivalence, the
    killing lemma attaches a free orbit of cells and leaves lower groups alone by Theorem 4.8, the
    colimit computes homotopy groups by compactness, and the Borel construction has the stated
    fundamental group, homotopy groups and action.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The last step applied Theorem 4.41, which is stated for fibrations, to a fiber bundle without saying
    why the bundle qualifies. Proposition 4.48 supplies exactly that: a fiber bundle has the homotopy
    lifting property with respect to all CW pairs, so over the CW base BG_1 the bundle F -> X -> BG_1 is a
    fibration in the sense Theorem 4.41 uses. The step now cites Proposition 4.48 for that, and nothing
    else changed.
---

::: {.problem}
Construct a CW complex $X$ with prescribed homotopy groups $\pi_i(X)$ and prescribed actions of $\pi_1(X)$ on the $\pi_i(X)$'s.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 7. No retained solution set covers this exercise, so the construction and its verification below are the card's own. It replaces the previous prose construction, which took $F=\prod_{i>1}K(G_i,i)$. That product does have the prescribed homotopy groups: $\pi_i$ of a product is the product of the $\pi_i$ of the factors, and $\pi_i(K(G_j,j))=0$ for $i\ne j$, so $\pi_i(F)=G_i$ exactly. What it is not is a CW complex: an infinite product of CW complexes carrying cells in unboundedly many dimensions is not one, and the construction here needs a CW complex, both to attach cells and to take the colimit. The repair is to replace the product by an equivariant CW approximation of it, which is a weak $G_1$-equivalence and so carries the same homotopy groups and the same action. A weak equivalence leaves no excess in any degree, so no cell is ever attached: the killing lemma is stated in general below, and the induction shows that its kernel is empty at every stage.

The equivariant machinery is not from Hatcher, who treats CW complexes and CW approximation without a group acting: $G$-CW complexes, their equivariant approximation, and $EG$ are standard material of equivariant homotopy theory, and the card uses them as such rather than citing them to the book. What the card does take from Hatcher is Theorem 4.8, the cellular approximation theorem, in the killing lemma, and the long exact sequence of a fibration, Theorem 4.41, in the last step.

Throughout, $G_1$ is a group, $G_i$ for $i>1$ is an abelian group with a homomorphism $\rho_i:G_1\to\operatorname{Aut}(G_i)$, and "prescribed action" means the action of $G_1$ on $\pi_i$ through $\rho_i$; $EG_1$ is a free contractible $G_1$-CW complex.

::: pf

::: {.pf-step #kill}
Let $X$ be a $G_1$-CW complex, $m\ge1$, and $A\subset\pi_m(X)$ a $G_1$-invariant set of classes whose normal closure $N(A)$ is $G_1$-invariant. Then there is a $G_1$-CW complex $X'\supset X$ with $\pi_m(X')=\pi_m(X)/N(A)$, with $\pi_k(X')\cong\pi_k(X)$ for $k\le m-1$, and with the $G_1$-action compatible with the isomorphism.

::: pf-proof
Choose a representative map $f_\alpha:S^m\to X$ for each class $\alpha\in A$ and attach a free $G_1$-orbit of $(m+1)$-cells along the maps $g\circ f_\alpha$ for $g\in G_1$; the result $X'$ is again a $G_1$-CW complex. Attaching an $(m+1)$-cell along $f_\alpha$ kills the class of $f_\alpha$ in $\pi_m$ and imposes no other relation, which is the procedure the book describes when it kills $\pi_{n+1}(S^n)$ by attaching $(n+2)$-cells; attaching the whole orbit kills the orbit of the class, and the classes killed generate $N(A)$ by construction, so $\pi_m(X')=\pi_m(X)/N(A)$. Since $N(A)$ is $G_1$-invariant, the quotient inherits the action. For the lower groups, a map $S^k\to X'$ and a homotopy of such maps can be pushed off the open $(m+1)$-cells when $k\le m-1$, by cellular approximation (Theorem 4.8), so the inclusion induces an isomorphism $\pi_k(X)\cong\pi_k(X')$ for $k\le m-1$; the action is transported along it because the inclusion is equivariant.

:::

:::

::: {.pf-step #start}
There is a simply connected $G_1$-CW complex $F_0$ with $\pi_k(F_0)$ mapping onto $G_k$ for every $k\ge2$, the map being a homomorphism of $G_1$-groups onto the prescribed module.

::: pf-proof
Take a $G_1$-CW model of $K(G_k,k)$ on which $G_1$ acts through $\rho_k$; such a model exists because $G_k$ is a $\ZZ[G_1]$-module by $\rho_k$, so an equivariant Moore space $M(G_k,k)$ with $\pi_k=G_k$ is built from a free $\ZZ[G_1]$-resolution of $G_k$ by attaching free orbits of $k$- and $(k+1)$-cells, and the remaining homotopy is then killed in higher degrees by step [](#kill){.pf-ref}. Let $P=\prod_{k\ge2}K(G_k,k)$ with the diagonal $G_1$-action, and let $F_0\to P$ be an equivariant CW approximation, which exists for a $G_1$-space and is a weak $G_1$-equivalence. For a product of spaces, $\pi_k$ of the product is the product of the $\pi_k$ of the factors (a map into a product is a tuple of maps), and $\pi_k(K(G_j,j))=0$ for $j\ne k$, so $\pi_k(P)=\pi_k(K(G_k,k))=G_k$; the identification is $G_1$-equivariant because the action on $P$ is diagonal and the action on the $k$th factor is $\rho_k$. Since $F_0\to P$ is a weak equivalence inducing isomorphisms of homotopy groups compatible with the $G_1$-action, $\pi_k(F_0)\cong G_k$ as $G_1$-modules, and $\pi_1(F_0)=\pi_1(P)=\prod_{j\ge2}\pi_1(K(G_j,j))=0$. Being a $G_1$-CW approximation, $F_0$ is a $G_1$-CW complex.

:::

:::

::: {.pf-step #induction}
There is a chain $F_0\subset F_1\subset F_2\subset\cdots$ of $G_1$-CW complexes with: $\pi_k(F_m)=G_k$ for $2\le k\le m$ as $G_1$-modules, and $\pi_k(F_m)\twoheadrightarrow G_k$ a $G_1$-equivariant surjection for $k>m$.

::: pf-proof
Induction on $m$, with the stronger claim that $F_m$ may be taken equal to $F_0$ at every stage. The case $m=0$ is step [](#start){.pf-ref}, which gives $\pi_k(F_0)\cong G_k$ for every $k\ge2$. For the step, let $A\subset\pi_{m+1}(F_m)$ be the kernel of the map onto $G_{m+1}$; by the induction hypothesis $F_m=F_0$, and $\pi_{m+1}(F_0)\cong G_{m+1}$, so $A$ is empty. Step [](#kill){.pf-ref}, applied with $m+1$ in place of $m$, therefore attaches no cell and returns $F_{m+1}=F_m=F_0$. Then $\pi_k(F_{m+1})=G_k$ for $2\le k\le m+1$ and $\pi_k(F_{m+1})\cong G_k$ for $k>m+1$, the last because $F_{m+1}=F_0$ and step [](#start){.pf-ref} identifies $\pi_k(F_0)$ with $G_k$ in every degree; each of these isomorphisms is compatible with the $G_1$-action, by the induction hypothesis and by step [](#start){.pf-ref}.

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
$X$ is the total space of the fiber bundle $F\to X\to BG_1=K(G_1,1)$ associated to $EG_1\to BG_1$. A fiber bundle with CW base has the homotopy lifting property with respect to all CW pairs, by Proposition 4.48, so it is a fibration in the sense Theorem 4.41 needs, $BG_1$ being a CW complex. Its fibre is simply connected, so the long exact sequence of a fibration, Theorem 4.41, gives $\pi_1(X)\cong\pi_1(BG_1)=G_1$ and $\pi_k(X)\cong\pi_k(F)$ for $k\ge2$. The total space $EG_1\times F$ of the pullback over $EG_1$ is homotopy equivalent to $F$, hence simply connected, and it is the universal cover of $X$; its group of deck transformations is $G_1$, acting by $g\cdot(e,y)=(ge,gy)$, so the action of $\pi_1(X)$ on $\pi_k(X)=\pi_k(F)$ is the given action of $G_1$ on $\pi_k(F)$, which is $\rho_k$ by step [](#colimit){.pf-ref}.

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
