---
schema: qual/card@1
id: E-HAT-2.1-27
kind: problem
title: Map that is homotopy equivalence on $X$ and $A$ induces isomorphism on relative homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Relative Homology
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $f: (X, A) \to (Y, B)$ be a map such that both $f: X \to Y$ and the restriction $f: A \to B$ are homotopy equivalences.

(a) Show that $f_*: H_n(X, A) \to H_n(Y, B)$ is an isomorphism for all $n$.

(b) For the case of the inclusion $f: (D^n, S^{n-1}) \hookrightarrow (D^n, D^n - \{0\})$, show that $f$ is not a homotopy equivalence of pairs — there is no $g: (D^n, D^n - \{0\}) \to (D^n, S^{n-1})$ such that $fg$ and $gf$ are homotopic to the identity through maps of pairs.
[Observe that a homotopy equivalence of pairs $(X, A) \to (Y, B)$ is also a homotopy equivalence for the pairs obtained by replacing $A$ and $B$ by their closures.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The map $f$ induces isomorphisms $H_k(X,A)\to H_k(Y,B)$ in every degree.

::: pf-proof

Naturality gives a map from the long exact sequence of $(X,A)$ to that of $(Y,B)$. In the five-term segment centered on $H_k(X,A)\to H_k(Y,B)$, the other four vertical maps are induced on $H_k(X)$, $H_k(A)$, $H_{k-1}(A)$, and $H_{k-1}(X)$. They are isomorphisms because $f$ is a homotopy equivalence on each of $X$ and $A$. The five lemma gives the claim. This proves (a).

:::

:::

::: {.pf-step #s2}

If $f:(X,A)\to(Y,B)$ is a homotopy equivalence of pairs, then the same maps and pair homotopies give a homotopy equivalence $(X,\overline A)\to(Y,\overline B)$.

::: pf-proof

A continuous map taking $A$ into $B$ takes $\overline A$ into $\overline B$. The same holds for a proposed pair inverse. At each time, a homotopy through maps of pairs takes $A$ into $A$ or $B$ into $B$ as appropriate, so continuity extends the inclusion to its closure. The endpoint identities and pair homotopies therefore remain valid on the closure pairs.

:::

:::

::: {.pf-step #s3}

For $n\ge1$, the inclusion
$$
(D^n,S^{n-1})\hookrightarrow(D^n,D^n\setminus\{0\})
$$
is not a homotopy equivalence of pairs.

::: pf-proof

The sphere is closed in $D^n$, while $D^n\setminus\{0\}$ is dense. If the inclusion had a pair homotopy inverse, step [](#s2){.pf-ref} would give a homotopy equivalence
$$
(D^n,S^{n-1})\simeq(D^n,D^n).
$$
By step [](#s1){.pf-ref}, their relative homology groups would be isomorphic. But
$$
H_n(D^n,S^{n-1})\cong\widetilde H_{n-1}(S^{n-1})\cong\ZZ,
\qquad
H_n(D^n,D^n)=0,
$$
a contradiction. This proves (b).

:::

:::

:::
:::
