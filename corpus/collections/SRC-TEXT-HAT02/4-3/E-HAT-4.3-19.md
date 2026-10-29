---
schema: qual/card@1
id: E-HAT-4.3-19
kind: problem
title: "Exactness at $\\langle X, F \\rangle$ improved via the $\\Omega B$-action on the homotopy fiber"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Given a fibration $F \to E \xrightarrow{p} B$, define a natural action of $\Omega B$ on the homotopy fiber $F_p$ and use this to show that exactness at $\langle X, F \rangle$ in the long exact sequence in the preceding problem can be improved to the statement that two elements of $\langle X, F \rangle$ have the same image in $\langle X, E \rangle$ iff they are in the same orbit of the induced action of $\langle X, \Omega B \rangle$ on $\langle X, F \rangle$.
:::

::: {.solution}
Fix the basepoint $b_0 \in B$ and let $\Omega B$ be the loops at $b_0$. The homotopy fiber is
$$F_p = \theset{(e, \gamma) \suchthat e \in E,\ \gamma: I \to B,\ \gamma(0) = p(e),\ \gamma(1) = b_0},$$
with $i: F_p \to E$, $i(e, \gamma) = e$. For a path $\gamma$ write $\bar\gamma$ for the reversed path and $\gamma \cdot \delta$ for $\gamma$ followed by $\delta$. Let $X$ be a based CW complex; all maps and homotopies are based.

::: pf

::: {.pf-step #action}
$\lambda \cdot (e, \gamma) = (e, \gamma \cdot \lambda)$ is a continuous action of $\Omega B$ on $F_p$, up to the usual reparametrization homotopies, and it induces an action of the group $\langle X, \Omega B \rangle$ on $\langle X, F_p \rangle$ by $(u \cdot f)(x) = u(x) \cdot f(x)$.

::: pf-proof
$\gamma \cdot \lambda$ runs from $p(e)$ to $b_0$, so $(e, \gamma \cdot \lambda) \in F_p$, and concatenation is continuous in the compact-open topology. Concatenation is associative and unital up to reparametrization homotopies that are natural in the paths, so on homotopy classes $(u \cdot v) \cdot f = u \cdot (v \cdot f)$ and $\mathrm{const} \cdot f = f$. A homotopy of $u$ or $f$ gives a homotopy of $u \cdot f$. At the basepoint, $u(x_0) \cdot f(x_0)$ is a reparametrized constant path; a based homotopy corrects this, by the homotopy extension property of $(X, x_0)$.
:::

:::

::: {.pf-step #same-orbit}
If $g = u \cdot f$ in $\langle X, F_p \rangle$, then $i_* f = i_* g$.

::: pf-proof
The action does not change the first coordinate, so $i \circ (u \cdot f) = i \circ f$.
:::

:::

::: {.pf-step #converse}
If $i_* f = i_* g$, then $f = \lambda \cdot g$ for some $\lambda \in \langle X, \Omega B \rangle$.

::: pf-proof

::: pf-step
Write $f(x) = (f_E(x), \alpha_x)$ and $g(x) = (g_E(x), \beta_x)$, and let $H: X \times I \to E$ be a based homotopy from $f_E$ to $g_E$. For $s \in I$, let $\eta_{x, s}$ be the path $t \mapsto pH(x, (1-t)s)$ from $pH(x, s)$ to $p f_E(x)$. Then
$$K(x, s) = (H(x, s),\ \eta_{x, s} \cdot \alpha_x)$$
is a homotopy in $F_p$ from $f$ to the map $x \mapsto (g_E(x), \eta_{x, 1} \cdot \alpha_x)$.

::: pf-proof
$\eta_{x, s} \cdot \alpha_x$ runs from $pH(x, s)$ to $b_0$, so $K(x, s) \in F_p$, and $K$ is continuous. $\eta_{x, 0}$ is constant, so $K_0$ is $f$ up to reparametrization. At $x_0$, $H$ is constant at the basepoint of $E$, so $K$ is based up to reparametrization.
:::

:::

::: pf-step
Let $\lambda(x) = \bar\beta_x \cdot \eta_{x, 1} \cdot \alpha_x$, a loop at $b_0$. Then $\lambda \cdot g \simeq f$.

::: pf-proof
$(\lambda \cdot g)(x) = (g_E(x), \beta_x \cdot \bar\beta_x \cdot \eta_{x, 1} \cdot \alpha_x)$, and $\beta_x \cdot \bar\beta_x$ contracts to a constant path continuously in $x$. So $\lambda \cdot g \simeq K_1 \simeq f$ by the previous step.
:::

:::

:::

:::

::: pf-step
Two elements of $\langle X, F_p \rangle$ have the same image in $\langle X, E \rangle$ if and only if they are in the same orbit of $\langle X, \Omega B \rangle$. With $F \simeq F_p$, this is the stated improvement of exactness at $\langle X, F \rangle$.

::: pf-proof
Steps [](#same-orbit){.pf-ref} and [](#converse){.pf-ref} give the two directions. The inclusion $F = p^{-1}(b_0) \to F_p$, $e \mapsto (e, \mathrm{const})$, is a homotopy equivalence over $E$ because $p$ is a fibration, so it identifies $\langle X, F \rangle$ with $\langle X, F_p \rangle$ compatibly with the maps to $\langle X, E \rangle$.
:::

:::

:::

:::
