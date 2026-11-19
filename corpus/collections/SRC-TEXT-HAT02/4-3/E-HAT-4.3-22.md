---
schema: qual/card@1
id: E-HAT-4.3-22
kind: problem
title: "Principal fibrations with sections split"
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
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 22, printed p. 420,
    against the definition of a principal fibration on printed p. 412, and against the
    remark on printed p. 405 that a fibre-preserving map which is a homotopy equivalence
    is a fibre homotopy equivalence. The card opened with "by definition, a principal
    fibration is fiber homotopy equivalent to the pullback", which the definition does not
    say: p. 412 asks only for weak homotopy equivalences in the comparison diagram. The
    gap is closable and is now closed: a weak homotopy equivalence of total spaces between
    fibrations with CW type is a homotopy equivalence by Whitehead, and a fibre-preserving
    homotopy equivalence is a fibre homotopy equivalence by the fact Hatcher states on
    p. 405; the two properties the exercise compares are invariant under fibre homotopy
    equivalence over B, so the pullback model may be used. The card also now cites
    Proposition 4.62 for the homotopy invariance of the pullback instead of Exercise 11.
    The converse direction and the product section were correct as written. Statement
    unchanged. Not checked: the §4.H exercise that proves the p. 405 fact.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof completed: the statement is an iff, and only the direction section => fibre homotopy equivalent to Omega C x B was proved. The converse is now supplied: a fibre homotopy equivalence over B contains a map r: B x Omega C -> E with p r = pr_B, and composing with the product's own section const_{c_0} gives a section of E -> B.
---

::: {.problem}
Show that a principal fibration $\Omega C \to E \xrightarrow{p} B$ is fiber homotopy equivalent to the product $\Omega C \times B$ if and only if it has a section, a map $s: B \to E$ with $ps = \id$.
:::

::: {.solution}
Hatcher's definition (printed p. 412) is that a fibration $F\to E\to B$ is principal if there is a commutative diagram whose second row is a fibration sequence and whose vertical maps are weak homotopy equivalences; as he notes there, this says that $E\to B$ is, up to a weak homotopy equivalence over $B$, the pullback of the path--loop fibration
$$
\Omega C\longrightarrow PC\xrightarrow{\operatorname{ev}_1}C
$$
along a map $f:B\to C$. That comparison can be taken to be a fibre homotopy equivalence: a fibre-preserving map that is a homotopy equivalence is a fibre homotopy equivalence (printed p. 405, where Hatcher records the fact and defers its proof to §4.H), and a weak homotopy equivalence of total spaces is a homotopy equivalence by Whitehead's theorem as soon as both spaces have CW type, which fibrations over a CW base do. So the total space may be represented, up to fibre homotopy equivalence over $B$, by pairs $(b,\gamma)$ with $\gamma(0)=c_0$ and $\gamma(1)=f(b)$, and both properties in the statement — having a section up to homotopy, and being fibre homotopy equivalent to a product — are invariant under fibre homotopy equivalence over $B$.

A section assigns to each $b$ such a path $\gamma_b$, continuously in $b$. The formula
$$
H(b,t)=\gamma_b(t)
$$
is a homotopy from the constant map at $c_0$ to $f$. By homotopy invariance of pullback fibrations (Proposition 4.62, printed p. 406), pulling the path-space fibration back along $f$ gives a fibration fibre homotopy equivalent to its pullback along the constant map. The latter is
$$
B\times\Omega C\longrightarrow B.
$$
Consequently $E\to B$ is fiber homotopy equivalent to the stated product fibration.

Conversely, suppose $E\to B$ is fiber homotopy equivalent to the product fibration
$B\times\Omega C\to B$. A fiber homotopy equivalence over $B$ contains a map
$r:B\times\Omega C\to E$ with $p\,r=\mathrm{pr}_B$, and the product fibration has the section
$s_0(b)=(b,\mathrm{const}_{c_0})$. Then $s=r\circ s_0$ satisfies $p\,s=\mathrm{pr}_B\circ s_0=\id$,
so $E\to B$ has a section. Together with the preceding paragraph this shows that $E\to B$ has a
section if and only if it is fiber homotopy equivalent to $\Omega C\times B\to B$.
:::
