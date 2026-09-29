---
schema: qual/card@1
id: P-ALGS17B
kind: problem
title: "Subgroup indices in the simple group of order 168"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose that $G$ is a simple group of order $|G| = 168 = 2^3 \cdot 3 \cdot 7$.

(a) Show that $G$ does not have any subgroup $H$ with index $[G:H] \leq 6$.

(b) Show that $G$ does have a subgroup $H$ with index $[G:H] = 8$.
:::

::: {.solution}
**(a).**

::: pf

::: pf-step

Literally, \(H=G\) is a subgroup of index \(1\), so the intended assertion must concern proper subgroups.
We prove that \(G\) has no proper subgroup of index at most \(6\).

::: pf-proof

This is the only reading compatible with the statement, since \([G:G]=1\).

:::

:::

::: {.pf-step #s2}

Suppose \(H<G\) has index \(n\le6\). The action of \(G\) on the left cosets \(G/H\) gives a nontrivial homomorphism
\[
\rho:G\longrightarrow S_n.
\]

::: pf-proof

The coset action is transitive.
If it were trivial, every coset would be fixed by every element of \(G\); in particular the coset \(H\) would be fixed, so every \(g\in G\) would satisfy \(gH=H\), hence \(g\in H\), contradicting \(H<G\).

:::

:::

::: {.pf-step #s3}

Since \(G\) is simple, \( ho\) is injective.

::: pf-proof

The kernel of \( ho\) is a normal subgroup of \(G\). By step [](#s2){.pf-ref} it is not all of \(G\), so simplicity forces the kernel to be trivial.

:::

:::

::: {.pf-step #s4}

No such injection \(G\hookrightarrow S_n\) exists for \(n\le6\).

::: pf-proof

For \(n\le5\), \(|S_n|\le120<168=|G|\). For \(n=6\), injectivity would imply \(168\mid720\), but \(720/168=30/7\) is not an integer.
This contradicts step [](#s3){.pf-ref}.

:::

:::

::: pf-step

Hence \(G\) has no proper subgroup of index at most \(6\).

::: pf-proof

By contradiction from steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

**(b).**

:::

:::

::: pf-step

The number \(n_7\) of Sylow \(7\)-subgroups of \(G\) is \(8\).

::: pf-proof

Sylow's theorem gives \(n_7\equiv1\pmod7\) and \(n_7\mid24\), so \(n_7\in\{1,8\}\). If \(n_7=1\), the unique Sylow \(7\)-subgroup would be nontrivial and normal, contradicting simplicity.
Therefore \(n_7=8\).

:::

:::

::: {.pf-step #s7}

If \(P\) is a Sylow \(7\)-subgroup, then its normalizer \(N_G(P)\) has index \(8\).

::: pf-proof

The conjugation action of \(G\) on its Sylow \(7\)-subgroups is transitive, and the stabilizer of \(P\) is exactly \(N_G(P)\). By orbit-stabilizer,
\[
[G:N_G(P)]=n_7=8.
\]

:::

:::

::: pf-step

Thus \(H=N_G(P)\) is a subgroup of \(G\) with \([G:H]=8\).

::: pf-proof

This is step [](#s7){.pf-ref}.

:::

:::

:::

:::
