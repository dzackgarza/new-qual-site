---
schema: qual/card@1
id: P-WOUSR
kind: problem
title: $\Out(A_4)$ is nontrivial
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard example of a nontrivial outer automorphism group, no repair needed),
    and the existing prose solution against a fresh re-derivation: A_4 has index 2
    in S_4 hence is normal, so conjugation by the odd permutation (12) restricts to
    an automorphism phi of A_4; if phi were inner, phi = c_g with g in A_4, the
    identity (12)x(12)^{-1} = gxg^{-1} rearranges to g^{-1}(12) x (g^{-1}(12))^{-1} =
    x, so g^{-1}(12) centralizes A_4; a 3-cycle's centralizer in S_4 has order
    24/8 = 3 because there are 8 three-cycles, matching the cyclic subgroup it
    generates, so C((123)) = <(123)> and C((124)) = <(124)>, whose intersection is
    trivial; hence g^{-1}(12) = 1, forcing g = (12), which is odd and not in A_4.
    All correct. The prose asserted both centralizer computations; the structured
    proof now derives them by orbit-stabilizer and gives the reason the two
    subgroups meet trivially. No source solution is retained for this card, so no
    source comparison was made. What was not checked: any printed source.
---

::: {.problem}
Show that $\Out(A_4)$ is nontrivial.
:::

::: {.solution}
Let $A_4\trianglelefteq S_4$ be the alternating group, the group of even permutations of $\{1,2,3,4\}$, of order $12$; for $g\in S_4$ let $c_g$ denote conjugation by $g$, and recall $\Inn(A_4)=\theset{c_g|_{A_4}:g\in A_4}$ and $\Out(A_4)=\Aut(A_4)/\Inn(A_4)$.

::: pf

::: {.pf-step #restricts}
$c_{(12)}$ restricts to an automorphism $\varphi$ of $A_4$.

::: pf-proof
$A_4$ has index $2$ in $S_4$, and a subgroup of index $2$ is normal, so $A_4\trianglelefteq S_4$; hence $c_{(12)}(A_4)=A_4$ and $\varphi\coloneqq c_{(12)}|_{A_4}$ is a homomorphism $A_4\to A_4$. Conjugation by an element is bijective on $S_4$ with inverse $c_{(12)^{-1}}$, and $c_{(12)^{-1}}$ also preserves $A_4$ by normality, so $\varphi$ is bijective.
:::

:::

::: {.pf-step #inner-form}
If $\varphi$ is inner, then there is $g\in A_4$ with $(12)\,x\,(12)^{-1}=gxg^{-1}$ for every $x\in A_4$, and then $g^{-1}(12)$ centralizes $A_4$.

::: pf-proof
Being inner means $\varphi=c_g|_{A_4}$ for some $g\in A_4$, which is the displayed identity. Multiplying it on the left by $g^{-1}$ and on the right by $g$ gives $g^{-1}(12)\,x\,(12)^{-1}g=x$, that is $\bigl(g^{-1}(12)\bigr)x\bigl(g^{-1}(12)\bigr)^{-1}=x$ for every $x\in A_4$, so $g^{-1}(12)$ commutes with every element of $A_4$.
:::

:::

::: {.pf-step #centralizer}
$C_{S_4}(A_4)=1$.

::: pf-proof
An element centralizing $A_4$ centralizes $(123)$ and $(124)$, so $C_{S_4}(A_4)\subseteq C_{S_4}((123))\cap C_{S_4}((124))$.

::: {.pf-step #cycle-centralizer}
$C_{S_4}((123))=\generators{(123)}$ and $C_{S_4}((124))=\generators{(124)}$.

::: pf-proof
In $S_4$ the $3$-cycles form a single conjugacy class: there are $4$ choices for the fixed point and $2$ cyclic orders on the remaining three symbols, so $8$ of them. By orbit--stabilizer the centralizer of a $3$-cycle has order $24/8=3$, and it contains the cyclic subgroup that $3$-cycle generates, which already has order $3$; hence the two are equal. The same count applies to $(124)$.
:::

:::

::: {.pf-step #intersection}
$\generators{(123)}\cap\generators{(124)}=1$.

::: pf-proof
Each is a group of prime order $3$, so each is either trivial or equal to the other; they are not equal because $(124)\notin\generators{(123)}$, whose nonidentity elements are the two $3$-cycles $(123)$ and $(132)$, which fix $4$ whereas $(124)$ does not.
:::

:::

So $C_{S_4}(A_4)$ is contained in the trivial group, hence is trivial.
:::

:::

::: {.pf-step #not-inner}
$\varphi$ is not inner.

::: pf-proof
Suppose $\varphi=c_g$ on $A_4$ for some $g\in A_4$. By step [](#inner-form){.pf-ref} the element $g^{-1}(12)$ centralizes $A_4$, hence lies in $C_{S_4}(A_4)=1$ by step [](#centralizer){.pf-ref}, so $g^{-1}(12)=1$ and $g=(12)$; but $(12)$ is a transposition, hence odd, hence not in $A_4$, contradicting $g\in A_4$.
:::

:::

::: {.pf-step}
$\Out(A_4)$ is nontrivial.

::: pf-proof
By step [](#restricts){.pf-ref} $\varphi$ is an automorphism of $A_4$, and by step [](#not-inner){.pf-ref} it is not inner, so its class in $\Aut(A_4)/\Inn(A_4)$ is not the identity coset. Hence $\Out(A_4)$ has more than one element.
:::

:::

:::
:::
