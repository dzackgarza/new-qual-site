---
schema: qual/card@1
id: P-ARTALG-JU06-3
kind: problem
title: Subgroups of index the smallest prime divisor are normal
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the smallest-prime hypothesis with July 2006 Groups 3 in the retained extraction; retained that hypothesis in the title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the coset stabilizer, both image-order divisibilities, and equality of the subgroup with the action kernel, including p=2."
---

::: {.problem}
Let $G$ be a finite group of order $n$ and let $p$ be the smallest prime dividing $n$.
Show that any subgroup of $G$ of index $p$ is normal in $G$.
:::

::: {.solution}
Let $H\leq G$ have index $p$.

<1>1. Left multiplication on the $p$ left cosets of $H$ gives a
homomorphism $\rho:G\to S_p$, and the stabilizer of the coset $H$
is exactly $H$.

::: {.proof}
For $g\in G$, define $\rho(g)(aH)=gaH$. Equality of left cosets
is preserved by left multiplication, so the map is well-defined.
It is a permutation with inverse $\rho(g^{-1})$, and associativity
gives $\rho(gk)=\rho(g)\rho(k)$. Finally,
$\rho(g)(H)=H$ if and only if $gH=H$, which is equivalent to
$g\in H$. In particular, $\ker\rho\subseteq H$.
:::

<1>2. The subgroup $H$ is the kernel of $\rho$, and is therefore normal.

::: {.proof}
Every permutation in $\rho(H)$ fixes the coset $H$, so it acts as
a permutation of the other $p-1$ cosets. Thus $\rho(H)$ is a
subgroup of $S_{p-1}$, and its order divides $(p-1)!$.
Its order also divides $|H|$, by the first isomorphism theorem
and Lagrange's theorem [@DF04].

Every prime dividing $|H|$ divides $|G|=n$, so is at least $p$.
Every prime dividing $(p-1)!$ is less than $p$. Hence these two
integers are relatively prime. This includes $p=2$, when
$(p-1)!=1$. The two divisibilities imply $|\rho(H)|=1$.
Consequently $H\subseteq\ker\rho$, and step <1>1 gives the reverse
containment. Therefore $H=\ker\rho\lhd G$.
:::
:::
