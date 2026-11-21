---
schema: qual/card@1
id: P-TOPS11G
kind: problem
title: "Cohomology of the product of suspensions of lens space homology spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Suspensions
  - Lens Spaces
  - Künneth Formula
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subclaims suffice, and the 5
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    computation was re-checked: the suspension shifts $\tilde H_1=\ZZ_p$ and $\tilde H_3=\ZZ$ of $L(p)$ to
    degrees $2$ and $4$, coprimality of $p$ and $q$ kills both the tensor and the Tor term of the two
    torsion groups, Künneth gives $\ZZ$ in degrees $0,8$, $\ZZ^2$ in degree $4$ and $\ZZ_{pq}$ in degrees
    $2,6$, and universal coefficients moves each $\ZZ_{pq}$ from degree $2$ and $6$ up to $3$ and $7$
    while leaving the free parts in place. Checked against the statement on the card, from the UCSD Spring
    2011 topology qualifying exam. Nothing in the statement was changed.

---

::: {.problem}
Let $L(p)$ be a space whose integral homology groups are $\ZZ$, $\ZZ_p$, $0$, $\ZZ$ in dimensions $0$, $1$, $2$, $3$, and zero otherwise.
Let $\Sigma$ denote the suspension of a space.
Compute the cohomology $H^*(\Sigma L(p) \times \Sigma L(q); \ZZ)$, where $p$ and $q$ are coprime.
:::

::: {.solution}
Put $A=\Sigma L(p)$ and $B=\Sigma L(q)$.

::: pf

::: pf-step
The suspension isomorphism gives
$$
H_i(A;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,4,\\
\ZZ_p,&i=2,\\
0,&\text{otherwise},
\end{cases}
$$
and the analogous formula for $B$ with $p$ replaced by $q$.


::: pf-proof
Suspension shifts reduced homology up one degree, and $L(p)$ has $\tilde H_1=\ZZ_p$ and $\tilde H_3=\ZZ$ with all other reduced groups zero.
:::

:::

::: pf-step
Apply the homological Künneth theorem to $A\times B$.

::: pf-proof

::: pf-step
The only possible torsion--torsion tensor and Tor terms are
$$
\ZZ_p\otimes\ZZ_q
\quad\text{and}\quad
\operatorname{Tor}_1^{\ZZ}(\ZZ_p,\ZZ_q),
$$
and both vanish because $\gcd(p,q)=1$.


::: pf-proof
Since $p$ and $q$ are coprime, multiplication by $p$ is an automorphism of $\ZZ_q$, so $\ZZ_p\otimes\ZZ_q=0$ and $\operatorname{Tor}_1(\ZZ_p,\ZZ_q)=0$.
:::

:::

::: pf-step
Therefore
$$
H_i(A\times B;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,8,\\
\ZZ_p\oplus\ZZ_q,&i=2,6,\\
\ZZ^2,&i=4,\\
0,&\text{otherwise}.
\end{cases}
$$
Since $p$ and $q$ are coprime, $\ZZ_p\oplus\ZZ_q\cong\ZZ_{pq}$.


::: pf-proof
Collecting the Künneth terms: the free classes contribute $\ZZ$ in degrees $0$ and $8$ and $\ZZ^2$ in degree $4$, the torsion classes contribute $\ZZ_p\oplus\ZZ_q$ in degrees $2$ and $6$, and every Tor term vanishes by the preceding subclaim.
:::

:::

:::

:::

::: pf-step
The universal coefficient theorem for cohomology gives a split short exact sequence
$$
0\longrightarrow
\operatorname{Ext}(H_{k-1}(A\times B),\ZZ)
\longrightarrow H^k(A\times B;\ZZ)
\longrightarrow
\operatorname{Hom}(H_k(A\times B),\ZZ)
\longrightarrow0.
$$

::: pf-proof

::: pf-step
The free summands in homology contribute to cohomology in the same degree, while each $\ZZ_{pq}$ in degrees $2$ and $6$ contributes an $\operatorname{Ext}$ term $\ZZ_{pq}$ in degrees $3$ and $7$.


::: pf-proof
Universal coefficients: $H^k=\operatorname{Hom}(H_k,\ZZ)\oplus\operatorname{Ext}(H_{k-1},\ZZ)$, where $\operatorname{Hom}$ of a free group is itself and of a torsion group is $0$, while $\operatorname{Ext}(\ZZ,-)=0$ and $\operatorname{Ext}(\ZZ_{pq},\ZZ)=\ZZ_{pq}$.
:::

:::

::: pf-step
Hence
$$
H^k(\Sigma L(p)\times\Sigma L(q);\ZZ)\cong
\begin{cases}
\ZZ,&k=0,8,\\
\ZZ^2,&k=4,\\
\ZZ_{pq},&k=3,7,\\
0,&\text{otherwise}.
\end{cases}
$$


::: pf-proof
Substituting the homology computed above into the universal coefficient formula degree by degree.
:::

:::

:::

:::

:::

:::
