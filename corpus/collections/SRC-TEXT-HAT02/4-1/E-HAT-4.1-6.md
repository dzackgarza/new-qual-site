---

schema: qual/card@1
id: E-HAT-4.1-6
kind: problem
title: "Covering spaces and relative homotopy groups"
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
  date: 2026-11-16
  note: >-
    Two repairs from a local reader. (1) The exercise's citation now names Hatcher's text version
    `tmp/sources/hatcher-2002-algebraic-topology.md`; tom Dieck's was already named in the remark.
    (2) COMPLAINTS.md described this card's `pf` block as having four steps; it has five —
    `serre`, `cube-lift`, `surjective`, `injective`, and the closing bijection step — and the
    COMPLAINTS entry is corrected. The mathematics is unchanged: the reader checked Theorem
    (6.3.1) as stated on printed p. 129 and proved on printed p. 130, the use of (3.2.4) in both
    halves, and the exercise's own statement on Hatcher's p. 358 against the source's hypothesis
    $E_0=p^{-1}(B_0)$. Not checked here: the pagination of the 2008 bound volume.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 6; the stored statement matches.
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
    Read line by line. Correct. Surjectivity: a triple map `f : (D^n, S^{n-1}, s_0) -> (X, A, x_0)` lifts
    uniquely through `p` because `D^n` is simply connected, and since `f(S^{n-1}) subset A` the lift
    carries `S^{n-1}` into `p^{-1}(A) = A~`, so it represents a relative class upstairs. Injectivity: a
    relative homotopy of the projected maps lifts uniquely once its value at `(s_0,0)` is fixed, its two
    ends are the prescribed lifts by uniqueness, and its boundary stays in `p^{-1}(A)`; hence the two
    lifts were already relatively homotopic. The hypothesis `n > 1` is exactly what supplies the simple
    connectivity of `D^n` used in both halves. No correction was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 6, printed p. 358, with
    Proposition 4.1 and its proof on p. 342. Nothing false; two steps that were asserted are now
    derived: the existence of the lift of $f$ and of the lift of the relative homotopy is credited to
    the lifting criterion of Proposition 1.33 with the simply-connectedness of $D^n$, respectively of
    $D^n\times I$ (which the card had used without saying that existence, not only uniqueness, is at
    stake), and uniqueness with a prescribed value at one point is Proposition 1.34's uniqueness
    statement, p. 62. This is the relative form of Proposition 4.1 and the proof follows the book's
    argument for that proposition, with $D^n$ in place of $S^n$. No published exercise solution is in
    the retained sets; the book's own Proposition 4.1 proof covers the absolute case only.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 358, and it is exactly the statement of Hatcher's Proposition 4.1, printed p. 342, whose proof the book prints there: a covering space $p:(\tilde X,\tilde A,\tilde x_0)\to(X,A,x_0)$ with $\tilde A=p^{-1}(A)$ induces an isomorphism on $\pi_n$ for $n\ge2$, first for $\tilde X\to X$ by lifting a homotopy of maps of $S^n$ through the covering homotopy property, then for the pair by applying the five-lemma to the long exact sequences of the two pairs. The card's proof is that proof, with the lifting criterion of Proposition 1.33 (printed p. 61) named where the book names it. Checked against the book: the printed statement of Proposition 4.1 including the hypothesis $\tilde A=p^{-1}(A)$ and the path-connectedness of $\tilde X$, and the long exact sequence of Theorem 4.3 on p. 344 that the five-lemma step uses.
- event: source-corrected
  by: claude
  date: 2026-11-13
  note: >-
    The preceding note's claim that Exercise 6 "is exactly the statement of Hatcher's Proposition
    4.1" is false and is withdrawn. Proposition 4.1, printed p. 342, is the absolute statement
    $p_*:\pi_n(\tilde X,\tilde x_0)\to\pi_n(X,x_0)$, with proof by the lifting criterion and the
    covering homotopy property. The exercise, printed p. 358, is the relative statement
    $p_*:\pi_n(\tilde X,\tilde A,\tilde x_0)\to\pi_n(X,A,x_0)$ for the pair with
    $\tilde A=p^{-1}(A)$, which the book does not print. The card's remark now says what is printed
    where, and records why the relative case is not Proposition 4.1 plus the five-lemma: in the
    ladder of Theorem 4.3 the map $p_*:\pi_1(\tilde A)\to\pi_1(A)$ is injective and not in general
    surjective, so at $\pi_2$ the five-lemma gives injectivity only. The proof itself is unchanged
    and is the book's lifting argument for triples $(D^n,S^{n-1},s_0)$. Not established here: a
    published proof of the relative statement. Searched for one without result in the retained
    sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR Math 205B help
    file, May's *Concise Course* §4, Bredon Chapters III and VII, Maxim's Math 752 notes) and in
    Hatcher's printed text and its errata.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The relative statement now has a published proof, supplied by the owner for #123 and read in
    the text version: Tammo tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European
    Mathematical Society 2008, translation of the Ranicki text
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md` (read as text; the PDF was not opened).
    Theorem (6.3.1), statement on printed p. 129 and proof on printed p. 130, is exactly this
    statement: for a Serre fibration $p:E\to B$, $B_0\subset B$, $E_0=p^{-1}B_0$, and basepoints
    $\epsilon\in E_0$, $b=p(\epsilon)\in B_0$, the map $p_*:\pi_n(E,E_0,\epsilon)\to\pi_n(B,B_0,b)$
    is a bijection for $n\ge1$. The hypothesis that a covering is a Serre fibration is Theorem
    (3.2.2) on printed p. 66, with the definition of Serre fibration in §5.5 on printed p. 115, and
    the lifting lemma used twice is Proposition (3.2.4) on printed p. 67. The solution is that proof
    transcribed, in tom Dieck's cube model, which his Remark (6.1.4) on printed p. 125 identifies
    with the disk model $(D^n,S^{n-1})$ that the exercise uses. What the source gives is stronger
    than the exercise asks: $n\ge1$ rather than $n>1$. Checked against the exercise as printed on
    Hatcher's p. 358, whose hypothesis $\tilde A=p^{-1}(A)$ is the source's $E_0=p^{-1}B_0$ with
    $B_0=A$; the exercise is not Hatcher's Proposition 4.1 (printed p. 342), which is the absolute
    statement, and the relative case is not obtained from it by the five-lemma (the earlier note of
    2026-11-13 records why). Not claimed: that tom Dieck states the exercise; he states and proves
    the theorem the exercise asks for.
- event: solution-reviewed
  by: claude
  date: 2026-11-14
  note: >-
    Read the transcribed proof line by line against the source text: the lifting of the cube in
    (6.3.1)'s surjectivity half is Proposition (3.2.4) with the cube $I^{n-1}$ and the initial
    condition the constant map at $\epsilon$, legitimate because the representative $h$ carries
    $J^{n-1}$ to the basepoint; the injectivity half is (6.3.1)'s own subspace
    $T=I^n\times\partial I\cup J^{n-1}\times I$, whose image under the transposition of the last two
    coordinates is $J^n$ and to which (3.2.4) therefore applies, and the two ends of the resulting
    $H$ are the prescribed lifts. Checked that $H(\partial I^n\times\{t\})\subset E_0$ for every $t$
    follows from $pH=\varphi$ and $\varphi(\partial I^n\times I)\subset B_0$, which is what makes
    $H$ a homotopy of maps of triples rather than only of maps of pairs. Checked the exercise's
    printed statement on Hatcher's p. 358 against the source's hypothesis, the correspondence
    $B_0=A$, $E_0=p^{-1}(B_0)$, and the identification of models in (6.1.4), printed p. 125. Not
    verified: the Ranicki translation against tom Dieck's original German edition, which this
    machine does not hold; the proof is read in the translation.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The remark's description of the reading copy is removed. It said that in
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md` the colon of a map $p:E\to B$ is transcribed
    as `W` and the arrow as `!`, which described the earlier text version of the file; the reading
    copy now held there renders maps with `\colon` and `\to`. The sentence now names the reading copy
    and nothing more, which is all the citation needs. Nothing in the proof or in the source
    references changes. Checked against tom Dieck, *Algebraic Topology* (EMS Textbooks in
    Mathematics, 2008), Theorem (6.3.1) on printed pp. 129--130, and against Hatcher (2002), §4.1
    Exercise 6 on printed p. 358.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied to step #surjective: it is the surjectivity half of tom
    Dieck's proof of (6.3.1), printed p. 130, with the lifting lemma (3.2.4), printed p. 67, and
    the step now says so; the other three steps already named their pages. Checked: the two pages.

---

::: {.problem}
If $p: (\tilde{X}, \tilde{A}, \tilde{x}_0) \to (X, A, x_0)$ is a covering space with $\tilde{A} = p^{-1}(A)$, show that the map $p_*: \pi_n(\tilde{X}, \tilde{A}, \tilde{x}_0) \to \pi_n(X, A, x_0)$ is an isomorphism for all $n > 1$.
:::

::: {.solution}

Throughout, $\pi_n$ of a pointed pair is taken in tom Dieck's cube model

$$
\pi_n(X,A,x_0)=\bigl[(I^n,\partial I^n,J^{n-1}),(X,A,x_0)\bigr],
\qquad
J^{n-1}=\partial I^{n-1}\times I\cup I^{n-1}\times\{0\}\subset\partial I^n,
$$

and Remark (6.1.4) of tom Dieck, identifies this set with the homotopy classes of pointed maps $(D^n,S^{n-1})\to(X,A)$, which is the model the exercise uses. Put $B_0=A$ and $E_0=p^{-1}(A)=\tilde A$, and let $\epsilon\in E_0$ be a point over $b=p(\epsilon)\in B_0$; in the exercise's notation $\epsilon=\tilde x_0$ and $b=x_0$.

::: pf

::: {.pf-step #serre}

$p$ is a Serre fibration.

::: pf-proof

By (3.2.2), a covering $p:E\to B$ has the homotopy lifting property for every space, and by the definition in §5.5, a map with the homotopy lifting property for every space has it for every cube $I^n$, which is what a Serre fibration is.

:::

:::

::: {.pf-step #cube-lift}

Every map of triples $h:(I^n,\partial I^n,J^{n-1})\to(B,B_0,b)$, $n\ge1$, lifts to a map $H:I^n\to E$ with $pH=h$ and $\restrictionof{H}{J^{n-1}}$ the constant map at $\epsilon$.

::: pf-proof

Read $h$ as a homotopy $I^{n-1}\times I\to B$ in the last coordinate, and read $J^{n-1}=I^{n-1}\times\{0\}\cup\partial I^{n-1}\times I$ as a subspace of $I^{n-1}\times I=I^n$. Proposition (3.2.4), lifts such a homotopy once one is given a map $a:J^{n-1}\to E$ over $\restrictionof{h}{J^{n-1}}$; since $h(J^{n-1})=\{b\}$, the constant map $a=\mathrm{const}_\epsilon$ is such a lift, and step [](#serre){.pf-ref} supplies the homotopy lifting property for the cube $I^{n-1}$ that the proposition assumes. The conclusion is a map $H:I^{n-1}\times I\to E$ with $\restrictionof{H}{J^{n-1}}=a$ and $pH=h$.

:::

:::

::: {.pf-step #surjective}

$p_*:\pi_n(E,E_0,\epsilon)\to\pi_n(B,B_0,b)$ is surjective for $n\ge1$.

::: pf-proof

This is the surjectivity half of tom Dieck's proof of (6.3.1), with the lifting lemma Proposition (3.2.4). Let $x\in\pi_n(B,B_0,b)$ be represented by $h$. The lift $H$ of step [](#cube-lift){.pf-ref} has $pH=h$ and $H(J^{n-1})=\{\epsilon\}$, and $H(\partial I^n)\subset p^{-1}(B_0)=E_0$ because $h(\partial I^n)\subset B_0$. So $H$ is a map of triples $(I^n,\partial I^n,J^{n-1})\to(E,E_0,\epsilon)$ and $p_*[H]=[pH]=[h]$.

:::

:::

::: {.pf-step #injective}

$p_*$ is injective for $n\ge1$.

::: pf-proof

Let $f_0,f_1:(I^n,\partial I^n,J^{n-1})\to(E,E_0,\epsilon)$ be maps of triples with $p_*[f_0]=p_*[f_1]$, and let

$$
\varphi:\bigl(I^n\times I,\ \partial I^n\times I,\ J^{n-1}\times I\bigr)\longrightarrow(B,B_0,b)
$$

be a homotopy from $pf_0$ to $pf_1$ through maps of triples. Put $T=I^n\times\partial I\cup J^{n-1}\times I\subset\partial(I^n\times I)$ and define $G:T\to E$ by $G(u,t)=f_t(u)$ for $u\in I^n$ and $t\in\{0,1\}$, and $G(u,t)=\epsilon$ for $u\in J^{n-1}$ and $t\in I$. The two clauses agree on $J^{n-1}\times\partial I$, where $f_t(J^{n-1})=\{\epsilon\}$, so $G$ is a well-defined continuous map with $pG=\restrictionof{\varphi}{T}$. Transposing the last two coordinates carries $T$ to $J^n=\partial I^n\times I\cup I^n\times\{0\}$, the subspace of $\partial I^{n+1}$ to which (3.2.4), applies, so that proposition gives $H:I^n\times I\to E$ with $\restrictionof{H}{T}=G$ and $pH=\varphi$. For each $t$ the map $H(-,t)$ satisfies $H(\partial I^n\times\{t\})\subset p^{-1}(B_0)=E_0$, because $\varphi(\partial I^n\times I)\subset B_0$, and $H(J^{n-1}\times\{t\})=\{\epsilon\}$; and $H(-,0)=f_0$, $H(-,1)=f_1$. So $H$ is a homotopy of maps of triples from $f_0$ to $f_1$.

:::

:::

::: pf-step

$$
p_*:\pi_n(E,E_0,\epsilon)\xrightarrow{\ \cong\ }\pi_n(B,B_0,b)\quad\text{for all }n\ge1,
\qquad
\boxed{p_*:\pi_n(\tilde X,\tilde A,\tilde x_0)\xrightarrow{\ \cong\ }\pi_n(X,A,x_0)\ \text{ for all }n>1.}
$$

::: pf-proof

Steps [](#surjective){.pf-ref} and [](#injective){.pf-ref} give a bijection for every $n\ge1$, and $n>1$ is a case of $n\ge1$.

:::

:::

:::

In the notation of the exercise, $E=\tilde X$, $E_0=\tilde A=p^{-1}(A)$, $\epsilon=\tilde x_0$ and $b=x_0$, so the bijection just proved is the one the exercise asks for.

:::

::: {.remark title="Source"}

The exercise is Exercise 6 of §4.1 (Hatcher read in the text version `tmp/sources/hatcher-2002-algebraic-topology.md`). The proof above is transcribed from **Tammo tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European Mathematical Society 2008**: Theorem (6.3.1), stated and proved in §6.3, with the input that a covering is a fibration from Theorem (3.2.2), the lifting lemma Proposition (3.2.4), the definition of a Serre fibration in §5.5, and the identification of the cube model with the disk model in Remark (6.1.4). The reading copy is the text of the Ranicki translation held as `tmp/sources/tomdieck-algebraic-topology-ranicki.md`. The theorem is stronger than the exercise in one direction and more general in another: it holds for $n\ge1$ rather than $n>1$, and it takes an arbitrary subspace $B_0\subset B$ with $E_0=p^{-1}(B_0)$, the exercise being the case $B_0=A$.

Hatcher's Proposition 4.1 with its proof there, is the absolute statement only: for a covering space projection $p:(\tilde X,\tilde x_0)\to(X,x_0)$, the map $p_*:\pi_n(\tilde X,\tilde x_0)\to\pi_n(X,x_0)$ is an isomorphism for all $n\ge2$. The relative statement is not a proposition of the book, and it does not follow from Proposition 4.1 by the five-lemma on the ladder of Theorem 4.3: the map $p_*:\pi_1(\tilde A,\tilde x_0)\to\pi_1(A,x_0)$ is injective and in general not surjective, so at $\pi_2$ the five-lemma gives injectivity and not surjectivity. The source's proof avoids the ladder: it lifts the cube and the relative homotopy themselves, which is what replaces the simply connected $D^n$ of Proposition 4.1's argument by the lifting lemma (3.2.4) for the pair of subspaces $J^n\subset I^{n+1}$.

:::
