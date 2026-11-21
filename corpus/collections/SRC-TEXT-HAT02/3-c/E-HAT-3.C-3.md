---
schema: qual/card@1
id: E-HAT-3.C-3
kind: problem
title: Path-components of homotopy-associative H-spaces
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof: left multiplication $L_x$ maps the identity component to the component of $x$,
    homotopy associativity gives $L_yL_x\simeq L_{yx}$, and $yx$ lies in the identity component, so
    a path from $yx$ to $e$ inside it makes $L_{yx}\simeq L_e\simeq\mathrm{id}$. The same in the
    other order gives a homotopy inverse, so each component is homotopy equivalent to the identity
    component. The only input beyond the H-space axioms is that the component set is a group, which
    is the exercise's hypothesis.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps. Supplied what the prose used silently: that left
    multiplication by x carries the component of e into the component of mu(x,e), which is the
    component of x because mu(x,e) is homotopic to x; that left multiplication by a point of the
    identity component is homotopic to the identity, through the path in that component together
    with continuity of mu in both variables; and that the two composites are the identity maps on
    the nose. The route is the one the earlier review recorded; no printed page was re-read this
    session, and the statement check remains the earlier event.
---

::: {.problem}
Show that in a homotopy-associative H-space whose set of path-components is a group with respect to the multiplication induced by the H-space structure, all the path-components must be homotopy equivalent.
[Homotopy-associative means associative up to homotopy.]
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 3.C Exercise 3. The statement was checked against Hatcher, *Algebraic Topology* (2002), §3.C Exercise 3, and the H-space axioms are those of printed p. 281.

Let $(X,e)$ be an H-space with multiplication $\mu$, homotopy associative in the sense that $\mu\bigl(\mu(x,y),z\bigr)\simeq\mu\bigl(x,\mu(y,z)\bigr)$ for all $x,y,z$. Assume the set $\pi_{0}(X)$ of path-components is a group under the multiplication induced by $\mu$, and let $X_{0}$ be the path-component of $e$. For $p\in X$ write $L_{p}$ for left multiplication, $L_{p}(z)=\mu(p,z)$.

::: pf

::: {.pf-step #components}
$\pi_{0}(X)$ is a group whose product is induced by $\mu$, so $\mu$ carries $X_{a}\times X_{b}$ into $X_{ab}$, and the component of $e$ is the identity element.

::: pf-proof
The product on $\pi_{0}(X)$ is defined by $[x][y]\coloneqq[\mu(x,y)]$, which is well defined because $\mu$ is continuous and a homotopy of either factor gives a homotopy of the product. That $\mu$ maps $X_{a}\times X_{b}$ into $X_{ab}$ is exactly this definition read on components, and the hypothesis says the resulting multiplication is a group law, so the class of $X_{0}$ is the identity.
:::

:::

::: {.pf-step #left-mult}
For $p\in X_{b}$ and any $z\in X_{c}$, $\mu(p,z)\in X_{bc}$; in particular $L_{x}$ maps $X_{0}$ into $X_{a}$ when $x\in X_{a}$.

::: pf-proof
$\mu(p,z)\in X_{bc}$ is step [](#components){.pf-ref}. Taking $p=x\in X_{a}$ and $z\in X_{0}$ gives $\mu(x,z)\in X_{a\cdot e}=X_{a}$, using that the class of $X_{0}$ is the identity in $\pi_{0}(X)$.
:::

:::

::: {.pf-step #unit}
$L_{e}=\mu(e,-)$ is homotopic to the identity of $X_{0}$.

::: pf-proof
By the definition of an H-space (printed p. 281) the map $x\mapsto\mu(e,x)$ is homotopic to the identity of $X$ through maps $(X,e)\to(X,e)$; restricting that homotopy to the subspace $X_{0}$, which is carried into itself because it fixes $e$, gives a homotopy $L_{e}\simeq\mathrm{id}_{X_{0}}$.
:::

:::

::: {.pf-step #assoc}
$L_{y}\circ L_{x}\simeq L_{\mu(y,x)}$ as maps $X_{0}\to X_{0}$.

::: pf-proof
$L_{y}(L_{x}(z))=\mu\bigl(y,\mu(x,z)\bigr)$ and $L_{\mu(y,x)}(z)=\mu\bigl(\mu(y,x),z\bigr)$. These maps of $(y,x,z)$ are homotopic by homotopy associativity, and a homotopy depending continuously on $z$ gives a homotopy of the maps of $z$ obtained by fixing $x,y$.
:::

:::

::: {.pf-step #inner}
If $p\in X_{0}$ then $L_{p}\simeq\mathrm{id}_{X_{0}}$.

::: pf-proof
Choose a path $\gamma\colon I\to X_{0}$ with $\gamma(0)=p$ and $\gamma(1)=e$, possible because $X_{0}$ is path-connected. Define $H(z,t)=\mu\bigl(\gamma(t),z\bigr)$, which is continuous because $\mu$ and $\gamma$ are; then $H(z,0)=\mu(p,z)=L_{p}(z)$ and $H(z,1)=\mu(e,z)=L_{e}(z)$, so $L_{p}\simeq L_{e}$, and $L_{e}\simeq\mathrm{id}_{X_{0}}$ by step [](#unit){.pf-ref}.
:::

:::

::: {.pf-step #equiv}
For $x\in X_{a}$ and $y\in X_{a^{-1}}$, the map $L_{x}\colon X_{0}\to X_{a}$ is a homotopy equivalence.

::: pf-proof
$\mu(y,x)\in X_{a^{-1}a}=X_{0}$ by steps [](#components){.pf-ref} and [](#left-mult){.pf-ref}, so $L_{\mu(y,x)}\simeq\mathrm{id}_{X_{0}}$ by step [](#inner){.pf-ref}. Composing, $L_{y}\circ L_{x}\simeq L_{\mu(y,x)}\simeq\mathrm{id}_{X_{0}}$ by steps [](#assoc){.pf-ref} and [](#inner){.pf-ref}, and symmetrically $L_{x}\circ L_{y}\simeq L_{\mu(x,y)}\simeq\mathrm{id}_{X_{a}}$ because $\mu(x,y)\in X_{aa^{-1}}=X_{0}$. So $L_{x}$ has the homotopy inverse $L_{y}$, using that $L_{y}$ maps $X_{a}$ into $X_{0}$ and $L_{x}$ maps $X_{0}$ into $X_{a}$ by step [](#left-mult){.pf-ref}.
:::

:::

::: {.pf-step}
All path-components of $X$ are homotopy equivalent.

::: pf-proof
Every component is $X_{a}$ for some class $a\in\pi_{0}(X)$, and the group structure supplies the inverse class, so step [](#equiv){.pf-ref} applies to each: $X_{0}\simeq X_{a}$. Homotopy equivalence is an equivalence relation, so any two components are homotopy equivalent.
:::

:::

:::

:::
