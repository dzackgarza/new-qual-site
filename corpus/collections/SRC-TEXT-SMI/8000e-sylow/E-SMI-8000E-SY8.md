---
schema: qual/card@1
id: E-SMI-8000E-SY8
kind: problem
title: Sylow subgroups of symmetric groups are abelian
classification:
  areas:
  - algebra
  topics:
  - Sylow Theorems
  - Symmetric Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Checked Smith 8000e Sylow problem 8 against the PDF. Part (i) omits p>2; p=2 gives the nonabelian Sylow 2-subgroup D8 of S4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved the general p>n statement using p-adic valuation of (np)!, the orbit decomposition on np letters, and the faithful embedding into a product of cyclic order-p permutation groups; parts (i) and (ii) follow as n=2,3."
---

::: {.exercise}
(i) If $p>2$ and $P$ is a Sylow $p$-subgroup of $S(2p)$, prove $P$ is abelian.

(ii) Prove it for $p > 3$, and $P$ a Sylow $p$-subgroup of $S(3p)$.

(iii) Prove it for $p > n$, with $P$ a Sylow $p$-subgroup of $S(np)$.
:::

::: {.remark}
The printed first part omits the condition $p>2$. For $p=2$, a Sylow
$2$-subgroup of $S_4$ has order $8$ and is isomorphic to the nonabelian
dihedral group $D_8$. The corrected first part is exactly the case $n=2$ of
part (iii).
:::

::: {.solution}
It is enough to prove the general assertion in part (iii).

<1>1. Determine the order of a Sylow $p$-subgroup of $S_{np}$ when $p>n$.
::: {.proof}
Because $n<p$,
$$
np<p^2.
$$
Hence Legendre's formula gives
$$
v_p((np)!)
=\left\lfloor\frac{np}{p}\right\rfloor
+\left\lfloor\frac{np}{p^2}\right\rfloor+\cdots
=n.
$$
Therefore a Sylow $p$-subgroup $P$ of $S_{np}$ has order
$$
\boxed{|P|=p^n.}
$$
:::

<1>2. Every nontrivial $P$-orbit on the $np$ letters has size exactly $p$.
::: {.proof}
Let $\Omega$ be the set of $np$ letters on which $S_{np}$ acts. Since $P$ is
a $p$-group, every orbit size is a power of $p$. But
$$
|\Omega|=np<p^2,
$$
so an orbit cannot have size $p^2$ or larger. Therefore every orbit has size
either
$$
1\quad\text{or}\quad p.
$$
:::

<1>3. The action on each nontrivial orbit has cyclic image of order $p$.
::: {.proof}
Let $O$ be a $P$-orbit of size $p$. Restriction of permutations gives a
homomorphism
$$
\rho_O:P\longrightarrow S(O)\cong S_p.
$$
Its image is a $p$-subgroup of $S_p$. Since
$$
v_p(p!)=1,
$$
every $p$-subgroup of $S_p$ has order at most $p$. Because the orbit is
nontrivial, the image is nontrivial; hence
$$
|\rho_O(P)|=p.
$$
Thus $\rho_O(P)$ is cyclic.
:::

<1>4. There are exactly $n$ nontrivial orbits, and $P$ embeds in their product action.
::: {.proof}
Suppose there are $k$ nontrivial orbits
$$
O_1,\ldots,O_k.
$$
Since each has size $p$ and there are only $np$ letters,
$$
k\le n.
$$
Consider the product of the restricted actions
$$
\rho:P\longrightarrow
\rho_{O_1}(P)\times\cdots\times\rho_{O_k}(P).
$$
If an element lies in the kernel of $\rho$, it fixes every point in every
nontrivial orbit. It also fixes every point in every singleton orbit by
definition. Hence it fixes all $np$ letters, so it is the identity
permutation. Thus $\rho$ is injective.

Each factor on the right has order $p$ by step <1>3, so
$$
|P|\le p^k.
$$
Using step <1>1,
$$
p^n\le p^k.
$$
Therefore $n\le k$. Combined with $k\le n$, this gives
$$
k=n.
$$
:::

<1>5. Conclude that $P$ is abelian.
::: {.proof}
By step <1>4, $P$ embeds in a direct product of $n$ cyclic groups of order
$p$:
$$
P\hookrightarrow C_p^n.
$$
The target is abelian, and every subgroup of an abelian group is abelian.
Hence
$$
\boxed{P\text{ is abelian whenever }p>n.}
$$

Taking $n=2$ gives part (i) for $p>2$, and taking $n=3$ gives part (ii) for
$p>3$.
:::
:::
