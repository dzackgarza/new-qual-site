---
schema: qual/card@1
id: P-RE2VW
kind: problem
title: Minimal polynomial degrees in a Galois extension with group $A_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked June 2012 Fields 4 on PDF page 11, including the handwritten exclusion alpha not in F; retained the corrected coefficient field F and restored the exclusion."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked nontriviality of the root action from the fixed-field property, simplicity of A_n for n at least five, and the strict factorial inequality excluding every smaller degree."
---

::: {.problem}
Suppose $K/F$ is a Galois extension and that $\mathrm{Gal}(K/F)$ is isomorphic to $A_n$, with $n \geq 5$.
Suppose $\alpha \in K\setminus F$.
Prove that the minimal polynomial of $\alpha$ over $F$ has degree at least $n$.
(You may use whatever group theoretic facts you know about $A_n$ without proof.)
:::

::: {.remark}
The exclusion $\alpha\notin F$ is necessary: every element
of $F$ has a linear minimal polynomial over $F$.
The coefficient field in the conclusion must also be $F$,
not $K$; over $K$, the minimal polynomial of $\alpha\in K$
is always $T-\alpha$.
:::

::: {.solution}
Let $G=\operatorname{Gal}(K/F)$, let $m(T)\in F[T]$ be
the minimal polynomial of $\alpha$, and put $d=\deg m$.

<1>1. The action of $G$ on the roots of $m$ defines a
nontrivial homomorphism $\rho:G\to S_d$.

::: {.proof}
Normality and separability of the Galois extension imply
that $m$ splits in $K$ with $d$ distinct roots [@DF04].
Every $\sigma\in G$ fixes its coefficients, so sends each
root to a root. These permutations respect composition and
give the stated homomorphism.

The fixed field $K^G$ is $F$ [@DF04]. Since
$\alpha\notin F$, some $\sigma\in G$ satisfies
$\sigma(\alpha)\ne\alpha$. Thus the root action is not
trivial and $\ker\rho\ne G$.
:::

<1>2. The homomorphism $\rho$ is injective.

::: {.proof}
For $n\geq5$, the group $A_n$ is simple [@DF04], a
group-theoretic fact permitted in the question. Hence
$G\cong A_n$ has no normal subgroups other than $1$ and
$G$. The kernel of a homomorphism is normal, and step
<1>1 excludes the latter possibility. Therefore
$\ker\rho=1$.
:::

<1>3. One has $d\geq n$.

::: {.proof}
Injectivity gives $|A_n|=n!/2\leq |S_d|=d!$.
If $d<n$, then $d\leq n-1$, so
$$
d!\leq(n-1)!<\frac n2(n-1)!=\frac{n!}{2},
$$
where strictness follows from $n\geq5>2$.
This contradicts the previous inequality. Thus $d\geq n$,
as required.
:::
:::
