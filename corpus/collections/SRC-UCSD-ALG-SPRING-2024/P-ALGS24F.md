---
schema: qual/card@1
id: P-ALGS24F
kind: problem
title: Abelian Galois group implies $E = F[\alpha_i]$; prime-degree case
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
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
Suppose $F$ is a field of characteristic zero and $f$ is an irreducible polynomial of degree $n$ in $F[x]$.
Let $E$ be a splitting field of $f$ over $F$.
Let $\{\alpha_1, \ldots, \alpha_n\}$ be the set of zeros of $f$ in $E$.

(a) Prove that if $\operatorname{Gal}(E/F)$ is abelian, then $E = F[\alpha_i]$ for every $i$.

(b) Prove that if $n = p$ is prime, then $E = F[\alpha_1]$ implies that $\operatorname{Gal}(E/F) \simeq \mathbb{Z}/p\mathbb{Z}$.
:::

::: {.solution}
Let \(G=\operatorname{Gal}(E/F)\).

**(a).**

::: pf

::: {.pf-step #s1}

The group \(G\) acts transitively on the roots \(\alpha_1,\dots,\alpha_n\) of \(f\).

::: pf-proof

The polynomial \(f\) is irreducible over \(F\), and \(E\) is its splitting field. In a normal extension, any two roots of the same irreducible polynomial are conjugate by an \(F\)-automorphism of \(E\).

:::

:::

::: {.pf-step #s2}

For each \(i\), let
\[
H_i=\{\sigma\in G:\sigma(\alpha_i)=\alpha_i\}
=\operatorname{Gal}(E/F(\alpha_i)).
\]
If \(g(\alpha_i)=\alpha_j\), then
\[
H_j=gH_i g^{-1}.
\]

::: pf-proof

This is the usual conjugacy relation between stabilizers in a group action. The equality with \(\operatorname{Gal}(E/F(\alpha_i))\) follows because fixing \(F\) and \(\alpha_i\) is equivalent to fixing the field they generate.

:::

:::

::: pf-step

If \(G\) is abelian, then all the subgroups \(H_i\) are equal.

::: pf-proof

By step [](#s1){.pf-ref}, for every \(i,j\) there exists \(g\in G\) sending \(\alpha_i\) to \(\alpha_j\). Then step [](#s2){.pf-ref} gives \(H_j=gH_i g^{-1}=H_i\) because \(G\) is abelian.

:::

:::

::: {.pf-step #s4}

This common subgroup is trivial.

::: pf-proof

Let \(H=H_1=\cdots=H_n\). Every \(h\in H\) fixes every root \(\alpha_i\). Since \(E\) is the splitting field of \(f\), it is generated over \(F\) by these roots. Hence \(h\) fixes all of \(E\), so \(h=1\).

:::

:::

::: pf-step

Therefore \(E=F(\alpha_i)\) for every \(i\).

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s4){.pf-ref},
\[
\operatorname{Gal}(E/F(\alpha_i))=H_i=1.
\]
By the Galois correspondence, the fixed field of the trivial subgroup is \(E\), hence \(F(\alpha_i)=E\).

**(b).**

:::

:::

::: {.pf-step #s6}

Suppose \(n=p\) is prime and \(E=F(\alpha_1)\). Then
\[
[E:F]=p.
\]

::: pf-proof

The minimal polynomial of \(\alpha_1\) over \(F\) is the irreducible polynomial \(f\), whose degree is \(p\). Since \(E=F(\alpha_1)\), the extension degree is \(p\).

:::

:::

::: {.pf-step #s7}

The extension \(E/F\) is Galois.

::: pf-proof

The field \(E\) is the splitting field of \(f\). Since \(F\) has characteristic zero, every irreducible polynomial over \(F\) is separable. Thus \(E/F\) is normal and separable.

:::

:::

::: pf-step

Hence
\[
|\operatorname{Gal}(E/F)|=[E:F]=p,
\]
so
\[
\operatorname{Gal}(E/F)\cong\mathbb Z/p\mathbb Z.
\]

::: pf-proof

Use steps [](#s6){.pf-ref} and [](#s7){.pf-ref}. Every group of prime order is cyclic.

:::

:::

:::

:::
