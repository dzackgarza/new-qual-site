---
schema: qual/card@1
id: E-HAT-4.3-12
kind: problem
title: "Homotopic maps give fiber homotopy equivalent fibrations"
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
  date: 2026-11-21
  note: >-
    Citation convention. Every locator of the form "printed page N" or "PDF page N" written into
    this card before today, here and in the events below, is superseded: sources are cited by
    chapter, section and numbered statement only. The events below are left as their sessions wrote
    them, as QUAL-11 requires, so their locators stand as a historical record; the statement and the
    solution above are the current text and cite by number. This event records the convention and no
    further reading: the mathematics of the card is as the events below describe it.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 12, printed p. 420,
    and Proposition 4.62, printed p. 406. The maps Phi and Psi, their being fibre
    preserving, and the shape of the two composites are right. The homotopy contracting
    Psi Phi was described by a parametrization that at time s traverses H_a on
    [0,(1-s)/2], the reverse on [(1-s)/2,1-s] and then stays at f(a) on [1-s,1], which
    at s = 1 gives the constant path at f(a), not gamma: it contracts the whole
    concatenation and changes the endpoint, so it is not a fibre homotopy to the
    identity. Repaired to contract the backtracking loop inside a shrinking initial
    segment while gamma is reparametrized onto the rest, which is (Psi Phi)(a,gamma) at
    s = 0 and gamma at s = 1 and keeps the endpoint gamma(1) throughout. Independent
    reports from the swarm flagged the same defect. Statement unchanged. Not checked:
    nothing outside this exercise.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 12; the stored statement matches.
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
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.3 Exercise 12, printed p. 420, and the retained solution of
    Steven V. Sam, §4.3 Exercise 12, printed p. 27 of
    `tmp/sources/hatcher-solutions-sam-2008.pdf`. The maps $\Phi$ and $\Psi$, their being
    fibre-preserving and the two composites are correct, and the repair of 2026-11-19 states
    the right contraction; one error remained in its parametrization. At $s=0$ the three pieces
    occupied $[0,\tfrac14]$, $[\tfrac14,\tfrac12]$ and $[\tfrac12,1]$, a reparametrized
    $(H_a*\overline{H_a})*\gamma$ and not the composite $H_a*(\overline{H_a}*\gamma)$ the card
    said it started from. The breakpoints are now $(1-s)/2$ and $3(1-s)/4$, so the $s=0$ path
    is exactly $H_a*(\overline{H_a}*\gamma)$ and the $s=1$ path is $\gamma$. The lead said the
    argument was the card's own; Sam's set covers the exercise and is now cited. Not checked:
    no certificate, and only the $\Psi\Phi$ composite was recomputed, $\Phi\Psi$ being the same
    argument with $H$ replaced by its reverse.

---

::: {.problem}
Show that for homotopic maps $f, g: A \to B$ the fibrations $E_f \to B$ and $E_g \to B$ are fiber homotopy equivalent.
:::

::: {.solution}

The construction is that of the retained solution set: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.3 Exercise 12**, which sends $(a,\gamma)$ to $(a,\overline{H_{a}}\cdot\gamma)$ and states that the two composites are fiber homotopic to the identities. The explicit contraction, with its parametrization, is the card's own.

Let $f,g:A\to B$ be homotopic and let
$$
E_{f}=\{(a,\gamma):\gamma(0)=f(a)\},\qquad p_{f}(a,\gamma)=\gamma(1),
$$
and similarly $E_{g}$ with $\gamma(0)=g(a)$.

::: pf

::: {.pf-step #maps}
A homotopy $H:A\times I\to B$ from $f$ to $g$, with $H_{a}(t)=H(a,t)$ a path from $f(a)$ to $g(a)$, gives maps
$$
\Phi:E_{f}\to E_{g},\ \Phi(a,\gamma)=(a,\overline{H_{a}}*\gamma),\qquad \Psi:E_{g}\to E_{f},\ \Psi(a,\delta)=(a,H_{a}*\delta),
$$
where $\overline{H_{a}}$ is the reverse path.

::: pf-proof
$H_{a}$ runs from $f(a)$ to $g(a)$, so its reverse $\overline{H_{a}}$ runs from $g(a)$ to $f(a)$; concatenating with $\gamma$, which starts at $f(a)$, gives a path from $g(a)$ to $\gamma(1)$, so $(a,\overline{H_{a}}*\gamma)\in E_{g}$. Symmetrically $\delta$ starts at $g(a)$ and $H_{a}*\delta$ is a path from $f(a)$ to $\delta(1)$, so $(a,H_{a}*\delta)\in E_{f}$. Both constructions are continuous in $(a,\gamma)$ because $H$ and the concatenation operation are.
:::

:::

::: {.pf-step #fiber-preserving}
$p_{g}\Phi=p_{f}$ and $p_{f}\Psi=p_{g}$.

::: pf-proof
The endpoint of $\overline{H_{a}}*\gamma$ is the endpoint of $\gamma$, so $p_{g}\Phi(a,\gamma)=\gamma(1)=p_{f}(a,\gamma)$; likewise the endpoint of $H_{a}*\delta$ is that of $\delta$.
:::

:::

::: {.pf-step #composites}
$\Psi\Phi\simeq1_{E_{f}}$ and $\Phi\Psi\simeq1_{E_{g}}$ through fiber-preserving homotopies.

::: pf-proof
On $E_{f}$, the composite sends $(a,\gamma)$ to $(a,\,H_{a}*(\overline{H_{a}}*\gamma))$, which is the path $H_{a}*(\overline{H_{a}}*\gamma)$, a loop at $f(a)$ followed by $\gamma$. The loop $H_{a}*\overline{H_{a}}$ is contracted inside a shrinking initial segment while $\gamma$ keeps the rest of the interval: at time $s\in[0,1]$ the path traverses $H_{a}$ on $\bigl[0,(1-s)/2\bigr]$, then $\overline{H_{a}}$ on $\bigl[(1-s)/2,3(1-s)/4\bigr]$, then $\gamma$ reparametrized affinely onto $\bigl[3(1-s)/4,1\bigr]$. At $s=0$ the three pieces occupy $\bigl[0,\tfrac12\bigr]$, $\bigl[\tfrac12,\tfrac34\bigr]$ and $\bigl[\tfrac34,1\bigr]$, which is exactly the concatenation $H_{a}*(\overline{H_{a}}*\gamma)=(\Psi\Phi)(a,\gamma)$; at $s=1$ the first two pieces have length zero and the path is $\gamma$ itself; and at every $s$ it runs from $f(a)$ to $\gamma(1)$, because the contracted piece is a loop at $f(a)$. Reparametrization and concatenation are continuous in $(a,\gamma,s)$, so this is a homotopy
$$
(a,\gamma,s)\longmapsto\bigl(a,\ \text{the reparametrized concatenation at time } s\bigr)
$$
from $\Psi\Phi$ to the identity. Each stage leaves the endpoint unchanged, so the homotopy is fiber-preserving. The same argument with $g$ in place of $f$ and $\overline{H_{a}}$ in place of $H_{a}$ contracts $H_{a}$ followed by its reverse, giving $\Phi\Psi\simeq1_{E_{g}}$.
:::

:::

::: {.pf-step #conclusion}
$E_{f}\to B$ and $E_{g}\to B$ are fiber homotopy equivalent.

::: pf-proof
Steps [](#fiber-preserving){.pf-ref} and [](#composites){.pf-ref} exhibit fiber-preserving maps $\Phi$ and $\Psi$ between the total spaces with $p_{g}\Phi=p_{f}$ and $p_{f}\Psi=p_{g}$ whose composites are fiber homotopically the identities. That is precisely a fiber homotopy equivalence over $B$:
$$
\boxed{E_{f}\to B\ \text{and}\ E_{g}\to B\ \text{are fiber homotopy equivalent}.}
$$
:::

:::

:::
:::
