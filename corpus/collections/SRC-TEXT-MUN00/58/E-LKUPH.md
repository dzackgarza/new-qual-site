---
schema: qual/card@1
id: E-LKUPH
kind: problem
title: Transitivity of deformation retracts
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
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
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 1, printed p. 366,
    with the definition of a deformation retraction and the pasting lemma (Theorem 18.3). The card pastes $H$ on the first half of the interval to $K\circ(H(\cdot,1))$ on the second and checks the three defining properties. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located, in two sets: UC Riverside Math 205A, Fall 2014,
    Solutions Part 7, Munkres §58 Exercise 1, the sheet's p. 8, and Pearse, *Topology (2nd ed.) —
    James R. Munkres*, solutions, Cornell 2005, §58 Exercise 1, his p. 20, both held in
    tmp/sources and read in the MinerU extractions. The solution transcribes the sheet's
    composition argument ($s\circ r$ is a retraction, $e\circ s\circ r$ is homotopic to
    $e\circ r$ through $K$ and $e\circ r$ to the identity through $H$, and homotopy is transitive)
    and records Pearse's two-stage formula for the resulting deformation retraction. Both proofs
    are correct and neither needed repair; the sheet's remark that Munkres's "deformation
    retract" is the strong one is right, and is why the homotopies may be taken to fix $B$. Checked
    against the book: the exercise on printed p. 366, the definition of deformation retract on
    printed p. 360, the pasting lemma (Theorem 18.3) on printed p. 108, and Lemma 51.1 on printed
    p. 324, whose argument is what makes homotopy fixed on a subspace transitive. Not claimed:
    that the sheet states the pasting argument -- it takes continuity of the two-stage formula for
    granted.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, with the sources and their pages named
    in its own text. The earlier proof wrote Pearse's two-stage formula directly and checked its
    three defining properties; it was a correct proof and was replaced because the card is to
    carry the published arguments and the reason the composition works.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Step 3 corrected: it read "$G(x,t)=x$ whenever $r(x)\in B$", which is false — $G$ is
    $e\bigl(K(r(x),t)\bigr)$, and since $K$ fixes $B$ pointwise the value is $r(x)$, not $x$,
    whenever $r(x)\in B$. The sentence now states $G(x,t)=r(x)$ there and singles out the case the
    conclusion uses, $x\in B$, where $r(x)=x$ and so $G(x,t)=x$. The conclusion is unchanged and
    did not depend on the false general clause. Checked against the book: the exercise on printed
    p. 366 and the definition of deformation retract on printed p. 360; the two-stage formula of
    step 4 was re-read and is unaffected.
---

::: {.exercise}

Show that if $A$ is a deformation retract of $X$, and $B$ is a deformation retract of $A$, then $B$ is a deformation retract of $X$.
:::

::: {.solution}
The exercise is §58 Exercise 1, printed p. 366, and the notion is the book's
definition of a deformation retract on printed p. 360: $A\subseteq X$ is a
deformation retract of $X$ when there is a continuous $H:X\times I\to X$ with
$H(x,0)=x$ and $H(x,1)\in A$ for all $x\in X$, and $H(a,t)=a$ for all $a\in A$.
The last clause is what some texts call a *strong* deformation retraction, and
both sources below use the book's version.

The proof is transcribed from UC Riverside Math 205A, Fall 2014, Solutions Part
7, Munkres §58 Exercise 1, the sheet's p. 8, held at
`tmp/sources/ucr-math205A-2014-solutions07.md`, which composes the two
deformation retractions. Pearse, *Topology (2nd ed.) — James R. Munkres*,
solutions, Cornell 2005, §58 Exercise 1, his p. 20, proves the same statement by
writing the composite homotopy in two stages, and that formula is step
[](#two-stage){.pf-ref}.

::: pf

::: {.pf-step #data}
There are maps $r:X\to A$ and $s:A\to B$ with $\restrictionof{r}{A}=\operatorname{id}_A$ and
$\restrictionof{s}{B}=\operatorname{id}_B$, and homotopies $H:\operatorname{id}_X\simeq r$ fixed on
$A$ and $K:\operatorname{id}_A\simeq s$ fixed on $B$.

::: pf-proof
Let $H:X\times I\to X$ be a deformation retraction of $X$ onto $A$ and put
$r(x)=H(x,1)$; then $r(X)\subseteq A$, $H$ is a homotopy from
$\operatorname{id}_X$ to $r$, and $r(a)=H(a,1)=a$ for $a\in A$. Let
$K:A\times I\to A$ be a deformation retraction of $A$ onto $B$ and put
$s(a)=K(a,1)$; then $s(A)\subseteq B$, $K$ is a homotopy from
$\operatorname{id}_A$ to $s$, and $s(b)=K(b,1)=b$ for $b\in B$.
:::

:::

::: {.pf-step #retraction}
$\rho=s\circ r:X\to B$ satisfies $\restrictionof{\rho}{B}=\operatorname{id}_B$.

::: pf-proof
For $b\in B$ we have $b\in A$, so $r(b)=b$ by step [](#data){.pf-ref}, and then
$\rho(b)=s(r(b))=s(b)=b$.
:::

:::

::: {.pf-step #composite}
The composite $e\circ\rho:X\to X$, where $e:B\to X$ is the inclusion, is
homotopic to $\operatorname{id}_X$ by a homotopy that fixes $B$ pointwise.

::: pf-proof
First, $K$ is a homotopy from $\operatorname{id}_A$ to $s$ fixing $B$, so
$$
G:X\times I\to X,\qquad G(x,t)=e\bigl(K(r(x),t)\bigr),
$$
is continuous, and it is a homotopy from $e\circ s\circ r=e\circ\rho$ to
$e\circ\operatorname{id}_A\circ r=e\circ r$; moreover $G(x,t)=r(x)$ whenever
$r(x)\in B$, because $K$ fixes the points of $B$. In particular $G(x,t)=x$ for
every $x\in B$: there $r(x)=x$ because $\restrictionof{r}{A}$ is the identity and
$B\subseteq A$, so $r(x)\in B$ and $G(x,t)=r(x)=x$.

Second, $H$ is a homotopy from $\operatorname{id}_X$ to $r$ and it fixes $A$,
hence fixes $B$.

Homotopy is transitive, by the argument of Lemma 51.1 (printed p. 324) applied to
homotopies that fix $B$ pointwise, so the two compose to a homotopy from
$e\circ\rho$ to $\operatorname{id}_X$ fixing $B$ pointwise.
:::

:::

::: {.pf-step #two-stage}
$\boxed{B\ \text{is a deformation retract of}\ X}$, by the deformation retraction
$$
F(x,t)=
\begin{cases}
H(x,2t), & 0\le t\le\tfrac12,\\[2pt]
K\bigl(r(x),2t-1\bigr), & \tfrac12\le t\le1.
\end{cases}
$$

::: pf-proof
The two formulas agree at $t=\tfrac12$, where $H(x,1)=r(x)=K(r(x),0)$, so $F$ is
continuous by the pasting lemma (Theorem 18.3, printed p. 108) on the two closed
sets $X\times[0,\tfrac12]$ and $X\times[\tfrac12,1]$. Further $F(x,0)=H(x,0)=x$
and $F(x,1)=K(r(x),1)=s(r(x))=\rho(x)\in B$; and for $b\in B$ we have
$F(b,t)=H(b,2t)=b$ for $t\le\tfrac12$, while $F(b,t)=K(r(b),2t-1)=K(b,2t-1)=b$
for $t\ge\tfrac12$, because $r(b)=b$ and $K$ fixes $B$. So $F$ is a deformation
retraction of $X$ onto $B$ in the sense of printed p. 360, which is the
assertion.
:::

:::

:::
:::
