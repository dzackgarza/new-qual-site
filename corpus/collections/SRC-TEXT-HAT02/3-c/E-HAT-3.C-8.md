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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located, so the argument is the card's own. Re-read Hatcher's definition of a Hopf algebra in
    Section 3.C, printed p. 283, to fix what must be proved: conditions (1) connectedness and (2)
    a coproduct that is a homomorphism of graded algebras with the stated expansion and positive
    degrees, and explicitly no associativity, commutativity, counit or antipode. The steps follow
    that: the signed product and total grading; $(A x B)^0 = A^0 x B^0 = R$; the coproduct as the
    signed interchange after $(Delta_A x Delta_B)$; multiplicativity as a composite of algebra
    homomorphisms; then the expansion, where the nine products are enumerated and only the two
    with a factor $1 x 1$ are of degree zero on both sides, with the degenerate cases $|a|=0$ or
    $|b|=0$ handled separately. The last step keeps the earlier remark that the degree condition is
    not automatic, now with its reason: $R[x]$ with $Delta(x)=x x x$ is a connected graded algebra
    with an algebra-homomorphism coproduct that fails condition (2). Not claimed: any counit,
    antipode or associativity statement.
---

::: {.problem}
Show that the tensor product of two Hopf algebras is a Hopf algebra.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Hatcher's definition of a Hopf algebra in Section 3.C : a graded algebra with $A^0\cong R$ (connected) and a coproduct $\Delta:A\to A\otimes A$ that is a homomorphism of graded algebras with $\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha+\sum_i\alpha_i'\otimes\alpha_i''$ where $\abs{\alpha_i'}>0$ and $\abs{\alpha_i''}>0$ whenever $\abs{\alpha}>0$. Hatcher assumes neither associativity, commutativity, a counit nor an antipode, so none of them is proved here.

::: pf

::: {.pf-step #setup}
$A\otimes B$ is a graded algebra for the multiplication
$$
(a\otimes b)(a'\otimes b')=(-1)^{\gradeddegree{b}\gradeddegree{a'}}aa'\otimes bb' ,
$$
graded by total degree.

::: pf-proof
Bilinearity and the grading are immediate from the same properties in $A$ and $B$; the sign is the standard one for the tensor product of graded algebras, and it is exactly the formula Hatcher fixes for the multiplication in $A\otimes A$ in Section 3.C.
:::

:::

::: {.pf-step #connected}
$(A\otimes B)^0\cong R$.

::: pf-proof
The grading is by total degree, so $(A\otimes B)^0=A^0\otimes B^0$. Both algebras are connected, so $A^0\cong R\cong B^0$ as graded algebras, and $R\otimes_RR\cong R$. Hence the unit map $R\to(A\otimes B)^0$ is an isomorphism, which is condition (1).
:::

:::

::: {.pf-step #coproduct}
The formula
$$
\Delta_{A\otimes B}(a\otimes b)=\sum(-1)^{\gradeddegree{a_{(2)}}\gradeddegree{b_{(1)}}}(a_{(1)}\otimes b_{(1)})\otimes(a_{(2)}\otimes b_{(2)})
$$
defines a map $A\otimes B\to(A\otimes B)\otimes(A\otimes B)$, and it is the composite of $\Delta_A\otimes\Delta_B$ with the signed interchange of the middle two factors.

::: pf-proof
Write $\Delta_A(a)=\sum a_{(1)}\otimes a_{(2)}$ and $\Delta_B(b)=\sum b_{(1)}\otimes b_{(2)}$; $(\Delta_A\otimes\Delta_B)(a\otimes b)=\sum(a_{(1)}\otimes a_{(2)})\otimes(b_{(1)}\otimes b_{(2)})$ lies in $(A\otimes A)\otimes(B\otimes B)$. The interchange $(x\otimes x')\otimes(y\otimes y')\mapsto(-1)^{\gradeddegree{x'}\gradeddegree{y}}(x\otimes y)\otimes(x'\otimes y')$ is an isomorphism of graded modules onto $(A\otimes B)\otimes(A\otimes B)$, and composing with it gives the displayed sum with $x=a_{(1)}$, $x'=a_{(2)}$, $y=b_{(1)}$, $y'=b_{(2)}$.
:::

:::

::: {.pf-step #hom}
$\Delta_{A\otimes B}$ is a homomorphism of graded algebras.

:::: pf-proof

::: {.pf-step #factors}
$\Delta_A\otimes\Delta_B$ is a homomorphism of graded algebras $A\otimes B\to(A\otimes A)\otimes(B\otimes B)$, and the signed interchange is an isomorphism of graded algebras.

::: pf-proof
A tensor product of algebra homomorphisms is an algebra homomorphism for the signed multiplications of the tensor products, since the signs on the two sides are those of the respective middle factors and commute past one another. The signed interchange is invertible, with inverse again a signed interchange, and it is multiplicative: interchanging $(x\otimes x')$ past $(y\otimes y')$ multiplies by $(-1)^{\gradeddegree{x'}\gradeddegree{y}}$, and doing this on both sides of a product gives the same total sign because the multiplications in $A\otimes B$ carry exactly the signs $(-1)^{\gradeddegree{\text{right of first}}\,\gradeddegree{\text{left of second}}}$ of the widened product. This is the same computation Hatcher records when he notes that the multiplication in a tensor product of graded algebras is given by the signed formula.
:::

:::

::: {.pf-step}
$\Delta_{A\otimes B}$ is a homomorphism of graded algebras.

::: pf-proof
It is a composite of two homomorphisms of graded algebras by steps [](#coproduct){.pf-ref} and [](#factors){.pf-ref}, hence a homomorphism of graded algebras.
:::

:::

:::

:::

::: {.pf-step #degreecondition}
For $z\in A\otimes B$ of positive degree,
$$
\Delta_{A\otimes B}(z)=z\otimes1+1\otimes z+\text{(terms of positive degree in both factors)} .
$$

:::: pf-proof

::: {.pf-step #decomposable}
It suffices to prove this for $z=a\otimes b$ a homogeneous decomposable of positive total degree.

::: pf-proof
Both sides are linear in $z$, and the decomposables span $A\otimes B$.
:::

:::

::: {.pf-step #expand}
Expand the two coproducts using the Hopf-algebra condition in $A$ and in $B$.

::: pf-proof
By condition (2) in $A$ and in $B$,
$$
\Delta_A(a)=a\otimes1+1\otimes a+\sum_i a_i'\otimes a_i'',\qquad
\Delta_B(b)=b\otimes1+1\otimes b+\sum_j b_j'\otimes b_j'',
$$
where every $a_i',a_i''$ has positive degree when $\abs{a}>0$, and every $b_j',b_j''$ has positive degree when $\abs{b}>0$. Take $\abs{a}+\abs{b}>0$.
:::

:::

::: {.pf-step #multiply}
Multiplying out, and applying the signed interchange, leaves exactly two terms with a factor of degree zero; every other term is of positive degree on both sides.

::: pf-proof
The nine products of the displayed terms pair as follows. $(a\otimes1)\otimes(b\otimes1)$ becomes $(a\otimes b)\otimes1$ and $(1\otimes a)\otimes(1\otimes b)$ becomes $1\otimes(a\otimes b)$: these are the two terms whose second, respectively first, factor is $1\otimes1$, of degree zero. The mixed products $(a\otimes1)\otimes(1\otimes b)$ and $(1\otimes a)\otimes(b\otimes1)$ keep $a$ or $b$ on both sides, and each is of positive degree in both factors because $\abs{a}+\abs{b}>0$ and each side carries one of them. Every product involving an $a_i'$, an $a_i''$, a $b_j'$ or a $b_j''$ likewise has a positive-degree factor on both sides, since those elements have positive degree and appear on exactly one side each, and the remaining factor on the other side is either the same positive-degree element or a positive-degree $a$ or $b$. The Koszul signs are $\pm1$ and do not affect which factors are of positive degree.
:::

:::

::: {.pf-step #degenerate}
If $\abs{a}=0$ or $\abs{b}=0$ the formula still holds.

::: pf-proof
If $a\in A^0=R$ then $\Delta_{A\otimes B}(a\otimes b)=a\,\Delta_B(b)$ under the canonical identification, which is $a\otimes b\otimes1+1\otimes a\otimes b$ plus terms of positive degree in both factors, since $a$ has degree zero; symmetrically for $b\in B^0$. One of the two displayed sums then has a vanishing "pure" term of the corresponding shape, and the required form still holds because $\abs{a}+\abs{b}>0$.
:::

:::

:::

:::

::: {.pf-step #hopf}
$A\otimes B$ is a Hopf algebra.

::: pf-proof
Steps [](#setup){.pf-ref} and [](#connected){.pf-ref} give a graded algebra that is connected; steps [](#coproduct){.pf-ref} and [](#hom){.pf-ref} give a coproduct that is a homomorphism of graded algebras; and step [](#degreecondition){.pf-ref} gives the degree condition of Hatcher's definition (2). These are exactly the two conditions, so $A\otimes B$ is a Hopf algebra.
:::

:::

::: {.pf-step #notautomatic}
The degree condition is not a consequence of the other axioms, which is why it has to be transported.

::: pf-proof
On $A=R[x]$ with $x$ of even positive degree, $A^0=R$ and the algebra homomorphism specified by $\Delta(x)=x\otimes x$ makes $\Delta$ a homomorphism of graded algebras; but $\Delta(x)=x\otimes x$ has no term $x\otimes1$ or $1\otimes x$, so $A$ with that coproduct fails condition (2) of Hatcher's definition. Hence "algebra homomorphism plus connectedness" does not imply the degree condition, and the expansion of step [](#multiply){.pf-ref} is not redundant.
:::

:::

:::
:::
