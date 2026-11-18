---
schema: qual/card@1
id: E-HAT-4.3-8
kind: problem
title: "Fibrations from sections of $E^I \\to E_p$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 8; corrected the stored one-way implication to Hatcher's if-and-only-if statement.
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
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located among the retained Hatcher sets, so the argument is the card's own. Checked against
    Hatcher, Section 4.3 Exercise 8, printed p. 420, and the homotopy lifting property as defined
    there. Each step re-read: a lifting problem gives a map into the pullback E_p by taking the
    pair (f(x), H_x), which is continuous because x -> H_x is the adjoint of H; the section
    evaluated at t lifts because both coordinates of pi s are known; conversely the universal
    problem over E_p with the homotopy K((e,alpha),t) = alpha(t) starts at p q, and its lift,
    read as a path, is a section. Not claimed: any statement about Serre fibrations versus
    Hurewicz fibrations, or about a section of pi over a subspace of E_p only.
---

::: {.problem}
Show that a map $p: E \to B$ is a fibration if and only if the map $\pi: E^I \to E_p$, $\pi(\gamma) = (\gamma(0), p\gamma)$ has a section, that is, a map $s: E_p \to E^I$ such that $\pi s = \id$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves Section 4.3 Exercise 8. It is checked against Hatcher, Algebraic Topology, Section 4.3 Exercise 8, printed p. 420, and against the homotopy lifting property as defined there.

::: pf

::: {.pf-step #setup}
Let
$$
E_p=\{(e,\alpha)\in E\times B^I: p(e)=\alpha(0)\},\qquad \pi:E^I\to E_p,\quad \pi(\gamma)=(\gamma(0),p\gamma).
$$
The space $E_p$ is the pullback of $p$ along evaluation at $0$, and $\pi$ is continuous because evaluation and composition with $p$ are.

::: pf-proof
$E_p$ is a subspace of $E\times B^I$, defined by the equation $p(e)=\alpha(0)$; the defining equation is closed, and both maps entering $\pi$ are continuous (evaluation at $0$ on $E^I$, and $p$ composed with evaluation at $0$ on $B^I$), so $\pi$ is continuous.
:::

:::

::: {.pf-step #sectionimplies}
If $\pi$ has a section $s$, then $p$ has the homotopy lifting property.

:::: pf-proof

::: {.pf-step #liftingdata}
Let $f:X\to E$ and $H:X\times I\to B$ satisfy $H(x,0)=p f(x)$.

::: pf-proof
This is the data of a lifting problem; write $H_x$ for the path $t\mapsto H(x,t)$.
:::

:::

::: {.pf-step #intopullback}
The formula $\Phi(x)=(f(x),H_x)$ defines a map $\Phi:X\to E_p$.

::: pf-proof
$\Phi$ is continuous because $f$ is and $x\mapsto H_x$ is the adjoint of the continuous map $H$. Its values lie in $E_p$ because $p(f(x))=H(x,0)=H_x(0)$ by the hypothesis on $H$.
:::

:::

::: {.pf-step #lift}
$\widetilde H(x,t)=s\bigl(\Phi(x)\bigr)(t)$ is a lift of $H$ starting at $f$.

::: pf-proof
$\widetilde H$ is continuous as the composite of $\Phi$, $s$ and evaluation. At $t=0$, $\widetilde H(x,0)=s(\Phi(x))(0)$; since $\pi s=\operatorname{id}$, the first coordinate of $\pi s(\Phi(x))$, which is $s(\Phi(x))(0)$, equals the first coordinate of $\Phi(x)$, namely $f(x)$. And $p\widetilde H(x,t)=p\,s(\Phi(x))(t)$, which is the second coordinate of $\pi s(\Phi(x))=\Phi(x)$ evaluated at $t$, namely $H_x(t)=H(x,t)$.
:::

:::

:::

:::

::: {.pf-step #fibrationimplies}
If $p$ is a fibration, then $\pi$ has a section.

:::: pf-proof

::: {.pf-step #problem}
The maps $q:E_p\to E$, $q(e,\alpha)=e$, and $K:E_p\times I\to B$, $K((e,\alpha),t)=\alpha(t)$, satisfy $K(-,0)=p q$.

::: pf-proof
Both are continuous (projections and evaluation), and $K((e,\alpha),0)=\alpha(0)=p(e)=p q(e,\alpha)$ by the definition of $E_p$.
:::

:::

::: {.pf-step #hlp}
There is a lift $\widetilde K:E_p\times I\to E$ with $\widetilde K(-,0)=q$ and $p\widetilde K=K$.

::: pf-proof
This is the homotopy lifting property of $p$ applied to the map $q$ and the homotopy $K$ starting at $pq$.
:::

:::

::: {.pf-step #section}
$s(e,\alpha)(t)=\widetilde K((e,\alpha),t)$ defines a section of $\pi$.

::: pf-proof
$s$ is continuous as the adjoint of the continuous map $\widetilde K$. At $t=0$, $s(e,\alpha)(0)=\widetilde K((e,\alpha),0)=q(e,\alpha)=e$, and $p\,s(e,\alpha)(t)=p\widetilde K((e,\alpha),t)=K((e,\alpha),t)=\alpha(t)$, so $p\,s(e,\alpha)=\alpha$. Hence $\pi s(e,\alpha)=s(e,\alpha)(0),p\,s(e,\alpha)=(e,\alpha)$.
:::

:::

:::

:::

::: {.pf-step}
$p$ is a fibration if and only if $\pi:E^I\to E_p$ has a section.

::: pf-proof
Steps [](#sectionimplies){.pf-ref} and [](#fibrationimplies){.pf-ref} prove the two implications. In the forward direction the section is produced from the lifting property applied to the universal example $E_p$; in the reverse direction the lifting property for an arbitrary $X$ is obtained from the section by adjunction. No hypothesis on $B$ or on the spaces $X$ is needed beyond the maps being continuous.
:::

:::

:::
:::
