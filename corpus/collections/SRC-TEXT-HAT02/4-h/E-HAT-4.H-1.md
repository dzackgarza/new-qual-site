---
schema: qual/card@1
id: E-HAT-4.H-1
kind: problem
title: "Cofibrations give fibrations on function spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.H, Exercise 1; the stored statement matches.
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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the adjunction as separate steps. Re-checked: the
    exponential law applies because $X$ and $A$ are compact Hausdorff, so $f_0$ and $g$ are adjoint
    to $F_0$ and $G$ agreeing on $Z\times\{0\}\times A$; the cofibration $A\hookrightarrow X$ stays
    one after product with $Z$, which gives the extension property for the inclusion of
    $(Z\times X\times\{0\})\cup(Z\times A\times I)$; the two formulas defining the map on that
    subspace agree on the intersection; and adjunction returns a homotopy of $f_0$ lifting $g$.
    Added: the explicit statement of the extension property as the form of the homotopy extension
    property that is used, and the verification that $f_0$ and $g$ agree on the intersection after
    restricting. No defect found in the statement, §4.H Exercise 1; no retained solution set covers
    it.
---

::: {.problem}
Show that if $A \hookrightarrow X$ is a cofibration of compact Hausdorff spaces, then for any space $Y$, the map $Y^X \to Y^A$ obtained by restriction of functions is a fibration.
[If $A \hookrightarrow X$ is a cofibration, so is $A \times Y \hookrightarrow X \times Y$ for any space $Y$.]
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; it is the adjunction between a homotopy and its transpose that turns the homotopy extension property into the homotopy lifting property. Write $i\colon A\hookrightarrow X$ for the cofibration and $r\colon Y^X\to Y^A$ for restriction, with the compact-open topology on mapping spaces.

::: pf

::: {.pf-step #definitions}
A cofibration is a map with the homotopy extension property and a fibration is a map with the homotopy lifting property for all spaces.

::: pf-proof
These are the definitions of §0.4 (p. 14) and of p. 375 respectively. The pair $(X,A)$ has the homotopy extension property exactly when the inclusion $(X\times\{0\})\cup(A\times I)\hookrightarrow X\times I$ has the extension property for maps into every space, which is the form used below.
:::

:::

::: {.pf-step #adjoint}
Given $Z$, a map $f_0\colon Z\to Y^X$ and a homotopy $g\colon Z\times I\to Y^A$ with $g(z,0)=r(f_0(z))$, there are adjoint maps $F_0\colon Z\times X\to Y$ and $G\colon Z\times I\times A\to Y$ agreeing on $Z\times\{0\}\times A$.

::: pf-proof
$X$ and $A$ are compact Hausdorff, so the exponential law (Proposition A.16, p. 531) identifies maps $Z\to Y^X$ with maps $Z\times X\to Y$ and maps $Z\times I\to Y^A$ with maps $Z\times I\times A\to Y$. Under these identifications $f_0$ corresponds to $F_0$ and $g$ to $G$, and the condition $g(z,0)=r(f_0(z))$ says that both restrict to the same map on $Z\times\{0\}\times A$, since $r$ is restriction of functions.
:::

:::

::: {.pf-step #extension}
The inclusion $(Z\times X\times\{0\})\cup(Z\times A\times I)\hookrightarrow Z\times X\times I$ has the extension property for maps into $Y$.

::: pf-proof
$A\hookrightarrow X$ is a cofibration, and a cofibration remains one after taking the product with any space, which is the printed hint; so $Z\times A\hookrightarrow Z\times X$ has the homotopy extension property. By the form of that property recalled in step [](#definitions){.pf-ref}, the inclusion $(Z\times X\times\{0\})\cup(Z\times A\times I)\hookrightarrow Z\times X\times I$ therefore has the extension property for maps into every space, in particular into $Y$.
:::

:::

::: {.pf-step #lift}
There is a homotopy $\widetilde g\colon Z\times I\to Y^X$ with $\widetilde g(-,0)=f_0$ and $r\widetilde g=g$.

::: pf-proof
Define a map on $(Z\times X\times\{0\})\cup(Z\times A\times I)$ by $(z,x,0)\mapsto F_0(z,x)$ and $(z,a,t)\mapsto G(z,t,a)$; the two formulas agree on the intersection $Z\times A\times\{0\}$ by step [](#adjoint){.pf-ref}, so this is well defined and continuous on the closed subspace. The extension property of step [](#extension){.pf-ref} extends it to $\widetilde G\colon Z\times X\times I\to Y$. Adjointing back gives $\widetilde g\colon Z\times I\to Y^X$, whose value at time $0$ is $f_0$ and whose composite with $r$ is $g$ by construction.
:::

:::

::: {.pf-step}
$\boxed{Y^X\to Y^A\text{ is a fibration}}$.

::: pf-proof
Steps [](#adjoint){.pf-ref} and [](#lift){.pf-ref} show that for every space $Z$, every $f_0\colon Z\to Y^X$ and every homotopy of $r\circ f_0$ there is a homotopy of $f_0$ lifting it, which is the homotopy lifting property of $r$ for all $Z$; that is the definition of a fibration.
:::

:::

:::
:::
