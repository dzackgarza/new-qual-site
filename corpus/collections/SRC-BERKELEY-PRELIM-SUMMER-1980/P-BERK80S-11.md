---
schema: qual/card@1
id: P-BERK80S-11
kind: problem
title: Finite groups as permutation and even-permutation groups
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 11 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified Cayley’s left-regular embedding and the parity-correcting embedding of a symmetric group into an alternating group on two additional letters.
---

::: {.problem}
Prove that every finite group is isomorphic to

1. A group of permutations;

2. A group of even permutations.
:::


::: {.solution}
Let $G$ be a finite group with $|G|=n$.

<1>1. $G$ is isomorphic to a group of permutations.
::: {.proof}
For each $g\in G$, let
\[
L_g:G\longrightarrow G,
\qquad
L_g(x)=gx.
\]
Because multiplication by $g$ has inverse multiplication by $g^{-1}$, each $L_g$ is a permutation of the underlying set $G$.
Moreover,
\[
L_g\circ L_h=L_{gh},
\]
so
\[
\lambda:G\longrightarrow \operatorname{Sym}(G),
\qquad
\lambda(g)=L_g
\]
is a homomorphism.
If $L_g$ is the identity permutation, then
\[
g=L_g(e)=e,
\]
so $\lambda$ is injective. Hence
\[
G\cong \lambda(G)\le \operatorname{Sym}(G)\cong S_n.
\]
This is Cayley’s theorem.
:::

<1>2. Every finite group is isomorphic to a group of even permutations.
::: {.proof}
By <1>1 it suffices to embed $S_n$ into an alternating group.
Regard $S_n$ as the permutations of $\{1,\ldots,n+2\}$ that fix $n+1$ and $n+2$, and let
\[
\tau=(n+1\ n+2).
\]
Then $\tau$ commutes with every element of this copy of $S_n$.

Define
\[
\Phi:S_n\longrightarrow A_{n+2}
\]
by
\[
\Phi(\sigma)=
\begin{cases}
\sigma,&\sigma\text{ even},\\
\sigma\tau,&\sigma\text{ odd}.
\end{cases}
\]
Equivalently, if $\varepsilon(\sigma)\in\{0,1\}$ is the parity of $\sigma$, then
\[
\Phi(\sigma)=\sigma\tau^{\varepsilon(\sigma)}.
\]
The permutation $\Phi(\sigma)$ is always even, because an odd $\sigma$ is multiplied by the odd transposition $\tau$.

Since $\tau$ commutes with $S_n$ and parity is additive modulo $2$,
\[
\begin{aligned}
\Phi(\sigma\rho)
&=\sigma\rho\,\tau^{\varepsilon(\sigma\rho)}\\
&=\sigma\rho\,\tau^{\varepsilon(\sigma)+\varepsilon(\rho)}\\
&=\sigma\tau^{\varepsilon(\sigma)}\rho\tau^{\varepsilon(\rho)}\\
&=\Phi(\sigma)\Phi(\rho).
\end{aligned}
\]
Thus $\Phi$ is a homomorphism.
If $\Phi(\sigma)=e$, then restricting to the first $n$ letters gives $\sigma=e$, so $\Phi$ is injective.
Therefore
\[
S_n\hookrightarrow A_{n+2}.
\]
Composing this embedding with the Cayley embedding of $G$ proves that $G$ is isomorphic to a subgroup of an alternating group, hence to a group of even permutations.
:::
:::
