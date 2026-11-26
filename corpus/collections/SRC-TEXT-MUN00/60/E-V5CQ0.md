---
schema: qual/card@1
id: E-V5CQ0
kind: problem
title: Antipodal identification on the disk gives the projective plane
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 2, printed p. 375,
    with Theorem 60.3 and the definition of $P^2$ as $S^2$ modulo antipodes. The upper hemisphere is homeomorphic to $B^2$ by dropping the third coordinate, and every antipodal pair meets it in exactly one point unless the pair lies on the equator, where the two representatives are antipodal boundary points; so both quotients identify the same pairs, and the compact-to-Hausdorff argument makes the induced bijection a homeomorphism. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §60 Exercise 2, his pp. 26-27, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution transcribes the source's two maps and its
    pasting check, and repairs the final step: the source applies the compact-to-Hausdorff theorem
    to $f^{-1}$, which is circular because $f^{-1}$'s continuity is what it wants to prove. The
    card applies the theorem to the source's own $g:X\to P^2$, which is continuous by the
    quotient property and bijective by the source's two computations, with $X$ compact and $P^2$
    Hausdorff. Everything else in the source is correct, including that $p(x)=p(-x)$ for $x$ with
    $x_3=0$, which is what makes $f$ well defined. Checked against the book: the exercise on
    printed p. 375, the definition of $P^2$ on printed p. 372, Theorem 60.3 on printed pp. 372-373
    for the Hausdorff property, Theorem 26.5 on printed p. 166, Theorem 26.6 on printed p. 167 and
    Theorem 27.3 on printed p. 173. Not claimed: that the source verifies that its own $g$ is a map
    of the quotient -- it builds $f$ first and inverts it, which is the step repaired here.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription plus the one-line repair above, in Lamport
    form, with the source, the defect and the book's pages named in its own text.
---

::: {.exercise}

Let $X$ be the quotient space obtained from $B^2$ by identifying each point $x$ of $S^1$ with its antipode $-x$.
Show that $X$ is homeomorphic to the projective plane $P^2$.
:::

::: {.solution}
The exercise is §60 Exercise 2, with the projective plane defined
in §60 as the quotient of $S^2$ by the identification of each point
with its antipode; write $p:S^2\to P^2$ for that quotient map, and
$q:B^2\to X=B^2/\!\sim$ for the quotient of the exercise.

The proof is transcribed from Pearse, *Topology (2nd ed.) — James R. Munkres*,
solutions, Cornell 2005, §60 Exercise 2, his, read in
`tmp/sources/cornell-erin-munkres.md`: the two maps $f$ and $g$ below are the
source's, the pasting check that $f$ is well defined is the source's, and the
final step is the compact-to-Hausdorff theorem. That final step is where the
source is defective. It applies the theorem to $f^{-1}$, whose continuity is
exactly what has to be proved; applying the theorem needs a continuous map, so
as written the argument is circular. The repair is one line and step
[](#homeomorphism){.pf-ref} takes it: the source's $g:X\to P^2$ is already a
continuous bijection with compact domain $X$ and Hausdorff target $P^2$, so the
theorem applies to $g$, and $f=g^{-1}$ is a homeomorphism as well.

For $b\in B^2$ write $\hat b=(b,\sqrt{1-\norm b^2})\in S^2_+$, the point of the
closed upper hemisphere above $b$.

::: pf

::: {.pf-step #well-defined}
There is a continuous bijection $g:X\to P^2$ with $g(q(b))=p(\hat b)$ for every
$b\in B^2$.

::: pf-proof
Define $G:B^2\to P^2$ by $G(b)=p(\hat b)$. It is continuous, since
$b\mapsto(b,\sqrt{1-\norm b^2})$ is continuous from $B^2$ into $S^2$ and $p$ is
continuous. If $b\in S^1$ then $\hat b=(b,0)$ and $\widehat{-b}=(-b,0)=-\hat b$,
so $G(-b)=p(-\hat b)=p(\hat b)=G(b)$; thus $G$ is constant on the fibres of the
quotient map $q$, and it induces a continuous $g:X\to P^2$ with $g\circ q=G$.

$g$ is surjective: a point of $P^2$ is $p(x)$ for some $x\in S^2$, and
$x$ or $-x$ has non-negative third coordinate, say $x$; then $x=\hat b$ for
$b=(x_1,x_2)\in B^2$ and $p(x)=g(q(b))$.

$g$ is injective: if $g(q(b))=g(q(b'))$ then $p(\hat b)=p(\widehat{b'})$, so
$\widehat{b'}=\hat b$ or $\widehat{b'}=-\hat b$. In the first case $b'=b$. In the second,
the third coordinates satisfy $\sqrt{1-\norm{b'}^2}=-\sqrt{1-\norm b^2}$, so both
are $0$, $b,b'\in S^1$, and $b'=-b$; hence $q(b')=q(b)$.
:::

:::

::: {.pf-step #compact-hausdorff}
$X$ is compact and $P^2$ is Hausdorff.

::: pf-proof
$B^2$ is closed and bounded in $\RR^2$, hence compact by the Heine--Borel theorem
(Theorem 27.3); $q$ is continuous and onto, so $X=q(B^2)$ is
compact by Theorem 26.5 . The projective plane $P^2$ is Hausdorff
by Theorem 60.3 , whose proof gives both the Hausdorff
property and the covering property of $p$.
:::

:::

::: {.pf-step #homeomorphism}
$\boxed{X\ \text{is homeomorphic to}\ P^2}$.

::: pf-proof
By steps [](#well-defined){.pf-ref} and [](#compact-hausdorff){.pf-ref}, $g$ is a
continuous bijection from the compact space $X$ onto the Hausdorff space $P^2$, so
$g$ is a homeomorphism by Theorem 26.6 . This is the source's
argument with the theorem applied to the continuous map $g$ rather than to
$f^{-1}$; the source's $f:P^2\to X$, given by $f(\theset{x,-x})=q(x_1,x_2)$ when
$x_3\ge0$ and $q(-x_1,-x_2)$ when $x_3\le0$ and continuous by the pasting lemma,
is then the inverse homeomorphism.
:::

:::

:::
:::
