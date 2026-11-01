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

---

::: {.problem}
Generalizing the example of $\RP^2$ and $S^2 \times \RP^\infty$, show that if $X$ is a connected finite-dimensional CW complex with universal cover $\tilde{X}$, then $X$ and $\tilde{X} \times K(\pi_1(X), 1)$ have isomorphic homotopy groups but are not homotopy equivalent if $\pi_1(X)$ contains elements of finite order.
:::

::: {.solution}
Put $G=\pi_1(X)$ and $Y=\widetilde X\times K(G,1)$. The first homotopy groups of $X$ and $Y$ are both $G$. For $n\ge2$, the covering map and the product formula give
$$
\pi_n(X)\cong\pi_n(\widetilde X)\cong\pi_n(Y).
$$
These are abstract group isomorphisms; they need not preserve the $G$-actions.

Suppose that $X\simeq Y$ and let $C_p\le G$ be a cyclic subgroup of prime order, obtained from an element of finite order. The homotopy equivalence induces an isomorphism $\pi_1(X)\to\pi_1(Y)=G$, so it carries $C_p$ to the cyclic subgroup $f_*(C_p)\le G$ of order $p$, and it lifts to a homotopy equivalence between the cover of $X$ corresponding to $C_p$ and the cover of $Y$ corresponding to $f_*(C_p)$; that subgroup is again cyclic of order $p$, so $K(f_*(C_p),1)\simeq K(C_p,1)$. The cover of $Y$ is
$$
\widetilde X\times K(f_*(C_p),1)\simeq\widetilde X\times K(C_p,1),
$$
whereas the corresponding cover $X_{C_p}$ of $X$ has the same finite CW dimension as $X$. Projection and inclusion make $K(C_p,1)$ a retract of the cover of $Y$. Hence its homology would be a direct summand of $H_*(X_{C_p};\ZZ)$ and would vanish above $\dim X$.

But the standard periodic resolution of the cyclic group gives
$$
H_{2k+1}(K(C_p,1);\ZZ)\cong\ZZ/p\qquad(k\ge0).
$$
This contradicts the finite dimension of $X_{C_p}$. Therefore $X$ and $Y$ are not homotopy equivalent.
:::
