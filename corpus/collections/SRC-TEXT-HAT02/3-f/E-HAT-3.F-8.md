---
schema: qual/card@1
id: E-HAT-3.F-8
kind: problem
title: "Bockstein sequence on Moore spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 8, printed page
    320; the statement matches word for word. Checked: for a Moore space
    H̃_n(M(G,n)) = G with all other reduced homology zero, so the universal
    coefficient theorem (Theorem 3.2, p. 195) gives H^n = Hom(G,−) and
    H^{n+1} = Ext(G,−) and kills the rest; the Bockstein sequence of
    0 → A → B → C → 0 (§3.E, p. 305) therefore has only two nonzero terms, and the
    displayed six-term sequence is its exactness written out. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 8, printed p. 320.
    The mathematics of the conclusion is right, but the proof had three defects and
    was rewritten. (1) Step #s1's proof read only "definition of a Moore space." and
    #s2's only "Step [](#s1) and the universal coefficient theorem."; both now carry
    the argument, including the degree range. (2) Step #s4 said all other terms
    vanish, which is false at n = 1: the term before H^1(M;A) is H^0(M;C) = C, and
    the sequence begins 0 -> H^1 only because A -> B injective makes B -> C onto, so
    the connecting map C -> H^1(M;A) is zero. That case is now argued. (3) The
    vanishing range is stated for i >= 1 with the two exceptional degrees. Statement
    unchanged. Not checked: nothing outside this exercise.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read again against Hatcher, §3.F Exercise 8. The proof is correct: the universal coefficient
    theorem puts $\operatorname{Hom}(G,-)$ in degree $n$ and $\operatorname{Ext}(G,-)$ in degree
    $n+1$ for a Moore space $M(G,n)$ with nothing in the other degrees $\ge1$; the Bockstein sequence
    for $0\to A\to B\to C\to0$ collapses to those six groups; and the collapse is exact at both ends,
    through $B\to C$ onto when $n=1$ and through the vanishing of $H^{n+2}$ of the space. Three
    corrections, none of mathematics. The left end attributed "$B\to C$ onto" to the injectivity of
    $A\to B$; it follows from exactness of the coefficient sequence, and the step now says so. The
    trailing `pf-qed` only restated that the earlier steps answered the question, which STYLE-08
    forbids, and is removed: step `s5` states the required sequence and is the QED step. The retained
    sets' state is now recorded in the preamble.
---

::: {.problem}
Show that for a Moore space $M(G, n)$ the Bockstein long exact sequence in cohomology associated to the short exact sequence of coefficient groups $0 \to A \to B \to C \to 0$ reduces to an exact sequence

$$0 \to \operatorname{Hom}(G,A) \to \operatorname{Hom}(G,B) \to \operatorname{Hom}(G,C) \to \operatorname{Ext}(G,A) \to \operatorname{Ext}(G,B) \to \operatorname{Ext}(G,C) \to 0.$$
:::

::: {.solution}
The statement is Hatcher, §3.F Exercise 8. The argument is the card's own: no retained solution set holds a solution of any exercise of §3.F — Koukpari's set carries the §3.F heading *Limits and Ext* with nothing under it, Sam's begins at §4.1, and the others stop earlier — so there is no published proof to transcribe.

::: pf

::: {.pf-step #s1}

For a Moore space $M(G, n)$ with $n\ge1$: $\widetilde H_n(M(G,n)) = G$, $\widetilde H_i(M(G,n)) = 0$ for $i \neq n$, and $M(G,n)$ is path connected.

::: pf-proof

A Moore space $M(G,n)$ is by definition a CW complex with $\widetilde H_n(M(G,n))\cong G$ and $\widetilde H_i(M(G,n))=0$ for $i\ne n$, and with $n\ge1$ its reduced homology in degree $0$ vanishes, so it is connected and hence path connected as a CW complex.

:::

:::

::: {.pf-step #s2}

$H^n(M(G,n); A) \cong \operatorname{Hom}(G, A)$ and $H^{n+1}(M(G,n); A) \cong \operatorname{Ext}(G, A)$, while $H^i(M(G,n); A)=0$ for $1\le i\le n-1$ and for $i\ge n+2$.

::: pf-proof

The universal coefficient theorem gives, for each $i$, the short exact sequence
$$
0\to\operatorname{Ext}(H_{i-1}(M(G,n)), A)\to H^i(M(G,n);A)\to\operatorname{Hom}(H_i(M(G,n)),A)\to0 .
$$
By step [](#s1){.pf-ref} the group $H_i(M(G,n))$ vanishes for $i\ne n$ and equals $G$ for $i=n$, so the $\operatorname{Hom}$ term vanishes unless $i=n$ and the $\operatorname{Ext}$ term vanishes unless $i-1=n$. For $i=n$ the sequence reads $0\to0\to H^n\to\operatorname{Hom}(G,A)\to0$, and for $i=n+1$ it reads $0\to\operatorname{Ext}(G,A)\to H^{n+1}\to0$; for every other $i\ne n,n+1$ both ends vanish, and $i=n$ and $i=n+1$ are the only degrees where either end can be nonzero.

:::

:::

::: {.pf-step #s3}

The Bockstein long exact sequence associated to $0 \to A \to B \to C \to 0$ is
$$\cdots \to H^i(M; A) \to H^i(M; B) \to H^i(M; C) \xrightarrow{\beta} H^{i+1}(M; A) \to \cdots.$$

::: pf-proof

A short exact sequence of coefficient groups induces a long exact sequence in cohomology, natural in the space and additive in the coefficients; that sequence is displayed, its connecting homomorphism being the Bockstein homomorphism $\beta$.

:::

:::

::: {.pf-step #s4}

Since $H^i(M(G,n); \cdot) = 0$ for $i\ne n,n+1$ with $i\ge1$, the long exact sequence collapses to the exact sequence
$$0 \to H^n(M;A) \to H^n(M;B) \to H^n(M;C) \to H^{n+1}(M;A) \to H^{n+1}(M;B) \to H^{n+1}(M;C) \to 0.$$

::: pf-proof

By step [](#s2){.pf-ref} the six displayed groups are the only ones in degrees $\ge1$ that can be nonzero, and the sequence of step [](#s3){.pf-ref} restricts to an exact sequence through them. At the left end: for $n\ge2$ the preceding term is $H^{n-1}(M;A)=0$; for $n=1$ it is $H^0(M;A)=A$, and $B\to C$ is onto by exactness of the coefficient sequence, so the map $H^0(M;B)\to H^0(M;C)$, which is $B\to C$ again, is onto and the connecting map $H^0(M;C)\to H^1(M;A)$ is zero; hence the sequence begins $0\to H^1(M;A)$. At the right end the next term is $H^{n+2}(M;A)=0$ in both cases, since $n+2\ge3$.

:::

:::

::: {.pf-step #s5}

Substituting step [](#s2){.pf-ref}, this is exactly
$$0 \to \operatorname{Hom}(G,A) \to \operatorname{Hom}(G,B) \to \operatorname{Hom}(G,C) \to \operatorname{Ext}(G,A) \to \operatorname{Ext}(G,B) \to \operatorname{Ext}(G,C) \to 0.$$

::: pf-proof

In step [](#s4){.pf-ref} replace $H^n(M;-)$ by $\operatorname{Hom}(G,-)$ and $H^{n+1}(M;-)$ by $\operatorname{Ext}(G,-)$, which step [](#s2){.pf-ref} licenses, and use that both are functors in the coefficient group, so the maps of the exact sequence are the ones displayed.

:::

:::


:::
:::
