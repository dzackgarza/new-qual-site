---
schema: qual/card@1
id: P-MAXAT-4-02
kind: problem
title: Maxim algebraic topology 4.2
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 4, problem 2 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Prove the Suspension Theorem for homotopy groups.
:::

::: {.solution}

The suspension theorem is the Freudenthal suspension theorem: if $X$ is $(r-1)$-connected, $r\geq1$, then the suspension homomorphism
$$
E:\pi_i(X)\longrightarrow\pi_{i+1}(\Sigma X)
$$
is an isomorphism for $i<2r-1$ and a surjection for $i=2r-1$.

::: pf

::: pf-step

Let
$$
\eta:X\longrightarrow\Omega\Sigma X
$$
be the adjoint of the identity map of $\Sigma X$.


::: pf-proof

The suspension-loop adjunction gives a natural bijection
$$
[\Sigma X,Y]_*\cong[X,\Omega Y]_*.
$$
Taking $Y=\Sigma X$ and the identity of $\Sigma X$ yields the unit map $\eta$.

:::

:::

::: {.pf-step #s1-2}

Under the natural identification
$$
\pi_i(\Omega\Sigma X)\cong\pi_{i+1}(\Sigma X),
$$
the map
$$
\eta_*:\pi_i(X)\to\pi_i(\Omega\Sigma X)
$$
is exactly the suspension homomorphism $E$.


::: pf-proof

An element of $\pi_i(X)$ is represented by a based map $S^i\to X$. Composing with $\eta$ and then applying the loop-suspension adjunction produces the suspended map
$$
S^{i+1}=\Sigma S^i\to\Sigma X.
$$
This is the definition of the suspension homomorphism.

:::

:::

::: pf-step

The reduced diagonal
$$
\widetilde\Delta:X\longrightarrow X\wedge X
$$
is $(2r-1)$-connected when $X$ is $(r-1)$-connected, in the sense relevant to the first nontrivial cross-effect of the suspension-loop unit.


::: pf-proof

If $X$ is $(r-1)$-connected, then $X\wedge X$ is $(2r-1)$-connected: cellularly, the first possible non-basepoint cell in each factor has dimension at least $r$, so the first cell in the smash has dimension at least $2r$. Equivalently, the connectivity formula
$$
\operatorname{conn}(X\wedge Y)
\geq\operatorname{conn}(X)+\operatorname{conn}(Y)+1
$$
gives $2r-1$.

:::

:::

::: {.pf-step #s1-4}

The Freudenthal connectivity lemma says that the unit
$$
\eta:X\to\Omega\Sigma X
$$
is $(2r-1)$-connected.


::: pf-proof

Cover $\Sigma X$ by its two open cones $C_+X$ and $C_-X$. Each cone is contractible and their intersection deformation retracts onto $X$. The homotopy excision theorem applied to this triad says that, because the two cone inclusions are $r$-connected, the canonical comparison from the intersection $X$ to the homotopy pullback of the two cones is $(r+r-1)=(2r-1)$-connected. That homotopy pullback is naturally homotopy equivalent to $\Omega\Sigma X$, and the comparison map is the adjunction unit $\eta$. Hence $\eta$ is $(2r-1)$-connected.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\eta_*:\pi_i(X)\to\pi_i(\Omega\Sigma X)
$$
is an isomorphism for
$$
i<2r-1
$$
and a surjection for
$$
i=2r-1.
$$


::: pf-proof

By definition, a $k$-connected map induces isomorphisms on homotopy groups in degrees strictly below $k$ and a surjection in degree $k$. Apply this to the $(2r-1)$-connected map of step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Translating step [](#s1-5){.pf-ref} through step [](#s1-2){.pf-ref} gives
$$
\boxed{
E:\pi_i(X)\xrightarrow{\cong}\pi_{i+1}(\Sigma X)
\quad(i<2r-1),}
$$
and
$$
\boxed{
E:\pi_{2r-1}(X)\twoheadrightarrow
\pi_{2r}(\Sigma X).}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} identifies $\eta_*$ with the suspension homomorphism after the canonical loop-space shift of homotopy groups. Apply the isomorphism and surjectivity ranges from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

In particular, for $X=S^n$ one obtains
$$
\pi_i(S^n)\xrightarrow{\cong}\pi_{i+1}(S^{n+1})
\quad(i<2n-1)
$$
and a surjection at $i=2n-1$.


::: pf-proof

The sphere $S^n$ is $(n-1)$-connected, so set $r=n$ in step [](#s1-6){.pf-ref} and use $\Sigma S^n\cong S^{n+1}$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the Freudenthal suspension theorem, and step [](#s1-7){.pf-ref} records its standard sphere formulation.

:::

:::

:::
