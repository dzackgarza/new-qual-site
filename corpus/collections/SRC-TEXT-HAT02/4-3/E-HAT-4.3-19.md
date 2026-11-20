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
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 19 of §4.3, printed p. 420, with the homotopy fibre of a
    fibration. Correct. The action $(e,\gamma)\cdot\lambda=(e,\gamma\cdot\lambda)$ is a right
    action of $\Omega B$ on $F_p$ preserving the first coordinate, so $f\cdot u$ and $f$ have the
    same image in $\langle X,E\rangle$; conversely, from a based homotopy $H$ between the $E$-parts,
    the path $\eta_{x,s}(t)=pH(x,(1-t)s)$ joins $pH(x,s)$ to $pf_E(x)$, the formula
    $K(x,s)=(H(x,s),\eta_{x,s}\cdot\alpha_x)$ is a homotopy in $F_p$ from $f$ to
    $(g_E,\eta_{x,1}\alpha_x)$, and $\lambda(x)=\bar\beta_x\cdot\eta_{x,1}\cdot\alpha_x$ is a loop
    at $b_0$ with $g\cdot\lambda\simeq f$ because $\beta_x\bar\beta_x$ contracts continuously in
    $x$. The passage from $F$ to $F_p$ is the usual homotopy equivalence over $E$ for a fibration.
    Nothing changed. The earlier audit event of 2026-11-02 was a batch summary and named no page.
    Not claimed: a published solution, and no certificate.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The event above says no published solution is claimed, and that is false: Steven V. Sam's
    set, retained as `tmp/sources/hatcher-solutions-sam-2008.pdf`, solves §4.3 Exercise 19 on
    printed p. 28, by lifting $\overline\eta\cdot\gamma\cdot\eta$ to define an action of
    $\Omega B$ on the homotopy fibre and reading the orbit condition off a homotopy through
    basepoint-preserving maps. The solution's lead now cites it and says how the card's right
    action by concatenation differs from Sam's lifted left action. Re-read in the same pass:
    the whole $\lambda$ construction, from $H$ through $\eta_{x,s}$ to
    $\lambda(x)=\overline\beta_x\cdot\eta_{x,1}\cdot\alpha_x$, is correct, and $\lambda$ is a
    loop at $b_0$ because $\alpha_{x_0}$, $\beta_{x_0}$ and $\eta_{x_0,1}$ are constant at the
    basepoint. No step changed. Not checked: the homotopy equivalence $F\to F_p$ is cited to
    Proposition 4.65's argument rather than recomputed, and there is no certificate.
---

::: {.problem}
Given a fibration $F \to E \xrightarrow{p} B$, define a natural action of $\Omega B$ on the homotopy fiber $F_p$ and use this to show that exactness at $\langle X, F \rangle$ in the long exact sequence in the preceding problem can be improved to the statement that two elements of $\langle X, F \rangle$ have the same image in $\langle X, E \rangle$ iff they are in the same orbit of the induced action of $\langle X, \Omega B \rangle$ on $\langle X, F \rangle$.
:::

::: {.solution}
The exercise is solved in the retained set **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.3 Exercise 19**: Sam defines an action of $\Omega B$ on $F_p$ by lifting the loop $\overline\eta\cdot\gamma\cdot\eta$, and shows that two elements of $\langle X,F_p\rangle$ have the same image in $\langle X,E\rangle$ exactly when they lie in one orbit. The action used below is the right action by concatenation, $(e,\gamma)\cdot\lambda=(e,\gamma\cdot\lambda)$; the criterion proved is the same, and the loop carrying $g$ to $f$ is constructed explicitly.

Fix the basepoint $b_0 \in B$ and let $\Omega B$ be the loops at $b_0$. The homotopy fiber is
$$F_p = \theset{(e, \gamma) \suchthat e \in E,\ \gamma: I \to B,\ \gamma(0) = p(e),\ \gamma(1) = b_0},$$
with $i: F_p \to E$, $i(e, \gamma) = e$. For a path $\gamma$ write $\bar\gamma$ for the reversed path and $\gamma \cdot \delta$ for $\gamma$ followed by $\delta$. Let $X$ be a based CW complex; all maps and homotopies are based.

::: pf

::: {.pf-step #action}
$(e, \gamma) \cdot \lambda = (e, \gamma \cdot \lambda)$ is a continuous right action of $\Omega B$ on $F_p$, up to the usual reparametrization homotopies, and it induces a right action of the group $\langle X, \Omega B \rangle$ on $\langle X, F_p \rangle$ by $(f \cdot u)(x) = f(x) \cdot u(x)$.

::: pf-proof
$\gamma \cdot \lambda$ runs from $p(e)$ to $b_0$, so $(e, \gamma \cdot \lambda) \in F_p$, and concatenation is continuous in the compact-open topology. Concatenation is associative and unital up to reparametrization homotopies that are natural in the paths, so on homotopy classes $(f \cdot u) \cdot v = f \cdot (u \cdot v)$ and $f \cdot \mathrm{const} = f$. A homotopy of $u$ or $f$ gives a homotopy of $f \cdot u$. At the basepoint, $f(x_0) \cdot u(x_0)$ is a reparametrized constant path; a based homotopy corrects this, by the homotopy extension property of $(X, x_0)$.
:::

:::

::: {.pf-step #same-orbit}
If $g = f \cdot u$ in $\langle X, F_p \rangle$, then $i_* f = i_* g$.

::: pf-proof
The action does not change the first coordinate, so $i \circ (f \cdot u) = i \circ f$.
:::

:::

::: {.pf-step #converse}
If $i_* f = i_* g$, then $f = g \cdot \lambda$ for some $\lambda \in \langle X, \Omega B \rangle$.

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
Let $\lambda(x) = \bar\beta_x \cdot \eta_{x, 1} \cdot \alpha_x$, a loop at $b_0$. Then $g \cdot \lambda \simeq f$.

::: pf-proof
$(g \cdot \lambda)(x) = (g_E(x), \beta_x \cdot \bar\beta_x \cdot \eta_{x, 1} \cdot \alpha_x)$, and $\beta_x \cdot \bar\beta_x$ contracts to a constant path continuously in $x$. So $g \cdot \lambda \simeq K_1 \simeq f$ by the previous step.
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
