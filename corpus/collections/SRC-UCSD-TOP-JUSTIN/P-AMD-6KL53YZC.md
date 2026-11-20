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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Eight of the card's fifteen steps --- the definition of degree, the open cover, and every
    leaf of the suspension-degree argument --- asserted their claim with no proof body; each now
    carries a `pf-proof`. The two `pf-qed` steps, whose whole content was to point back at the
    parts, are removed under STYLE-08, the last step of the suspension argument and the last
    step of the construction each concluding on its own. No claim was changed and the
    construction is the same. Checked: that the integer in the definition of degree does not
    depend on the choice of generator; that the two cones cover the suspension with the stated
    intersection; that $\Sigma f$ preserves each cone and restricts to $f$ on the equator, which
    is what lets the naturality square be applied; and that the final comparison of integers is
    legitimate because $\widetilde{H}_{n+1}(\Sigma S^n)\cong\ZZ$ is torsion-free. Not checked:
    the naturality of the Mayer--Vietoris connecting map is cited to P-AMD-2IFZW3JK, not
    reproved here, and the source sheet UCSD_290_F14_sheet7.pdf was not re-read.
---

::: {.problem}
For a self-map $f:S^n\to S^n$, show that $\deg(\Sigma f)=\deg(f)$.

Conclude that for every $n\ge1$ and every integer $d\in\ZZ$, there exists a self-map $S^n\to S^n$ of degree $d$.
:::

::: {.solution}

Throughout, $f \colon S^n \to S^n$ is continuous with $n\ge1$, and $\Sigma f$ is its suspension.

::: pf

::: pf-step

Definition of degree and suspension isomorphism in homology.

::: pf-proof

Step 1.1 records what degree means, 1.2 the open cover of the suspension, and 1.3 the Mayer--Vietoris identification of the suspension isomorphism $\sigma=\partial^{-1}$.

::: pf-step

For any continuous map $g \colon S^k \to S^k$ ($k \ge 1$), the degree $\deg(g) \in \ZZ$ is defined by the induced map on top homology: $g_*(\alpha) = (\deg g) \cdot \alpha$ for any generator $\alpha \in \widetilde{H}_k(S^k) \cong \ZZ$.

::: pf-proof

$\widetilde{H}_k(S^k)\cong\ZZ$ is infinite cyclic, so for a generator $\alpha$ there is a unique integer $m$ with $g_*(\alpha)=m\alpha$. The integer does not depend on the generator: the other generator is $-\alpha$, and $g_*(-\alpha)=-g_*(\alpha)=m(-\alpha)$. That integer $m$ is by definition $\deg(g)$.

:::

:::

::: pf-step

Decompose $\Sigma S^n$ as the union of two open cones $C_+ S^n$ and $C_- S^n$ intersecting along $S^n \times (-1, 1) \simeq S^n$.

::: pf-proof

$\Sigma S^n$ is the quotient of $S^n\times[-1,1]$ collapsing $S^n\times\{-1\}$ and $S^n\times\{1\}$ to the two cone points. Let $C_+$ be the image of $S^n\times(-1,1]$ and $C_-$ the image of $S^n\times[-1,1)$; both are open in the quotient, they cover it, and their intersection is the image of $S^n\times(-1,1)$, which the quotient map carries homeomorphically onto its image, so it is homeomorphic to $S^n\times(-1,1)\simeq S^n$.

:::

:::

::: pf-step

The suspension isomorphism $\sigma \colon \widetilde{H}_n(S^n) \xrightarrow{\cong} \widetilde{H}_{n+1}(\Sigma S^n)$ is the connecting isomorphism in the Mayer-Vietoris sequence of the suspension:
$$\widetilde{H}_{n+1}(C_+ S^n) \oplus \widetilde{H}_{n+1}(C_- S^n) \to \widetilde{H}_{n+1}(\Sigma S^n) \xrightarrow{\partial} \widetilde{H}_n(S^n) \to \widetilde{H}_n(C_+ S^n) \oplus \widetilde{H}_n(C_- S^n).$$
Since cones are contractible, $\partial \colon \widetilde{H}_{n+1}(\Sigma S^n) \to \widetilde{H}_n(S^n)$ is an isomorphism, and $\sigma = \partial^{-1}$.

::: pf-proof

In the Mayer--Vietoris sequence of the open cover of step 1.2, the terms $\widetilde{H}_*(C_+S^n)$ and $\widetilde{H}_*(C_-S^n)$ vanish because the cones are contractible, so the terms flanking $\partial$ in degree $n+1$ vanish and $\partial$ is an isomorphism. Its inverse is what the card calls $\sigma$.

:::

:::

:::

:::

::: {.pf-step #s2}

Prove $\deg(\Sigma f) = \deg(f)$.

::: pf-proof

Steps 2.1--2.6 run the naturality square: $\Sigma f$ restricts to $f$ on the equator (2.1), the connecting map is natural (2.2), and the comparison of the two descriptions of $(\Sigma f)_*(\beta)$ gives the equality of degrees (2.3--2.6).

::: pf-step

The suspension map $\Sigma f \colon \Sigma S^n \to \Sigma S^n$ preserves the cones $C_+ S^n, C_- S^n$ and restricts on the equator $S^n$ to $f$.

::: pf-proof

In coordinates $\Sigma f([x,t])=[f(x),t]$, so $S^n\times(-1,1]$ maps into itself and $S^n\times[-1,1)$ into itself, which is the statement that $C_+$ and $C_-$ are preserved. On the equator $t=0$ the formula reads $[x,0]\mapsto[f(x),0]$, the image of $f$ under the identification $S^n\cong S^n\times\{0\}$.

:::

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

::: pf-proof

$\Sigma f$ carries the pair of open sets $(C_+S^n,C_-S^n)$ into itself by step 2.1 and restricts to $f$ on their intersection by step 2.1, so it is a map of the two Mayer--Vietoris data. The connecting homomorphism is natural with respect to such a map, and that naturality is exactly the commutativity of the displayed square; the isomorphy of $\partial$ is step 1.3.

:::

:::

::: pf-step

Let $\beta \in \widetilde{H}_{n+1}(\Sigma S^n)$ be a generator such that $\partial(\beta) = \alpha \in \widetilde{H}_n(S^n)$ is a generator.

::: pf-proof

$\partial$ is an isomorphism by step 1.3, so for a generator $\alpha$ of $\widetilde{H}_n(S^n)\cong\ZZ$ there is a unique $\beta=\partial^{-1}(\alpha)$; the image of a generator under an isomorphism is a generator, so $\beta$ generates $\widetilde{H}_{n+1}(\Sigma S^n)$.

:::

:::

::: {.pf-step #s2-4}

Computing along the diagram:
$$\partial((\Sigma f)_*(\beta)) = f_*(\partial(\beta)) = f_*(\alpha) = (\deg f) \alpha.$$

::: pf-proof

The first equality is the commutativity of the square in step 2.2 applied to $\beta$; the second is $\partial(\beta)=\alpha$ from step 2.3; the third is the definition of $\deg f$ (step 1.1) applied to the generator $\alpha$.

:::

:::

::: {.pf-step #s2-5}

Applying $\sigma = \partial^{-1}$ yields:
$$(\Sigma f)_*(\beta) = (\deg f) \beta.$$

::: pf-proof

Apply $\partial^{-1}$ to both sides of step 2.4: on the left it undoes $\partial$, giving $(\Sigma f)_*(\beta)$; on the right, $\partial^{-1}((\deg f)\alpha)=(\deg f)\partial^{-1}(\alpha)=(\deg f)\beta$, since $\partial^{-1}$ is a group homomorphism and $\partial^{-1}(\alpha)=\beta$ by step 2.3.

:::

:::

::: pf-step

By definition of degree, $(\Sigma f)_*(\beta) = (\deg \Sigma f) \beta$, hence $\deg(\Sigma f) = \deg(f)$.

::: pf-proof

$\beta$ generates $\widetilde{H}_{n+1}(\Sigma S^n)$, so the definition of degree (step 1.1) gives $(\Sigma f)_*(\beta)=(\deg\Sigma f)\beta$. Comparing with step 2.5 gives $(\deg\Sigma f)\beta=(\deg f)\beta$, that is $(\deg\Sigma f-\deg f)\beta=0$; $\widetilde{H}_{n+1}(\Sigma S^n)\cong\ZZ$ is torsion-free, so the integer in parentheses is $0$.

:::

:::

:::

:::

::: {.pf-step #s3}

For every $n\ge1$ and $d\in\ZZ$, construct a self-map of $S^n$ of degree $d$.

::: pf-proof

Step 3.1 builds the map on $S^1$, steps 3.2--3.3 suspend it $n-1$ times and read off the degree with part 2.

::: pf-step

On $S^1\subset\CC$, the map
$$
g_d(z)=z^d
$$
has degree $d$ for $d\ge0$; for $d<0$ the same formula means $z^d=\overline z^{\,\abs{d}}$ on $S^1$ and again has degree $d$. For $d=0$, it is the constant map $1$.

::: pf-proof

Writing $z=e^{i\theta}$ gives $g_d(e^{i\theta})=e^{id\theta}$. Thus the induced map on $H_1(S^1)\cong\ZZ$ is multiplication by $d$.

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

:::
:::