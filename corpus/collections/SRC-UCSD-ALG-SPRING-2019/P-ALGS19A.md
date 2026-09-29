---
schema: qual/card@1
id: P-ALGS19A
kind: problem
title: "Non-cyclic group of order pn with element of order n implies p | φ(n)"
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
Suppose $G$ is a non-cyclic finite group of order $pn$ where $p$ is prime and $n \in \mathbb{Z}^+$.
Suppose $\gcd(p!, n) = 1$, and $G$ has an element of order $n$.
Prove that $p \mid \phi(n)$, where $\phi(n) = |\{k \in \mathbb{Z} \mid 1 \leq k \leq n, \gcd(k, n) = 1\}|$ is the Euler $\phi$-function.
:::

::: {.solution}

::: pf

::: pf-step

Let \(x\in G\) have order \(n\), and put \(H=\langle x\rangle\). Then \(|H|=n\) and \([G:H]=p\).

::: pf-proof

By hypothesis \(|G|=pn\) and \(|x|=n\).

:::

:::

::: pf-step

Let \(G\) act on the \(p\) left cosets of \(H\), and let
\[
\rho:G\longrightarrow S_p
\]
be the corresponding homomorphism.
Then \(|\rho(G)|=p\).

::: pf-proof

The action is transitive, so \(p\) divides \(|\rho(G)|\) by orbit-stabilizer.
On the other hand, \(|\rho(G)|\) divides both \(|G|=pn\) and \(|S_p|=p!\). Since \(\gcd(n,p!)=1\), one has
\[
\gcd(pn,p!)=p,
\]
so \(|\rho(G)|\mid p\). Hence \(|\rho(G)|=p\).

:::

:::

::: pf-step

The kernel of \(\rho\) is \(H\). In particular, \(H\trianglelefteq G\) and \(G/H\cong C_p\).

::: pf-proof

Since \(|\rho(G)|=p\), the first isomorphism theorem gives
\[
|\ker\rho|=\frac{|G|}{p}=n.
\]
The kernel of the coset action is contained in the stabilizer of the coset \(H\), namely \(H\). Since both have order \(n\), they are equal.

:::

:::

::: pf-step

Conjugation induces a homomorphism
\[
\theta:G/H\longrightarrow \operatorname{Aut}(H).
\]
This homomorphism is nontrivial.

::: pf-proof

Because \(H\trianglelefteq G\), conjugation preserves \(H\), and because \(H\) is abelian, conjugation by elements of \(H\) acts trivially on \(H\); hence the action factors through \(G/H\).

If \(\theta\) were trivial, then \(H\subseteq Z(G)\). Thus \(G\) would be abelian.
Since \(|G|=pn\) and \(\gcd(p,n)=1\), its Sylow \(p\)-subgroup \(P\) would have order \(p\), and
\[
G=H\times P\cong C_n\times C_p\cong C_{pn},
\]
because \(H\cap P=1\) and \(np=|G|\). This contradicts the hypothesis that \(G\) is non-cyclic.

:::

:::

::: pf-step

Since \(G/H\cong C_p\) has prime order and \(\theta\) is nontrivial, \(\theta\) is injective.
Therefore
\[
p\mid |\operatorname{Aut}(H)|.
\]

::: pf-proof

A nontrivial homomorphism from a group of prime order has trivial kernel.
Hence \(C_p\cong G/H\) embeds in \(\operatorname{Aut}(H)\), so Lagrange's theorem gives the divisibility.

:::

:::

::: pf-step

Since \(H\cong C_n\), one has \(|\operatorname{Aut}(H)|=\varphi(n)\). Hence
\[
p\mid\varphi(n).
\]

::: pf-proof

The automorphisms of a cyclic group of order \(n\) are exactly the maps sending a generator to another generator, so their number is Euler's \(\varphi(n)\).

:::

:::

:::

:::
