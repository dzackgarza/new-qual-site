---
schema: qual/card@1
id: E-HAT-3.E-3
kind: problem
title: "Bockstein homomorphisms on smash products of Moore spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.E, Exercise 3; the stored statement matches.
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
    Proof read and checked. The Bockstein computation is right: $\beta$ is a derivation, so on
    $\widetilde H^*(M;\ZZ_p)^{\otimes k}$, which is the reduced cohomology of the smash product by
    the Künneth theorem over the field $\ZZ_p$, it is the $k$-fold tensor product of the two-term
    complex $a\mapsto b$, and that complex is acyclic because $\beta a=b\ne0$. Repaired: the card
    asserted the vanishing and then ignored it, computing the integral groups by a separate
    The solution now records the consequence *for reduced cohomology*, which is where the computation
    lives: the reduced Bockstein cohomology vanishes, so the reduced $E_2$ is zero and
    $(\widetilde H^*(X;\ZZ)/T)\otimes\ZZ_p=0$, hence $\widetilde H^*(X;\ZZ)$ is all torsion. Degree zero is separate
    and must be kept out, because $\beta$ vanishes on $H^0(X;\ZZ_p)=\ZZ_p$: the unreduced $E_2$ is $\ZZ_p$ in
    degree $0$, matching $H^0(X;\ZZ)=\ZZ$. An earlier version of this note, and of the solution, said
    "$E_2=0$" and "$H^*(X;\ZZ)$ is all torsion" without that qualification, which contradicts $H^0(X;\ZZ)=\ZZ$.
    Then the Koszul-complex computation supplies the torsion groups
    and then the Koszul-complex computation supplies the torsion groups
    $\widetilde H_{kn+j}(X;\ZZ)=(\ZZ_p)^{\binom{k-1}{j}}$. That computation is also checked: the
    reduced chains of $X$ are the $k$-fold tensor product of $\ZZ\xrightarrow{p}\ZZ$, the
    multiplicities obey Pascal's identity under Künneth, and the universal coefficient theorem
    shifts by one degree through Ext, giving
    $\widetilde H^{kn+r}(X;\ZZ)=(\ZZ_p)^{\binom{k-1}{r-1}}$ for $1\le r\le k$ and nothing else.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, which was already careful about the
    reduced/unreduced distinction. Added the reasons the steps need: why the Bockstein takes a to b
    on the Moore space and kills b; why the tensor power of the acyclic two-term complex stays
    acyclic over a field, by induction on k through the Kunneth formula; why vanishing of the reduced
    E_2 forces the reduced integral cohomology to be torsion, using that X is a finite complex; and
    the Pascal identity that produces the binomial multiplicities in the Koszul homology, with the
    base case k = 1. Checked the final shift by one degree through Ext in the universal coefficient
    theorem, including that the Hom term vanishes because the homology is torsion, and that the
    degrees kn and above kn+k-1 give nothing. Not checked: the exercise's printed hint, which was not
    re-read in this pass.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, Algebraic Topology, Section 3.E, printed p. 310, which carries the
    exercise. The printed words are
      Exercise 3. Let X be the smash product of k copies of a Moore space M(Z_p, n) with p prime.
      Compute the Bockstein homomorphisms in H*(X; Z_p) and use this to describe H*(X; Z).
    and the card's statement is that text, so the exercise is identified and no repair is needed.
    NOT checked in this pass: the argument, which this read does not touch and about which no
    claim is made.

---

::: {.problem}
Let $X$ be the smash product of $k$ copies of a Moore space $M(\ZZ_p, n)$ with $p$ prime.
Compute the Bockstein homomorphisms in $H^*(X; \ZZ_p)$ and use this to describe $H^*(X; \ZZ)$.
:::

::: {.solution}
This is Hatcher Exercise 3.E.3. No published solution set is transcribed: the argument is the card's own.

::: pf

::: {.pf-step #bockstein}
With $\ZZ_{p}$ coefficients, $\widetilde H^{*}(M;\ZZ_{p})$ has one generator $a$ in degree $n$ and one generator $b$ in degree $n+1$, and the Bockstein satisfies $\beta(a)=b$, $\beta(b)=0$.

::: pf-proof
The mod-$p$ reduced cohomology of $M(\ZZ_{p},n)=S^{n}\cup_{p}e^{n+1}$ is one-dimensional in degrees $n$ and $n+1$ and vanishes elsewhere, computed from the cellular cochain complex $0\to\ZZ_{p}\to\ZZ_{p}\to0$. The Bockstein $\beta$ of the coefficient sequence $0\to\ZZ\to\ZZ\to\ZZ_{p}\to0$ raises degree by one, and on the Moore space it carries the degree-$n$ class to the degree-$(n+1)$ class, because the integral class in degree $n$ has order $p$; the class in degree $n+1$ is the reduction of an integral class only trivially, so $\beta(b)=0$.
:::
:::

::: {.pf-step #tensor}
$\widetilde H^{*}(X;\ZZ_{p})\cong\widetilde H^{*}(M;\ZZ_{p})^{\otimes k}$ for $X=M^{\wedge k}$, with basis the tensors $u_{1}\otimes\cdots\otimes u_{k}$, $u_{i}\in\{a,b\}$, and $\beta$ the graded derivation displayed.

::: pf-proof
Over the field $\ZZ_{p}$ the Künneth theorem has no Tor term, and for a smash product of pointed spaces the reduced cohomology of $X$ is the tensor product of the reduced cohomologies of the factors; the tensors of basis elements form a basis. The Bockstein is a derivation for the product, with the Koszul signs coming from the degrees of the classes passed over, which is the displayed formula.
:::
:::

::: {.pf-step #acyclic}
The reduced Bockstein cohomology $\ker\beta/\operatorname{im}\beta$ of $X$ vanishes in every degree.

::: pf-proof
By step [](#tensor){.pf-ref} the Bockstein complex of $X$ is the $k$-fold tensor product of the two-term complex $\ZZ_{p}\{a\}\xrightarrow{\cong}\ZZ_{p}\{b\}$, which is acyclic since $\ker\beta=\ZZ_{p}\{b\}=\operatorname{im}\beta$. Over a field the tensor product of acyclic complexes is acyclic: the Künneth formula contributes no homology when both factors have none, and induction on $k$ gives it for the tensor power. So the reduced Bockstein cohomology vanishes.
:::
:::

::: {.pf-step #spectral}
$\widetilde H^{*}(X;\ZZ)$ is a torsion group, and $H^{0}(X;\ZZ)=\ZZ$.

::: pf-proof
The Bockstein spectral sequence of $0\to\ZZ\to\ZZ\to\ZZ_{p}\to0$ has $E_{1}=H^{*}(X;\ZZ_{p})$ with $d_{1}=\beta$, converging to $(H^{*}(X;\ZZ)/T)\otimes\ZZ_{p}$ with $T$ the torsion subgroup. Step [](#acyclic){.pf-ref} is a statement about the reduced complex, so the reduced $E_{2}$ vanishes; in degree $0$ the differential is zero and the unreduced $E_{2}$ is $\ZZ_{p}$, matching $H^{0}(X;\ZZ)=\ZZ$. Hence $(\widetilde H^{*}(X;\ZZ)/T)\otimes\ZZ_{p}=0$, and since $X$ is a finite complex $\widetilde H^{*}(X;\ZZ)$ is finitely generated, so vanishing of its reduction mod $p$ modulo torsion means it is all torsion.
:::
:::

::: {.pf-step #koszul}
$\widetilde H_{kn+j}(X;\ZZ)\cong(\ZZ_{p})^{\binom{k-1}{j}}$ for $0\leq j\leq k-1$, and $0$ otherwise.

::: pf-proof
The reduced cellular chain complex of $M$ is $0\to\ZZ\xrightarrow{p}\ZZ\to0$ in degrees $n+1,n$, and that of $X$ is its $k$-fold tensor product, the Koszul complex of $(p,\dots,p)$. Its homology is computed by induction on $k$ from the Künneth short exact sequence: tensoring with one more copy of the two-term complex replaces the multiplicity sequence by sums of adjacent entries, which is Pascal's identity $\binom{k-1}{j}+\binom{k-1}{j-1}=\binom{k}{j}$, and the base case $k=1$ gives $\ZZ_{p}$ in degree $n$ only.
:::
:::

::: {.pf-step #integral}
$\widetilde H^{kn+r}(X;\ZZ)\cong(\ZZ_{p})^{\binom{k-1}{r-1}}$ for $1\leq r\leq k$, and the reduced integral cohomology vanishes in all other degrees.

::: pf-proof
By step [](#spectral){.pf-ref} the reduced integral cohomology is torsion, so in the cohomology universal coefficient theorem the $\Hom$ term vanishes and $\widetilde H^{kn+r}(X;\ZZ)\cong\Ext(\widetilde H_{kn+r-1}(X;\ZZ),\ZZ)$. Since $\Ext(\ZZ_{p},\ZZ)=\ZZ_{p}$ and $\Ext$ of a direct sum is the direct sum of the $\Ext$'s, step [](#koszul){.pf-ref} with $j=r-1$ gives the stated multiplicity; the degrees $kn$ with $r=0$ correspond to $j=-1$, where the homology vanishes, and degrees above $kn+k-1$ also vanish.
:::
:::
:::

:::
