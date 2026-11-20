---
schema: qual/card@1
id: E-HAT-4.1-23
kind: problem
title: "Mapping cylinders and cones have CW type"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 23; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17913-17915 for the statement). Correct: replace f by a cellular map f'
    between CW models, note that the square with the homotopy equivalences is homotopy commutative so that
    homotopy invariance of homotopy pushouts gives (M_f', X') ~ (M_f, X) as pairs, and observe that a
    cellular f' has a CW structure on its mapping cylinder with X' a subcomplex; then C_f ~ M_f'/X', a
    quotient of a CW complex by a subcomplex. The one step taken at reference level rather than expanded is
    homotopy invariance of homotopy pushouts, which is standard. Not checked: no independent construction of
    the explicit pair homotopy equivalence.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps without changing it, and made explicit the three
    steps the prose takes at reference level: cellular approximation applied to f' = v^{-1} f u; the
    mapping cylinder as the homotopy pushout of the diagram whose maps are f' and the inclusion of
    X' at t = 0, which is what lets homotopy invariance of homotopy pushouts act on the
    homotopy-commutative square; and, for cellular f', the CW structure on M_{f'} with the cells of
    Y' together with a cell e^k x (0,1) of dimension k+1 for each cell of X', X' itself a
    subcomplex, cellularity of f' being what makes the attaching maps land in the right skeleta.
    Also supplied the reason the quotient of a CW complex by a subcomplex is a CW complex. Not
    checked this session: the printed page of the exercise, and no explicit pair homotopy
    equivalence was constructed.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §4.1 Exercise 23, printed p. 360,
    Example 4.11 (cellular approximation for pairs) and Corollary 4.12. One repair, in step
    `cw-cylinder`: its cell list named the cells of Y' and the cells e^k x (0,1) but not the cells
    e^k x {0}, so the closure of e^k x (0,1) contained points of X' x {0} that were not cells; the
    decomposition was therefore not a CW structure, and the claim that X' x {0} is a subcomplex did
    not follow — the step also described the image of X' as X' x {0} together with the cylinders on
    its cells, which is X' x [0,1] and not the image. The step now lists e^k x {0} as a k-cell,
    checks closure-finiteness, and identifies X' x {0} as the subcomplex they form. Steps `models`,
    `cellular`, `square`, `pushout`, `pair` and `cone` are unchanged and correct: f' = v^{-1} f u is
    homotopic to a cellular map with the same mapping-cylinder homotopy type, the homotopy-commutative
    square gives a homotopy equivalence of homotopy pushouts and hence of pairs, and a homotopy
    equivalence of CW pairs induces one of the quotients. Not checked: no pair equivalence was
    constructed explicitly, and no page number for the exercise is claimed.

---

::: {.problem}
If $f: X \to Y$ is a map with $X$ and $Y$ homotopy equivalent to CW complexes, show that the pair $(M_f, X)$ is homotopy equivalent to a CW pair, where $M_f$ is the mapping cylinder.
Deduce that the mapping cone $C_f$ has the homotopy type of a CW complex.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.1 Exercise 23. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 23.

For a map $f\colon X\to Y$ the mapping cylinder is $M_{f}=\bigl((X\times I)\sqcup Y\bigr)/\sim$ with $(x,1)\sim f(x)$, and the mapping cone is $C_{f}=M_{f}/(X\times\{0\})$.

::: pf

::: {.pf-step #models}
There are CW complexes $X',Y'$ and homotopy equivalences $u\colon X'\to X$, $v\colon Y'\to Y$ with homotopy inverses $u^{-1}$, $v^{-1}$.

::: pf-proof
$X$ and $Y$ are homotopy equivalent to CW complexes, so choose such $X'$, $Y'$ and equivalences $u$, $v$; a homotopy equivalence has a homotopy inverse.
:::

:::

::: {.pf-step #cellular}
The composite $f'=v^{-1}fu\colon X'\to Y'$ is homotopic to a cellular map.

::: pf-proof
$f'$ is a map between CW complexes and the cellular approximation theorem states that every such map is homotopic to a cellular one. Replacing $f'$ by a homotopic cellular map leaves its homotopy class, hence the homotopy type of its mapping cylinder, unchanged.
:::

:::

::: {.pf-step #square}
$vf'\simeq fu$, and $u,v$ are homotopy equivalences.

::: pf-proof
$vf'=v\,v^{-1}f\,u\simeq fu$, since $vv^{-1}\simeq\mathrm{id}$; the vertical maps are equivalences by step [](#models){.pf-ref}. So the square with corners $X',Y',X,Y$ and maps $f',u,v,f$ commutes up to homotopy.
:::

:::

::: {.pf-step #pushout}
$(M_{f'},X')\simeq(M_{f},X)$ as pairs.

::: pf-proof
The mapping cylinder $M_{g}$ of $g\colon A\to B$ is the homotopy pushout of the diagram consisting of $g$ and the inclusion $A\to A\times\{0\}\subset A\times I$. A homotopy-commutative square whose vertical maps are homotopy equivalences induces a homotopy equivalence of the two homotopy pushouts, compatibly with the images of the domain, hence a homotopy equivalence of pairs.
:::

:::

::: {.pf-step #cw-cylinder}
For cellular $f'\colon X'\to Y'$, the pair $(M_{f'},X')$ is a CW pair.

::: pf-proof
Take as cells of $M_{f'}$ the cells of $Y'$, the cells $e^{k}\times\{0\}$ for the cells $e^{k}$ of $X'$, of dimension $k$, and the cells $e^{k}\times(0,1)$, of dimension $k+1$. The attaching maps come from those of $Y'$ together with the characteristic maps of the cells of $X'$ and the map $f'$; cellularity of $f'$ is exactly the condition that the $(k+1)$-cell $e^{k}\times(0,1)$ attaches to the $k$-skeleton, along $e^{k}\times\{0\}$ and $\partial e^{k}\times(0,1)$ through the characteristic map of $e^{k}$ and along $e^{k}\times\{1\}$ through $f'$, which lands in the $k$-skeleton of $Y'$. Closure-finiteness holds because the closure of $e^{k}\times(0,1)$ meets only the cells $e^{j}\times\{0\}$ and $e^{j}\times(0,1)$ with $j\le k$ and the finitely many cells of $Y'$ in the closure of $f'(e^{k})$. So $M_{f'}$ is a CW complex, and $X'\times\{0\}$ is the subcomplex that is the union of the cells $e^{k}\times\{0\}$.
:::

:::

::: {.pf-step #pair}
$(M_{f},X)$ is homotopy equivalent to a CW pair.

::: pf-proof
Steps [](#pushout){.pf-ref} and [](#cw-cylinder){.pf-ref} give a CW pair $(M_{f'},X')$ homotopy equivalent to $(M_{f},X)$.
:::

:::

::: {.pf-step #cone}
$C_{f}$ has the homotopy type of a CW complex.

::: pf-proof
$C_{f}=M_{f}/(X\times\{0\})=M_{f}/X$, and a homotopy equivalence of pairs $(M_{f'},X')\to(M_{f},X)$ induces a homotopy equivalence of quotients $M_{f'}/X'\to M_{f}/X$. A quotient of a CW complex by a subcomplex is a CW complex: the cells of the complement survive as cells, the quotient map being a homeomorphism on each of them, and they are attached as before. Hence $C_{f}\simeq M_{f'}/X'$ is homotopy equivalent to a CW complex.
:::

:::

:::

:::
