---
schema: qual/card@1
id: P-BERK89S-05
kind: problem
title: Elements of odd order form a normal index-two subgroup when the group has twice odd order
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Computed the sign of each left translation from its cycle decomposition,
    then identified the odd-order elements as the kernel of the resulting sign
    character and used Cauchy's theorem to show that its image has order two.
---

::: {.problem}
Let $G$ be a finite group whose order is twice an odd number. For $g\in G$, let
\[
\lambda_g(x)=gx
\]
be the left-translation permutation of $G$.

1. Prove that $\lambda_g$ is even if and only if the order of $g$ is odd.
2. Let
   \[
   N=\{g\in G:\operatorname{ord}(g)\text{ is odd}\}.
   \]
   Prove that $N$ is a normal subgroup of index $2$.
:::

::: {.solution}
Write $\abs{G}=2m$, where $m$ is odd, and define
$$
\chi(g)=\operatorname{sgn}(\lambda_g)\in\{\pm1\}.
$$

<1>1. If $g\in G$ has order $d$, then $\lambda_g$ is a product of
$2m/d$ disjoint cycles, each of length $d$.

::: {.proof}
For any $x\in G$, the orbit of $x$ under repeated application of
$\lambda_g$ is
$$
x,\ gx,\ g^2x,\ldots.
$$
The equality $g^k x=x$ holds exactly when $g^k=e$, so the orbit has size
$d$. These orbits are the cycles of $\lambda_g$, they partition the $2m$
elements of $G$, and therefore there are $2m/d$ of them.
:::

<1>2. The permutation $\lambda_g$ is even if and only if $d$ is odd.

::: {.proof}
A cycle of length $d$ has sign $(-1)^{d-1}$, so step <1>1 gives
$$
\chi(g)=(-1)^{(d-1)(2m/d)}.
$$
If $d$ is odd, then $d-1$ is even, hence $\chi(g)=1$.

Suppose instead that $d$ is even. Since $d$ divides $2m$ and $m$ is odd,
we may write $d=2e$ with $e\mid m$. Thus
$$
\frac{2m}{d}=\frac{m}{e}
$$
is odd, while $d-1$ is also odd. Hence $\chi(g)=-1$. This proves the
equivalence.
:::

<1>3. The map $\chi:G\to\{\pm1\}$ is a group homomorphism.

::: {.proof}
For $g,h,x\in G$,
$$
\lambda_{gh}(x)=ghx=\lambda_g(\lambda_h(x)),
$$
so $\lambda_{gh}=\lambda_g\lambda_h$. Since the sign of permutations is
multiplicative,
$$
\chi(gh)=\chi(g)\chi(h).
$$
:::

<1>4. The set $N$ is the kernel of $\chi$.

::: {.proof}
By definition, $\chi(g)=1$ exactly when $\lambda_g$ is even. Step <1>2
shows that this occurs exactly when $g$ has odd order. Hence
$$
N=\ker\chi.
$$
:::

<1>5. The homomorphism $\chi$ is surjective.

::: {.proof}
Because $2$ divides $\abs{G}$, Cauchy's theorem gives an element $t\in G$
of order $2$. By step <1>2, $\lambda_t$ is odd, so $\chi(t)=-1$. Also
$\chi(e)=1$. Thus the image of $\chi$ is all of $\{\pm1\}$.
:::

<1>6. The set $N$ is a normal subgroup of $G$ of index $2$.

::: {.proof}
By steps <1>3 and <1>4, $N$ is the kernel of a homomorphism, hence is a
normal subgroup. By step <1>5 and the first isomorphism theorem,
$$
[G:N]=\abs{\operatorname{im}\chi}=2.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (1), and step <1>6 proves part (2).
:::
:::
