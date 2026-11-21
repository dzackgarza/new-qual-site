---
schema: qual/card@1
id: E-HAT-4.3-14
kind: problem
title: "Fibration classes bijection with map classes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation convention. Sources on this card are cited by chapter, section and numbered statement
    only, and the statement and solution above cite every source by its numbered statement. The
    events dated before today are left as their sessions wrote them, which QUAL-11 requires, so a
    locator in one of them stands as a historical record and is superseded by the citation now on
    the card. This event records the convention and claims no further reading: the
    mathematics of the card is as those events describe it.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Provenance and page corrected. The body's sentence "none of the retained Hatcher sets solves
    Section 4.3 Exercise 14" was false: Sam solves Exercise 14, by exactly the
    route the card takes, and the body now cites him. Proposition 4.65 is now cited by number, and
    the event of 2026-11-19 is left as written under QUAL-11.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 14, printed p. 420.
    The argument is right but one citation was wrong: the step identifying p_i with its
    mapping path replacement cited Exercise 12 of the section, which is about homotopic
    maps f, g: A -> B having fibre homotopy equivalent fibrations E_f, E_g, not about a
    fibration and its mapping path replacement. That is Proposition 4.65, printed p. 409
    ("If p: E -> B is a fibration, then the inclusion E -> E_p is a fiber homotopy
    equivalence"), now cited. The citation of Exercise 13 for E_{p_2 g} ~ E_{p_2} is
    correct as printed. An independent report from the swarm flagged the same citation.
    Statement unchanged. Not checked: nothing outside this exercise.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
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
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Checked against Hatcher, Section 4.3 Exercise 14, printed
    p. 420 (PDF p. 429, folio 420). Each step re-read: a fibre homotopy equivalence is exactly a
    homotopy equivalence of total spaces over B, so the map on classes is well defined; the
    mapping path replacement is a fibration and the inclusion of A is a deformation retract of it,
    which gives surjectivity with p_f i = f on the nose; and injectivity chains the fibre homotopy
    equivalences p_i ~ E_{p_i} (Exercise 12) and E_{p_1} ~ E_{p_2 g} ~ E_{p_2} (Exercise 13). The
    two cited exercises are the book's, as the exercise's own pointer says, and are used as
    citations rather than reproved. Not claimed: functoriality of the bijection or any statement
    about a fixed basepoint.
---

::: {.problem}
For a space $B$, let $\mathcal{M}(B)$ denote the set of equivalence classes of maps $f: A \to B$ where $f_1: A_1 \to B$ is equivalent to $f_2: A_2 \to B$ if there exists a homotopy equivalence $g: A_1 \to A_2$ such that $f_1 \simeq f_2 g$.
Show the natural map $\mathcal{F}(B) \to \mathcal{M}(B)$ is a bijection. [See Exercises 11 and 13.]
:::

::: {.solution}
The retained solution set of **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.3 Exercise 14** of `tmp/sources/hatcher-solutions-sam-2008.pdf`, solves this exercise by the same route: surjectivity from the inclusion $A\hookrightarrow E_f$, injectivity from Exercise 13 and Proposition 4.65. The steps below follow that argument and are checked against Hatcher, Algebraic Topology, Section 4.3 Exercise 14, and uses Exercises 11--13 of the same section, which the exercise points to; here $\mathcal F(B)$ is the set of fibre homotopy equivalence classes of fibrations over $B$.

::: pf

::: {.pf-step #well-defined}
Sending a fibration $p:E\to B$ to the class of $p$ in $\mathcal M(B)$ defines a map $\mathcal F(B)\to\mathcal M(B)$.

::: pf-proof
A fibre homotopy equivalence $g:E_1\to E_2$ over $B$ is a homotopy equivalence of total spaces with $p_1\simeq p_2g$; this is exactly the relation defining $\mathcal M(B)$. So fibre homotopy equivalent fibrations have the same class, and the assignment is well defined.
:::

:::

::: {.pf-step #surjective}
The map is surjective.

:::: pf-proof

::: {.pf-step #replacement}
For any map $f:A\to B$ the mapping path replacement $p_f:E_f\to B$, with $E_f=\{(a,\gamma):\gamma(0)=f(a)\}$ and $p_f(a,\gamma)=\gamma(1)$, is a fibration.

::: pf-proof
This is the standard mapping path fibration of Section 4.3: lifting a homotopy amounts to reparametrising the path coordinate, which gives an explicit lift, so $p_f$ has the homotopy lifting property.
:::

:::

::: {.pf-step #equivalent}
The inclusion $i:A\to E_f$, $a\mapsto(a,\text{constant path at }f(a))$, is a homotopy equivalence and $p_f\,i=f$.

::: pf-proof
$p_f i=f$ because the constant path at $f(a)$ ends at $f(a)$. The map $i$ is a homotopy equivalence: the map $(a,\gamma)\mapsto a$ is a deformation retraction of $E_f$ onto the image of $i$, contracting each path $\gamma$ to the constant path at its initial point, which lies in the image of $i$ because $\gamma(0)=f(a)$.
:::

:::

::: {.pf-step}
The class of $f$ in $\mathcal M(B)$ is the class of the fibration $p_f$.

::: pf-proof
$i$ is a homotopy equivalence and $f=p_f i$ exactly, so $f$ and $p_f$ are equivalent maps in $\mathcal M(B)$. Since $f$ was arbitrary, every class in $\mathcal M(B)$ is the image of a fibration class.
:::

:::

:::

:::

::: {.pf-step #injective}
The map is injective.

:::: pf-proof

::: {.pf-step #data}
Suppose fibrations $p_1:E_1\to B$ and $p_2:E_2\to B$ have the same class in $\mathcal M(B)$.

::: pf-proof
Then there is a homotopy equivalence $g:E_1\to E_2$ with $p_1\simeq p_2 g$, by the definition of $\mathcal M(B)$.
:::

:::

::: {.pf-step #chain}
$p_1$ and $p_2$ are fibre homotopy equivalent.

::: pf-proof
Each $p_i$ is fibre homotopy equivalent to its mapping path replacement $E_{p_i}\to B$ (Proposition 4.65: for a fibration $p$ the inclusion $E\hookrightarrow E_p$ is a fibre homotopy equivalence, whose construction is the one of step [](#replacement){.pf-ref} applied to $p_i$). A homotopy $p_1\simeq p_2g$ together with the homotopy equivalence $g$ gives a fibre homotopy equivalence $E_{p_1}\simeq_f E_{p_2 g}$, and composing with $g$ gives $E_{p_2g}\simeq_f E_{p_2}$; this is the content of Exercise 13 of this section. Chaining the three fibre homotopy equivalences gives $p_1\simeq_f p_2$.
:::

:::

::: {.pf-step}
Equal classes in $\mathcal M(B)$ imply equal classes in $\mathcal F(B)$.

::: pf-proof
Step [](#chain){.pf-ref} produces a fibre homotopy equivalence between the two representatives, so their classes in $\mathcal F(B)$ coincide.
:::

:::

:::

:::

::: {.pf-step}
$\mathcal F(B)\to\mathcal M(B)$ is a bijection.

::: pf-proof
Steps [](#well-defined){.pf-ref}, [](#surjective){.pf-ref} and [](#injective){.pf-ref} give a well-defined, surjective and injective map:
$$
\boxed{\mathcal F(B)\xrightarrow{\ \cong\ }\mathcal M(B).}
$$
No hypothesis on $B$ is used: both constructions are natural in $B$.
:::

:::

:::
:::
