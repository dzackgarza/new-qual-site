---
schema: qual/card@1
id: P-MMAQ-VE5GUZV5YG
kind: problem
title: Index-$n$ subgroups of $S_n$ and point stabilizers
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Subgroups
  - Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared both assertions with Groups 3 on PDF page 1; the conclusion concerns an automorphism, not necessarily conjugation."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the coset kernel using the normal subgroups of each symmetric group, including n=4 and n=6, the labeled stabilizer, and maximality; treated n=1 without claiming a proper maximal subgroup."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Groups (3) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAG3, whose solution repeats this coset-action argument."
---

::: {.problem}
Let $H$ be a subgroup of $S_n$ of index $n$.
Prove:

1. There is an isomorphism $f: S_n \to S_n$ such that $f(H)$ is the subgroup of $S_n$ stabilizing $n$.
   In particular, $H$ is isomorphic to $S_{n-1}$.

2. The only subgroups of $S_n$ containing $H$ are $S_n$ and $H$.
:::

::: {.solution}
For $n=1$, both $S_1$ and $H$ are trivial. The identity
automorphism proves both assertions, with $S_0$ also
the trivial group. Henceforth suppose $n\geq2$.

<1>1. The left-coset action defines an injective homomorphism
$\rho:S_n\longrightarrow\operatorname{Sym}(S_n/H)$.

::: {.proof}
Left multiplication is well defined: replacing a
representative $x$ by $xh$ with $h\in H$ does not change
$gxH$. Multiplication by $g^{-1}$ is its inverse, and
the multiplication law in $S_n$ verifies the action law.
Its kernel $N$ is normal in $S_n$ and contained in $H$,
since an element fixing all cosets fixes the coset $H$.
In particular $|N|$ divides $|H|=(n-1)!$.

For $n\geq5$, every nontrivial normal subgroup of $S_n$
contains $A_n$ [@DF04]. Since
$|A_n|=n!/2>(n-1)!=|H|$, this forces $N=1$.
For $n=4$, the nontrivial normal subgroups are
$V_4,A_4,S_4$, of orders $4,12,24$ [@DF04]. None has
order dividing $|H|=6$, so again $N=1$.
For $n=3$, the only nontrivial proper normal subgroup
is $A_3$, of order three [@DF04]; neither it nor $S_3$
can lie in the order-two group $H$.
Finally, for $n=2$ the group $H$ itself is trivial.
Thus the action is faithful in every case.
:::

<1>2. Relabeling the cosets produces the required
automorphism $f$ and the isomorphism $H\cong S_{n-1}$.

::: {.proof}
The set $S_n/H$ has $n$ elements. Choose a bijection
with $\{1,\ldots,n\}$ that labels the coset $H$ by $n$.
Through this bijection, $\rho$ becomes an injective
homomorphism $f:S_n\to S_n$. Both groups have $n!$
elements, so $f$ is an automorphism.

An element $g$ fixes the coset $H$ exactly when $gH=H$,
which is equivalent to $g\in H$. Surjectivity of $f$
therefore gives
$$
f(H)=\{\sigma\in S_n:\sigma(n)=n\}=:H_n.
$$
Restriction to $\{1,\ldots,n-1\}$ is an isomorphism
$H_n\to S_{n-1}$: any permutation of those letters
extends uniquely by fixing $n$. This proves part (1).
No assertion that $f$ is inner is needed.
:::

<1>3. The only subgroups containing $H$ are $H$ and $S_n$.

::: {.proof}
It suffices to prove this for $H_n$, since $f$ bijects
subgroups and preserves inclusion. Suppose
$H_n\subsetneq J\leq S_n$ and choose $g\in J\setminus H_n$.
Then $g(n)=i\ne n$. The group $H_n$ acts transitively on
the other $n-1$ letters, so the $J$-orbit of $n$ contains
all letters: it contains $i$ and every $h(i)$ with
$h\in H_n$, as well as $n$. The stabilizer of $n$ in
$J$ is exactly $H_n$, because $H_n\leq J$ and $H_n$
is the full stabilizer in $S_n$.
Orbit-stabilizer gives
$|J|=n|H_n|=n!$, hence $J=S_n$.
This proves part (2) and, for $n\geq2$, maximality of $H$.
:::
:::
