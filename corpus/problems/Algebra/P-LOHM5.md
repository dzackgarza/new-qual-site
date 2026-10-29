---
schema: qual/card@1
id: P-LOHM5
kind: problem
title: Groups of order $p^3$ have a normal subgroup of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Source part (b) read "Suppose N = <h> is cyclic and classify all possibilities for G if |h| = p^3, |h| = p", which is inconsistent since |N| = p^2; the statement takes h to be an element of G of largest order, as on E-AMD-LSAG5UZT.
---

::: {.problem}
Let $p$ be a prime and $\abs{G} = p^3$.

(a) Prove that $G$ has a normal subgroup $N$ of order $p^2$.

(b) Let $h \in G$ be an element of largest order. Classify all possibilities for $G$ if (i) $\abs h = p^3$; (ii) $\abs h = p$.
:::

::: {.hint}
Sylow and semidirect products.
:::

::: {.solution}

::: pf

::: pf-step
(a) $G$ has a normal subgroup of order $p^2$.

::: pf-proof
Since $G$ is a nontrivial finite $p$-group, $Z(G)\ne1$ by the class equation.

::: pf-step
If $\abs{Z(G)}\ge p^2$, the claim holds.

::: pf-proof
The $p$-group $Z(G)$ has a subgroup of order $p^2$, and every subgroup of the center is normal.
:::

:::

::: pf-step
If $\abs{Z(G)}=p$, the claim holds.

::: pf-proof
Then $G/Z(G)$ has order $p^2$, so it is abelian. Choose a subgroup $L/Z(G)$ of order $p$; it is normal in the abelian group $G/Z(G)$, so its preimage $L$ is normal in $G$, and $\abs{L}=p\cdot p=p^2$.
:::

:::

:::

:::

::: pf-step
(b) If $h$ has largest order in $G$, then (i) $\abs h=p^3$ gives $\boxed{G\cong C_{p^3}}$, and (ii) $\abs h=p$ gives $\boxed{G\cong C_p^3}$ or, for odd $p$, $\boxed{G\cong\operatorname{UT}_3(\FF_p)}$, the group of upper unitriangular $3\times3$ matrices over $\FF_p$.

::: pf-proof

::: pf-step
(i) If $\abs h=p^3$, then $G=\generators h\cong C_{p^3}$.

::: pf-proof
$\generators h$ has $p^3=\abs G$ elements, and a cyclic group is determined by its order.
:::

:::

::: {.pf-step #abelian-exponent-p}
(ii) If $\abs h=p$ and $G$ is abelian, then $G\cong C_p^3$.

::: pf-proof
Every nonidentity element has order $p$, since $p$ is the largest order, so $G$ is an abelian group of exponent $p$, that is, a $3$-dimensional vector space over $\FF_p$.
:::

:::

::: {.pf-step #heisenberg}
If $\abs h=p$ and $G$ is nonabelian, then $p$ is odd and $G\cong\operatorname{UT}_3(\FF_p)$.

::: pf-proof
If $p=2$, then $g^2=1$ for all $g$, so $gk=(gk)^{-1}=k^{-1}g^{-1}=kg$ for all $g,k$, and $G$ is abelian; hence $p$ is odd.
Since $G$ is nonabelian, $G/Z(G)$ is not cyclic, so $\abs{Z(G)}=p$ and $G/Z(G)\cong C_p^2$.
Choose $x,y\in G$ whose images generate $G/Z(G)$, and put $z=[x,y]$.
Then $z\in Z(G)$ because $G/Z(G)$ is abelian, and $z\ne1$ because $x,y$ and $Z(G)$ generate $G$ and $G$ is nonabelian, so $Z(G)=\generators z$.
Thus $x^p=y^p=z^p=1$, $[x,y]=z$ and $z$ is central, and every element of $G$ is $x^ay^bz^c$ with $0\le a,b,c<p$.
The matrices $x=I+E_{12}$, $y=I+E_{23}$, $z=I+E_{13}$ satisfy the same relations in $\operatorname{UT}_3(\FF_p)$, which has order $p^3$, so $x^ay^bz^c\mapsto x^ay^bz^c$ is an isomorphism.
:::

:::

::: pf-qed
Both cases of (ii) occur: $C_p^3$ has exponent $p$, and for odd $p$ every element $I+M$ of $\operatorname{UT}_3(\FF_p)$, with $M$ strictly upper triangular and $M^3=0$, satisfies $(I+M)^p=I+pM+\binom p2M^2=I$, so $\operatorname{UT}_3(\FF_p)$ has exponent $p$.
Steps [](#abelian-exponent-p){.pf-ref} and [](#heisenberg){.pf-ref} cover the abelian and nonabelian cases.
:::

:::

:::

:::

:::
