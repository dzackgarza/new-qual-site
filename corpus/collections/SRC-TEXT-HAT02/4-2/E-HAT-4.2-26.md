---
schema: qual/card@1
id: E-HAT-4.2-26
kind: problem
title: "Isomorphic homotopy but different homotopy type"
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
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 26, printed p. 391,
    and Proposition 2.45, printed p. 146. The proof is Sam's, §4.2 Exercise 26, and is
    correct: pi_i(X~ x K(pi_1 X,1)) = pi_i(X) for i >= 2 and pi_1 = pi_1(X); a connected
    finite-dimensional CW complex has finitely many nonzero homology groups, while
    K(pi_1 X,1) is infinite dimensional when pi_1 has an element of finite order and its
    homology, being the group homology, is nonzero in infinitely many degrees. One slip of
    Sam's is not copied: he writes pi_i(X~) = pi_i(X) for i > 2 where i >= 2 is meant.
    Statement unchanged.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 26 (AT.txt 19423-19425) and repaired. The card said
    the homotopy equivalence X -> Y "lifts to a homotopy equivalence between the covers corresponding
    to C_p", which is false as stated: the equivalence induces an isomorphism pi_1(X) -> pi_1(Y) = G
    that need not fix the subgroup C_p, and the lifting criterion applies only with the source
    subgroup C_p and the target subgroup f_*(C_p). Since f_*(C_p) is again cyclic of prime order and
    K(f_*(C_p),1) is homotopy equivalent to K(C_p,1), the conclusion is unaffected; the card now
    names f_*(C_p) explicitly. Verified as correct and left unchanged: the pi_n comparison, the
    retract argument making H_*(K(C_p,1)) a direct summand of H_*(X_{C_p}), the vanishing above dim X,
    and the periodicity of H_odd(K(C_p,1);Z). Not checked: nothing outside this exercise.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 26, and against Sam's retained §4.2 Exercise 26. The prose
    contradicted itself: it said the argument below was Sam's and then that it was the card's own. It
    is the card's own, and the paragraph now says so, records that Sam's solution covers the exercise,
    and keeps the comparison. The mathematical content — equal homotopy groups, and no homotopy
    equivalence because a finite-dimensional CW complex has finitely many nonzero homology groups
    while $K(\pi_1(X),1)$ with torsion in $\pi_1(X)$ has infinitely many — reads correct.
---

::: {.problem}
Generalizing the example of $\RP^2$ and $S^2 \times \RP^\infty$, show that if $X$ is a connected finite-dimensional CW complex with universal cover $\tilde{X}$, then $X$ and $\tilde{X} \times K(\pi_1(X), 1)$ have isomorphic homotopy groups but are not homotopy equivalent if $\pi_1(X)$ contains elements of finite order.
:::

::: {.solution}
A retained solution covers this exercise: **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.2 Exercise 26**. The argument below is the card's own, not a transcription, and it agrees with that solution where the two overlap: the homotopy groups agree because the universal cover has the same $\pi_i$ for $i\ge2$ and $\pi_1(X)$ is recovered from $K(\pi_1(X),1)$; the two spaces cannot be homotopy equivalent because a connected finite-dimensional CW complex has only finitely many nonzero homology groups, while $K(\pi_1(X),1)$ for a group with an element of finite order is infinite dimensional (Proposition 2.45) and has infinitely many nonzero homology groups — its homology is the group homology of $\pi_1(X)$, whose torsion shows in infinitely many degrees.



The two spaces have the same homotopy groups, and a homotopy equivalence would make the homology of a finite-dimensional cover receive the periodic homology of $K(C_{p},1)$ as a direct summand.

Let $G=\pi_{1}(X)$, $p_{X}:\widetilde X\to X$ the universal cover, and $Y=\widetilde X\times K(G,1)$.

::: pf

::: {.pf-step #homotopy-groups}
$\pi_{n}(X)\cong\pi_{n}(Y)$ for all $n\ge0$.

::: pf-proof
For $n=1$ both are $G$: $\pi_{1}(X)=G$ by definition and $\pi_{1}(Y)=\pi_{1}(\widetilde X)\times\pi_{1}(K(G,1))=1\times G$. For $n\ge2$ the covering map $p_{X}$ induces an isomorphism $\pi_{n}(\widetilde X)\cong\pi_{n}(X)$, and the product formula gives $\pi_{n}(Y)=\pi_{n}(\widetilde X)\times\pi_{n}(K(G,1))=\pi_{n}(\widetilde X)$ because $K(G,1)$ has trivial higher homotopy groups. So the groups agree in every degree; these are isomorphisms of abstract groups and need not be compatible with the $G$-actions.
:::

:::

::: {.pf-step #subgroup}
If $X\simeq Y$ and $\pi_{1}(X)$ has an element of finite order, there is a subgroup $C_{p}\le G$ of order $p$ for some prime $p$, carried by the induced isomorphism to a subgroup $C'_{p}=f_{*}(C_{p})\le G$ of order $p$.

::: pf-proof
Let $g\in G$ have finite order $m>1$ and let $p\mid m$ be prime; then $g^{m/p}$ has order $p$ and generates a cyclic subgroup $C_{p}$ of order $p$. A homotopy equivalence $f:X\to Y$ induces an isomorphism $f_{*}:\pi_{1}(X)\to\pi_{1}(Y)=G$, so $f_{*}(C_{p})$ is a subgroup of order $p$, hence cyclic of order $p$.
:::

:::

::: {.pf-step #covers}
The cover $X_{C_{p}}$ of $X$ corresponding to $C_{p}$ and the cover $Y_{C'_{p}}$ of $Y$ corresponding to $C'_{p}$ are homotopy equivalent; $Y_{C'_{p}}\simeq\widetilde X\times K(C_{p},1)$, and $K(C_{p},1)$ is a retract of it; $X_{C_{p}}$ is a CW complex of dimension $\dim X$.

::: pf-proof
A homotopy equivalence lifts to a homotopy equivalence between the covers corresponding to subgroups matched by the induced isomorphism on $\pi_{1}$, so $X_{C_{p}}\simeq Y_{C'_{p}}$. The cover of $Y=\widetilde X\times K(G,1)$ corresponding to $C'_{p}$ is $\widetilde X\times K(C'_{p},1)$: the cover of a product is the product of the covers, and $K(G,1)$ is covered by $K(C'_{p},1)$ with $C'_{p}$ the image subgroup. Since $C'_{p}\cong C_{p}\cong\ZZ/p$, this is $\widetilde X\times K(C_{p},1)$. Choosing a point $x_{0}\in\widetilde X$, the inclusion $k\mapsto(x_{0},k)$ and the projection $(x,k)\mapsto k$ exhibit $K(C_{p},1)$ as a retract of $\widetilde X\times K(C_{p},1)$. Finally a covering space of a $d$-dimensional CW complex is a CW complex of dimension $d$, so $\dim X_{C_{p}}=\dim X<\infty$.
:::

:::

::: {.pf-step #contradiction}
$X$ and $Y$ are not homotopy equivalent.

::: pf-proof
Suppose $X\simeq Y$ and take $C_{p}$ as in step [](#subgroup){.pf-ref}. The homology of $K(C_{p},1)$ is a direct summand of that of $\widetilde X\times K(C_{p},1)$, because a retract induces a split injection on homology; transferring along the homotopy equivalence of step [](#covers){.pf-ref}, $H_{*}(K(C_{p},1);\ZZ)$ is a direct summand of $H_{*}(X_{C_{p}};\ZZ)$. Since $\dim X_{C_{p}}=\dim X<\infty$, its homology vanishes above $\dim X$. But the periodic free resolution of $\ZZ/p$ gives
$$
H_{2k+1}(K(C_{p},1);\ZZ)\cong\ZZ/p\ne0\qquad(k\ge0),
$$
in degrees tending to infinity, which cannot be a direct summand of a group vanishing above $\dim X$. So no homotopy equivalence exists:
$$
\boxed{X\not\simeq\widetilde X\times K(\pi_{1}(X),1)\ \text{whenever}\ \pi_{1}(X)\ \text{has an element of finite order}.}
$$
:::

:::

:::
:::
