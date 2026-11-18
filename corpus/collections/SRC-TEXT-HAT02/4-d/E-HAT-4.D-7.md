---
schema: qual/card@1
id: E-HAT-4.D-7
kind: problem
title: Thom class implies orientability
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument above. The prose said that
    naturality of restriction gives $L_\gamma^*(c_{\gamma(1)})=c_{\gamma(0)}$; the card now
    supplies the reason (the pulled-back bundle over the path is trivial, so the generators at
    the two ends agree by homotopy invariance of the slices), and it bridges from the Thom
    class on the disk pair to the class on the sphere fibre through the connecting isomorphism
    $\delta$, which is what Hatcher's definition of orientability refers to. Cited: Thom class
    printed p. 441, orientability printed p. 442, transport for a fibration printed p. 405,
    exercise printed p. 447. Not claimed: a retained solution set; the Hatcher sets in
    `tmp/sources` do not reach §4.D, so the argument is the card's own.
---

::: {.problem}
Show that if a disk bundle $D^n \to E \to B$ has a Thom class with $\ZZ$ coefficients, then it is orientable.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §4.D Exercise 7, printed p. 447, and it is the converse of Theorem 4D.10, printed p. 442. No retained solution set covers this exercise — the Hatcher sets in `tmp/sources` do not reach §4.D — so the argument below is the card's own; the definitions used are the Thom class on printed p. 441 and the orientability of a sphere bundle on printed p. 442.

Throughout, $(D^n,S^{n-1})\to(E,E')\xrightarrow{p}B$ is a disk bundle over a base $B$ with boundary sphere bundle $S^{n-1}\to E'\xrightarrow{p}B$, and $c\in H^n(E,E';\ZZ)$ is a Thom class: its restriction $c_b$ to the fibre pair $(D^n_b,S^{n-1}_b)$ is a generator of $H^n(D^n_b,S^{n-1}_b;\ZZ)\cong\ZZ$ (printed p. 441).

::: pf

::: {.pf-step #orientation-of-fibre}
Each fibre pair $(D_b,S_b)$ carries the orientation determined by the generator $c_b$, and by the connecting isomorphism of the pair this is the same as a generator $\delta c_b$ of $H^{n-1}(S_b;\ZZ)$.

::: pf-proof
$c_b$ is a generator of $H^n(D_b,S_b;\ZZ)\cong\ZZ$ by the definition of a Thom class, and a generator of that infinite cyclic group is a choice of orientation of the $n$-disk pair. The connecting homomorphism $\delta:H^n(D_b,S_b;\ZZ)\to H^{n-1}(S_b;\ZZ)$ of the long exact sequence of the pair is an isomorphism because $D_b$ is contractible, so $H^n(D_b)=0=H^{n-1}(D_b)$; it carries the generator $c_b$ to a generator of $H^{n-1}(S_b;\ZZ)\cong\ZZ$.

:::

:::

::: {.pf-step #transport}
For a path $\gamma:I\to B$ with $\gamma(0)=b_0$, $\gamma(1)=b_1$, the transport homotopy equivalence of pairs $L_\gamma:(D_{b_0},S_{b_0})\to(D_{b_1},S_{b_1})$ satisfies $L_\gamma^*(c_{b_1})=c_{b_0}$.

::: pf-proof
The pullback bundle $\gamma^*E\to I$ is trivial, since $I$ is contractible, so there is a homeomorphism over $I$
$$
\Phi:\gamma^*E\longrightarrow I\times D^n
$$
respecting the pairs, and its restrictions $\Phi_t:D_{\gamma(t)}\to D^n$ are homeomorphisms of pairs. The class $\Phi^*c$ restricts to the slice $\{t\}\times D^n$ as a generator of $H^n(D^n,S^{n-1};\ZZ)$, and the inclusions of the slices $\{0\}\times D^n\to I\times D^n$ and $\{1\}\times D^n\to I\times D^n$ are homotopic, so these generators coincide under the identification: $\Phi_0^*c_{b_0}=\Phi_1^*c_{b_1}$. The transport $L_\gamma$ of the fibration $E\to B$ is the composite $\Phi_1\circ\Phi_0^{-1}$ up to homotopy (the construction of Proposition 4.61, printed p. 405, applied to the bundle), so $L_\gamma^*c_{b_1}=c_{b_0}$.

:::

:::

::: {.pf-step #loop}
For every loop $\gamma$ at $b_0\in B$, the induced map $L_\gamma^*$ is the identity on $H^{n-1}(S_{b_0};\ZZ)$.

::: pf-proof
By step [](#transport){.pf-ref} with $b_0=b_1$, $L_\gamma^*c_{b_0}=c_{b_0}$, and $\delta$ is natural for maps of pairs, so
$$
L_\gamma^*(\delta c_{b_0})=\delta\bigl(L_\gamma^*c_{b_0}\bigr)=\delta c_{b_0}.
$$
Since $\delta c_{b_0}$ is a generator of $H^{n-1}(S_{b_0};\ZZ)\cong\ZZ$ by step [](#orientation-of-fibre){.pf-ref}, and a homomorphism $\ZZ\to\ZZ$ fixing a generator is the identity, $L_\gamma^*=\mathrm{id}$ on $H^{n-1}(S_{b_0};\ZZ)$.

:::

:::

::: {.pf-step #conclusion}
The sphere bundle $E'\to B$ is orientable, and therefore so is the disk bundle $E\to B$.

::: pf-proof
Hatcher's definition, printed p. 442, calls the sphere bundle orientable when $L_\gamma$ induces the identity on $H^{n-1}(S^{n-1};\ZZ)$ for each loop $\gamma$ in $B$; that is step [](#loop){.pf-ref}, after identifying $H^{n-1}(S_{b_0};\ZZ)$ with $H^{n-1}(S^{n-1};\ZZ)$ through a trivialization. A disk bundle is defined to be orientable when its boundary sphere bundle is, again printed p. 442. So an integral Thom class forces orientability of the bundle, which is the assertion.

:::

:::

:::
:::
