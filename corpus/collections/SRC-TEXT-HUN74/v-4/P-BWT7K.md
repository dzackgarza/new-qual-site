---
schema: qual/card@1
id: P-BWT7K
kind: problem
title: Galois correspondence for $(x^3-2)(x^2-3)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved UGA problem-set reproduction and an independent discussion explicitly identifying the problem as Hungerford's subgroup/intermediate-field exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section V.4,
    exercise 11, book page 277: "Determine all the subgroups of the Galois group
    and all of the intermediate fields of the splitting field (over Q) of the
    polynomial (x^3 - 2)(x^2 - 3) ∈ Q[x]." The card states exactly this. I
    recomputed the subgroup list from scratch: G = S_3 × C_2 has order 12, and
    writing a subgroup by its projection to S_3 gives, with graphs of
    homomorphisms P → C_2, ten subgroups, plus the four containing ε: ⟨ε⟩, the
    three ⟨τ_j, ε⟩, ⟨ρ, ε⟩ and G, for sixteen in total, matching the card's count
    of 1 + 7 + 1 + 3 + 3 + 1 rows. The involution count of seven, the unique
    order-3 subgroup, the three order-4 subgroups (no element of order 4 exists,
    and a subgroup of order 4 must contain ε because its projection has order 2),
    and the three index-2 kernels via G_ab = C_2 × C_2 all check. Each fixed field
    in the table was verified together with its degree against the subgroup
    index, including that τ_j inverts √-3 and ε inverts √3 so that τ_j ε fixes
    i = √-3/√3. Complete; no defect.
---

::: {.problem}
Determine all subgroups of the Galois group and all intermediate fields of the splitting field (over $\QQ$) of the polynomial $(x^{3}-2)(x^{2}-3)\in \QQ[x]$.
:::

::: {.solution}
Put
$$
a=\sqrt[3]{2},\qquad \zeta=e^{2\pi i/3},\qquad b=\sqrt3.
$$
The splitting field is
$$
L=\QQ(a,\zeta,b).
$$

::: pf

::: {.pf-step #s1}

One has
$$
\operatorname{Gal}(L/\QQ)\cong S_3\times C_2.
$$

::: pf-proof

Let
$$
M=\QQ(a,\zeta),
\qquad
N=\QQ(b).
$$
The field $M$ is the splitting field of $x^3-2$ and
$$
\operatorname{Gal}(M/\QQ)\cong S_3.
$$
Its unique quadratic subfield is the fixed field of $A_3$, namely
$$
\QQ(\sqrt{-3})=\QQ(\zeta).
$$
Since $N=\QQ(\sqrt3)$ is a different quadratic field,
$$
M\cap N=\QQ.
$$
Both extensions are Galois, so their compositum satisfies
$$
\operatorname{Gal}(L/\QQ)
\cong\operatorname{Gal}(M/\QQ)\times\operatorname{Gal}(N/\QQ)
\cong S_3\times C_2.
$$

Choose generators $\rho,\tau,\epsilon$ by
$$
\rho(a)=\zeta a,\quad \rho(\zeta)=\zeta,\quad \rho(b)=b,
$$
$$
\tau(a)=a,\quad \tau(\zeta)=\zeta^2,\quad \tau(b)=b,
$$
and
$$
\epsilon(a)=a,\quad \epsilon(\zeta)=\zeta,\quad \epsilon(b)=-b.
$$
Then
$$
\rho^3=\tau^2=\epsilon^2=1,
\qquad
\tau\rho\tau=\rho^{-1},
\qquad
\epsilon\rho=\rho\epsilon,
\qquad
\epsilon\tau=\tau\epsilon.
$$
For $j=0,1,2$, set
$$
a_j=\zeta^j a,
\qquad
\tau_j=\rho^j\tau\rho^{-j}.
$$
Thus $\tau_j$ is the transposition fixing $a_j$.

Also put
$$
i=\frac{\sqrt{-3}}{\sqrt3}\in L.
$$

:::

:::

::: {.pf-step #s2}

The complete subgroup list of $G=S_3\times C_2$ is
$$
\begin{array}{c|c|c}
\cardinality{H}&H&L^H\\
\hline
1&\{1\}&L\\[2mm]
2&\langle\epsilon\rangle&\QQ(a,\zeta)\\
2&\langle\tau_j\rangle&\QQ(a_j,b)\quad(j=0,1,2)\\
2&\langle\tau_j\epsilon\rangle&\QQ(a_j,i)\quad(j=0,1,2)\\[1mm]
3&\langle\rho\rangle&\QQ(\zeta,b)\\[1mm]
4&\langle\tau_j,\epsilon\rangle&\QQ(a_j)\quad(j=0,1,2)\\[1mm]
6&\langle\rho,\tau\rangle&\QQ(b)\\
6&\langle\rho,\epsilon\rangle&\QQ(\zeta)\\
6&\langle\rho,\tau\epsilon\rangle&\QQ(i)\\[1mm]
12&G&\QQ.
\end{array}
$$

::: pf-proof

We first verify that no subgroups are missing.

The involutions of $G$ are
$$
\epsilon,\quad \tau_0,\tau_1,\tau_2,
\quad \tau_0\epsilon,\tau_1\epsilon,\tau_2\epsilon,
$$
so there are exactly seven subgroups of order $2$.

The only elements of order $3$ are $\rho$ and $\rho^2$, giving the unique
subgroup $\langle\rho\rangle$ of order $3$.

If $H$ has order $4$, its projection to $S_3$ has order $2$, so the kernel of
that projection on $H$ has order $2$ and equals $\langle\epsilon\rangle$.
Therefore
$$
H=\langle\tau_j,\epsilon\rangle
$$
for exactly one $j$, giving the three subgroups of order $4$.

Every subgroup of order $6$ has index $2$, hence is the kernel of a nontrivial
homomorphism $G\to C_2$. Since
$$
G_{\mathrm{ab}}\cong C_2\times C_2,
$$
there are exactly three such kernels, namely
$$
\langle\rho,\tau\rangle,
\qquad
\langle\rho,\epsilon\rangle,
\qquad
\langle\rho,\tau\epsilon\rangle.
$$
Together with the trivial subgroup and $G$, this is the full subgroup list by
Lagrange's theorem.

It remains to verify the fixed fields in the table. The subgroup
$\langle\epsilon\rangle$ changes only $b$, so its fixed field is $M$.
The involution $\tau_j$ fixes $a_j$ and $b$, and the field
$\QQ(a_j,b)$ has degree $3\cdot2=6=[G:\langle\tau_j\rangle]$, hence is its
full fixed field.

Every transposition $\tau_j$ changes $\sqrt{-3}$ to its negative, while
$\epsilon$ changes $b=\sqrt3$ to its negative. Consequently
$\tau_j\epsilon$ fixes both $a_j$ and
$$
i=\frac{\sqrt{-3}}{\sqrt3}.
$$
The field $\QQ(a_j,i)$ has degree $6$, so it is exactly
$L^{\langle\tau_j\epsilon\rangle}$.

The subgroup $\langle\rho\rangle=A_3$ fixes $\zeta$ and $b$, and
$\QQ(\zeta,b)$ has degree $4$, so this is its fixed field. The subgroup
$\langle\tau_j,\epsilon\rangle$ fixes $a_j$, and $[\QQ(a_j):\QQ]=3$ is its
index, so $\QQ(a_j)$ is its fixed field.

Finally, the three index-$2$ subgroups correspond to the three quadratic
characters of $S_3\times C_2$. Their fixed fields are respectively
$$
\QQ(b)=\QQ(\sqrt3),
\qquad
\QQ(\zeta)=\QQ(\sqrt{-3}),
\qquad
\QQ(i),
$$
the last because $\tau\epsilon$ fixes the quotient
$\sqrt{-3}/\sqrt3=i$. The degree of each field equals the subgroup index, so
each displayed inclusion is the full fixed field.

:::

:::

::: pf-step

The table in step [](#s2){.pf-ref} gives all intermediate fields of $L/\QQ$.

::: pf-proof

The extension $L/\QQ$ is finite Galois by step [](#s1){.pf-ref}. The fundamental theorem of
Galois theory gives a bijection between its subgroups and its intermediate
fields via $H\mapsto L^H$. Since step [](#s2){.pf-ref} lists every subgroup and identifies its
fixed field, it lists every intermediate field exactly once.

:::

:::

:::

:::
