---
schema: qual/card@1
id: P-3RGXW
kind: problem
title: Isomorphism classes of subgroups of $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Subgroups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Describe the isomorphism classes of subgroups of the additive group of rational numbers $(\QQ, +)$ (rank 1 torsion-free abelian groups).

(1) How many isomorphism classes are there (what is the exact cardinality)?

(2) Are the subrings $\ZZ[1/p \mid p \in S]$ associated to different sets of primes $S \subseteq \mathbb{P}$ distinct and non-isomorphic?

(3) Do these exhaust all subgroups of $\QQ$? (Explain Baer's classification via height vectors and types).
:::

::: {.solution}
Let $G\le\QQ$ be nonzero and fix $0\ne x\in G$. For each prime $p$, define
$$
h_p(x)=\sup\{m\ge0:x\in p^mG\}\in\NN\cup\{\infty\}.
$$
The sequence $(h_p(x))_p$ is called a characteristic of $G$.
Two characteristics $(a_p)$ and $(b_p)$ are called equivalent when they agree at all but finitely many primes and $a_p=\infty\iff b_p=\infty$ for every $p$.
The equivalence class of a characteristic of $G$ is the type of $G$.

::: pf

::: {.pf-step #s1}
Changing the nonzero element changes its characteristic only at finitely many primes, and never changes which coordinates are infinite. Hence the type of $G$ is well defined.

::: pf-proof
If $0\ne y\in G$, then $by=ax$ for nonzero integers $a,b$. In the torsion-free group $G\le\QQ$, $h_p(nz)=h_p(z)+v_p(n)$ for every nonzero integer $n$ and $0\neq z\in G$, since $nz\in p^mG$ if and only if $z\in p^{m-v_p(n)}G$ for $m\ge v_p(n)$. Hence for every prime $p$,
$$
h_p(y)=h_p(x)+v_p(a)-v_p(b)
$$
with the convention $\infty+c=\infty$. Only primes dividing $ab$ can change, and an infinite height remains infinite.
:::

:::

::: {.pf-step #s2}
Two nonzero subgroups of $\QQ$ are isomorphic if and only if they have the same type.

::: pf-proof

::: {.pf-step #recover}
If $0\ne x\in G\le\QQ$, then $G=\{qx: q\in\QQ,\ v_p(q)\ge -h_p(x)\text{ for every prime }p\}$.

::: pf-proof
For a prime $p$ and $m\ge0$, the element $x/p^m\in\QQ$ is the only rational $g$ with $p^mg=x$, so $x/p^m\in G$ exactly when $x\in p^mG$, that is, when $m\le h_p(x)$. Let $q=a/b$ in lowest terms with $b=\prod_p p^{m_p}$. If $qx\in G$, then $x/p^{m_p}$ is an integer combination of $qx$ and $x$, because $a$ is prime to $p^{m_p}$, so $m_p\le h_p(x)$. Conversely, if $m_p\le h_p(x)$ for every $p\mid b$, then each $x/p^{m_p}$ lies in $G$, and since the integers $b/p^{m_p}$ have gcd $1$, the element $x/b$ is an integer combination of the $x/p^{m_p}$; hence $qx=a\cdot x/b\in G$.
:::

:::

::: pf-step
Isomorphic subgroups have the same type.

::: pf-proof
An isomorphism $\varphi\colon G\to H$ satisfies $x\in p^mG\iff\varphi(x)\in p^mH$, so $h_p(\varphi(x))=h_p(x)$ for every $p$.
:::

:::

::: pf-step
Subgroups of the same type are isomorphic.

::: pf-proof
Let $0\ne x\in G$ and $0\ne y\in H$ have equivalent characteristics. At the finitely many primes where they differ, both heights are finite, so replacing $y$ by $(c/d)y$ for suitable coprime integers $c,d$, with $d$ dividing a power of those primes within the height of $y$, changes $h_p(y)$ by $v_p(c)-v_p(d)$ at those primes only, by the computation of step [](#s1){.pf-ref}; choose $c,d$ so that $h_p(y)=h_p(x)$ for every $p$. By step [](#recover){.pf-ref}, multiplication by the rational number $y/x$ maps $G$ onto $H$, and it is injective.
:::

:::

:::

:::

::: pf-step
(1), (2) The groups $G_S$ for distinct sets of primes $S$ are pairwise non-isomorphic, and there are exactly $\boxed{2^{\aleph_0}}$ isomorphism classes.

::: pf-proof
There are at most $2^{\aleph_0}$ subgroups because $\QQ$ is countable.
For each set of primes $S$, let
$$
G_S=\ZZ[1/p:p\in S].
$$
For $1\in G_S$,
$$
h_p(1)=\begin{cases}
\infty,&p\in S,\\
0,&p\notin S.
\end{cases}
$$
The set of primes with infinite height is an invariant of the type, so step [](#s2){.pf-ref} shows that $G_S\cong G_T$ implies $S=T$. The set of primes is countably infinite, so there are $2^{\aleph_0}$ choices of $S$.
:::

:::

::: pf-step
(3) The groups $G_S$ do not exhaust all subgroups of $\QQ$.

::: pf-proof
Choose finite numbers $e_p\ge0$ with $e_p>0$ for infinitely many primes $p$ (for example $e_p=1$ for all $p$), and set
$$
G=\left\langle p^{-j}:p\text{ prime},\ 0\le j\le e_p\right\rangle\le\QQ.
$$
Then $h_p(1)=e_p$. This characteristic has infinitely many positive finite coordinates, so it is not equivalent to a characteristic with values only $0$ and $\infty$, as every type of a $G_S$ is. By step [](#s2){.pf-ref}, $G$ is isomorphic to no $G_S$.
:::

:::

:::

:::
