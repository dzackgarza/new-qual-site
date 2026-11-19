---
schema: qual/card@1
id: E-HAT-3.B-1
kind: problem
title: "Homology and cohomology of $\\RP^m \\times \\RP^n$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.B, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.B, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read and rechecked the formulas: with $H_p(\RP^r)$ free on $F_r$ and $\ZZ_2$ on $T_r$, Künneth
    gives $\ZZ^{f_i}$ for the free part and $(\ZZ_2)^{t_i}$ where the three tensor contributions
    and the shifted Tor contribution are counted separately; the integral cohomology then shifts
    the torsion count by one through $\operatorname{Ext}(\ZZ_2,\ZZ)=\ZZ_2$ and
    $\operatorname{Hom}(\ZZ_2,\ZZ)=0$, and over $\ZZ_2$ every differential vanishes so both
    theories are $(\ZZ_2)^{N_i}$ with $N_i$ the number of product cells of total dimension $i$.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Checked with Stanford Math 215C Solution Set 2, Hatcher 3.B.1, printed pp.3-4 (the p.5 text is
    about 3.B.3). Its even-parity chain complex decomposes into an edge column/row plus independent
    squares, and odd parity adds a column or row; the mod-2 cell count agrees with N_i here. It
    explicitly skips cohomology details, and the card's Z-cohomology formula is derived separately
    by universal coefficients rather than attributed to the set.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the retained Stanford solution set left as the
    source of the cellular-tensor computation and the mod-2 count, as the card already recorded.
    Re-checked: the one-cell-per-dimension complexes with boundary 0 and multiplication by 2 give
    Z in degrees F_r and Z_2 in degrees T_r; the product complex is the tensor complex with the
    Leibniz sign; Kueneth then contributes Z when both indices are in F, Z_2 when at least one is in
    T and neither is a vanishing index, and Tor(Z_2,Z_2)=Z_2 in total degree p+q+1=i; universal
    coefficients give H^i = Hom(H_i,Z) + Ext(H_{i-1},Z) = Z^{f_i} + (Z_2)^{t_{i-1}}; and over Z_2
    every differential is 2=0, so homology and cohomology are both the cell count. Added: the
    F_r/T_r bookkeeping as a step, the derivation of the one-factor homology from the complex, the
    term-by-term identification of the Kueneth summands, and the closed form
    N_i = max(0, min(m,i) - max(0,i-n) + 1). No defect found in the statement, §3.B Exercise 1.
---
---

::: {.problem}
Compute the groups $H_i(\RP^m \times \RP^n; G)$ and $H^i(\RP^m \times \RP^n; G)$ for $G = \ZZ$ and $\ZZ_2$ via the cellular chain and cochain complexes.
[See Example 3B.4.]
:::

::: {.solution}
The cellular-tensor computation and the mod-$2$ count are those of the retained published solution: **Stanford Math 215C, Solution Set 2**, Hatcher 3.B.1, printed pp. 3--4, held at `tmp/sources/stanford-math215c-spring2009-solution2.pdf`; that set decomposes the complex into a leftmost column, a bottom row and independent $2\times2$ squares with extra rows or columns for odd $m$ or $n$, and its mod-$2$ count is the cell count $N_i$ below. The set says it omits cohomology details, so the $\ZZ$-cohomology formula is derived here from the universal coefficient sequence.

::: pf

::: {.pf-step #complex}
$\RP^r$ has a CW structure with one cell $e_j$ in each dimension $0\le j\le r$, and cellular boundary $\partial e_j=0$ for $j$ odd and $\partial e_j=2e_{j-1}$ for $j$ even.

::: pf-proof
This is the standard cell structure, one cell in each dimension attached by the quotient map $S^{j-1}\to\RP^{j-1}$; the boundary is the degree of the attaching map, which is $0$ for $j$ odd and $2$ for $j$ even, the case $j=1$ being the collapse $S^0\to$ a point.
:::

:::

::: {.pf-step #tensor}
The product $\RP^m\times\RP^n$ has one cell $e_p\times e_q$ for each $0\le p\le m$, $0\le q\le n$, and its cellular chain complex is the tensor product of the two complexes with
$$
\partial(e_p\otimes e_q)=(\partial e_p)\otimes e_q+(-1)^pe_p\otimes(\partial e_q).
$$

::: pf-proof
A product of CW complexes has the product cells, and the cellular chain complex of a product is the tensor product of the factors' complexes, the differential being the Leibniz rule with the sign $(-1)^p$ coming from the degree of the first factor.
:::

:::

::: {.pf-step #one-factor}
For $r\ge0$ put $F_r=\{0\}\cup(\{r\}$ if $r$ is odd$)$ and $T_r=\{j:1\le j<r,\ j\ \text{odd}\}$. Then $H_p(\RP^r;\ZZ)$ is $\ZZ$ for $p\in F_r$, $\ZZ_2$ for $p\in T_r$, and $0$ otherwise.

::: pf-proof
With the complex of step [](#complex){.pf-ref}, the kernel of $\partial_p$ is generated by $e_p$ for $p$ odd and by $e_p$ and $2e_{p-1}$-multiples for $p$ even, and the image is generated by $2e_{p-1}$ for $p-1$ even; computing $H_p=\ker\partial_p/\operatorname{im}\partial_{p+1}$ gives $\ZZ$ in degree $0$ and in the top odd degree, $\ZZ_2$ in the intermediate odd degrees, and $0$ in the intermediate even degrees.
:::

:::

::: {.pf-step #kunneth}
$H_i(\RP^m\times\RP^n;\ZZ)\cong\ZZ^{f_i}\oplus(\ZZ_2)^{t_i}$, where
$$
f_i=\#\{(p,q)\in F_m\times F_n:p+q=i\},\qquad
t_i=\#\{(p,q)\in U_i\}+\#\{(p,q)\in T_m\times T_n:p+q+1=i\},
$$
with $U_i=\{(p,q):p+q=i,\ (p,q)\in(T_m\times F_n)\cup(F_m\times T_n)\cup(T_m\times T_n)\}$.

::: pf-proof
The Künneth formula applied to the tensor complex of step [](#tensor){.pf-ref} reads
$$
H_i\cong\bigoplus_{p+q=i}H_p(\RP^m)\otimes H_q(\RP^n)\ \oplus\bigoplus_{p+q=i-1}\operatorname{Tor}(H_p(\RP^m),H_q(\RP^n)).
$$
With the groups of step [](#one-factor){.pf-ref}, the tensor terms are $\ZZ$ when both indices lie in $F$ (counted by $f_i$) and $\ZZ_2$ when at least one lies in $T$ and neither index is a vanishing one (counted by the first part of $t_i$); the Tor terms are $\ZZ_2$ exactly when both indices lie in $T$, by $\operatorname{Tor}(\ZZ_2,\ZZ_2)=\ZZ_2$, and they sit in total degree $p+q+1=i$, which is the second part. All torsion is $2$-torsion, so the sum is a direct sum of copies of $\ZZ$ and $\ZZ_2$ as displayed.
:::

:::

::: {.pf-step #cohomology}
$H^i(\RP^m\times\RP^n;\ZZ)\cong\ZZ^{f_i}\oplus(\ZZ_2)^{t_{i-1}}$.

::: pf-proof
The universal coefficient theorem gives $H^i\cong\operatorname{Hom}(H_i,\ZZ)\oplus\operatorname{Ext}(H_{i-1},\ZZ)$. Since $\operatorname{Hom}(\ZZ,\ZZ)=\ZZ$, $\operatorname{Hom}(\ZZ_2,\ZZ)=0$ and $\operatorname{Ext}(\ZZ_2,\ZZ)=\ZZ_2$, this is $\ZZ^{f_i}\oplus(\ZZ_2)^{t_{i-1}}$: the free part of $H_i$ dualises, and the torsion of $H_{i-1}$ contributes the Ext term.
:::

:::

::: {.pf-step}
With $\ZZ_2$ coefficients, $H_i(-;\ZZ_2)\cong H^i(-;\ZZ_2)\cong(\ZZ_2)^{N_i}$ where $N_i=\#\{(p,q):0\le p\le m,\ 0\le q\le n,\ p+q=i\}$.

::: pf-proof
Over $\ZZ_2$ every differential of the complex of step [](#complex){.pf-ref} is zero, since each nonzero integral differential is multiplication by $2=0$ in $\ZZ_2$; the same holds for the tensor complex, whose differentials are built from those. So both the cellular chain and cochain complexes have one $\ZZ_2$ basis vector per cell and zero differentials, and homology and cohomology are both $(\ZZ_2)^{N_i}$ with $N_i$ the number of $i$-cells.
:::

:::

::: {.pf-step}
$\boxed{H_i\cong\ZZ^{f_i}\oplus(\ZZ_2)^{t_i},\quad H^i\cong\ZZ^{f_i}\oplus(\ZZ_2)^{t_{i-1}}\ \ (G=\ZZ);\qquad H_i\cong H^i\cong(\ZZ_2)^{N_i}\ \ (G=\ZZ_2)}$.

::: pf-proof
The two $\ZZ$-coefficient formulas are steps [](#kunneth){.pf-ref} and [](#cohomology){.pf-ref}, and the $\ZZ_2$-coefficient formula is the last step. Equivalently $N_i=\max(0,\min(m,i)-\max(0,i-n)+1)$, the number of pairs $(p,q)$ in the rectangle with $p+q=i$.
:::

:::

:::
:::
