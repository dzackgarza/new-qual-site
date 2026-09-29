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
**(a).**

::: pf

::: {.pf-step #p1-1}
$f$ induces a map of long exact sequences of the pairs $(X, A)$ and $(Y, B)$.

::: pf-proof
functoriality of the long exact sequence of a pair.
:::

:::

::: {.pf-step #p1-2}
$f_* : H_n(X) \to H_n(Y)$ and $f_* : H_n(A) \to H_n(B)$ are isomorphisms for all $n$.

::: pf-proof
hypothesis (both $f : X \to Y$ and $f : A \to B$ are homotopy equivalences).
:::

:::

::: {.pf-step #p1-3}
By the five lemma applied to the map of long exact sequences, $f_* : H_n(X, A) \to H_n(Y, B)$ is an isomorphism for all $n$.

::: pf-proof
Steps [](#p1-1){.pf-ref} and [](#p1-2){.pf-ref} (the five lemma).
:::

:::

:::

**(b).**

::: pf

::: pf-step
$f : D^n \to D^n$ is a homotopy equivalence (it is the identity), and $f : S^{n-1} \to D^n - \{0\}$ is a homotopy equivalence (both are homotopy equivalent to $S^{n-1}$).

::: pf-proof
$D^n$ is contractible, and $D^n - \{0\}$ deformation retracts onto $S^{n-1}$.
:::

:::

::: {.pf-step #p2-2}
But $f$ is not a homotopy equivalence of pairs.

::: pf-proof
suppose $g : (D^n, D^n - \{0\}) \to (D^n, S^{n-1})$ were a homotopy inverse of pairs.
:::

:::

::: pf-step
Then $g$ would restrict to a map $D^n - \{0\} \to S^{n-1}$ that is a homotopy inverse to the inclusion $S^{n-1} \hookrightarrow D^n - \{0\}$.

::: pf-proof
Step [](#p2-2){.pf-ref} (homotopy inverse of pairs restricts to homotopy inverse on the subspaces).
:::

:::

::: {.pf-step #p2-4}
This would give a retraction $D^n - \{0\} \to S^{n-1}$ (or, after the homotopy, a retraction of $D^n$ onto $S^{n-1}$), which is impossible.

::: pf-proof
$S^{n-1}$ is not a retract of $D^n$ (e.g. $H_{n-1}(S^{n-1}) = \ZZ$ does not split off $H_{n-1}(D^n) = 0$).
:::

:::

::: {.pf-step #p2-5}
Hence $f$ is not a homotopy equivalence of pairs.

::: pf-proof
Step [](#p2-4){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#p1-3){.pf-ref} (a) and [](#p2-5){.pf-ref} (b).
:::

:::

:::
