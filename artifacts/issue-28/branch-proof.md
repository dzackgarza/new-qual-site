# Topology subject branch: build proof

Manifest: `publications/topology-guide.yaml`. Built and inspected at `c6fa2be0`.

The captures are of `c6fa2be0`. `286c5cc3` came after them and removed three refs, so the
captures of `constructions-of-spaces`, `the-fundamental-group` and `covering-spaces` each
show one card the manifest no longer lists — `D-TNBFZ`, `D-EBNUE` and `T-F4PQY`. Reading
those three captures is what found the duplication, and the repository was under
continuous builds from the other subject lanes afterwards, which deleted and rebuilt
`build/quarto/_site` faster than a second inspection could be taken.

`uv run qualc build` -> 8,207 cards and 327 wiki pages OK.

## What had to happen first

The manifest could not be extended without classifying the subject. 1,981 Topology-area
cards carried `topics: []`, so six of the seven query panels had almost nothing to draw
on, and every term the algebraic half of the tree needs — homotopy, covering spaces,
homology, degree, duality — was absent from the registry entirely.

| | cards |
| --- | ---: |
| Topology-area cards with no topic at the start | 1,981 |
| of those, substantive kinds (definition, theorem, proposition, corollary, fact, example, exercise, problem) | 1,092 |
| read card-by-card and classified | 1,083 |
| left unclassified, listed below | 9 |
| occurrence cards, taking their canonical's topics | 809 |
| occurrence cards skipped, canonical unclassified | 5 |
| source cards, unclassified by corpus-wide convention | 75 |

Every assignment on the 1,083 was made by reading the card body. Commits `9b8524f6`,
`f6de61ab`, `65b926c5`, `66d6b5c2`, `afcf05da`, `bb4feba9`, `aac178b2` carry them in
reading batches; `1ee17016` carries the occurrence layer.

17 registry entries were added, each with the member count that justifies it: homotopy 145,
product-topology 73, van-kampen 58, manifolds 52, retracts 44, degree 42, countability 42,
mayer-vietoris 39, euler-characteristic 38, separation-axioms 37, homeomorphisms 35,
cohomology 34, subspace-topology 22, orientation 18, category-theory 17,
poincare-duality 14, paracompactness 6.

## Routes

14 emitted, one root and 13 sections:

```
/guide/GUIDE-TOPOLOGY.html
/guide/GUIDE-TOPOLOGY/spaces-and-continuous-maps.html
/guide/GUIDE-TOPOLOGY/constructions-of-spaces.html
/guide/GUIDE-TOPOLOGY/separation-and-countability.html
/guide/GUIDE-TOPOLOGY/metric-spaces.html
/guide/GUIDE-TOPOLOGY/compactness.html
/guide/GUIDE-TOPOLOGY/connectedness-and-homotopy.html
/guide/GUIDE-TOPOLOGY/the-fundamental-group.html
/guide/GUIDE-TOPOLOGY/covering-spaces.html
/guide/GUIDE-TOPOLOGY/cell-complexes.html
/guide/GUIDE-TOPOLOGY/homology.html
/guide/GUIDE-TOPOLOGY/degree-and-fixed-points.html
/guide/GUIDE-TOPOLOGY/surfaces.html
/guide/GUIDE-TOPOLOGY/manifolds-and-duality.html
```

The sections cover the tree under `wiki/40_Topology`: `020_Point_Set` by the first six,
`040_pi_1` by the fundamental group, covering spaces and cell complexes, `060_Homology`
by homology, `080_Degree` by degree and fixed points, and `100_Manifolds` by surfaces and
by manifolds and duality.

Reading order is the order of the sections in the file, and it is what the numbered path
on the root and the previous/next links follow. The parent of a section is a separate
claim — what that section needs in order to be read — and the tree it defines has
maximum depth 5:

```
spaces-and-continuous-maps
  constructions-of-spaces
    cell-complexes
      homology
        degree-and-fixed-points
        surfaces
        manifolds-and-duality
  separation-and-countability
    metric-spaces
    compactness
  connectedness-and-homotopy
    the-fundamental-group
      covering-spaces
```

## What was inspected

Headless Chromium at 1440x1400 against the built site, one capture per route, all 14 read
directly rather than merely produced. They are in `screenshots/`.

**Root.** Study-path sidebar showing all 13 sections with the tree above, every label
legible. Lede, the numbered reading path 1 through 13, and `NEXT Spaces and Continuous
Maps`.

**Spaces and Continuous Maps.** Breadcrumb `Topology / Spaces and Continuous Maps`. The
topology, basis, closed-set, closure, limit-point and continuity definitions each as a
titled block with its card id, mathematics typeset throughout, and Munkres 18.1 as
`T-FA6VI`.

**Constructions of Spaces.** The subspace, product and box topologies render their
displayed definitions correctly, including the generated-topology and
coarsest-topology characterisations of the product.

**Separation and Countability.** The $T_0$ through $T_4$ list renders as a list, with the
counterexample block beneath it. Urysohn's lemma, the neighborhood basis, first and
second countability, dense and separable.

**Metric Spaces.** Diameter, boundedness, distance to a subspace, uniform continuity,
total boundedness, the two compactness reformulations, the Lebesgue number, Baire.

**Compactness.** Cover, compact, quasicompact, locally compact, paracompact, then the
theorems: continuous image, closed subset, extreme value, continuous bijection to a
Hausdorff target, the tube lemma, complete-and-totally-bounded, Cantor.

**Connectedness and Homotopy.** The four equivalent forms of disconnectedness render as
one list including $\Hom_{\Top}(X,\{0,1\}) \cong \{0,1\}$, followed by components, path
components, local connectedness, homotopy, homotopy classes, nullhomotopy, homotopy
equivalence, contractibility, retracts and deformation retracts.

**The Fundamental Group.** Path concatenation renders as a cases display. The group
construction, simple connectedness, free products, amalgamated free products,
Seifert-van Kampen, $\pi_1$ of a wedge and of a product, higher homotopy groups.

**Covering Spaces.** Breadcrumb carries the whole chain, `Topology / Spaces and Continuous
Maps / Connectedness and Homotopy / The Fundamental Group / Covering Spaces`. Sixteen
statements from the definition through the lifting criterion, the fundamental theorem,
deck transformations and monodromy to free subgroups of free groups.

**Cell Complexes.** The CW attaching formula
$X^n = (X^{n-1} \disjoint \Disjoint_\alpha D^n_\alpha)/(x \sim \varphi_\alpha(x))$ renders,
as do the cone, suspension, wedge, smash, mapping cylinder and mapping cone.

**Homology.** The singular boundary map and $H_n(X) = \ker \del_n / \im \del_{n+1}$
render; then the long exact sequence, excision, Mayer-Vietoris, wedges, Kunneth, the
universal coefficient theorem and Hurewicz.

**Degree and Fixed Points.** The degree definition, local degree, the Lefschetz number
$\tau(f) = \sum_n (-1)^n \tr(f_* \mid H_n(X;\QQ))$, Lefschetz's theorem, Brouwer, the
hairy ball theorem and Borsuk-Ulam.

**Surfaces.** The lede's monoid relation $\RP^2 \# \RP^2 \# \RP^2 = \RP^2 \# T^2$ renders,
and the polygon-model figures load as images rather than as broken references.

**Manifolds and Duality.** Manifold, boundary, orientation and the orientation cover, the
fundamental class, cup and cap product, the Kronecker pairing, Poincaré duality in its
absolute and relative forms, Lefschetz duality, Alexander duality, the intersection form.

## Coverage, measured

The branch addresses 1,014 of the 1,135 Topology cards of substantive kind, by 173 refs
and 59 panels; every panel returns matches, 2,010 hits in total. The 121 it does not
address break down as 39 definitions, 34 exercises, 13 propositions, 11 theorems, 11
facts, 9 problems, 2 corollaries and 2 examples.

## What this does not claim

**It is not every card.** Issue #28 asks for every Topology source page and extracted card
addressable from the branch. 121 are not, and the reason is structural rather than an
oversight: a `QueryItem` carries no title, so every panel renders under the same `More
from the catalog` heading. A section already shows that heading up to five times, and the
sections that would close the gap need eight to twenty panels each, which would leave the
reader a page of identically labelled lists. Closing it properly needs a title on the
panel, which is a change to `qualc/publication.py` and `qualc/emit.py` and belongs to
whoever owns the emitter, not to this manifest. The 121 remain reachable from
`/problems.html`, from their sitting pages, and from their own tag routes.

**Nine cards could not be classified at all**, so no panel can reach them: `P-557LL`
("3. $\RP^2$"), `P-ALVYE`, `P-AMD-CM4OPBUE` ("IMages"), `P-AMD-ERYR6LDW` ("(Images)"),
`P-GAA3C` ("Does the converse hold?"), `P-MFWBK` ("$\QQ$"), `P-OTXNQ`, `P-V33RL`
(titled "Untitled", body a question mark) and `P-ZQBPZ` (titled "Untitled", body an image
link). Each is a fragment split from a stem that is not in the card. Five occurrences of
three of them are unclassified for the same reason.

**Source cards carry no topics**, here or in any other subject. A sitting is an
institution, an area and a date; its topics are the union of its problems', which is a
query rather than a stored fact.

**Occurrence topics reach no route.** `emit.py` gives a tag page to problems and to cards
whose kind is not problem, source or occurrence, and renders occurrences inside their
problem's page and their sitting's page. The 809 assignments are for the catalog and for
facet queries.

**Not exercised here**: search, the generator, hint and solution disclosure states, and
any viewport other than 1440 wide.

**The site was not otherwise validated.** `artifacts/issue-17/validate-site` was not run
over this build; the repository was under concurrent builds from other subject lanes
throughout, and `build/quarto/_site` was deleted and rebuilt underneath this inspection
twice.

## Defects found while reading, not repaired here

Recorded for issue #2 rather than fixed, since this branch was not to touch card bodies.

False statements: `E-2LZES` and `E-6MBWQ` ("metrizable implies compact"); `E-5FLKZ`
("every first countable space is second countable"); `FF-BOIT5` ($\chi = -2 \implies
X \cong \RP^2$, when $\chi(\RP^2) = 1$); `P-AMD-6GFMKZVQ` and its occurrence
`O-AMD-00107` ($\pi_1(T) \cong \ZZ/2$ for the torus); `P-LKYOC` ($\pi_1(S^1\cross S^1)$
called the free group on two generators, and $F_2$ identified with $\ZZ\cross\ZZ$);
`P-TOPOLOGY-PHD-F08-18` ("there is no $n$-sheeted covering of $S^1$ for any finite $n$",
contradicted by the fact the card itself quotes); `T-7DICT`, whose Cantor intersection
statement drops the Hausdorff hypothesis and is false in $\NN$ with the cofinite topology,
where every subset is compact and $\bigcap_n \{n, n+1, \ldots\} = \emptyset$;
`FT-52GNK` and `FT-J7RQV`, whose Urysohn's lemma omits that the two closed sets are
disjoint, and the first of which also states the Urysohn metrization theorem as an
equivalent; `T-TZ3X7`, whose Kunneth splitting writes $H_i X \oplus H_j Y$ where the
tensor product is meant; `PR-UL3KL`, which gives closed orientable 3-manifolds a
torsion-free $H_1$, false for lens spaces; `P-T12A3`, which calls
$\{x^2+y^2+z^2=1\}\subseteq\RR^3$ the 3-sphere.

Unwritten statements: `D-6CI7D` (Local Orientation), `D-FAIJX` (Mayer-Vietoris Sequence)
and `D-GIUR3` (Lefschetz duality) have empty bodies.

Mathematics only in an unextracted image, which routes to issue #9: `P-AMD-6TSC527D`,
`P-AMD-7INMAFDG`, `P-AMD-FV5LNKN4` ("This identification space:" followed by a figure),
and `P-ZQBPZ`.

Solutions kinded as problems, thirty-nine cards whose body is a worked solution with no
statement: `P-2ICK2`, `P-3QUC7`, `P-3TOOU`, `P-6DZST`, `P-6OVVU`, `P-7FRUL`,
`P-7NQO2`, `P-AY6TZ`, `P-BBFQR`, `P-BBI5H`, `P-DKDKR`, `P-DPYAI`, `P-E53UO`, `P-G6GOO`,
`P-IXL2P`, `P-JZXST`, `P-KUYTP`, `P-LJTUV`, `P-LKYOC`, `P-MZZJH`, `P-NESQN`, `P-NQKCX`,
`P-O2J6S`, `P-OX7OF`, `P-P4P4L`, `P-PJH3T`, `P-QFLQB`, `P-QNUFT`, `P-TIRTE`, `P-V4A37`,
`P-V554H`, `P-WAI3F`, `P-XAQEZ`, `P-XGHXK`, `P-XPDMQ`, `P-XTPAP`, `P-XWNF6`, `P-XYYRM`
and `P-Z6THT`. This is what the reading found; it is not an exhaustive scan.

Truncated exercises, a bare bullet from a `TFAE` list with no stem: `E-E7FYR`, `E-WFE4T`,
`E-YAEMZ`.

Titles that are a statement rather than a name, surviving issue #40: `D-B7CYY`,
`D-2GCTV`, `D-EILKJ`, `D-ZFRV4`, `D-YO6NZ`, `D-NCLVD`, `D-XRHTV`, `D-UI7ZL`, `D-3KS2F`,
`D-X6LZD`, `D-HQSEQ`. `T-FBMYQ` is titled "Excision: Todo" although its body is written.

Pairs of cards defining the same notion, some of them differing only in wording and some
in generality: `D-ITBUT` and `D-TNBFZ` (Quotient Map), `D-YD6DH`
and `D-EBNUE` (Fundamental Group), `PR-UBJ6P` and `T-F4PQY` (Hatcher 1.39), `FT-52GNK`
and `FT-J7RQV` (Urysohn), `D-6JJJU` and `D-B3BVQ` (Locally Finite), `D-2O3N7` and
`D-6UHU7` (Deformation Retract), `D-MQSFD` and `D-VW2Z3` (Quasicompact), `D-KW52R` and
`D-MVBYO` (Comparability of topologies), `D-I7D56` and `D-MVNSV` (Basis of a module),
`D-3ZBXG` and `D-BUAYX` (Injection), `D-S7L6M` and
`D-Z2V7T` (Exact Functor), `D-B7CYY` and `D-HS6DE` (Diameter), `D-2GCTV` and `D-EHUCS`
(Bounded), `D-5EOQZ` and `D-RZ7I3` (Locally Compact), `D-23NTI` and `D-UHM6M` (Second
Countable), `D-ASXW6` and `D-UHTGH` (Closure), `D-3KS2F` and `D-KT5XH` (Boundary),
`D-6FSWY` and `D-NCLVD` (Retract), `D-4DXA7` and `D-OM7TD` ($T_n$ spaces), `D-6FMP3` and
`D-ZFRV4` (Hausdorff). `D-5MX7E` and `D-TD6AO` are the wider case: one defines the colimit
over a diagram and the other over a directed system, so they want reading together rather
than collapsing. Four cards carry one problem, that every $f: S^2 \to S^1$ agrees at some
antipodal pair: `P-AMD-SYO3GZHS`, `P-DDUA3`, `P-KPDL7` and `P-VROCX`.

Out of subject: `P-AMD-OXM52UGE` asks for the homophony group of English, a joke, and sits
in the Topology area.

Cosmetic residue in card bodies: `PR-JL5JP` ends a figure with a stray `?`, and `D-YO6NZ`
carries an example block titled `?`.
