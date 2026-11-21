---
schema: qual/card@1
id: E-HAT-4.H-4
kind: problem
title: "Dual of an iterated mapping cylinder"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 4 of §4.H, printed p. 462, whose wording the problem block
    reproduces. Checked the definition as a definition: the conditions $\phi_\sigma|_\tau =
    f_{\max\sigma,\max\tau}\circ\phi_\tau$ are consistent over chains
    $\rho\subseteq\tau\subseteq\sigma$ because the $f_{ji}$ compose, and for $n=1$ the data reduce
    to $\gamma(0)=f_1(\phi_{v_0})$ and $\gamma(1)=\phi_{v_1}$, which is the mapping path space
    $E_{f_1}$ of printed p. 405, the Eckmann--Hilton dual of the mapping cylinder. Checked the
    pages the card uses: $\Delta X$ for a complex of spaces and the surrounding discussion are on
    printed p. 459 inside §4.G, which the table of contents puts at p. 456, and §4.H begins on
    printed p. 460. The passage from $\nabla(f_1,\dots,f_n)$ to $\nabla X$ reverses the structure
    maps, which is what the duality requires. Not claimed: a certificate, and no uniqueness claim
    for the definition, which the exercise does not ask for.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher §4.H Exercise 4, the Eckmann--Hilton duality discussion that precedes it,
    the definition of $\Delta X$ in §4.G and the mapping path space of §4.3. The definition is
    right: dualizing the quotient $\coprod_\sigma X_{\min\sigma}\times\sigma$ of the iterated
    mapping cylinder gives the subspace of $\prod_\sigma X_{\max\sigma}^{\,\sigma}$ satisfying
    the face conditions, the conditions are consistent because the maps compose, and for $n=1$ the
    result is the mapping path space of $f_1$, the dual of its mapping cylinder. Two steps that
    carried no label now have one, and the solution says where its argument comes from: no retained
    set covers the exercise, and what is being given is a definition, so there is nothing to prove
    beyond the consistency and the case $n=1$, both of which are shown. No statement changed. Not
    checked: no certificate; no claim of uniqueness, which the exercise does not ask for.
---

::: {.problem}
Define the dual of an iterated mapping cylinder precisely, in terms of maps from $\Delta^n$, and use this to give a definition of $\nabla X$, the dual of $\Delta X$, for $X$ a complex of spaces.
:::

::: {.solution}
No retained solution set covers this exercise, which asks for a definition rather than a theorem: the retained sets stop at §4.3 or record no §4.H solution. The definition below is the card's own transcription of the duality that §4.H describes, checked against the definition of $\Delta X$ in §4.G and of the mapping path space in §4.3.

Let $X_0 \xrightarrow{f_1} X_1 \xrightarrow{f_2} \cdots \xrightarrow{f_n} X_n$ be maps, and for $i \le j$ write $f_{ji} = f_j \circ \cdots \circ f_{i+1}: X_i \to X_j$, with $f_{ii} = \id$. Faces of $\Delta^n = [v_0, \dots, v_n]$ are written $\sigma = [v_{i_0}, \dots, v_{i_k}]$ with $i_0 < \dots < i_k$, and $\max \sigma = i_k$. All mapping spaces have the compact-open topology.

Here a complex of spaces over a $\Delta$-complex is as in §4.G, and the duals used below are those of Eckmann--Hilton duality as in §4.H : mapping cylinder versus mapping path space, quotient versus subspace. The iterated mapping cylinder $M(f_1, \dots, f_n)$ is a quotient of $\coprod_\sigma X_{\min \sigma} \times \sigma$, where $X_{\min\sigma} \times \tau$ is glued to $X_{\min \tau} \times \tau$ by $f_{\min\tau, \min\sigma} \times \id$ for each face $\tau \subseteq \sigma$. It deformation retracts onto $X_n$. The dual replaces the product $X \times \sigma$ by the mapping space $X^\sigma$, the quotient by a subspace, and the end $X_n$ by the end $X_0$.

::: pf

::: {.pf-step #dual-cylinder}
The dual of the iterated mapping cylinder is
$$\nabla(f_1, \dots, f_n) = \Bigl\{ (\phi_\sigma)_{\sigma \subseteq \Delta^n} \in \prod_\sigma X_{\max\sigma}^{\,\sigma} \;:\; \phi_\sigma\restrict_\tau = f_{\max\sigma, \max\tau} \circ \phi_\tau \text{ for every face } \tau \subseteq \sigma \Bigr\}.$$
Each condition is a closed condition, and the conditions are consistent: for $\rho \subseteq \tau \subseteq \sigma$, $f_{\max\sigma,\max\tau} \circ f_{\max\tau,\max\rho} = f_{\max\sigma,\max\rho}$.

::: pf-proof
The condition compares two maps $\tau \to X_{\max\sigma}$, and each side is continuous in $(\phi_\sigma)$; when $X_{\max \sigma}$ is Hausdorff, equality is closed. The composition rule holds by the definition of $f_{ji}$.
:::

:::

::: {.pf-step #n-equals-one}
For $n = 1$, $\nabla(f_1)$ is the mapping path space $E_{f_1} = \theset{(x, \gamma) \in X_0 \times X_1^I \suchthat \gamma(0) = f_1(x)}$ of §4.3, the dual of the mapping cylinder $M_{f_1}$.

::: pf-proof
The data are $\phi_{v_0} \in X_0$, $\phi_{v_1} \in X_1$, and $\gamma = \phi_{[v_0, v_1]}: I \to X_1$. The conditions say $\gamma(0) = f_1(\phi_{v_0})$ and $\gamma(1) = \phi_{v_1}$, so $\phi_{v_1}$ is determined by $\gamma$, and $(\phi_{v_0}, \gamma)$ ranges over $E_{f_1}$.
:::

:::

::: {.pf-step #complex-of-spaces}
Let $X$ be a complex of spaces over a $\Delta$-complex $\Gamma$: a space $X_\sigma$ for each simplex $\sigma$ of $\Gamma$ and, for each face $\tau \subseteq \sigma$, a map between $X_\sigma$ and $X_\tau$, compatible with composition. In $\Delta X = \coprod_\sigma X_\sigma \times \sigma / {\sim}$ these maps run $X_\sigma \to X_\tau$, as for the iterated mapping cylinder with $X_\sigma = X_{\min\sigma}$. The dual uses the reversed maps $g_{\sigma\tau}: X_\tau \to X_\sigma$, as for the dual cylinder with $X_\sigma = X_{\max\sigma}$, and is
$$\nabla X = \Bigl\{ (\phi_\sigma)_{\sigma \in \Gamma} \in \prod_{\sigma} X_\sigma^{\,\sigma} \;:\; \phi_\sigma\restrict_\tau = g_{\sigma\tau} \circ \phi_\tau \text{ for every face } \tau \subseteq \sigma \Bigr\}.$$
For $\Gamma = \Delta^n$ and $X_\sigma = X_{\max\sigma}$, $\nabla X$ is $\nabla(f_1, \dots, f_n)$.

::: pf-proof
The consistency of the conditions follows from compatibility of the $g_{\sigma\tau}$ with composition, as in step [](#dual-cylinder){.pf-ref}. For the chain, $g_{\sigma\tau} = f_{\max\sigma, \max\tau}$, and the definition of $\nabla X$ becomes the definition in step [](#dual-cylinder){.pf-ref}.
:::

:::

:::

:::
