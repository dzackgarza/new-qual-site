---
schema: qual/card@1
id: E-HAT-1.3-32
kind: problem
title: "Covering spaces of CW complexes from 1-skeleton coverings"
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
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 32; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced all three assertions to the surjection pi_1(X^1) -> pi_1(X) and the subgroup/normalizer classification of covers.
---

Consider covering spaces $p: \tilde{X} \to X$ with $\tilde{X}$ and $X$ connected CW complexes, the cells of $\tilde{X}$ projecting homeomorphically onto cells of $X$.
Restricting $p$ to the 1-skeleton then gives a covering space $\tilde{X}^1 \to X^1$ over the 1-skeleton of $X$.
Show:

(a) Two such covering spaces $\tilde{X}_1 \to X$ and $\tilde{X}_2 \to X$ are isomorphic if the restrictions $\tilde{X}_1^1 \to X^1$ and $\tilde{X}_2^1 \to X^1$ are isomorphic.

(b) $\tilde{X} \to X$ is a normal covering space if $\tilde{X}^1 \to X^1$ is normal.

(c) The groups of deck transformations of the coverings $\tilde{X} \to X$ and $\tilde{X}^1 \to X^1$ are isomorphic, via the restriction map.


::: {.solution}
Choose a basepoint $x_0$ in the $0$-skeleton and write
\[
j:X^1\hookrightarrow X.
\]
Since $X$ is obtained from $X^1$ by attaching cells of dimension at least $2$,
\[
j_*:\pi_1(X^1,x_0)\twoheadrightarrow\pi_1(X,x_0)
\]
is surjective.

<1>1. If a connected cover $p:\widetilde X\to X$ corresponds to the subgroup
\[
H\le\pi_1(X,x_0),
\]
then its restricted $1$-skeleton cover corresponds to
\[
j_*^{-1}(H)\le\pi_1(X^1,x_0).
\]
::: {.proof}
A loop in $X^1$ lifts closed to $\widetilde X^1$ exactly when the same loop, viewed in $X$, lifts closed to $\widetilde X$.
By the lifting criterion for connected covers, this is exactly the condition that its class lie in $j_*^{-1}(H)$.
:::

<1>2. If the restricted covers
\[
\widetilde X_1^1\to X^1,
\qquad
\widetilde X_2^1\to X^1
\]
are isomorphic, then the full covers
\[
\widetilde X_1\to X,
\qquad
\widetilde X_2\to X
\]
are isomorphic.
::: {.proof}
Let $H_1,H_2\le\pi_1(X)$ be the subgroups corresponding to the two connected covers.
Isomorphism of the unpointed restricted covers means that
\[
j_*^{-1}(H_1)
\]
and
\[
j_*^{-1}(H_2)
\]
are conjugate in $\pi_1(X^1)$.
Applying the surjection $j_*$ shows that $H_1$ and $H_2$ are conjugate in $\pi_1(X)$.
The connected-covering classification therefore gives an isomorphism of the full covers.
This proves (a).
:::

<1>3. If the restricted cover $\widetilde X^1\to X^1$ is normal, then $\widetilde X\to X$ is normal.
::: {.proof}
Normality of the restricted cover means
\[
j_*^{-1}(H)\triangleleft\pi_1(X^1).
\]
Let $g\in\pi_1(X)$ and $h\in H$.
Choose lifts
\[
\hat g,\hat h\in\pi_1(X^1)
\]
with
\[
j_*(\hat g)=g,
\qquad
j_*(\hat h)=h,
\]
possible because $j_*$ is surjective.
Since $\hat h\in j_*^{-1}(H)$ and this subgroup is normal,
\[
\hat g\hat h\hat g^{-1}\in j_*^{-1}(H).
\]
Applying $j_*$ gives
\[
ghg^{-1}\in H.
\]
Thus $H\triangleleft\pi_1(X)$, so the full cover is normal.
This proves (b).
:::

<1>4. Restriction gives an injective homomorphism
\[
\operatorname{Deck}(\widetilde X/X)
\longrightarrow
\operatorname{Deck}(\widetilde X^1/X^1).
\]
::: {.proof}
A deck transformation preserves cells and hence restricts to the $1$-skeleton.
If its restriction is the identity, then it fixes a point of the connected covering space $\widetilde X$.
A deck transformation of a connected cover is determined by the image of one point, so it is the identity.
:::

<1>5. The restriction homomorphism in <1>4 is surjective.
::: {.proof}
For the full cover corresponding to $H\le G=\pi_1(X)$,
\[
\operatorname{Deck}(\widetilde X/X)\cong N_G(H)/H.
\]
For the restricted cover, put
\[
G_1=\pi_1(X^1),
\qquad
H_1=j_*^{-1}(H).
\]
Then
\[
\operatorname{Deck}(\widetilde X^1/X^1)
\cong N_{G_1}(H_1)/H_1.
\]
Because $j_*:G_1\twoheadrightarrow G$ is surjective,
\[
j_*^{-1}(N_G(H))=N_{G_1}(H_1).
\]
Indeed, conjugating $H_1$ into itself is equivalent after applying $j_*$ to conjugating $H$ into itself, and the reverse implication follows from taking preimages under $j_*$.
Therefore $j_*$ induces an isomorphism
\[
N_{G_1}(H_1)/H_1
\xrightarrow{\sim}
N_G(H)/H,
\]
which is exactly the deck transformation obtained by extending a deck transformation from the $1$-skeleton.
Thus restriction is surjective.
:::

<1>6. Hence the deck groups of the two covers are naturally isomorphic.
::: {.proof}
Combine <1>4 and <1>5.
This proves (c).
:::
:::
