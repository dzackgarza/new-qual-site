---
schema: qual/card@1
id: T-DEFNAKA
kind: theorem
title: Nakayama's lemma, in its several forms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Nakayama's Lemma
  - Local Rings
relations:
- kind: uses
  target: D-DEFNOETH
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Checked the stated forms of Nakayama's lemma against Stacks Project Tag 00DV and the constant-fiber-dimension criterion against Tag 0FWG. Added the missing reducedness hypothesis and the dual-number counterexample to the unconditional claim.
prompts:
- State Nakayama's lemma.
- Over a local ring, how do you produce a minimal generating set of a finitely generated module?
- Where does finite generation get used, and what goes wrong without it?
---

::: {.theorem title="Nakayama's lemma"}
Let $A$ be a ring, $I$ an ideal, and $M$ an $A$-module.

(i) If $M$ is finitely generated and $M = IM$, there exists $a \equiv 1 \pmod I$ with $aM = 0$.

(ii) If in addition $I \subseteq \Jac A$, then $M = 0$.

(iii) If $I \subseteq \Jac A$, $M$ is finitely generated and $N \subseteq M$ is a submodule such that $N/IN \to M/IM$ is surjective, then $M = N$.

(iv) If $(A,\mm)$ is local, $M$ is finitely generated, and $f_1,\ldots,f_n \in M$ have images generating $M/\mm M$ as an $A/\mm$-vector space, then the $f_i$ generate $M$ as an $A$-module.
:::

::: {.remark}
Part (i) is the determinant trick: writing $m_i = \sum_j a_{ij}m_j$ with $a_{ij}\in I$ says $\id - (a_{ij})$ kills $M$, and multiplying by the adjugate shows $\det(\id - (a_{ij}))$ does too, an element congruent to $1$ modulo $I$.
Part (ii) follows because such an $a$ lies in no maximal ideal, hence is a unit.
Part (iii) applies (ii) to the cokernel $L$ of $N \injects M$, using right exactness of $\wait\tensor A/I$ to get $L = IL$.
Part (iv) is (iii) with $N = \generators{f_1,\ldots,f_n}$ and $I = \mm$.

For a finite module $M$ over a local ring $(A,\mm)$, the images of a minimal generating set form a basis of the vector space $M/\mm M$.
Conversely, lifts of a basis generate by part (iv), and no proper subset generates because its residue classes do not span.
Hence the minimal number of generators is $\dim_{A/\mm}(M/\mm M)$.
:::

::: {.proposition title="Constant fiber dimension over a reduced local ring"}
Let $A$ be a reduced local ring, let $M$ be a finite $A$-module, and let $r\ge0$ be an integer.
For each prime $\mathfrak p\subseteq A$, let $k(\mathfrak p)$ be the residue field of $A_{\mathfrak p}$.
If
$$
\dim_{k(\mathfrak p)}\bigl(M\otimes_A k(\mathfrak p)\bigr)=r
$$
for every prime $\mathfrak p\subseteq A$, then $M\cong A^r$.
This is the local case of the [finite locally free criterion](https://stacks.math.columbia.edu/tag/0FWG); the noetherian sheaf formulation is proved in [[P-AGH258SEMICONT]].
:::

::: {.example title="Constant fiber dimension over a nonreduced local ring"}
Let $k$ be a field, $A=k[\varepsilon]/(\varepsilon^2)$, and $M=A/(\varepsilon)$.
The only prime of $A$ is $(\varepsilon)$, and $M\otimes_A k\cong k$, so the fiber dimension is constantly one.
The module $M$ is cyclic but not free: the nonzero element $\varepsilon$ annihilates $M$, while every nonzero free $A$-module has zero annihilator.
:::

::: {.example title="Finite generation in Nakayama's lemma"}
Let $p$ be a prime number, $A=\ZZ_{(p)}$, and $\mm=pA$.
The $A$-module $M=\QQ$ is nonzero and satisfies $M=\mm M$, since multiplication by $p$ is surjective on $\QQ$.
It is not finitely generated: the denominators of any finite set of rational numbers have bounded powers of $p$, and taking $A$-linear combinations preserves that bound, whereas $\QQ$ contains $p^{-n}$ for every $n\ge0$.
:::
