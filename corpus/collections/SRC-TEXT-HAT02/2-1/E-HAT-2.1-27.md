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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.1, Exercise 27.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the five-lemma argument: naturality compares the two long exact sequences, the four outer vertical maps are isomorphisms because $f$ is a homotopy equivalence on $X$ and on $A$, so the middle map is too; part (b) is read at the level of the stated non-equivalence of pairs.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line, all three steps. (a): naturality gives a map from the long exact sequence of
    `(X,A)` to that of `(Y,B)`; the four surrounding vertical maps are isomorphisms because `f` is a
    homotopy equivalence on `X` and on `A`; the five lemma then gives the isomorphism on `H_n(X,A) ->
    H_n(Y,B)`, and this is a genuine isomorphism of the relative groups, not of the absolute ones.
    (b): the closure step is the tool and it is needed for exactly the reason the book's hint gives.
    The second pair `(D^n, D^n - {0})` has relative homology `H_n = H_{n-1}(S^{n-1}) = Z`, the *same*
    group as `H_n(D^n, S^{n-1})`, so comparing those two pairs directly proves nothing; what separates
    them is taking closures: `S^{n-1}` is already closed while `D^n - {0}` is dense with closure
    `D^n`, and a pair homotopy equivalence carries its maps and pair homotopies to the closure pairs,
    so a pair equivalence `(D^n, S^{n-1}) ~ (D^n, D^n - {0})` would give one
    `(D^n, S^{n-1}) ~ (D^n, D^n)`, whence `H_n(D^n,S^{n-1}) = Z` would have to equal
    `H_n(D^n,D^n) = 0`. So the inclusion is not a pair homotopy equivalence, although `f` is a
    homotopy equivalence on the total spaces and on the subspaces — which is precisely the hypothesis
    of (a), so the lesson is the one the exercise intends: pair homotopy equivalence implies relative
    homology isomorphism, and the converse direction fails because the two conditions on `f` (on `X`
    and on `A`) do not suffice for a *pair* equivalence. No correction was needed.
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
