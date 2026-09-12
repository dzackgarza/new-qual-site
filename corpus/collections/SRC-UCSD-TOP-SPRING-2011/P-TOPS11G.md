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
---

::: problem
Let $L(p)$ be a space whose integral homology groups are $\mathbb{Z}$, $\mathbb{Z}_p$, $0$, $\mathbb{Z}$ in dimensions $0$, $1$, $2$, $3$, and zero otherwise.
Let $\Sigma$ denote the suspension of a space.
Compute the cohomology $H^*(\Sigma L(p) \times \Sigma L(q); \mathbb{Z})$, where $p$ and $q$ are coprime.
:::

::: solution
Put $A=\Sigma L(p)$ and $B=\Sigma L(q)$.

<1>1. The suspension isomorphism gives
$$
H_i(A;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,4,\\
\mathbb Z_p,&i=2,\\
0,&\text{otherwise},
\end{cases}
$$
and the analogous formula for $B$ with $p$ replaced by $q$.

<1>2. Apply the homological Künneth theorem to $A\times B$.
<2>1. The only possible torsion--torsion tensor and Tor terms are
$$
\mathbb Z_p\otimes\mathbb Z_q
\quad\text{and}\quad
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z_p,\mathbb Z_q),
$$
and both vanish because $\gcd(p,q)=1$.
<2>2. Therefore
$$
H_i(A\times B;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,8,\\
\mathbb Z_p\oplus\mathbb Z_q,&i=2,6,\\
\mathbb Z^2,&i=4,\\
0,&\text{otherwise}.
\end{cases}
$$
Since $p$ and $q$ are coprime, $\mathbb Z_p\oplus\mathbb Z_q\cong\mathbb Z_{pq}$.

<1>3. The universal coefficient theorem for cohomology gives a split short exact sequence
$$
0\longrightarrow
\operatorname{Ext}(H_{k-1}(A\times B),\mathbb Z)
\longrightarrow H^k(A\times B;\mathbb Z)
\longrightarrow
\operatorname{Hom}(H_k(A\times B),\mathbb Z)
\longrightarrow0.
$$
<2>1. The free summands in homology contribute to cohomology in the same degree, while each $\mathbb Z_{pq}$ in degrees $2$ and $6$ contributes an $\operatorname{Ext}$ term $\mathbb Z_{pq}$ in degrees $3$ and $7$.
<2>2. Hence
$$
H^k(\Sigma L(p)\times\Sigma L(q);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,8,\\
\mathbb Z^2,&k=4,\\
\mathbb Z_{pq},&k=3,7,\\
0,&\text{otherwise}.
\end{cases}
$$
:::
