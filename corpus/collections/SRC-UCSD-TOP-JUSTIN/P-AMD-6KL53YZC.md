---
schema: qual/card@1
id: P-AMD-6KL53YZC
kind: problem
title: 'For $f: S^n\circlearrowleft$, show $\deg f = \deg \Sigma f$'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: >-
    Checked against UCSD_290_F14_sheet7.pdf, problem 3. The source asks to
    deduce existence of a degree-d self-map of S^n for every integer d; the
    previous card incorrectly replaced this by the stronger statement
    pi_n(S^n)=Z.
---

::: {.problem}
For a self-map $f:S^n\to S^n$, show that $\deg(\Sigma f)=\deg(f)$.

Conclude that for every $n\ge1$ and every integer $d\in\ZZ$, there exists a self-map $S^n\to S^n$ of degree $d$.
:::

::: {.solution}
**Goal:** Let $f \colon S^n \to S^n$ be continuous with $n\ge1$. Prove $\deg(\Sigma f)=\deg(f)$ and deduce that every integer occurs as the degree of a self-map of every sphere $S^n$, $n\ge1$.

::: pf

::: pf-step
Definition of degree and suspension isomorphism in homology.

::: pf-proof

::: pf-step
For any continuous map $g \colon S^k \to S^k$ ($k \ge 1$), the degree $\deg(g) \in \mathbb{Z}$ is defined by the induced map on top homology: $g_*(\alpha) = (\deg g) \cdot \alpha$ for any generator $\alpha \in \widetilde{H}_k(S^k) \cong \mathbb{Z}$.
:::

::: pf-step
Decompose $\Sigma S^n$ as the union of two open cones $C_+ S^n$ and $C_- S^n$ intersecting along $S^n \times (-1, 1) \simeq S^n$.
:::

::: pf-step
The suspension isomorphism $\sigma \colon \widetilde{H}_n(S^n) \xrightarrow{\cong} \widetilde{H}_{n+1}(\Sigma S^n)$ is the connecting isomorphism in the Mayer-Vietoris sequence of the suspension:
$$\widetilde{H}_{n+1}(C_+ S^n) \oplus \widetilde{H}_{n+1}(C_- S^n) \to \widetilde{H}_{n+1}(\Sigma S^n) \xrightarrow{\partial} \widetilde{H}_n(S^n) \to \widetilde{H}_n(C_+ S^n) \oplus \widetilde{H}_n(C_- S^n).$$
Since cones are contractible, $\partial \colon \widetilde{H}_{n+1}(\Sigma S^n) \to \widetilde{H}_n(S^n)$ is an isomorphism, and $\sigma = \partial^{-1}$.

::: pf-proof
In the Mayer–Vietoris sequence of the suspension, the terms $\widetilde{H}_*(C_+ S^n)$ and $\widetilde{H}_*(C_- S^n)$ vanish because cones are contractible, so the connecting homomorphism $\partial$ is an isomorphism.
:::

:::

:::

:::

::: {.pf-step #s2}
Prove $\deg(\Sigma f) = \deg(f)$.

::: pf-proof

::: pf-step
The suspension map $\Sigma f \colon \Sigma S^n \to \Sigma S^n$ preserves the cones $C_+ S^n, C_- S^n$ and restricts on the equator $S^n$ to $f$.
:::

::: {.pf-step #s2-2}
By naturality of the Mayer-Vietoris connecting homomorphism $\partial$ (proved in P-AMD-2IFZW3JK), the following square commutes:
$$
\begin{CD}
\widetilde{H}_{n+1}(\Sigma S^n) @>{\partial}>{\cong}> \widetilde{H}_n(S^n) \\
@VV{(\Sigma f)_*}V @VV{f_*}V \\
\widetilde{H}_{n+1}(\Sigma S^n) @>{\partial}>{\cong}> \widetilde{H}_n(S^n)
\end{CD}
$$
:::

::: pf-step
Let $\beta \in \widetilde{H}_{n+1}(\Sigma S^n)$ be a generator such that $\partial(\beta) = \alpha \in \widetilde{H}_n(S^n)$ is a generator.
:::

::: {.pf-step #s2-4}
Computing along the diagram:
$$\partial((\Sigma f)_*(\beta)) = f_*(\partial(\beta)) = f_*(\alpha) = (\deg f) \alpha.$$
:::

::: {.pf-step #s2-5}
Applying $\sigma = \partial^{-1}$ yields:
$$(\Sigma f)_*(\beta) = (\deg f) \beta.$$
:::

::: pf-step
By definition of degree, $(\Sigma f)_*(\beta) = (\deg \Sigma f) \beta$, hence $\deg(\Sigma f) = \deg(f)$.
:::

::: pf-qed
The naturality square of step [](#s2-2){.pf-ref} commutes, so $\partial((\Sigma f)_*(\beta)) = f_*(\partial(\beta))$; combining this with steps [](#s2-4){.pf-ref} and [](#s2-5){.pf-ref} gives $(\Sigma f)_*(\beta) = (\deg f)\beta$, and comparing with the definition of degree yields $\deg(\Sigma f) = \deg(f)$.
:::

:::

:::

::: {.pf-step #s3}
For every $n\ge1$ and $d\in\mathbb Z$, construct a self-map of $S^n$ of degree $d$.

::: pf-proof

::: pf-step
On $S^1\subset\mathbb C$, the map
$$
g_d(z)=z^d
$$
has degree $d$ for $d\ge0$; for $d<0$ the same formula means $z^d=\overline z^{\,|d|}$ on $S^1$ and again has degree $d$. For $d=0$, it is the constant map $1$.

::: pf-proof
Writing $z=e^{i\theta}$ gives $g_d(e^{i\theta})=e^{id\theta}$. Thus the induced map on $H_1(S^1)\cong\mathbb Z$ is multiplication by $d$.
:::

:::

::: pf-step
For $n>1$, define
$$
f_{n,d}=\Sigma^{\,n-1}g_d:S^n\cong\Sigma^{\,n-1}S^1\longrightarrow\Sigma^{\,n-1}S^1\cong S^n.
$$

::: pf-proof
Repeatedly use the canonical homeomorphisms $\Sigma S^k\cong S^{k+1}$.
:::

:::

::: pf-step
Then $\deg(f_{n,d})=d$.

::: pf-proof
Apply step [](#s2){.pf-ref} successively to the $n-1$ suspensions:
$$
\deg(\Sigma^{\,n-1}g_d)=\deg(g_d)=d.
$$
:::

:::

:::

:::

::: pf-qed
Step [](#s2){.pf-ref} proves suspension preserves degree, and step [](#s3){.pf-ref} constructs a self-map of every prescribed degree.
:::

:::
:::

