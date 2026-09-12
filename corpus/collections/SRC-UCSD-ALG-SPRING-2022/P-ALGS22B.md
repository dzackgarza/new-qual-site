---
schema: qual/card@1
id: P-ALGS22B
kind: problem
title: "A_n has no subgroup of index n/2 for n ≥ 5"
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

::: problem
(a) Prove that for $n \geq 5$, the alternating group $A_n$ has no subgroup $H$ such that $|A_n : H| = n/2$.
Conclude that $A_n$ has no subgroup isomorphic to $S_{n-1}$.

(b) Is the result of part (a) true when $n = 4$?
:::


::: {.solution}
<1>1. Suppose \(n\ge5\) and \(H\le A_n\) has index \([A_n:H]=n/2\). Then \(n\) must be even, and the action on left cosets gives a homomorphism
\[
\rho:A_n\longrightarrow S_{n/2}.
\]
::: {.proof}
The index is an integer, so the hypothesis is already impossible when \(n\) is odd. For even \(n\), every group acts on its left cosets by permutation, giving the displayed homomorphism.
:::

<1>2. The homomorphism \(\rho\) is nontrivial and therefore injective.
::: {.proof}
Because \(H\) is proper, the coset action is nontrivial. For \(n\ge5\), the alternating group \(A_n\) is simple. Hence \(\ker\rho\trianglelefteq A_n\) is either \(1\) or \(A_n\); nontriviality of the action rules out the latter, so \(\ker\rho=1\).
:::

<1>3. This is impossible. Hence \(A_n\) has no subgroup of index \(n/2\).
::: {.proof}
Injectivity would imply
\[
|A_n|=\frac{n!}{2}\le \left(\frac n2\right)!.
\]
But for every even \(n\ge6\),
\[
\frac{n!}{2}>\left(\frac n2\right)!,
\]
for example because \(n!/2\) contains the product of the \(n/2\) integers \(n/2+1,\ldots,n\), each at least \(2\), in addition to \((n/2)!\). Thus no such injection exists. Together with the odd case from <1>1, this proves the claim for all \(n\ge5\).
:::

<1>4. Consequently \(A_n\) has no subgroup isomorphic to \(S_{n-1}\).
::: {.proof}
A subgroup isomorphic to \(S_{n-1}\) would have order \((n-1)!\), hence index
\[
\frac{|A_n|}{(n-1)!}=\frac{n!/2}{(n-1)!}=\frac n2.
\]
This contradicts <1>3.
:::

<1>5. The result is also true for \(n=4\): \(A_4\) has no subgroup of index \(2\), hence no subgroup isomorphic to \(S_3\).
::: {.proof}
A subgroup \(H\le A_4\) of index \(2\) would be normal and have order \(6\). If \(H\) contained any element of order \(3\), normality would force it to contain the entire conjugacy class of that element in \(A_4\). The eight \(3\)-cycles of \(A_4\) split into two conjugacy classes of four, so this observation alone is not enough; instead use the quotient: an index-two subgroup would give a nontrivial homomorphism \(A_4\to C_2\). But the commutator subgroup of \(A_4\) is the Klein four group \(V_4\), so
\[
A_4^{\mathrm{ab}}\cong A_4/V_4\cong C_3,
\]
which has no quotient of order \(2\). Thus no index-two subgroup exists. Since \(|S_3|=6\), an embedded \(S_3\) would have index \(2\), so it cannot exist either.
:::
:::
