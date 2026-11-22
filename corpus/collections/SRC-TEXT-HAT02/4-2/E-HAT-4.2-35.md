---
schema: qual/card@1
id: E-HAT-4.2-35
kind: problem
title: "Quotient fiber bundle from quaternionic Hopf bundle"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 35; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: right multiplication by unit
    quaternions preserves the norm and its orbits are the quaternionic lines, giving the Hopf bundle
    with fibre $S^3$; complex numbers are central in $\quaternions$, so right multiplication by
    $e^{i\theta}$ is coordinatewise complex scalar multiplication under
    $\quaternions^{n+1}\cong\CC^{2n+2}$, whose orbit space on the unit sphere is $\CP^{2n+1}$; the
    $S^1$-orbits in $S^3$ are the Hopf fibres, giving $S^2$; and the trivializations are
    $S^3$-equivariant hence descend. Added: the centrality of $\CC$ in $\quaternions$ as the reason
    the right action is the complex one, the freeness of the $S^1$-action, and the equivariance
    clause that makes the descent work. No defect found in the statement, §4.2 Exercise 35; no
    retained solution set covers it.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 401 carries the running head 392.
    The durable part of the locator is that printed page; the file path names this machine's copy and
    `tmp/sources` does not survive a VM reset. No mathematics changed.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The statement block carried the locator "printed page = PDF page - 9" and the name of the file the
    exercise was read in. Both are removed: the exercise is cited as §4.2 Exercise 35, and the wording
    is otherwise untouched. No mathematics changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 35. The problem block carried a non-printed preamble ("This is
    Hatcher, ... the statement below is its wording"), which is removed, so the block is the printed
    statement alone. The proof reads correct and no retained set covers the exercise.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    One false step repaired, from an independent review. The card asserted that $qz=zq$ for
    $z\in\CC$, $q\in\quaternions$, "the complex numbers being central in $\quaternions$". They are
    not: $ij=k=-ji$, and on the second coordinate $j\lambda=\bar\lambda j$, so right multiplication
    by $e^{i\theta}$ is not complex scalar multiplication. The action that gives $\CP^{2n+1}$ is left
    multiplication, which under $\quaternions=\CC\oplus\CC j$ is $\lambda(a+bj)=\lambda a+\lambda bj$,
    complex scalar multiplication on both coordinates; the step now says that, names the failure of
    centrality, and the fibre step uses the left action (giving $S^1\backslash S^3=S^2$).
---

::: {.problem}
Show that the fiber bundle $S^3 \to S^{4n+3} \to \quatprojective^n$ gives rise to a quotient fiber bundle $S^2 \to \CP^{2n+1} \to \quatprojective^n$ by factoring out the action of $S^1$ on $S^{4n+3}$ by complex scalar multiplication.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; write $\quatprojective^n$ for the quaternionic projective space of quaternionic lines in $\quaternions^{n+1}$.

::: pf

::: {.pf-step #hopf}
$S^{4n+3}\subseteq\quaternions^{n+1}$ is the unit sphere, and the quaternionic Hopf bundle is the orbit map of right multiplication by $S^3$.

::: pf-proof
The unit sphere in $\quaternions^{n+1}\cong\RR^{4n+4}$ is a manifold of dimension $4n+3$. Right multiplication by unit quaternions preserves the norm, so $S^3$ acts on $S^{4n+3}$ on the right, and its orbits are the sets of unit vectors spanning a fixed quaternionic line, so the orbit space is $\quatprojective^n$ and the orbit map $S^{4n+3}\to\quatprojective^n$ has fibre $S^3$. It is a fibre bundle with local trivializations obtained from quaternionic linear charts.
:::

:::

::: {.pf-step #complex-action}
The subgroup $S^1=\{e^{i\theta}\}\subseteq\CC\subseteq\quaternions$ of $S^3$ acts on $S^{4n+3}$ by complex scalar multiplication under the identification $\quaternions^{n+1}\cong\CC^{2n+2}$, and the orbit space is $\CP^{2n+1}$.

::: pf-proof
The complex numbers are *not* central in the quaternions — $ij=k=-ji$ — so the action to take is left multiplication, not right: for $\lambda\in\CC$ and $q=a+bj$ with $a,b\in\CC$ one has $\lambda q=\lambda a+\lambda bj$, which under the left $\CC$-module identification $\quaternions\cong\CC\oplus\CC j\cong\CC^2$ is complex scalar multiplication on both coordinates. (Right multiplication would not do: $j\lambda=\bar\lambda j$, so on the second coordinate it multiplies by $\bar\lambda$.) Left multiplication by $e^{i\theta}$ therefore acts on each quaternionic coordinate, hence on $\quaternions^{n+1}\cong\CC^{2n+2}$, by complex scalar multiplication. The orbits of that action on the unit sphere of $\CC^{2n+2}$ are the complex lines, so the orbit space is $\CP^{2n+1}$.
:::

:::

::: {.pf-step #fibre}
Dividing each fibre $S^3$ by the left $S^1$-action gives $S^2$, and the local trivializations descend.

::: pf-proof
The left action of $S^1$ on $S^3$ is free, its orbits being the cosets $S^1q$, and the orbit map $S^3\to S^1\backslash S^3$ is the Hopf bundle $S^3\to S^2$; so each fibre of the quaternionic bundle becomes an $S^2$. A local trivialization $\restrictionof{S^{4n+3}}{U}\cong U\times S^3$ of the quaternionic bundle is $S^3$-equivariant for left multiplication, hence $S^1$-equivariant, so it descends to a homeomorphism of $S^{4n+3}/S^1$ over $U$ with $U\times(S^3/S^1)$.
:::

:::

::: {.pf-step}
$\boxed{S^2\longrightarrow\CP^{2n+1}\longrightarrow\quatprojective^n}$ is a fibre bundle.

::: pf-proof
By step [](#complex-action){.pf-ref} the total space is $S^{4n+3}/S^1=\CP^{2n+1}$ and the base remains $\quatprojective^n$, the $S^1$-action preserving the quaternionic line of a vector because it is right multiplication by scalars. Steps [](#fibre){.pf-ref} give the fibre $S^2$ and local triviality, so this is a fibre bundle, obtained from the quaternionic Hopf bundle by factoring out the action of $S^1$ by complex scalar multiplication.
:::

:::

:::
:::
