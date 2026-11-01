---
schema: qual/card@1
id: E-HAT-3.C-8
kind: problem
title: Tensor product of Hopf algebras
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 8; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read. The signs are the ones the graded symmetry forces: $(-1)^{|b||a'|}$ in the
    product, $(-1)^{|a_{(2)}||b_{(1)}|}$ in the coproduct, and the Sweedler formula is the same
    map as the composite of $\Delta_A\otimes\Delta_B$ with the signed interchange of the middle
    factors, as the card says. That the coproduct is an algebra homomorphism for that reason is
    correct. The closing paragraph was repaired: it asserted that the degree-zero terms of the
    coproduct of a positive-degree element are $z\otimes1$ and $1\otimes z$ without displaying the
    expansion it appealed to, and that condition is not automatic — $\Delta(x)=x\otimes x$ on
    $R[x]$ is an algebra homomorphism with $A_0=R$ and violates it. The card now computes
    $(A\otimes B)_0=R$ and multiplies out the four products coming from the axioms for $A$ and
    $B$, which is what the assertion needs. Recorded, not verified: no counit and no antipode are
    treated, so the card proves the connected-graded-algebra form of the statement; if the
    definition in force includes an antipode it is $i_A\otimes i_B$ up to the sign $(-1)^{|a||b|}$,
    and that case is not checked here.
---

::: {.problem}
Show that the tensor product of two Hopf algebras is a Hopf algebra.
:::

::: {.solution}
Let $A$ and $B$ be graded Hopf algebras over the same commutative coefficient ring. Give $A\otimes B$ the usual graded tensor-product algebra structure
$$
(a\otimes b)(a'\otimes b')
=(-1)^{\gradeddegree{b}\gradeddegree{a'}}aa'\otimes bb'.
$$

Write the coproducts in Sweedler notation as
$$
\Delta_A(a)=\sum a_{(1)}\otimes a_{(2)},
\qquad
\Delta_B(b)=\sum b_{(1)}\otimes b_{(2)}.
$$
Define
$$
\Delta_{A\otimes B}(a\otimes b)
=
\sum (-1)^{\gradeddegree{a_{(2)}}\gradeddegree{b_{(1)}}}
(a_{(1)}\otimes b_{(1)})
\otimes
(a_{(2)}\otimes b_{(2)}).
$$
Equivalently, this is the composite
$$
A\otimes B
\xrightarrow{\Delta_A\otimes\Delta_B}
(A\otimes A)\otimes(B\otimes B)
\longrightarrow
(A\otimes B)\otimes(A\otimes B),
$$
where the second map interchanges the middle two factors with the Koszul sign.

The degree-zero part of $A\otimes B$ is the coefficient ring: the grading is by total degree, so $(A\otimes B)_0=A_0\otimes B_0=R\otimes_RR=R$.

The coproduct condition is where an expansion is needed, and it is not automatic. By the Hopf-algebra axiom in $A$ and in $B$,
$$
\Delta_A(a)=a\otimes1+1\otimes a+\sum_i a'_i\otimes a''_i,
\qquad
\Delta_B(b)=b\otimes1+1\otimes b+\sum_j b'_j\otimes b''_j,
$$
with every $a'_i,a''_i,b'_j,b''_j$ of positive degree. Composing $\Delta_A\otimes\Delta_B$ with the signed interchange and multiplying out, the four products of the displayed terms are
$$
(a\otimes1)\otimes(b\otimes1)=(a\otimes b)\otimes1,
\qquad
(1\otimes a)\otimes(1\otimes b)=1\otimes(a\otimes b),
$$
$$
(a\otimes1)\otimes(1\otimes b),
\qquad
(1\otimes a)\otimes(b\otimes1),
$$
and only the first two have a factor of degree zero. The last two, and every product involving an $a'_i$ or a $b'_j$, have a factor of positive degree on *both* sides. Hence
$$
\Delta_{A\otimes B}(a\otimes b)
=(a\otimes b)\otimes1+1\otimes(a\otimes b)+(\text{terms of positive degree in both factors}),
$$
which is the form the definition requires.

That the condition is not automatic is worth naming: on $R[x]$ the map $\Delta(x)=x\otimes x$, extended as an algebra homomorphism, has $A_0=R$ and is not of this form, so the higher-terms condition is part of the hypothesis and has to be transported, which is what the computation above does.

The displayed coproduct is an algebra homomorphism because it is the composite of $\Delta_A\otimes\Delta_B$, which is one, and the middle interchange with the Koszul sign, which is an algebra isomorphism for the signed multiplication of $A\otimes B$. That is where the signs in the product formula are used, and it is why they are there. Nothing in the verification uses a counit or an antipode: what is checked is the connected-graded form of the definition, $A_0=R$ together with a coproduct that is a homomorphism of graded algebras and introduces no terms of degree zero beyond $z\otimes1$ and $1\otimes z$.
:::
