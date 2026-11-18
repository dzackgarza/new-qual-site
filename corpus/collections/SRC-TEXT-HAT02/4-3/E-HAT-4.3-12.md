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

---

::: {.problem}
Show that for homotopic maps $f, g: A \to B$ the fibrations $E_f \to B$ and $E_g \to B$ are fiber homotopy equivalent.
:::

::: {.solution}

The argument is the card's own: the homotopy is used to prepend paths, and a path followed by its reverse is contracted by a reparametrisation.

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
On $E_{f}$, the composite sends $(a,\gamma)$ to $(a,\,H_{a}*(\overline{H_{a}}*\gamma))$, which is the path $\gamma$ preceded by the backtracking path $H_{a}*\overline{H_{a}}$ from $f(a)$ to $f(a)$. Since a path followed by its reverse is homotopic to the constant path relative to the endpoints — the standard contraction, which at time $s$ traverses $H_{a}$ on $[0,(1-s)/2]$, then $\overline{H_{a}}$ on $[(1-s)/2,1-s]$, and stays at $f(a)$ on $[1-s,1]$ — and since concatenation and reparametrisation are continuous in the data, there is a homotopy
$$
(a,\gamma,s)\longmapsto\big(a,\ \text{the reparametrised concatenation at time } s\big)
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
