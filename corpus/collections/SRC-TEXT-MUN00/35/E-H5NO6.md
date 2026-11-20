---
schema: qual/card@1
id: E-H5NO6
kind: problem
title: Retracts of Hausdorff spaces and the plane
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S35.pdf, Exercise 35.4, page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S35.pdf, Internet Archive snapshot 20220130234235),
    checked against Munkres, Topology (2000), Section 35 Exercise 4, printed p. 223, Exercise 31.5 and
    Theorem 23.5. Its three parts are the card's: Y is the equalizer of the retraction and the
    identity, hence closed in a Hausdorff Z; a retract of the connected plane is connected while a
    two-point set is not; and x -> x/|x| retracts the punctured plane onto the circle. What was
    corrected: "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 35.4, printed
    p. 13, argues (b) by "since A is Hausdorff as a subspace of R^2, there are disjoint open sets
    for each of the points in A, which form a separation of A", which is not valid as stated -- every
    Hausdorff space would be disconnected by that reasoning; the card uses connectedness of the
    plane, which is Moller's argument.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The solution opened by claiming that no retained solution set covers the exercise, contradicting the
    audit note above it, which transcribes Moller's file S35.pdf Exercise 35.4 from the copy kept at
    tmp/sources/munkres-solutions-poulsen-S35.md. That copy was read again: it answers all three parts,
    citing Exercise 31.5, Theorem 23.5 and the retraction $x/\abs x$, and leaves the book's closing
    question unanswered, which is the one step the card supplies itself. The opening sentence now names
    the set, its three citations and the card's own addition. Not checked here: the printed page of the
    exercise, which is the earlier session's citation, not re-read in this session.

---

::: {.exercise}

Let $Z$ be a topological space.
If $Y$ is a subspace of $Z$, we say that $Y$ is a retract of $Z$ if there is a continuous map $r: Z \to Y$ such that $r(y) = y$ for each $y \in Y$.

(a) Show that if $Z$ is Hausdorff and $Y$ is a retract of $Z$, then $Y$ is closed in $Z$.

(b) Let $A$ be a two-point set in $\RR^2$.
Show that $A$ is not a retract of $\RR^2$.

(c) Let $S^1$ be the unit circle in $\RR^2$; show that $S^1$ is a retract of $\RR^2 - \theset{\mathbf{0}}$, where $\mathbf{0}$ is the origin.
Can you conjecture whether or not $S^1$ is a retract of $\RR^2$?
:::

::: {.solution}

Parts (a), (b) and (c) are the retained published solution of Jesper Michael Møller, *Solutions to exercises in Munkres*, file `S35.pdf`, Exercise 35.4 (`tmp/sources/munkres-solutions-poulsen-S35.md`): $Y=\{z\in Z\mid r(z)=z\}$ is closed in a Hausdorff $Z$ by Exercise 31.5, a retract of $\RR^{2}$ is connected by Theorem 23.5 while a two-point set is not, and $r(x)=x/\abs x$ retracts the punctured plane onto $S^{1}$. The card states (a) as the equalizer of $r$ and the identity and answers the closing conjecture, which the sheet leaves as the book's question, in its own step. Checked against Munkres, *Topology* (2000), Section 35 Exercise 4, Exercise 31.5 and Theorem 23.5; "Doug's World"'s (b) is not used, because its separation argument would disconnect every Hausdorff space.

Recall that $Y\subseteq Z$ is a retract of $Z$ when there is a continuous $r:Z\to Y$ with $r(y)=y$ for $y\in Y$.

::: pf

::: {.pf-step #closed}
(a) If $Z$ is Hausdorff and $Y$ is a retract of $Z$, then $Y$ is closed in $Z$.

::: pf-proof
Let $i:Y\to Z$ be the inclusion, which is continuous, and $r:Z\to Y$ a retraction; then $R=i\circ r:Z\to Z$ is continuous. For $z\in Z$ one has $R(z)=r(z)\in Y$, and $z\in Y$ gives $R(z)=r(z)=z$; conversely $R(z)=z$ puts $z=R(z)$ in the image of $R$, which lies in $Y$. So $Y=\theset{z\in Z\mid R(z)=z}$ is the equalizer of the continuous maps $R$ and $\mathrm{id}_{Z}$ into the Hausdorff space $Z$, which is closed in $Z$ (card [[E-DWC4M]], the equalizer of two maps into a Hausdorff space).
:::

:::

::: {.pf-step #two-points}
(b) A two-point set $A\subseteq\RR^{2}$ is not a retract of $\RR^{2}$.

::: pf-proof
If $r:\RR^{2}\to A$ were a retraction then $r$ would be a continuous surjection, so $A=r(\RR^{2})$ would be connected, being a continuous image of the connected space $\RR^{2}$ (Theorem 23.5). But the two-point space $A$ is a subspace of the Hausdorff space $\RR^{2}$, hence Hausdorff, and a Hausdorff space with two points is disconnected: its points are disjoint nonempty open sets. Contradiction.
:::

:::

::: {.pf-step #circle}
(c) $S^{1}$ is a retract of $\RR^{2}\setminus\{\mathbf{0}\}$.

::: pf-proof
The radial map $r(x)=x/\norm{x}$ is continuous on $\RR^{2}\setminus\{\mathbf{0}\}$, since $\norm{x}\ne0$ there and $x\mapsto\norm{x}$ and division by a nonzero continuous function are continuous; its image lies in $S^{1}$ because $\norm{r(x)}=1$, and for $x\in S^{1}$ one has $r(x)=x/\norm{x}=x$. So $r$ is a retraction onto $S^{1}$.
:::

:::

::: {.pf-step #conjecture}
$S^{1}$ should not be a retract of $\RR^{2}$.

::: pf-proof
The question is recorded as a conjecture, as the exercise asks; the answer is the classical no-retraction theorem, which is proved in the book by the fundamental group, since the induced map $\pi_{1}(S^{1})\to\pi_{1}(\RR^{2})$ would have to be both a monomorphism and (as the inclusion followed by a retraction gives the identity) an isomorphism into the trivial group $\pi_{1}(\RR^{2})=0$.
:::

:::

::: {.pf-qed}
Part (a) is step [](#closed){.pf-ref}, part (b) is step [](#two-points){.pf-ref}, and part (c) is step [](#circle){.pf-ref} with the conjecture recorded in step [](#conjecture){.pf-ref}.
:::

:::

:::
