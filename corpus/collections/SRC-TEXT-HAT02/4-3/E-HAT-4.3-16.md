---
schema: qual/card@1
id: E-HAT-4.3-16
kind: problem
title: "Whitehead theorem via homotopy fiber"
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
  date: 2026-11-20
  note: >-
    The connectedness step said H~_0 is "the reduced group Z^{pi_0}", which is not the reduced
    homology of a space and would make H~_0 vanish for the empty space, which has no path
    component. F_f is nonempty (it contains (x_0, const_{y_0})), and for a nonempty space H~_0 is
    free abelian of rank |pi_0| - 1, so the conclusion is unchanged.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Restructured under #2 into numbered steps, argument unchanged except at one point: the
    earlier text concluded F_f simeq * by Whitehead, which needs the homotopy type of a CW
    complex for F_f. Milnor's theorem is available for that (printed p. 408), but the step is not
    needed: vanishing of all homotopy groups of F_f makes the long exact sequence give
    pi_n(E_f) -> pi_n(Y) an isomorphism directly, and Whitehead's theorem is applied only to the
    given map f of connected CW complexes. No retained solution set covers §4.3 Exercise 16 (Sam's
    set stops at 9, 11-15, 17-20, 23; the sets that stop earlier were checked in the 2026-11-19
    read), so the argument is the card's own. Checked against Proposition 4.64, printed p. 407,
    Theorem 4.41, printed p. 376, Exercise 10 and Exercise 16 on printed pp. 419-420, Theorem
    2A.1, printed p. 166, Theorem 4.32, printed p. 366, and Theorem 4.5, printed p. 346. Not
    checked: no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 16, printed p. 420,
    and Exercise 10 of the same section, printed p. 419. The argument is right: pi_1(E_f)
    -> pi_1(Y) an isomorphism makes pi_1(F_f) -> pi_1(E_f) zero by exactness, Exercise 10
    makes the action of pi_1(F_f) on its own homotopy groups factor through pi_1(E_f),
    hence trivial, so F_f is abelian and the Hurewicz theorem turns H̃_* = 0 into the
    vanishing of all homotopy groups. One sentence was missing, which independent reports
    from the swarm asked for: the hypothesis gives H̃_0(F_f) = 0 only if one notices that
    this is exactly path connectivity, which is what makes pi_1(F_f) a group to act. That
    is now said. Statement unchanged. Not checked: the last steps of the card beyond the
    Hurewicz application.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 16; the stored statement matches.
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

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own. It uses the mapping-path fibration of Proposition 4.64, the long exact sequence of Theorem 4.41, the action of Exercise 10, the Hurewicz theorem in degrees $1$ and $n\ge2$, and Whitehead's theorem, each at the printed place named in its step.

::: pf

::: {.pf-step #setup}
There is a fibration $p\colon E_f\to Y$ with $E_f\simeq X$, fibre $F_f=p^{-1}(y_0)$, and $\pi_1(E_f)\to\pi_1(Y)$ an isomorphism.

::: pf-proof
Let $E_f=\{(x,\gamma):x\in X,\ \gamma\colon I\to Y,\ \gamma(0)=f(x)\}$ and $p(x,\gamma)=\gamma(1)$; Proposition 4.64 (printed p.~407) says $p$ is a fibration. The map $x\mapsto(x,\mathrm{const}_{f(x)})$ includes $X$ in $E_f$, and $H_s(x,\gamma)=(x,\gamma_s)$ with $\gamma_s(t)=\gamma(st)$ is a deformation retraction of $E_f$ onto the image of $X$, so $E_f\simeq X$. The hypothesis that $f$ induces an isomorphism on $\pi_1$ therefore says that $\pi_1(E_f)\to\pi_1(Y)$ is an isomorphism.
:::

:::

::: {.pf-step #connected}
$F_f$ is path connected.

::: pf-proof
$F_f$ is nonempty, since it contains the pair $(x_0,\mathrm{const}_{y_0})$. The hypothesis $\widetilde H_*(F_f;\ZZ)=0$ includes $\widetilde H_0(F_f;\ZZ)=0$. For a nonempty space, $\widetilde H_0$ is free abelian of rank one less than the number of path components, so it vanishes exactly when there is one path component; hence $F_f$ is path connected.
:::

:::

::: {.pf-step #pi1}
$\pi_1(F_f)=0$.

::: pf-proof
The fibration of step [](#setup){.pf-ref} has long exact sequence $\cdots\to\pi_1(F_f)\to\pi_1(E_f)\to\pi_1(Y)\to\pi_0(F_f)$ (Theorem 4.41, printed p.~376). Since $\pi_1(E_f)\to\pi_1(Y)$ is injective, the image of $\pi_1(F_f)$ in $\pi_1(E_f)$ is zero. Exercise 10 (printed p.~419) provides a homomorphism $\pi_1(E_f)\to\operatorname{Aut}(\pi_n(F_f))$ whose composite with $\pi_1(F_f)\to\pi_1(E_f)$ is the usual action of $\pi_1(F_f)$ on $\pi_n(F_f)$; the composite is zero here, so that action is trivial for every $n\ge1$. For $n=1$ the usual action is conjugation, so $\pi_1(F_f)$ is abelian. Since $F_f$ is path connected by step [](#connected){.pf-ref}, Hurewicz in degree $1$ (Theorem 2A.1, printed p.~166) identifies $H_1(F_f;\ZZ)$ with the abelianization of $\pi_1(F_f)$, which is $\widetilde H_1(F_f;\ZZ)=0$ by hypothesis; an abelian group with zero abelianization is zero.
:::

:::

::: {.pf-step #higher}
$\pi_n(F_f)=0$ for every $n\ge2$.

::: pf-proof
$F_f$ is simply connected by step [](#pi1){.pf-ref} and has $\widetilde H_i(F_f;\ZZ)=0$ for all $i$ by hypothesis. Suppose $\pi_n(F_f)\ne0$ for some $n\ge2$ and take the least such $n$. Then $F_f$ is $(n-1)$-connected, so the Hurewicz theorem (Theorem 4.32, printed p.~366) gives $\pi_n(F_f)\cong\widetilde H_n(F_f;\ZZ)=0$, a contradiction.
:::

:::

::: {.pf-step #les}
$\pi_n(E_f)\to\pi_n(Y)$ is an isomorphism for every $n\ge1$.

::: pf-proof
The long exact sequence of the fibration (Theorem 4.41, printed p.~376) reads $\pi_n(F_f)\to\pi_n(E_f)\to\pi_n(Y)\to\pi_{n-1}(F_f)$ for $n\ge1$. The outer groups vanish for all $n$ by steps [](#pi1){.pf-ref} and [](#higher){.pf-ref}, so the middle map has zero kernel and zero cokernel.
:::

:::

::: {.pf-step #whitehead}
$f$ is a homotopy equivalence.

::: pf-proof
Under the homotopy equivalence $E_f\simeq X$ of step [](#setup){.pf-ref}, the map $\pi_n(E_f)\to\pi_n(Y)$ of step [](#les){.pf-ref} is the map induced by $f$. So $f_*\colon\pi_n(X)\to\pi_n(Y)$ is an isomorphism for every $n\ge1$. Both $X$ and $Y$ are connected CW complexes by hypothesis, so Whitehead's theorem (Theorem 4.5, printed p.~346) gives that $f$ is a homotopy equivalence.
:::

:::

::: {.pf-step}
A map $f\colon X\to Y$ of connected CW complexes inducing an isomorphism on $\pi_1$, with $\widetilde H_*(F_f;\ZZ)=0$, is a homotopy equivalence.

::: pf-proof
Steps [](#setup){.pf-ref} to [](#whitehead){.pf-ref}: the acyclicity of $F_f$ forces $\pi_1(F_f)=0$ and then all higher homotopy of $F_f$ to vanish, the long exact sequence transfers this to isomorphisms $\pi_n(X)\cong\pi_n(Y)$ for all $n$, and Whitehead's theorem concludes.
:::

:::

:::
:::
