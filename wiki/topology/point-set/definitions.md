---
order: 1
topics:
- Point-Set Topology
- Topological Spaces
- Bases
- Closure
- Closed Sets
- Subspace Topology
- Product Topology
- Quotient Spaces
- Quotient Topology
- Order Topology
- Nets
- Countability
---

# Definitions

## Point-set topology

::: {.remark title="The prefix \"locally\""}
For a property $P$, \"locally $P$\" usually means that every $x\in X$ has some neighborhood with property $P$; some notions, such as local connectedness, instead require a neighborhood basis of sets with property $P$ at every point.
:::

[[D-Y6JAS]]

[[D-WKURJ]]

[[D-3KS2F]] [[D-2GCTV]] [[D-KW52R]]

[[D-YO6NZ]]

[[D-3KS2F]]

[[D-MVBYO]]

[[D-FAEYE]]

[[D-Q5272]] [[D-EILKJ]]

[[D-UI7ZL]]

[[D-METXE]]

[[D-ASXW6]]

[[D-L6SGU]]

[[D-AEAAD]]

[[D-AOJG3]]

[[D-KJBAK]] [[D-HS6DE]]

[[FD-AHIOS]] [[FD-IV5GM]]

[[FD-EQPN4]]

[[D-E2NWN]]

[[FD-3TS3M]]

[[D-ZFRV4]] [[D-BUAYX]]

[[D-3ZBXG]]

[[D-5VCMJ]]

[[D-D7AFV]]

[[FD-PMA24]]

[[D-GYBZ2]]

[[D-RZ7I3]] [[D-6JJJU]]

[[D-5EOQZ]]

[[FD-7R4QC]]

[[FD-ONITX]]

[[FD-2XUJ5]]

[[D-6JJJU]]

[[D-7JSLO]]

[[D-JMRPA]]

[[D-YEQC3]]

[[D-EMJTU]]

[[FD-QCNG5]] [[FD-TUK7H]]

[[D-CTGON]]

[[D-HQSEQ]] [[D-TNBFZ]]

[[D-W56JR]]

[[D-ITBUT]]

[[D-X73EB]]

[[D-VZFJQ]]

[[D-7ALR2]]

[[D-JKH35]] [[D-WHVXL]] [[D-MQSFD]]

[[D-C5THN]]

[[D-GDXFZ]]

[[D-P6XCN]]

[[D-EPTMG]]

[[D-NCLVD]]

::: {.remark}
If $r\colon X\to A$ is a retraction and $\iota\colon A\injects X$ the inclusion, then $r\circ\iota=\id_A$, so $\iota_*$ is injective on $\pi_1$ and on homology.
For every point $x_0$ of a space $X$, the constant map $X\to\ts{x_0}$ is a retraction.
:::

[[D-6FSWY]]

[[FD-6SR5I]]

[[D-KWWVL]]

[[D-3O6QH]]

[[FD-OQO2U]]

[[FD-DXTBN]]

[[D-23NTI]]

[[D-23NTI]]

[[D-LB2LS]]

[[D-RT2FT]]

[[D-4DXA7]]

::: {.example title="Counterexamples for separation axioms"}
\envlist

- Not $T_0$: the space $\ts{ f\colon\RR\to \CC\st \int_\RR \abs{f}^2 < \infty }$ with the topology of the seminorm $\norm{f}_2$, since two functions that agree almost everywhere have the same neighborhoods.

- $T_0$ but not $T_1$: $\spec R$ with the Zariski topology, for a commutative ring $R$ with a prime ideal that is not maximal.
  The closure of a point $\mathfrak p$ is $V(\mathfrak p)$, so the points of $\spec R \sm \mspec R$ are not closed.
:::
[[D-2TZAI]]

::: {.example}
An infinite intersection of open sets need not be open: in $\RR$, $\bigcap_{n\geq 1} (-1/n, 1/n) = \ts{0}$, which is closed and not open.
:::

[[D-OM7TD]]

[[D-BCNUH]]

[[D-WGYSB]]

## Analysis and metric spaces

[[D-B7CYY]]

[[D-D5G27]]

[[D-2GCTV]]

[[D-SDMMS]]

[[FF-VWKGM]]

## Algebraic topology

[[D-5KDNB]]

[[D-MVNSV]]

[[D-MLMIR]]

[[D-RQS4J]]

[[D-A3PUW]]

[[D-3IWX2]]

[[D-SYKQW]]

[[FD-QPIIL]]

[[D-VZS33]]

[[D-TD6AO]]

::: {.example title="Limits and colimits"}
\envlist

- Coproducts, pushouts, and direct limits are colimits; for example, $\ZZ[1/p]$ is the direct limit of $\ZZ\xrightarrow{\times p}\ZZ\xrightarrow{\times p}\cdots$.

- Products, pullbacks, and inverse limits are limits; for example, the $p$-adic integers $\ZZ_{p}$ are the inverse limit of $\cdots\to\ZZ/p^2\to\ZZ/p$.
:::

[[D-5MX7E]]

[[D-K43GA]]

[[D-COC6C]]

[[D-ANO2D]]

[[D-B2JER]]

::: {.example title="Applications of the cup product"}
On a closed oriented manifold, the cup product of the Poincaré duals of transversely intersecting closed oriented submanifolds is the Poincaré dual of their intersection.
$T^2$ and $S^2 \vee S^1 \vee S^1$ have isomorphic cohomology groups, and they are not homotopy equivalent: the cup product of the two degree-$1$ generators is nonzero for $T^2$ and zero for the wedge.
:::

[[D-ZOU5G]]

[[D-MMDM3]]

[[D-SI6OM]]

[[D-UH3L5]]

[[D-2O3N7]]

::: {.remark}
If $A\subseteq X$ is a deformation retract, then the inclusion $A\injects X$ is a homotopy equivalence.
Spaces $X$ and $Y$ are homotopy equivalent if and only if there is a space $Z$ containing both as deformation retracts; for a homotopy equivalence $f\colon X\to Y$, the mapping cylinder of $f$ is such a $Z$.
If $A$ and $B$ both deformation retract onto a common subspace $X$, then $A \homotopic X\homotopic B$.
:::

[[D-6UHU7]]

[[FD-BDEI2]] [[FD-COPFN]]

[[D-XC53X]]

[[D-LOISU]]

[[D-QK5BM]]

[[D-S7L6M]]

::: {.example title="A right exact functor"}
For a commutative ring $R$ and an $R$-module $M$, $\wait \tensor_{R} M$ is right exact, and it is exact if and only if $M$ is flat.
:::

[[D-455S6]]

[[D-2PNEG]]

[[D-JDDCP]]

[[D-WSFYS]]

[[D-TS7TZ]]

[[D-EBNUE]]

[[D-HRU62]]

[[D-Z7I7F]]

[[D-SOVXO]]

[[D-IZI3T]]

[[D-HFR32]]

[[D-KVAI3]]

[[D-EUX36]]

[[D-HOCNK]]

[[D-TK4QD]]

[[D-6POU4]]

[[D-VP4LC]]

[[D-GIUR3]]

[[D-3UY5O]]

[[D-UI3FE]]

[[D-ZVY6X]]

[[D-6CI7D]]

[[D-BNCTG]]

[[D-JW63I]]

[[D-UBWVX]]

[[D-MN6QW]]

[[D-FAIJX]]

[[D-6BK54]]

[[D-MEPE3]]

[[D-4QNEW]]

[[D-MWD2L]]

[[D-MGRZP]]

[[D-O5NN7]]

[[D-K5MLW]]

[[D-WX7JH]]

[[D-CNLBT]]

[[D-J6XOC]]

[[D-OISBB]]

[[D-QP7WI]]

[[D-YD6DR]]

[[D-Y6LXB]]

[[D-2XKM5]]

[[D-VUDRJ]]

[[D-EPQ54]]

[[FD-SW76G]]

[[D-SIUWU]]

[[D-NJ2Y6]]

[[D-RU2GC]]

[[D-GFM35]]

[[D-ZWLD5]]

[[D-R6LA3]]

[[D-6BUWA]]

[[D-BX3WD]]

[[D-QMJHY]]

[[D-2KICH]]

[[D-IGUUS]]

## Homotopy

[[D-II4M4]]

[[D-RZKQD]]

[[D-R4ZCL]]

[[D-KC4BS]]

[[D-TFVPD]]

[[D-RMQ7W]]

[[D-TPTOG]]

[[D-T5Q3V]]

[[D-MENR4]]

## Homological algebra

[[D-4VGLT]]

[[D-OKSJJ]]

[[D-DUCA5]]

[[D-3VEC5]]

[[D-I7D56]] [[D-M3Y6X]]

[[D-5KMYI]]

[[D-36ONS]]

[[D-D2K6Z]]

[[D-EILQL]]

[[D-MQTEG]]

[[D-OH4ON]]

[[D-4VGAW]]

[[D-6B77N]]

[[D-NODFN]]

[[D-XSBR2]]

[[D-TZSG2]]

[[D-STPAM]]

[[D-BYIZA]]

[[D-FS52P]]

[[D-WBM7M]]

[[D-FHUV5]]

[[D-7UFN3]]

[[D-QXER7]]

[[D-5RWYR]]

[[D-UEWPN]]

[[D-EGHL6]]

[[D-VWYRN]]

[[D-5S7PK]]

[[D-HWN6T]]

[[D-PKIY7]]
