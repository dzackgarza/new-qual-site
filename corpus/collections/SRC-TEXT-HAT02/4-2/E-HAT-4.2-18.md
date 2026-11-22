---
schema: qual/card@1
id: E-HAT-4.2-18
kind: problem
title: "Wedge equals product for coprime homology"
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
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 18, printed p. 390,
    the Kunneth formula (printed p. 291) and Whitehead's theorem. The proof is correct:
    relatively prime finite orders kill the tensor and Tor terms of Kunneth, so
    H~_n(X x Y) = H~_n(X) + H~_n(Y), which is the image of H~_n(X v Y), so the inclusion
    is a homology isomorphism and, both spaces being simply connected CW complexes, a
    homotopy equivalence; then H~_*(X ^ Y) = 0 by the exact sequence of the pair and
    X ^ Y is simply connected, so it is contractible. The card's opening claim that no
    retained solution set covers the exercise was false: Sam's set does, at §4.2
    Exercise 18, and is now cited. Statement unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 18; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the smash-product computation and the conclusion, which is what Queue D asks for on this card. The reduced Kunneth description is now derived (the Kunneth theorem for the product plus the long exact sequence of the pair), the vanishing is argued from the cyclic case rather than asserted, and the two Whitehead applications name Corollary 4.33 on printed p. 367. No retained set covers this exercise; the card now says so. Locators checked: Theorem 3B.6 on printed p. 275, Corollary 4.33 on p. 367, the exercise on p. 390. No statement repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Item 8 of the current #163 repair split. Repaired the algebra: finite abelian groups
    decompose into prime-power cyclic summands, not prime-order ones. Every pair now uses
    $\ZZ_m\otimes\ZZ_n\cong\operatorname{Tor}(\ZZ_m,\ZZ_n)\cong\ZZ_{\gcd(m,n)}$ from
    §3.A, and $\ZZ/2\otimes\ZZ/4\cong\ZZ/2$ records why prime-order summands would be
    insufficient. The quotient computations were rechecked: the relative Künneth formula
    following Theorem 3B.6 applies directly to $(X,x_0)$ and $(Y,y_0)$, Proposition 2.22
    identifies its relative homology with reduced homology of the smash product, and
    Proposition 4.28 supplies simple connectivity of that quotient. The two conclusions
    still use Corollary 4.33, as in Sam's §4.2 Exercise 18, with these hypotheses made
    explicit.
---

::: {.problem}
If $X$ and $Y$ are simply-connected CW complexes such that $\tilde{H}_i(X)$ and $\tilde{H}_j(Y)$ are finite and of relatively prime orders for all pairs $(i, j)$, show that the inclusion $X \vee Y \hookrightarrow X \times Y$ is a homotopy equivalence and $X \wedge Y$ is contractible. [Use the Künneth formula.]
:::

::: {.solution}
A published solution covers this exercise: **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.2 Exercise 18**, which argues exactly this way — Künneth kills the mixed terms because the orders are relatively prime, the inclusion $X\vee Y\to X\times Y$ is then a homology isomorphism, and $X\wedge Y$ has vanishing reduced homology. The card's steps are that argument written out and checked against Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 18, with the Künneth formula of §3.B and Whitehead's theorem. (An earlier note on this card said no retained set covers the exercise; that was wrong — Proudfoot's Homework #7 is not the only §4.2 set in the checkout.)

::: pf

::: {.pf-step #kunneth}
The reduced homology of the smash product is built from the groups $\widetilde H_i(X;\ZZ)\otimes\widetilde H_j(Y;\ZZ)$ and $\operatorname{Tor}\bigl(\widetilde H_i(X;\ZZ),\widetilde H_j(Y;\ZZ)\bigr)$: $\widetilde H_k(X\wedge Y;\ZZ)$ is a direct sum of copies of those groups over the relevant index pairs.

::: pf-proof
Choose basepoints $x_0\in X$ and $y_0\in Y$. Since $X\wedge Y=(X\times Y)/(X\vee Y)$ and $(X\times Y,X\vee Y)$ is a CW pair, Proposition 2.22 gives $\widetilde H_k(X\wedge Y)\cong H_k(X\times Y,X\vee Y)$. Apply the relative Künneth formula stated immediately after Theorem 3B.6 to the pairs $(X,x_0)$ and $(Y,y_0)$. Its split short exact sequences express $H_k(X\times Y,X\times\{y_0\}\cup\{x_0\}\times Y)$, which is $H_k(X\times Y,X\vee Y)$, as a direct sum of tensor and Tor terms over $H_i(X,x_0)=\widetilde H_i(X)$ and $H_j(Y,y_0)=\widetilde H_j(Y)$, which is the claim.
:::

:::

::: {.pf-step #vanish}
Both kinds of term vanish, so $\widetilde H_k(X\wedge Y;\ZZ)=0$ for every $k$.

::: pf-proof
Decompose each finite abelian reduced homology group into prime-power cyclic summands. For arbitrary positive integers $m$ and $n$, the explicit formulas of §3.A give
$$
\ZZ_m\otimes\ZZ_n\cong\ZZ_{\gcd(m,n)},\qquad
\operatorname{Tor}(\ZZ_m,\ZZ_n)\cong\ZZ_{\gcd(m,n)}.
$$
The prime-power qualification is essential: $\ZZ/2\otimes\ZZ/4\cong\ZZ/2$, not $0$. Here, if one summand comes from $\widetilde H_i(X)$ and another from $\widetilde H_j(Y)$, their orders divide $\cardinality{\widetilde H_i(X)}$ and $\cardinality{\widetilde H_j(Y)}$ respectively, so their gcd is $1$ by the coprime-order hypothesis. Every tensor and Tor summand in step [](#kunneth){.pf-ref} therefore vanishes, and so does its direct sum.
:::

:::

::: {.pf-step #smash-contractible}
$X\wedge Y$ is contractible.

::: pf-proof
The wedge $X\vee Y$ is simply connected by van Kampen's theorem, Theorem 1.20, so the pair $(X\times Y,X\vee Y)$ is $1$-connected by its homotopy exact sequence. Proposition 4.28 with $r=s=1$ then gives $\pi_1(X\wedge Y)\cong\pi_1(X\times Y,X\vee Y)=0$. The smash product is a CW complex because it is the quotient of a CW pair by its subcomplex, and its reduced homology vanishes by step [](#vanish){.pf-ref}. Hence the map $X\wedge Y\to\ast$ is a homology isomorphism between simply connected CW complexes, and Corollary 4.33 makes it a homotopy equivalence.
:::

:::

::: {.pf-step #inclusion}
The inclusion $X\vee Y\hookrightarrow X\times Y$ is a homotopy equivalence.

::: pf-proof
The inclusion of a subcomplex is a cofibration with quotient $X\wedge Y$, so $H_*(X\times Y,X\vee Y)\cong\widetilde H_*(X\wedge Y)=0$ by step [](#smash-contractible){.pf-ref}: the inclusion induces an isomorphism on homology in every degree. Both spaces are simply connected CW complexes, so Corollary 4.33, applies and the inclusion is a homotopy equivalence. With the contractibility of $X\wedge Y$ this is the exercise.
:::

:::

:::
:::
