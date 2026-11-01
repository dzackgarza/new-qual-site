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
    cellular argument, whereas the exercise asks to *use* the Bockstein. The solution now records
    the consequence — $E_2=0$ for the Bockstein spectral sequence, hence
    $(H^*(X;\ZZ)/T)\otimes\ZZ_p=0$ and $H^*(X;\ZZ)$ is all torsion, since $X$ is a finite complex —
    and then the Koszul-complex computation supplies the torsion groups
    $\widetilde H_{kn+j}(X;\ZZ)=(\ZZ_p)^{\binom{k-1}{j}}$. That computation is also checked: the
    reduced chains of $X$ are the $k$-fold tensor product of $\ZZ\xrightarrow{p}\ZZ$, the
    multiplicities obey Pascal's identity under Künneth, and the universal coefficient theorem
    shifts by one degree through Ext, giving
    $\widetilde H^{kn+r}(X;\ZZ)=(\ZZ_p)^{\binom{k-1}{r-1}}$ for $1\le r\le k$ and nothing else.
---

::: {.problem}
Let $X$ be the smash product of $k$ copies of a Moore space $M(\ZZ_p, n)$ with $p$ prime.
Compute the Bockstein homomorphisms in $H^*(X; \ZZ_p)$ and use this to describe $H^*(X; \ZZ)$.
:::

::: {.solution}
Let
$$
M=M(\ZZ_p,n).
$$
With $\ZZ_p$ coefficients, its reduced cohomology has one generator
$$
a\in\widetilde H^n(M;\ZZ_p)
$$
and one generator
$$
b\in\widetilde H^{n+1}(M;\ZZ_p),
$$
with Bockstein
$$
\beta(a)=b,
\qquad \beta(b)=0.
$$

For the smash product of $k$ copies,
$$
X=M^{\wedge k},
$$
the reduced Künneth theorem over the field $\ZZ_p$ gives
$$
\widetilde H^*(X;\ZZ_p)
\cong
\widetilde H^*(M;\ZZ_p)^{\otimes k}.
$$
A basis consists of tensors
$$
u_1\otimes\cdots\otimes u_k,
\qquad u_i\in\{a,b\}.
$$
The Bockstein is a graded derivation, hence
$$
\beta(u_1\otimes\cdots\otimes u_k)
=
\sum_{j=1}^k
(-1)^{\gradeddegree{u_1}+\cdots+\gradeddegree{u_{j-1}}}
 u_1\otimes\cdots\otimes\beta(u_j)\otimes\cdots\otimes u_k.
$$
Thus the Bockstein complex is the $k$-fold tensor product of the two-term complex
$$
\ZZ_p\{a\}\xrightarrow{\cong}\ZZ_p\{b\},
$$
which is acyclic: $\beta a=b\ne0$, so $\ker\beta=\ZZ_p\{b\}$ and $\operatorname{im}\beta=\ZZ_p\{b\}$. Over a field the tensor product of acyclic complexes is acyclic, by the Künneth formula, so the Bockstein cohomology $\ker\beta/\operatorname{im}\beta$ of $X$ vanishes in every degree.

That vanishing is what the exercise asks for, and it already answers half of the second question: the Bockstein spectral sequence of $X$ for the coefficient sequence $0\to\ZZ\to\ZZ\to\ZZ_p\to0$ has $E_1=H^*(X;\ZZ_p)$ and $d_1=\beta$, so $E_2=0$, and $E_1\Rightarrow(H^*(X;\ZZ)/T)\otimes\ZZ_p$ with $T$ the torsion subgroup. Since $X$ is a finite complex and $(H^*/T)\otimes\ZZ_p=(H^*/T)/p(H^*/T)=0$, a finitely generated $H^*(X;\ZZ)/T$ vanishes, i.e. $H^*(X;\ZZ)$ is all torsion. The chain computation that follows identifies which torsion.

To recover the integral groups explicitly, use cellular chains. The reduced cellular chain complex of $M$ is the two-term complex
$$
0\to\ZZ\xrightarrow{p}\ZZ\to0
$$
in degrees $n+1,n$. The reduced chain complex of $X$ is its $k$-fold tensor product, the Koszul complex for the sequence $(p,\dots,p)$. Its homology is
$$
\widetilde H_{kn+j}(X;\ZZ)
\cong(\ZZ_p)^{\binom{k-1}{j}},
\qquad 0\le j\le k-1,
$$
and zero in all other degrees. This follows inductively from the Künneth short exact sequence: tensoring with one more Moore complex replaces the multiplicities by adjacent sums, giving Pascal's identity.

All these homology groups are torsion, so the cohomology universal coefficient theorem shifts them up by one degree through Ext. Hence
$$
\boxed{
\widetilde H^{kn+r}(X;\ZZ)
\cong(\ZZ_p)^{\binom{k-1}{r-1}}
\quad(1\le r\le k),}
$$
and the reduced integral cohomology vanishes in all other degrees.
:::
