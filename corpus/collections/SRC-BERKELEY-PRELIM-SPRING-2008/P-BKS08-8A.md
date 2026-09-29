---
schema: qual/card@1
id: P-BKS08-8A
kind: problem
title: A commutative ring of characteristic $pq$ is a product of rings of characteristics $p$ and $q$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the exact quotient characteristics, comaximality,
    zero intersection, and Chinese-remainder isomorphism against the vendored
    solution.
---

::: {.problem}
Let $p$ and $q$ be distinct primes, and let $R$ be a commutative ring with identity of characteristic $pq$. Show that there are rings $S,T$ of characteristics $p,q$, respectively, such that
$$
R\cong S\times T.
$$
:::

::: {.solution}
Define
$$
S\coloneqq R/pR,
\qquad
T\coloneqq R/qR.
$$

::: pf

::: {.pf-step #s-char-p}
The ring $S$ has characteristic exactly $p$.

::: pf-proof
Since $p=0$ in $S$, the characteristic of $S$ divides the prime $p$,
provided that $S$ is nonzero. If $S=0$, then $1\in pR$, so
$1=pr$ for some $r\in R$. Multiplying by $q$ gives
$$
q=pqr=0
$$
in $R$, contradicting $\operatorname{char}R=pq$. Hence $S\ne0$,
and therefore $\operatorname{char}S=p$.
:::

:::

::: {.pf-step #t-char-q}
The ring $T$ has characteristic exactly $q$.

::: pf-proof
The same argument with $p$ and $q$ interchanged shows that $T\ne0$,
while $q=0$ in $T$. Since $q$ is prime,
$\operatorname{char}T=q$.
:::

:::

::: {.pf-step #comaximal}
The ideals $pR$ and $qR$ are comaximal.

::: pf-proof
Since $p$ and $q$ are distinct primes, there exist integers $m,n$ such
that
$$
mp+nq=1.
$$
Multiplying by $1_R$ gives
$$
1_R\in pR+qR,
$$
so $pR+qR=R$.
:::

:::

::: {.pf-step #intersection-zero}
One has
$$
pR\cap qR=0.
$$

::: pf-proof
Let $a\in pR\cap qR$. Using the Bézout identity from step [](#comaximal){.pf-ref},
$$
a=(mp+nq)a=m(pa)+n(qa).
$$
Because $a\in qR$, one has $pa\in pqR$; because $a\in pR$, one has
$qa\in pqR$. Thus $a\in pqR$. But
$$
pqR=0
$$
because $R$ has characteristic $pq$. Hence $a=0$.
:::

:::

::: {.pf-step #phi-isomorphism}
The map
$$
\Phi:R\longrightarrow S\times T,
\qquad
r\longmapsto(r+pR,r+qR),
$$
is an isomorphism.

::: pf-proof
By step [](#comaximal){.pf-ref}, the ideals $pR$ and $qR$ are comaximal. The Chinese
remainder theorem therefore gives a surjection
$$
R\longrightarrow R/pR\times R/qR
$$
whose kernel is $pR\cap qR$. Step [](#intersection-zero){.pf-ref} identifies this kernel with
$0$, so the map is also injective.
:::

:::

::: {.pf-step #conclusion}
Consequently there are rings $S,T$ of characteristics $p,q$,
respectively, such that
$$
\boxed{R\cong S\times T}.
$$

::: pf-proof
Steps [](#s-char-p){.pf-ref} and [](#t-char-q){.pf-ref} give the required characteristics, and step [](#phi-isomorphism){.pf-ref} gives
the isomorphism.
:::

:::

::: pf-qed
Step [](#conclusion){.pf-ref} is the desired decomposition.
:::

:::

:::
