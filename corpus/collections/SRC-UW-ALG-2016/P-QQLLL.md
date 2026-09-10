---
schema: qual/card@1
id: P-QQLLL
kind: problem
title: An outer automorphism of $S_6$ from a transitive embedding $S_5\hookrightarrow
  S_6$
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Automorphisms
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Recall that an inner automorphism of a group is an automorphism given by conjugation by an element of the group.
An outer automorphism is an automorphism that is not inner.

- Prove that $S_5$ has a subgroup of order 20.

- Use the subgroup from (a) to construct a degree 6 permutation representation of $S_5$ (i.e., an embedding $S_5 \hookrightarrow S_6$ as a transitive permutation group on 6 letters).

- Conclude that $S_6$ has an outer automorphism.
:::


::: solution
<1>1. The affine transformations of \(\mathbb F_5\),
\[
H=\{x\mapsto ax+b:a\in\mathbb F_5^\times,\ b\in\mathbb F_5\},
\]
form a subgroup of \(S_5\) of order \(20\).
::: {.proof}
Each map \(x\mapsto ax+b\) with \(a\ne0\) is a permutation of the five-element set \(\mathbb F_5\). The composite of
\[
x\mapsto ax+b
\quad\text{and}\quad
x\mapsto cx+d
\]
is
\[
x\mapsto acx+(ad+b),
\]
and inverses have the same form, so these permutations form a subgroup. There are \(4\) choices for \(a\) and \(5\) choices for \(b\), hence
\[
|H|=4\cdot5=20.
\]
:::

<1>2. The action of \(S_5\) on the six left cosets of \(H\) gives a transitive homomorphism
\[
\rho:S_5\longrightarrow S_6.
\]
::: {.proof}
Since
\[
[S_5:H]=\frac{120}{20}=6,
\]
left multiplication on the set \(S_5/H\) defines a permutation representation of degree \(6\). Coset actions are always transitive.
:::

<1>3. The homomorphism \(\rho\) is injective.
::: {.proof}
Its kernel is the core
\[
\ker\rho=\bigcap_{g\in S_5}gHg^{-1},
\]
a normal subgroup of \(S_5\) contained in \(H\). We use the standard theorem that \(A_n\) is simple for \(n\ge5\), which implies that every nontrivial normal subgroup of \(S_n\) contains \(A_n\): indeed, if \(N\trianglelefteq S_n\) is nontrivial, then either \(N\cap A_n\ne1\), in which case simplicity gives \(A_n\subseteq N\), or \(N\cap A_n=1\), in which case \([N,A_n]\subseteq N\cap A_n=1\), so \(N\) centralizes \(A_n\); but the centralizer of \(A_n\) in \(S_n\) is trivial.

Thus a nontrivial kernel would contain \(A_5\), of order \(60\). This is impossible because \(\ker\rho\subseteq H\) and \(|H|=20\). Hence \(\ker\rho=1\).
:::

<1>4. Let
\[
J=\rho(S_5)\le S_6.
\]
Then \(J\cong S_5\), has index \(6\) in \(S_6\), and is transitive in the natural action on six letters.
:::

<1>5. Let \(S_6\) act by left multiplication on the six cosets \(S_6/J\). This gives a homomorphism
\[
\Phi:S_6\longrightarrow S_6.
\]
The homomorphism \(\Phi\) is injective, hence an automorphism.
::: {.proof}
The coset action has degree
\[
[S_6:J]=\frac{720}{120}=6.
\]
Its kernel is a normal subgroup of \(S_6\) contained in \(J\). By the same normal-subgroup consequence of the simplicity of \(A_6\) used in <1>3, any nontrivial normal subgroup of \(S_6\) contains \(A_6\), which has order \(360\). Since \(|J|=120\), the kernel cannot be nontrivial. Thus \(\Phi\) is injective. Because domain and codomain both have order \(720\), \(\Phi\) is an automorphism.
:::

<1>6. Under \(\Phi\), the subgroup \(J\) becomes a point stabilizer in the six-point coset action.
::: {.proof}
The stabilizer in \(S_6\) of the coset \(J\in S_6/J\) is exactly \(J\). Therefore, after identifying the six cosets with the six letters of the target symmetric group, \(\Phi(J)\) is the stabilizer of one letter. In particular \(\Phi(J)\) is intransitive in the natural degree-\(6\) action.
:::

<1>7. The automorphism \(\Phi\) is outer.
::: {.proof}
The subgroup \(J\) is transitive on the six letters by <1>4, whereas \(\Phi(J)\) is a point stabilizer and hence intransitive by <1>6. Conjugating a subgroup inside \(S_6\) merely relabels the six letters, so conjugation preserves the multiset of orbit sizes; in particular it preserves transitivity. Therefore \(J\) and \(\Phi(J)\) are not conjugate in \(S_6\).

If \(\Phi\) were inner, say \(\Phi(g)=sgs^{-1}\), then \(\Phi(J)=sJs^{-1}\) would be conjugate to \(J\), a contradiction. Hence \(\Phi\) is an outer automorphism of \(S_6\).
:::
:::
