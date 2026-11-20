---
schema: qual/card@1
id: E-HAT-3.1-1
kind: problem
title: Functoriality of $\operatorname{Ext}(H,G)$ in both variables
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both functorialities: a free resolution is projective, so any homomorphism lifts to a
    chain map and any two lifts are chain homotopic, which makes $\alpha^*$ well defined and
    independent of the lift; post-composition gives covariance in $G$, with
    $d^*\beta_*=\beta_*d^*$. Ext is taken here as the cokernel of
    $\operatorname{Hom}(F_0,G)\to\operatorname{Hom}(F_1,G)$, which is its definition for abelian
    groups.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Re-read against Hatcher pp.194-195 with Exercise 1 (p.204); the statement matches the printed text. Two placeholder proofs ("setup.") replaced by the existence of the free resolution of p.195 and by Lemma 3.1(b); the lifting step cites Lemma 3.1(a) (p.194) instead of an unnamed comparison theorem, and the independence-of-lift step now carries the chain-homotopy computation. Not covered: the extension interpretation of Ext on p.195, which the exercise does not ask for.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Re-read against Hatcher, Exercise 1 of §3.1, printed p. 204, and what it uses: Lemma 3.1(a),
    (b) on printed p. 194, the construction of the two-term free resolution and the definition of
    $\operatorname{Ext}(H,G)$ on printed pp. 194--195. Repaired the solution throughout. Four of
    its proofs were noun phrases rather than arguments ('contravariance of the
    $\operatorname{Hom}(-,G)$ functor', 'definition of $\operatorname{Ext}$ for abelian groups',
    'quotient map between cokernels', 'composition of chain maps'); a `pf` block was opened and
    closed inside the solution, leaving three separately numbered runs; and the final step
    concluded from two earlier steps alone, which STYLE-08 forbids. The solution is now six steps
    with substantive proofs: the lifting of $\alpha$ to a chain map by Lemma 3.1(a), the dual map
    and its descent to the cokernels, independence of the lift through the two-term chain homotopy
    formula $\alpha_i-\alpha_i'=d_1'\lambda_i+\lambda_{i-1}d_i$ with $\lambda_{-1}=0$ (this
    replaces the earlier sentence about kernels, which was superfluous: the difference of the two
    dual maps lands in $\operatorname{im}d_1^*$ on all of $\operatorname{Hom}(F_1',G)$),
    functoriality in $H$, the descent of post-composition by $\beta\colon G\to G'$, and
    functoriality in $G$. Not claimed: the extension interpretation of $\operatorname{Ext}(H,G)$
    on printed p. 195, which the exercise does not ask for.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 213 carries the running head 204,
    so the printed page is the one the card's earlier event claimed. The durable part of the locator
    is that printed page; the file path names this machine's copy and `tmp/sources` does not survive a
    VM reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 3.1 of Hatcher, *Algebraic Topology* (2002), read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf`; the statement below is its wording.

Show that $\operatorname{Ext}(H, G)$ is a contravariant functor of $H$ for fixed $G$, and a covariant functor of $G$ for fixed $H$.
:::

::: {.solution}
For an abelian group $H$ choose a free resolution
$$
0\longrightarrow F_1\xrightarrow{d_1}F_0\xrightarrow{\varepsilon}H\longrightarrow0,
$$
which exists with $F_0$ free on a set of generators of $H$ and $F_1=\ker\varepsilon$ free, being a subgroup of a free abelian group (Hatcher, p. 195). Applying $\operatorname{Hom}(-,G)$ gives the cochain complex
$$
0\longrightarrow\operatorname{Hom}(F_0,G)\xrightarrow{d_1^*}\operatorname{Hom}(F_1,G)\longrightarrow0,
\qquad d_1^*(\varphi)=\varphi\circ d_1,
$$
which vanishes above degree $1$, and
$$
\operatorname{Ext}(H,G)=H^1(\operatorname{Hom}(F_*,G))=\operatorname{Hom}(F_1,G)\big/d_1^*\operatorname{Hom}(F_0,G)
$$
by the definition on p. 195. Lemma 3.1(b) identifies this group for any two free resolutions of $H$, so it depends on $H$ and $G$ only. The exercise is Exercise 1 of §3.1.

::: pf

::: {.pf-step #s1}

Let $\alpha\colon H\to H'$ be a homomorphism and let $F_*$, $F_*'$ be free resolutions of $H$ and $H'$. Then $\alpha$ lifts to a chain map $(\alpha_0,\alpha_1)$, that is $\varepsilon'\alpha_0=\alpha\varepsilon$ and $d_1'\alpha_1=\alpha_0d_1$.

::: pf-proof

Lemma 3.1(a) chooses $\alpha_0$ on a free basis of $F_0$ by taking preimages under the surjection $\varepsilon'$, and then $\alpha_1$ on a free basis of $F_1$ by taking preimages under $d_1'$, which is possible because $\alpha_0d_1$ takes values in $\ker\varepsilon'=\operatorname{im}d_1'$: indeed $\varepsilon'\alpha_0d_1=\alpha\varepsilon d_1=0$.

:::

:::

::: {.pf-step #s2}

Dualizing a lift gives a homomorphism $\alpha^*\colon\operatorname{Ext}(H',G)\to\operatorname{Ext}(H,G)$.

::: pf-proof

The map $\alpha_1^*\colon\operatorname{Hom}(F_1',G)\to\operatorname{Hom}(F_1,G)$, $\psi\mapsto\psi\circ\alpha_1$, satisfies $d_1^*\circ\alpha_0^*=\alpha_1^*\circ(d_1')^*$, both sides sending $\psi$ to $\psi\circ\alpha_0\circ d_1=\psi\circ d_1'\circ\alpha_1$. Hence $\alpha_1^*$ carries $\operatorname{im}(d_1')^*$ into $\operatorname{im}d_1^*$ and descends to a homomorphism of the cokernels, which is $\alpha^*$.

:::

:::

::: {.pf-step #s3}

$\alpha^*$ is independent of the lift.

::: pf-proof

Let $(\alpha_0',\alpha_1')$ be a second lift. By Lemma 3.1(a) there is $\lambda\colon F_0\to F_1'$ with $\alpha_0-\alpha_0'=d_1'\lambda$ and $\alpha_1-\alpha_1'=\lambda d_1$; this is the chain homotopy formula $\beta_i=d_1'\lambda_i+\lambda_{i-1}d_i$ for a two-term complex, with $\lambda_{-1}=0$. Then for $\psi\in\operatorname{Hom}(F_1',G)$,
$$
(\alpha_1^*-\alpha_1'^*)(\psi)=\psi\circ(\alpha_1-\alpha_1')=\psi\circ\lambda\circ d_1=d_1^*(\psi\circ\lambda),
$$
which lies in $\operatorname{im}d_1^*$, so the two maps induce the same map of cokernels.

:::

:::

::: {.pf-step #s4}

$\operatorname{Ext}(-,G)$ is a contravariant functor of $H$.

::: pf-proof

The identity of $H$ lifts to the identity chain map, so $(\operatorname{id}_H)^*$ is the identity of $\operatorname{Ext}(H,G)$. If $(\alpha_i)$ lifts $\alpha\colon H\to H'$ and $(\beta_i)$ lifts $\beta\colon H'\to H''$, then $(\beta_i\circ\alpha_i)$ is a lift of $\beta\circ\alpha$, and since the induced map does not depend on the lift by the preceding step, $(\beta\alpha)^*=\alpha^*\circ\beta^*$. Thus $H\mapsto\operatorname{Ext}(H,G)$ is contravariant.

:::

:::

::: {.pf-step #s5}

A homomorphism $\beta\colon G\to G'$ induces $\beta_*\colon\operatorname{Ext}(H,G)\to\operatorname{Ext}(H,G')$.

::: pf-proof

Fix one free resolution $F_*$ of $H$; by Lemma 3.1(b) any other gives the same group, so it is enough to define the map on $\operatorname{Hom}(F_1,G)/\operatorname{im}d_1^*$. Post-composition $\beta_*(\psi)=\beta\circ\psi$ defines $\operatorname{Hom}(F_k,G)\to\operatorname{Hom}(F_k,G')$ for $k=0,1$, and $\beta_*d_1^*=d_1^*\beta_*$ because $\beta\circ(\psi\circ d_1)=(\beta\circ\psi)\circ d_1$; hence $\beta_*$ preserves $\operatorname{im}d_1^*$ and descends to the quotients.

:::

:::

::: {.pf-step #s6}

$\operatorname{Ext}(H,-)$ is a covariant functor of $G$.

::: pf-proof

On the fixed resolution, $(\operatorname{id}_G)_*$ is the identity, and for $\gamma\colon G'\to G''$ the composites satisfy $(\gamma\circ\beta)_*(\psi)=\gamma\circ\beta\circ\psi=\gamma_*(\beta_*(\psi))$, so $(\gamma\beta)_*=\gamma_*\circ\beta_*$. Both statements are independent of the resolution by the same lemma, so they hold for $\operatorname{Ext}$ as defined.

:::

:::

:::
:::
